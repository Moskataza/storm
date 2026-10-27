# Local Information Workbench (T01)

This first slice accepts a clear demand worksheet and supplied text evidence,
produces a short cited browser report, and reopens it after a process restart.
The included extractive model quotes supplied records deterministically. It does
not acquire live sources, translate evidence, perform numeric analysis, enforce
budgets, or export HTML/PDF. Those capabilities belong to later R1 tickets.

From the repository root:

```bash
conda activate storm
python -m pip install -r requirements-workbench.txt
python -m streamlit run frontend/workbench/app.py --server.address=127.0.0.1
```

The legacy application remains at `frontend/demo_light/storm.py`.

1. Review the visible example defaults and edit the worksheet.
2. Choose **Save worksheet**. Review or replace **Supplied evidence JSON** using
   the shape in [the example](../../examples/workbench/task.json).
3. Choose **Run task**. Read the purpose, findings, evidence links, qualifications,
   methods, measured usage and recorded allowances.
4. Stop Streamlit, start it again with the same command and workspace, and choose
   **Open task** in the sidebar. The same report revision and evidence are loaded
   from disk, without invoking retrieval or the model.

Tasks default to `local/workbench/` (Git ignored). Set `STORM_WORKSPACE` to choose
another local directory. Task IDs distinguish identical titles. Saving an edit
creates a draft revision; running creates a separate outcome revision. Use
**Report history** to inspect previous reports. Runs repeat the bounded fixture
work; selective invalidation, capture reuse and guided redirection are T08 work.

## Python boundary

```python
import json
from pathlib import Path
from knowledge_storm.workbench import TaskWorkflow, Worksheet
from knowledge_storm.workbench.fixtures import FixtureLM, FixtureRetriever

example = json.loads(Path("examples/workbench/task.json").read_text())
workflow = TaskWorkflow(
    "local/workbench",
    retriever=FixtureRetriever(example["evidence"]),
    model=FixtureLM(),
)
draft = workflow.create(Worksheet.model_validate(example["worksheet"]))
report = workflow.run(draft.task_id)
reopened = TaskWorkflow("local/workbench").open(report.task_id)
assert reopened == report
```

`TaskWorkflow` accepts an operator-configured retriever with STORM's existing
`query_or_queries`/`exclude_urls` callable interface and a DSPy-compatible model.
Each retrieval record supplies `url`, `title`, `description`, `snippets`, and
`meta` conforming to `EvidenceInput` in
[`models.py`](../../knowledge_storm/workbench/models.py). The full original
content belongs in `meta.content`; the snippets are the model projection. The
fixture retriever demonstrates this contract. Malformed or unselected-service
results produce a visible failed revision, retaining already saved captures.
Only operator-installed Python objects are injected; the browser accepts JSON,
never code or package instructions.

## Shared report bundle, version 1

`ReportBundle` is the shared renderer boundary. JSON uses UTF-8 and
`schema_version: 1`. Unknown versions fail validation. All bundle file references
are relative to the task directory; `read_file(task_id, path)` resolves them and
rejects references outside that task.

```text
<workspace>/<task_id>/
  captures/<capture_id>.txt            original supplied content
  captures/<capture_id>.json           original retrieval record
  revisions/<revision_id>/bundle.json  worksheet, metadata and result
  revisions/<revision_id>/report.md    inspectable report artifact
  revisions/<revision_id>/...          STORM stage artifacts
```

The bundle records task creation time, revision ID/number/parent/time, outcome,
worksheet and purpose, findings and their evidence IDs, capture provenance,
datasets, chart specifications, methods, limitations, usage/budget, and output
artifacts. Findings and artifacts receive stable IDs; empty dataset/chart lists
are reserved for later analysis slices, whose objects must also have stable IDs.
Unknown charges remain `null` with an explicit status, not zero or provider billing.
If a run fails before usage is returned, its unavailable query count is also `null`.
Only complete revisions are published by directory rename. Interrupted work can
leave hidden `.pending-*` directories, which history ignores. Storage assumes a
single operator and does not provide concurrent-writer coordination.

Before STORM cleans snippets or merges URL references, the adapter saves a new
capture ID, source/service identities, origin, method/outcome, retrieval and
available publication/observation dates, coverage, original record and content.
STORM sees `urn:storm:capture:<id>` reference identities; the actual origin stays
in the bundle and raw record. Thus repeat captures of one URL remain separately
citable. Persisted IDs never change on reopen. STORM's small-fixture table uses
supplied captures directly, without downloading an embedding model. Its existing
context limit still bounds generation; evidence snapshots retain full content.

## Verification

```bash
conda activate storm
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
python -m mypy
python -m pytest -q
python -m black --check knowledge_storm frontend/workbench tests
```

The primary test uses the public workflow to inspect report and evidence artifacts,
including duplicate titles/URLs and restart persistence. A Chromium smoke test
edits/saves/runs, restarts the Streamlit process, and reopens the original report.
The legacy test continues the topic runner from a supplied draft with injected
retrieval/model fixtures. No paid credentials, live services, or downloaded model
weights are used. CI installs Chromium's OS dependencies with Playwright's
`--with-deps` option. The package publication workflow remains manual.

Existing STORM imports initialize DSPy/LiteLLM caches in the user's home directory;
the account running the app/tests needs normal write access there.
