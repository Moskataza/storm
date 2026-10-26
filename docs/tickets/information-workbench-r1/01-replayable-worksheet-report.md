# T01: Deliver a replayable worksheet-to-report task

## Parent

[Information Workbench R1 specification](https://github.com/Moskataza/storm/issues/1)

## What to build

An operator enters a clear worksheet in the local browser, supplies a small evidence fixture, runs the task, and reads a purpose-related report. Closing and reopening the task preserves the worksheet, evidence references, report revision, and recorded outcome. This is the first complete path through local persistence, the task-workflow boundary, the STORM adapter, and the browser.

Keep the initial demonstration deterministic and fixture-backed; it does not pretend live acquisition or the full budget planner is already implemented. Add the minimal adapter seams needed without a broad rewrite of existing topic-oriented use.

## Acceptance criteria

- [ ] A worksheet records purpose, priority questions, scope, value/completion criteria, processing needs, audience/language, requested outputs, selected source identities, and time/cost allowances.
- [ ] A fixture-backed run creates identifiable task/report revisions and shows a short browser report with findings and evidence links.
- [ ] The task can be reopened after application restart with the same persisted content; tasks with the same title remain distinct.
- [ ] The public task-workflow boundary accepts injected retrieval/model fixtures. The legacy topic-to-article workflow still passes a deterministic compatibility scenario.
- [ ] A primary workflow test verifies worksheet-to-artifact behavior; a thin browser smoke test verifies create/run/reopen.
- [ ] CI runs the application tests and existing formatting checks without activating package publication or requiring live credentials.

## Specification coverage

AC02, AC12 foundation, AC17 foundation, AC20.

## Blocked by

None (can start immediately).

## Demonstration

Create a small task, run it from supplied evidence, restart the workbench, and reopen the same report and supporting evidence.
