# T08: Review and redirect a guided task without losing its history

## Parent

[Information Workbench R1 specification](https://github.com/Moskataza/storm/issues/1)

## What to build

A requester reviews intermediate evidence and analysis in Guided mode, changes a question or criterion, and obtains an updated report from the same task workflow. Previous worksheet, plan, evidence, and report revisions remain inspectable. The updated work is replanned against the remaining allowance while preserving delivery resources.

## Acceptance criteria

- [ ] Guided mode exposes meaningful evidence/analysis checkpoints and permits edits to worksheet requirements.
- [ ] An edit creates an identifiable worksheet/plan revision, invalidates affected downstream work, and retains reusable acquired evidence with provenance.
- [ ] The updated report references its own worksheet/plan revision, and earlier reports remain available rather than being overwritten.
- [ ] Redirection shows its time/cost implications and proposes feasible remaining scope without silently changing the user's purpose.
- [ ] Guided and Automatic modes use the same execution and reporting rules; identical unchanged fixture inputs yield equivalent final findings/data.
- [ ] A workflow test covers redirected completion and history; a browser test covers inspecting evidence, editing, and opening old/new reports.

- [ ] Revisions are immutable. Compare stage inputs and rerun from the earliest changed stage; reuse unchanged captures by stable ID. A presentation-only revision rerenders without reacquiring or reanalyzing evidence.

## Specification coverage

AC03 revisions, guided portion of AC10, revision consistency of AC18.

## Blocked by

- T02: Clarify vague needs and reuse saved worksheets.
- T03: Plan and finish an automatic report within its budget.
- T07: Produce evidence-qualified analysis and trustworthy visuals.

## Demonstration

Review a guided market task, change a priority, finish the updated report, and compare its worksheet/evidence lineage with the retained prior revision.
