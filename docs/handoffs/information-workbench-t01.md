# T01 implementation continuation

This supersedes the implementation state in `information-workbench-r1.md`.
That file had pre-existing uncommitted edits and was preserved.

The requester explicitly authorized only T01 / GitHub #2 in this session.
The published issue was open, unassigned, ready-for-agent, and had no comments.
Both its native blocker list and `issue_dependencies_summary.blocked_by` were
empty/zero. It was claimed by assigning the driving GitHub account.

## Delivered boundary

- `knowledge_storm/workbench/`: public `TaskWorkflow`, validated `Worksheet`,
  version 1 `ReportBundle`, fixture retriever/model, and minimal STORM adapter.
- `frontend/workbench/app.py`: worksheet editing, supplied evidence JSON,
  create/run/open, report history, findings, capture links, provenance and limits.
- `examples/workbench/task.json`: fictional bilingual, deterministic demonstration.
- `frontend/workbench/README.md`: setup, demo, testing and persisted contract.
- Application CI runs typechecking and deterministic workflow/legacy/Chromium
  smoke tests; existing Black CI includes the new Python paths. The manual
  package publication workflow was not changed or invoked.
- The shared STORM sentence cleanup recognizes Chinese sentence endings, so
  the fixture's Chinese text survives generation as well as saved captures.

Each task has a UUID, independent of title. Worksheet edits and runs append
immutable revisions with UUIDs, sequence numbers and parent links. Complete
JSON-plus-files revisions become visible by rename. Captures receive UUIDs and
full original content/record files before STORM's cleanup or URL merging.
Capture URNs in STORM's projection keep two captures of one URL separately
citable; origins, source/service IDs, coverage, acquisition outcome and dates
remain in the shared bundle. Opening saved tasks requires no providers.

The fixture model quotes supplied text; the full worksheet reaches its STORM
generation context. Datasets and chart specifications remain empty. Unknown
costs remain unknown. Empty evidence produces an insufficient-evidence report;
a failed model leaves a failed revision with already captured evidence intact.

## Local commands

```bash
conda activate storm
python -m streamlit run frontend/workbench/app.py --server.address=127.0.0.1
python -m mypy
python -m pytest -q
python -m black --check knowledge_storm frontend/workbench tests
```

Development dependencies were installed in the `storm` Conda environment from
`requirements-dev.txt`'s pinned tool versions. Playwright Chromium was installed
for the real browser smoke test. The dependency check reported no broken
requirements. Existing DSPy/LiteLLM imports write caches to the home directory;
normal escalation was used for tests in this restricted environment. Black's
multi-file workers also required normal escalation here.

Verification completed: `python -m pytest -q` passed all **7 tests** (including
the real Chromium restart/reopen journey and legacy compatibility) in 48.66s;
`python -m mypy` passed all 6 workbench Python files; Black checked all 44 Python
files in the package, workbench and tests. `git diff --cached --check` passed.
The implementation skill's independent Standards and Spec reviews each returned
**0 findings**, reviewing the staged implementation against task-start commit
`286ee78af2d2c9255855973da462dbdcea10f664`. No paid credentials or live evidence
sources were required. CI is configured but has not run remotely because these
commits have not been pushed.

## Continuation scope

T02 / #3, T03 / #4 and T07 / #8 are the next independent frontier after T01.
No later ticket was started. The planner, live SEC connector, catalogue,
crawling/browser acquisition, custom extension registration, numeric analysis,
guided selective recomputation, and HTML/PDF exports remain their owning tickets.
Platform access, actual provider costs and export fidelity remain unverified
release gates under T10. A working browser does not establish PDF fidelity.

The workspace remains on `main`. No push or package publication was authorized.
Unrelated `.omc/`, local `AGENTS.md`, Git exclusion entries, and pre-existing
handoff changes must remain intact. The new continuation and tracker manifest
are part of the implementation commit; the pre-existing handoff edit is not.
