# T03: Plan and finish an automatic report within its budget

## Parent

[Information Workbench R1 specification](https://github.com/Moskataza/storm/issues/1)

## What to build

A clear worksheet produces a visible plan sized to the complete requested deliverable. The operator can inspect scope, source/model effort, timing estimates, price assumptions, and reserved delivery resources before automatic execution. As controlled work consumes the allowance, the task finishes an honest report by limiting lower-priority research, rather than pausing solely because acquisition consumed the budget.

## Acceptance criteria

- [ ] The plan includes collection, fallback, processing, analysis, writing, visuals, rendering, and checking, with explicit delivery reserves and bounded request/concurrency/output estimates.
- [ ] Plans below minimum delivery effort propose feasible reduced scope before execution; unknown rates remain unknown until configured or omitted from executable paid work.
- [ ] Controlled rates and a fake clock prove that optional expansion and simultaneous work cannot consume the reserve.
- [ ] Automatic execution reaches a report with coverage limits without routine stage approvals or the default cost-triggered pause rejected in the design.
- [ ] The operator can compare planned versus measured time, token/request usage, and known/estimated charges; estimates and provider billing are distinguished.
- [ ] Source/model failure can still produce an explicit evidence-gap report from retained content; it never invents completion of unavailable deliverables.
- [ ] Workflow tests cover feasible/infeasible plans, concurrency, unknown costs, and research adaptation with final report delivery.

## Specification coverage

AC07, AC08, AC09, automatic portion of AC10, sparse-evidence portion of AC17.

## Blocked by

- T01: Deliver a replayable worksheet-to-report task.

## Demonstration

Run the same clear worksheet under two controlled budgets; show different research breadth, preserved reporting reserves, completed reports, and honest usage summaries.
