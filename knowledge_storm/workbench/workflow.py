"""Public local task workflow: worksheet in, immutable report bundle out."""

import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable
from uuid import uuid4

from .models import (
    Artifact,
    Capture,
    EvidenceInput,
    Finding,
    ReportBundle,
    Usage,
    Worksheet,
)
from .storm_adapter import StormAdapter


def new_id() -> str:
    return uuid4().hex


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class TaskWorkflow:
    """Single-operator, append-only storage; reopening needs no providers.

    Only a complete bundle is published into revisions/. A failed run publishes
    a failed revision retaining captures acquired before the error.
    """

    def __init__(self, root, *, retriever=None, model=None, clock=utc_now):
        self.root = Path(root).resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.retriever = retriever
        self.model = model
        self.clock: Callable[[], datetime] = clock

    def _task_dir(self, task_id: str) -> Path:
        if not re.fullmatch(r"[a-f0-9]{32}", task_id):
            raise ValueError("Invalid task ID")
        return self.root / task_id

    def _revisions(self, task_id: str) -> list[ReportBundle]:
        directory = self._task_dir(task_id) / "revisions"
        return sorted(
            (
                ReportBundle.model_validate_json(path.read_text(encoding="utf-8"))
                for path in directory.glob("*/bundle.json")
            ),
            key=lambda bundle: bundle.revision_number,
        )

    def open(self, task_id: str, revision_id: str | None = None) -> ReportBundle:
        revisions = self._revisions(task_id)
        if revision_id is None and revisions:
            return revisions[-1]
        for bundle in revisions:
            if bundle.revision_id == revision_id:
                return bundle
        raise FileNotFoundError("Saved task revision not found")

    def list_tasks(self) -> list[ReportBundle]:
        return [
            self.open(path.name)
            for path in sorted(self.root.iterdir())
            if path.is_dir()
            and re.fullmatch(r"[a-f0-9]{32}", path.name)
            and self._revisions(path.name)
        ]

    def history(self, task_id: str) -> list[ReportBundle]:
        return self._revisions(task_id)

    def read_file(self, task_id: str, relative_path: str) -> str:
        directory = self._task_dir(task_id).resolve()
        path = (directory / relative_path).resolve()
        if not path.is_relative_to(directory):
            raise ValueError("File reference must remain inside its task")
        return path.read_text(encoding="utf-8")

    def create(self, worksheet: Worksheet) -> ReportBundle:
        task_id = new_id()
        self._task_dir(task_id).mkdir()
        return self._save_worksheet(task_id, worksheet, None)

    def revise(self, task_id: str, worksheet: Worksheet) -> ReportBundle:
        return self._save_worksheet(task_id, worksheet, self.open(task_id))

    def _save_worksheet(self, task_id, worksheet, parent):
        now = self.clock()
        bundle = ReportBundle(
            task_id=task_id,
            task_created_at=parent.task_created_at if parent else now,
            revision_id=new_id(),
            parent_revision_id=parent.revision_id if parent else None,
            revision_number=parent.revision_number + 1 if parent else 1,
            created_at=now,
            status="draft",
            worksheet=worksheet,
            purpose=worksheet.purpose,
            budget={
                "time_allowance_minutes": worksheet.time_allowance_minutes,
                "cost_allowance": worksheet.cost_allowance,
                "currency": worksheet.cost_currency,
                "enforcement": "recorded only; full planner is not implemented in T01",
            },
        )
        pending = self._pending(bundle.task_id, bundle.revision_id)
        self._publish(bundle, pending)
        return bundle

    def _pending(self, task_id, revision_id):
        path = self._task_dir(task_id) / f".pending-{revision_id}"
        path.mkdir()
        return path

    def _publish(self, bundle: ReportBundle, pending: Path):
        with (pending / "bundle.json").open("x", encoding="utf-8") as output:
            output.write(bundle.model_dump_json(indent=2))
        revisions = self._task_dir(bundle.task_id) / "revisions"
        revisions.mkdir(exist_ok=True)
        pending.rename(revisions / bundle.revision_id)

    def run(self, task_id: str) -> ReportBundle:
        if self.retriever is None or self.model is None:
            raise ValueError("Running requires an injected retriever and DSPy model")
        parent = self.open(task_id)
        revision_id = new_id()
        pending = self._pending(task_id, revision_id)
        captures: list[Capture] = []
        started = time.monotonic()

        def save_capture(record: dict) -> Capture:
            raw = EvidenceInput.model_validate(record["meta"])
            capture_id = new_id()
            directory = self._task_dir(task_id) / "captures"
            directory.mkdir(exist_ok=True)
            content_path = f"captures/{capture_id}.txt"
            record_path = f"captures/{capture_id}.json"
            with (self._task_dir(task_id) / content_path).open(
                "x", encoding="utf-8"
            ) as output:
                output.write(raw.content)
            with (self._task_dir(task_id) / record_path).open(
                "x", encoding="utf-8"
            ) as output:
                json.dump(record, output, ensure_ascii=False, indent=2)
            capture = Capture(
                capture_id=capture_id,
                content_path=content_path,
                record_path=record_path,
                **raw.model_dump(exclude={"content"}),
            )
            captures.append(capture)
            return capture

        limitations = [
            "Fixture-backed run; no live acquisition or independent verification.",
            "Time and cost allowances are recorded; full budget planning is deferred.",
        ]
        findings: list[Finding] = []
        metrics: dict[str, Any] = {}
        status = "completed"
        try:
            text, citations, metrics = StormAdapter(
                self.retriever, self.model
            ).generate(parent.worksheet, pending, save_capture)
            for paragraph in text.splitlines():
                if not paragraph.strip() or paragraph.lstrip().startswith("#"):
                    continue
                refs = list(dict.fromkeys(re.findall(r"\[(\d+)\]", paragraph)))
                evidence_ids = [
                    citations[int(ref)] for ref in refs if int(ref) in citations
                ]
                if evidence_ids:
                    findings.append(
                        Finding(
                            finding_id=new_id(),
                            text=paragraph.strip(),
                            evidence_ids=evidence_ids,
                        )
                    )
                else:
                    limitations.append("An uncited model paragraph was withheld.")
            if not findings:
                status = "insufficient_evidence"
                limitations.append(
                    "Insufficient evidence to produce supported findings."
                )
        except Exception as error:
            status = "failed"
            limitations.append(f"Run failed ({type(error).__name__}): {error}")

        supplied_services = {capture.service_id for capture in captures}
        limitations.extend(
            f"Required service unmet: {source.service_id}"
            for source in parent.worksheet.selected_sources
            if source.required and source.service_id not in supplied_services
        )
        if parent.worksheet.requested_outputs != ["browser"]:
            limitations.append(
                "T01 delivers a browser report; other outputs are not rendered."
            )
        artifact = Artifact(
            artifact_id=new_id(),
            kind="report_markdown",
            path=f"revisions/{revision_id}/report.md",
            media_type="text/markdown",
            revision_id=revision_id,
        )
        bundle = ReportBundle.model_validate(
            {
                **parent.model_dump(),
                "revision_id": revision_id,
                "parent_revision_id": parent.revision_id,
                "revision_number": parent.revision_number + 1,
                "created_at": self.clock(),
                "status": status,
                "findings": findings,
                "evidence": captures,
                "methods": [
                    "Save original supplied captures before STORM snippet cleaning and URL merging.",
                    "STORM retrieval and article-generation stage with its bounded text context.",
                ],
                "limitations": limitations,
                "usage": Usage(elapsed_seconds=time.monotonic() - started, **metrics),
                "artifacts": [artifact],
            }
        )
        report_text = self._report_markdown(bundle)
        with (pending / "report.md").open("x", encoding="utf-8") as output:
            output.write(report_text)
        self._publish(bundle, pending)
        return bundle

    @staticmethod
    def _report_markdown(bundle: ReportBundle) -> str:
        sections = [
            f"# {bundle.worksheet.title}",
            f"Purpose: {bundle.purpose}",
            f"Revision: {bundle.revision_id} — {bundle.status}",
            "## Findings",
        ]
        for finding in bundle.findings:
            sections.append(f"{finding.text}\n\n{finding.qualification}")
            for capture_id in finding.evidence_ids:
                capture = next(c for c in bundle.evidence if c.capture_id == capture_id)
                sections.append(
                    f"[{capture.title}](../../{capture.content_path}) — {capture_id}"
                )
        sections.extend(
            ["## Limitations", *bundle.limitations, "## Methods", *bundle.methods]
        )
        return "\n\n".join(sections) + "\n"
