# T09: Deliver matching browser, HTML and PDF report artifacts

## Parent

[Information Workbench R1 specification](https://github.com/Moskataza/storm/issues/1)

## What to build

An operator opens the visual report and downloads HTML and PDF versions suitable for client delivery. All views render the same saved findings, datasets, evidence, methods, limitations, and report revision. Relevant expandable browser detail becomes printable appendices, and interactive charts receive readable static counterparts.

## Acceptance criteria

- [ ] Implement the shared report bundle and the selected browser/HTML/PDF renderer adapters, with rendering/checking effort charged against the delivery reserve.
- [ ] Browser, HTML, and PDF agree on conclusions, key values, source references, qualifications, and report identity; export does not rerun research or analysis.
- [ ] The fidelity fixture includes Chinese/English text, formulas, source citations, chart labels, long tables, missing data, and evidence/methods appendices.
- [ ] Inspect rendered pages and extracted text: no missing glyphs, lost citations, clipped tables/figures, invisible qualifications, or misleading static charts. Record the renderer versions, required fonts/tools, observed results, and any limits.
- [ ] Export failure is visible and retryable from saved report content; no broken file is marked delivered.
- [ ] Record whether Quarto/Plotly installation and static export meet the fixture; if not, evaluate an alternative renderer against the same acceptance case before claiming readiness.
- [ ] Workflow checks compare semantic artifact content and report revisions; a browser check exercises downloads. Document the reproducible fidelity check as release evidence.

## Specification coverage

AC18, AC19, export-fidelity portion of AC22, AC24.

## Blocked by

- T03: Plan and finish an automatic report within its budget.
- T07: Produce evidence-qualified analysis and trustworthy visuals.

## Demonstration

Show the browser overview and evidence, download HTML/PDF, and verify the same values and qualifications on representative exported pages.
