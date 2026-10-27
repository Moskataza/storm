# Information Workbench R1 ticket proposal

Status: published and verified. The requester explicitly approved commit 3963284 and authorized publication. Local files preserve the approved ticket content; GitHub uses native sub-issue and blocking relationships.

Parent specification: [GitHub #1](https://github.com/Moskataza/storm/issues/1). The primary workflow testing seam and thin browser checks were approved by the requester before specification publication.

T01–T09 deliver demonstrable vertical slices; T10 is the release-verification slice. Each implementation ticket delivers a demonstrable vertical slice, includes observable acceptance criteria and a verification approach, and is intended to fit one fresh implementation context. Existing retrieval/model injection permits a narrow task adapter, so a separate broad prefactoring ticket is not required.

1. **[T01: Deliver a replayable worksheet-to-report task](01-replayable-worksheet-report.md)**
   - **Blocked by:** none.
   - **What it delivers:** create a worksheet, run a fixture-backed report, restart, and reopen its persisted evidence and result; retain legacy workflow compatibility and establish application CI.
2. **[T02: Clarify vague needs and reuse saved worksheets](02-clarify-and-reuse-needs.md)**
   - **Blocked by:** T01.
   - **What it delivers:** conversation and worksheet editing turn an unclear need into a runnable task; reuse keeps task requirements and lasting preferences separate.
3. **[T03: Plan and finish an automatic report within its budget](03-plan-complete-delivery-within-budget.md)**
   - **Blocked by:** T01.
   - **What it delivers:** inspect a complete-delivery plan, run automatically, preserve reporting resources, and compare planned/observed usage in a completed report.
4. **[T04: Select described services and report from a real public API](04-select-services-and-use-public-api.md)**
   - **Blocked by:** T03.
   - **What it delivers:** browse service capabilities, let the LLM call approved tools, select permitted/required sources, and report from SEC EDGAR; catalogue discovery does not authorize execution.
5. **[T05: Acquire web evidence with browser fallback and honest access gaps](05-acquire-web-content-and-browser-fallback.md)**
   - **Blocked by:** T04.
   - **What it delivers:** web acquisition and bounded Playwright/crawler fallback reach a report, preserving inaccessible required sources and deterministic capability-probe interfaces; T10 owns live platform outcomes.
6. **[T06: Use a custom source and Python processing module in a report](06-use-custom-source-and-processing-module.md)**
   - **Blocked by:** T04.
   - **What it delivers:** operator-added source and processing capabilities produce visible, attributed report data without changing core execution.
7. **[T07: Produce evidence-qualified analysis and trustworthy visuals](07-evidence-qualified-analysis-and-visuals.md)**
   - **Blocked by:** T01.
   - **What it delivers:** fixture-backed findings, numeric comparisons and charts expose evidence, disagreement, lineage, methods, uncertainty, and missing values independently of live providers.
8. **[T08: Review and redirect a guided task without losing its history](08-review-and-redirect-guided-task.md)**
   - **Blocked by:** T02, T03, T07.
   - **What it delivers:** review intermediate evidence, revise a task, replan affected work, and compare retained old/new report revisions.
9. **[T09: Deliver matching browser, HTML and PDF report artifacts](09-deliver-browser-html-pdf-report-pack.md)**
   - **Blocked by:** T03, T07.
   - **What it delivers:** download client-ready artifacts from the same saved result and verify Chinese/English text, charts, formulas, long tables, citations, appendices, and visible export failure.
10. **[T10: Demonstrate R1 across finance and the Chinese AI market](10-demonstrate-release-across-two-domains.md)**
    - **Blocked by:** T05, T06, T08, T09.
    - **What it delivers:** reproducible cross-domain operator demonstrations and an honest release capability matrix covering live access, real provider costs, export fidelity, tests, and deferred functionality.

## Dependency frontier

Start with T01. Then T02, T03, and T07 can proceed independently. T03 unlocks T04; T04 unlocks T05 and T06. T02/T03/T07 unlock T08; T03/T07 unlock T09. T05/T06/T08/T09 unlock the final release demonstration, T10.

These are minimal direct blockers: transitive prerequisites are not repeated on every ticket.

## Acceptance coverage

| Specification criteria | Owning slices |
| --- | --- |
| AC01–AC03 | T01, T02, T08 |
| AC04–AC06 | T04, T05, T06 |
| AC07–AC10 | T03, T08 |
| AC11–AC13 | T01, T04, T05, T06 |
| AC14–AC17 | T03, T07 |
| AC18–AC20 | T01, T08, T09 |
| AC21 | T07, T10 |
| AC22–AC24 | T04, T05, T09, T10 |

## Published references

| Draft | GitHub issue | Blocked by |
| --- | --- | --- |
| T01 | [#2](https://github.com/Moskataza/storm/issues/2) — Deliver a replayable worksheet-to-report task | None |
| T02 | [#3](https://github.com/Moskataza/storm/issues/3) — Clarify vague needs and reuse saved worksheets | [#2](https://github.com/Moskataza/storm/issues/2) |
| T03 | [#4](https://github.com/Moskataza/storm/issues/4) — Plan and finish an automatic report within its budget | [#2](https://github.com/Moskataza/storm/issues/2) |
| T04 | [#5](https://github.com/Moskataza/storm/issues/5) — Select described services and report from a real public API | [#4](https://github.com/Moskataza/storm/issues/4) |
| T05 | [#6](https://github.com/Moskataza/storm/issues/6) — Acquire web evidence with browser fallback and honest access gaps | [#5](https://github.com/Moskataza/storm/issues/5) |
| T06 | [#7](https://github.com/Moskataza/storm/issues/7) — Use a custom source and Python processing module in a report | [#5](https://github.com/Moskataza/storm/issues/5) |
| T07 | [#8](https://github.com/Moskataza/storm/issues/8) — Produce evidence-qualified analysis and trustworthy visuals | [#2](https://github.com/Moskataza/storm/issues/2) |
| T08 | [#9](https://github.com/Moskataza/storm/issues/9) — Review and redirect a guided task without losing its history | [#3](https://github.com/Moskataza/storm/issues/3), [#4](https://github.com/Moskataza/storm/issues/4), [#8](https://github.com/Moskataza/storm/issues/8) |
| T09 | [#10](https://github.com/Moskataza/storm/issues/10) — Deliver matching browser, HTML and PDF report artifacts | [#4](https://github.com/Moskataza/storm/issues/4), [#8](https://github.com/Moskataza/storm/issues/8) |
| T10 | [#11](https://github.com/Moskataza/storm/issues/11) — Verify R1 and demonstrate finance and the Chinese AI market | [#6](https://github.com/Moskataza/storm/issues/6), [#7](https://github.com/Moskataza/storm/issues/7), [#9](https://github.com/Moskataza/storm/issues/9), [#10](https://github.com/Moskataza/storm/issues/10) |

All ten issues are open with ready-for-agent and native parent #1. All 15 blocking edges were read back and verified. The approved bodies match publication, with textual draft blocker sections replaced by native relationships. The parent body/state were unchanged.

Implementation has not started and is not authorized. Once explicitly instructed to implement, the initial frontier is T01 / #2. Keep platform access, real provider costs, and export fidelity as release verification work.
