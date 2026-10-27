"""Run from the repo root: python -m streamlit run frontend/workbench/app.py."""

import json
import os
from pathlib import Path
import re
import sys

import streamlit as st
from pydantic import ValidationError

# Streamlit executes a script, rather than a package module.
REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from knowledge_storm.workbench import TaskWorkflow, Worksheet
from knowledge_storm.workbench.fixtures import FixtureLM, FixtureRetriever


def lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def show_report(workflow, bundle):
    st.subheader("Report")
    st.caption(f"Report revision: {bundle.revision_id}")
    st.write(f"Outcome: {bundle.status}")
    st.write(f"Purpose: {bundle.purpose}")
    for finding in bundle.findings:
        # STORM's numeric citations are converted to capture links for this view.
        st.markdown(re.sub(r"\[\d+\]", "", finding.text))
        st.caption(finding.qualification)
        for index, capture_id in enumerate(finding.evidence_ids, 1):
            st.markdown(f"[Evidence {index}](#capture-{capture_id})")
    for limitation in bundle.limitations:
        st.warning(limitation)
    with st.expander("Supporting evidence", expanded=True):
        for capture in bundle.evidence:
            st.markdown(
                f'<span id="capture-{capture.capture_id}"></span>',
                unsafe_allow_html=True,
            )
            st.write(capture.title)
            st.text(workflow.read_file(bundle.task_id, capture.content_path))
            st.json(capture.model_dump(mode="json"))
    with st.expander("Methods, usage and allowances"):
        st.write(bundle.methods)
        st.json(bundle.usage.model_dump(mode="json"))
        st.json(bundle.budget)


def main():
    st.set_page_config(page_title="Information Workbench", layout="wide")
    st.title("Information Workbench")
    st.info(
        "T01 demonstration: supplied evidence and a deterministic extractive model. "
        "Review the example defaults below. Allowances are recorded only."
    )
    example = json.loads(
        (REPO_ROOT / "examples/workbench/task.json").read_text(encoding="utf-8")
    )
    workflow = TaskWorkflow(os.environ.get("STORM_WORKSPACE", "local/workbench"))
    tasks = workflow.list_tasks()
    with st.sidebar:
        st.header("Saved tasks")
        if tasks:
            by_id = {bundle.task_id: bundle for bundle in tasks}
            chosen = st.selectbox(
                "Saved task",
                list(by_id),
                format_func=lambda task_id: (
                    f"{by_id[task_id].worksheet.title} · {task_id[:8]}"
                ),
            )
            if st.button("Open task"):
                st.session_state.active_task_id = chosen
                st.rerun()
        if st.button("New task"):
            st.session_state.active_task_id = None
            st.rerun()

    task_id = st.session_state.get("active_task_id")
    bundle = workflow.open(task_id) if task_id else None
    defaults = bundle.worksheet.model_dump() if bundle else example["worksheet"]
    form_key = bundle.revision_id if bundle else "new"
    with st.form(f"worksheet-{form_key}"):
        st.subheader("Demand worksheet")
        values = {}
        for key, label in [
            ("title", "Title"),
            ("purpose", "Purpose"),
            ("scope", "Scope"),
            ("processing_needs", "Processing needs"),
            ("audience", "Audience"),
            ("language", "Language"),
        ]:
            values[key] = st.text_input(label, defaults[key])
        for key, label in [
            ("priority_questions", "Priority questions (one per line)"),
            ("value_criteria", "Value criteria (one per line)"),
            ("completion_criteria", "Completion criteria (one per line)"),
            ("requested_outputs", "Requested outputs (T01 supports browser)"),
        ]:
            values[key] = lines(st.text_area(label, "\n".join(defaults[key])))
        services = st.text_area(
            "Allowed service identities (one per line)",
            "\n".join(s["service_id"] for s in defaults["selected_sources"]),
        )
        required = st.text_area(
            "Required service identities (one per line)",
            "\n".join(
                s["service_id"] for s in defaults["selected_sources"] if s["required"]
            ),
        )
        values["selected_sources"] = [
            {"service_id": service, "required": service in lines(required)}
            for service in lines(services)
        ]
        values["time_allowance_minutes"] = st.number_input(
            "Time allowance (minutes)",
            min_value=0.1,
            value=float(defaults["time_allowance_minutes"]),
        )
        values["cost_allowance"] = st.number_input(
            "Cost allowance", min_value=0.0, value=float(defaults["cost_allowance"])
        )
        values["cost_currency"] = st.text_input(
            "Cost currency", defaults["cost_currency"]
        )
        if st.form_submit_button("Save worksheet"):
            try:
                if not set(lines(required)) <= set(lines(services)):
                    raise ValueError("Required services must also be allowed services.")
                worksheet = Worksheet.model_validate(values)
                saved = (
                    workflow.revise(task_id, worksheet)
                    if task_id
                    else workflow.create(worksheet)
                )
                st.session_state.active_task_id = saved.task_id
                st.rerun()
            except (ValidationError, ValueError) as error:
                st.error(f"Check the worksheet: {error}")

    evidence_defaults = example["evidence"]
    if bundle:
        previous_report = next(
            (r for r in reversed(workflow.history(bundle.task_id)) if r.evidence), None
        )
        if previous_report:
            evidence_defaults = [
                json.loads(workflow.read_file(bundle.task_id, c.record_path))["meta"]
                for c in previous_report.evidence
            ]
    evidence_json = st.text_area(
        "Supplied evidence JSON",
        json.dumps(evidence_defaults, ensure_ascii=False, indent=2),
        height=240,
    )
    st.caption(
        "Save worksheet edits before running. Evidence is saved when the task runs."
    )
    if st.button("Run task", disabled=bundle is None):
        try:
            retriever = FixtureRetriever(json.loads(evidence_json))
            task_runner = TaskWorkflow(
                workflow.root, retriever=retriever, model=FixtureLM()
            )
            with st.spinner("Creating report…"):
                task_runner.run(task_id)
            st.rerun()
        except (ValidationError, ValueError, TypeError) as error:
            st.error(f"Check the supplied evidence: {error}")
    if bundle:
        st.caption(f"Task ID: {bundle.task_id}")
        revisions = workflow.history(bundle.task_id)
        revision_id = st.selectbox(
            "Report history",
            [revision.revision_id for revision in reversed(revisions)],
            format_func=lambda value: next(
                f"Revision {r.revision_number} · {r.status} · {value[:8]}"
                for r in revisions
                if r.revision_id == value
            ),
        )
        saved_report = workflow.open(bundle.task_id, revision_id)
        if saved_report.status != "draft":
            show_report(workflow, saved_report)


if __name__ == "__main__":
    main()
