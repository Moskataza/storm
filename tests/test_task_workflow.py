from datetime import datetime, timezone
import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from knowledge_storm.workbench import TaskWorkflow, Worksheet
from knowledge_storm.workbench.fixtures import FixtureLM, FixtureRetriever


def test_worksheet_to_report_survives_restart_and_same_title_tasks(tmp_path):
    worksheet = Worksheet(
        title="Research tools / 研究工具",
        purpose="Choose a tool for a local research demonstration",
        priority_questions=["What can the sample tool do?"],
        scope="Only the supplied sample records",
        value_criteria=["Capabilities link to inspectable evidence"],
        completion_criteria=["A short report and saved evidence"],
        processing_needs="Summarize supplied text; no calculations",
        audience="Operator",
        language="English / 中文",
        requested_outputs=["browser"],
        selected_sources=[{"service_id": "fixture", "required": True}],
        time_allowance_minutes=5,
        cost_allowance=1,
        cost_currency="USD",
    )
    records = [
        {
            "source_id": "sample-tool",
            "service_id": "fixture",
            "origin": "https://example.test/tool",
            "title": "Tool note",
            "content": "The sample tool saves local notes. 本地笔记。",
            "retrieved_at": "2026-10-01T12:00:00Z",
            "published_at": "2026-09-30T00:00:00Z",
            "coverage": ["text"],
        },
        {
            "source_id": "sample-tool",
            "service_id": "fixture",
            "origin": "https://example.test/tool",
            "title": "A second capture of the same URL",
            "content": "The sample tool can reopen saved notes.",
            "retrieved_at": "2026-10-02T12:00:00Z",
            "coverage": ["text"],
        },
    ]
    workflow = TaskWorkflow(
        tmp_path,
        retriever=FixtureRetriever(records),
        model=FixtureLM(),
        clock=lambda: datetime(2026, 10, 3, tzinfo=timezone.utc),
    )
    draft = workflow.create(worksheet)
    report = workflow.run(draft.task_id)
    assert report.status == "completed"
    assert report.revision_id != draft.revision_id
    assert report.parent_revision_id == draft.revision_id
    assert report.worksheet == worksheet
    assert len(report.evidence) == 2
    assert len({capture.capture_id for capture in report.evidence}) == 2
    assert {capture.origin for capture in report.evidence} == {
        "https://example.test/tool"
    }
    assert any("本地笔记" in finding.text for finding in report.findings)
    assert all(finding.evidence_ids for finding in report.findings)
    evidence_ids = {capture.capture_id for capture in report.evidence}
    assert all(set(f.evidence_ids) <= evidence_ids for f in report.findings)
    assert report.datasets == []
    assert report.chart_specifications == []
    assert report.usage.estimated_cost is None
    assert report.budget["cost_allowance"] == 1
    artifact = next(a for a in report.artifacts if a.kind == "report_markdown")
    assert "本地笔记" in workflow.read_file(report.task_id, artifact.path)
    assert report.purpose == worksheet.purpose

    # A fresh facade has no injected providers or in-memory report state.
    reopened = TaskWorkflow(tmp_path)
    assert reopened.open(report.task_id) == report
    assert reopened.open(report.task_id, draft.revision_id) == draft
    assert "本地笔记" in reopened.read_file(
        report.task_id, report.evidence[0].content_path
    )
    assert reopened.create(worksheet).task_id != report.task_id
    assert len(reopened.list_tasks()) == 2


def test_revision_preserves_original_capture_and_prior_report(tmp_path):
    example = json.loads(
        Path("examples/workbench/task.json").read_text(encoding="utf-8")
    )
    original = "  Original source citation [7]. 保留原文。\n"
    example["evidence"][0]["content"] = original
    workflow = TaskWorkflow(
        tmp_path,
        retriever=FixtureRetriever(example["evidence"]),
        model=FixtureLM(),
    )
    draft = workflow.create(Worksheet.model_validate(example["worksheet"]))
    first_report = workflow.run(draft.task_id)
    capture = first_report.evidence[0]
    assert workflow.read_file(draft.task_id, capture.content_path) == original
    revised = workflow.revise(
        draft.task_id,
        Worksheet.model_validate(
            {**example["worksheet"], "purpose": "A revised purpose"}
        ),
    )
    assert revised.revision_id != first_report.revision_id
    assert revised.parent_revision_id == first_report.revision_id
    assert workflow.open(draft.task_id, first_report.revision_id) == first_report
    assert workflow.open(draft.task_id, draft.revision_id) == draft
    assert workflow.read_file(draft.task_id, capture.content_path) == original
    assert len(workflow.history(draft.task_id)) == 3


def test_blank_priority_question_is_not_a_clear_worksheet():
    example = json.loads(Path("examples/workbench/task.json").read_text())
    example["worksheet"]["priority_questions"] = ["  "]
    with pytest.raises(ValidationError, match="priority_questions"):
        Worksheet.model_validate(example["worksheet"])


def test_empty_evidence_produces_insufficient_evidence_report(tmp_path):
    example = json.loads(Path("examples/workbench/task.json").read_text())
    workflow = TaskWorkflow(tmp_path, retriever=FixtureRetriever([]), model=FixtureLM())
    draft = workflow.create(Worksheet.model_validate(example["worksheet"]))
    report = workflow.run(draft.task_id)
    assert report.status == "insufficient_evidence"
    assert report.findings == []
    assert report.chart_specifications == []
    assert "Required service unmet: fixture" in report.limitations
    assert "Insufficient evidence" in workflow.read_file(
        report.task_id, report.artifacts[0].path
    )
    assert TaskWorkflow(tmp_path).open(report.task_id) == report


def test_model_failure_preserves_captures_and_failure_outcome(tmp_path):
    class UnavailableModel(FixtureLM):
        def basic_request(self, prompt, **kwargs):
            raise RuntimeError(
                "Injected model is unavailable; configure a model and rerun."
            )

    example = json.loads(Path("examples/workbench/task.json").read_text())
    workflow = TaskWorkflow(
        tmp_path,
        retriever=FixtureRetriever(example["evidence"]),
        model=UnavailableModel(),
    )
    draft = workflow.create(Worksheet.model_validate(example["worksheet"]))
    report = workflow.run(draft.task_id)
    assert report.status == "failed"
    assert any("configure a model and rerun" in item for item in report.limitations)
    assert len(report.evidence) == 1
    assert workflow.read_file(report.task_id, report.evidence[0].content_path) == (
        "The example can save and reopen local notes. 本地笔记可以保存并重新打开。"
    )
    assert TaskWorkflow(tmp_path).open(report.task_id) == report
    assert workflow.open(report.task_id, draft.revision_id) == draft
