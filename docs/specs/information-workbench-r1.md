# Information Workbench R1: user-directed information work

## Problem Statement

People often begin information work without a clear definition of what they need to understand, decide, or produce. Collecting more results does not establish their relevance or reliability. Users need help clarifying their purpose, choosing useful sources, applying appropriate processing, and receiving readable conclusions whose supporting evidence and limits remain visible.

STORM currently accepts a topic and produces a cited article. It offers reusable retrieval and generation capabilities, but a topic does not express a requester's success criteria, selected services, processing needs, time/cost allowance, or delivery requirements. The first release must support information work across subjects; financial research and Chinese AI-market research are validation cases, not the product boundary.

## Solution

Provide a local, operator-assisted workbench. A requester and operator clarify a User need through conversation and an editable Demand worksheet. They select permitted and Required services, define the desired deliverable, and obtain a Task plan sized to the Task budget. A shared workflow collects evidence, invokes appropriate processing modules, forms qualified conclusions, and delivers a Visual report.

Guided mode permits intermediate review and redirection. Automatic mode completes a sufficiently clear task without routine stage approvals. Both modes preserve the worksheet, plan, evidence, data, usage, and outputs as a reproducible local task record.

### First release

R1 is a single-operator local browser application with online source access. It includes:

- Editable worksheets, guided clarification, task history, reusable needs, and explicitly saved preferences.
- Optional/required service selection using keyword search and detailed capability descriptions. The public-apis catalogue supplies discovery entries; enabled connectors provide executable services.
- A working configured web-search service, HTTP page acquisition, a bounded browser/crawler fallback, at least one verified public-API integration, and operator-configured custom website/API sources.
- Accessible text, structured data, and available captions/transcripts. Every acquisition records what content was actually obtained.
- Python extension contracts for connectors, processors, analyzers, and renderers, demonstrated by a custom source and processing function.
- Planning across the complete requested deliverable, including acquisition, analysis, writing, visuals, rendering, and checks. Research breadth and depth fit the budget and preserve resources for delivery.
- Evidence-linked findings, quantitative tables/charts when supported, and explicit disagreements, uncertainty, missing data, and access gaps.
- Interactive browser reports and downloadable HTML/PDF artifacts derived from the same saved report content. Chinese and English inputs and text must survive collection, display, and export.
- Two reproducible cross-domain examples: financial information work and Chinese AI-market research spanning hardware, software, agent skills, workflows, prompt packs, agent systems, and platforms.

The AI-market example studies product categories, target users, observed needs, competing offerings, pricing, sample demand signals, and supported opportunities. Rednote and Bilibili are requested sources whose actual access capabilities must be tested and honestly described. Sample observations must not be presented as representative market statistics without supporting evidence.

An original summary video derived from a report is an agreed optional capability, deferred beyond R1. Its scope and resources must be included explicitly when that output is introduced.

## User Stories

1. As a requester, I want to describe an unclear interest, so that I can begin before knowing the exact research question.
2. As a requester, I want the system to suggest possible purposes and ask relevant clarification questions, so that I can work out what I want to do.
3. As an operator, I want to help complete a worksheet during a conversation, so that I can deliver useful work before a hosted self-service product exists.
4. As a requester, I want to edit the purpose, priority questions, scope, audience, language, depth, and output requirements, so that the work reflects my needs.
5. As a requester, I want explicit value criteria and completion criteria, so that collecting more information does not substitute for a useful answer.
6. As a requester, I want minor assumptions to be visible, so that I can correct them without answering an unnecessarily long form.
7. As an operator, I want to save, reopen, and revise tasks, so that work survives application restarts.
8. As a requester, I want to reuse previous worksheets, so that similar tasks do not require starting from nothing.
9. As a requester, I want lasting preference changes to be explicit, so that one occasional interest does not silently affect unrelated tasks.
10. As a requester, I want to search services by keyword and read detailed descriptions, so that I can choose suitable information sources.
11. As a requester, I want to understand a service's coverage, content types, inputs, outputs, authentication, costs, limits, and readiness, so that I can make an informed selection.
12. As a requester, I want to allow optional sources and mark essential sources as required, so that the task reflects the importance of each source.
13. As an operator, I want executable services to be distinguishable from discovery-only catalogue entries, so that users know what is available now.
14. As an operator, I want to configure a requester-supplied website or API, so that custom sources can support a task.
15. As an ordinary requester, I want ready-to-use services without configuring APIs, so that integration work is handled for me.
16. As an operator, I want to add a Python connector or processing module, so that the system can grow beyond its initial capabilities.
17. As a requester, I want to set time and cost allowances, so that I can control the resources committed to a worksheet.
18. As a requester, I want the system to propose an achievable scope and schedule before starting, so that it can finish the requested deliverable within the plan.
19. As an operator, I want reporting resources reserved before expanding research, so that acquisition cannot consume the effort needed to deliver the result.
20. As a requester, I want usage and coverage compared with the plan, so that I understand what was accomplished and what remains uncertain.
21. As a requester, I want guided review of intermediate evidence and analysis, so that I can redirect work when my needs change.
22. As a requester, I want automatic execution for clear requests, so that routine stage decisions do not require my attention.
23. As an operator, I want task revisions to preserve previous results and refresh affected work, so that redirection does not destroy the audit trail.
24. As a requester, I want source acquisition to use suitable APIs, HTTP retrieval, or browser/crawler fallbacks, so that normally accessible information can be collected.
25. As a requester, I want to be notified when a required source is inaccessible, so that I understand the limits of the result.
26. As a requester, I want reports to state which text, data, captions, or transcripts were examined, so that metadata is not mistaken for full-content analysis.
27. As a requester, I want findings to link to evidence with dates and context, so that I can inspect the basis of a conclusion.
28. As a requester, I want source claims, experiences, opinions, promotions, and calculated results distinguished, so that I can assess their meaning.
29. As a requester, I want unknown sponsorship and conflicting evidence shown honestly, so that certainty is not invented.
30. As a requester, I want likes and views shown as contextual signals, so that popularity does not become an unsupported reliability claim.
31. As a requester, I want duplicate or derivative material recognized, so that repeated claims do not appear to be independent confirmations.
32. As a requester, I want appropriate calculations and comparisons based on structured data, so that analysis supports my purpose.
33. As a requester, I want observation dates, periods, units, currencies, and methods preserved, so that comparisons are interpretable.
34. As a requester, I want missing or incompatible data identified, so that charts do not silently invent or mix values.
35. As a requester, I want a concise visual overview followed by supporting detail, so that the report is comfortable to read.
36. As a requester, I want interactive charts and tables where they help, so that I can explore the analysis.
37. As a requester, I want a PDF suitable for client delivery, so that I can share and retain a readable result.
38. As a requester, I want browser and exported reports to agree on findings and data, so that changing format does not change the analysis.
39. As a requester, I want expandable evidence included in an export appendix where relevant, so that important qualifications survive PDF delivery.
40. As an operator, I want reports to work with Chinese and English text, formulas, long tables, and citations, so that the examples can be delivered without corrupted content.
41. As an operator, I want repeatable examples in finance and AI-market research, so that I can demonstrate the system's generality.
42. As an operator, I want dated verification records for source access, provider costs, and export fidelity, so that release claims match observed capabilities.
43. As a requester, I want an honest report even when evidence is sparse, so that an incomplete investigation is not disguised as a confident answer.
44. As an operator, I want future output modules to use saved findings and data, so that an optional promotional video can be added without repeating the research.

## Observable Acceptance Criteria

Each criterion is observable through the public task workflow, persisted artifacts, or the local browser interface. Exact generated wording is not an acceptance condition.

| ID | Scenario and observable result |
| --- | --- |
| AC01 | Starting from a vague request, the workbench proposes relevant directions and records the chosen purpose and priority questions in an editable worksheet; purpose changes are not silently invented. |
| AC02 | The operator can create, save, close, reopen, and revise a worksheet containing purpose, scope, value/completion criteria, processing needs, selected sources, audience, language, outputs, time allowance, and cost allowance. |
| AC03 | Reusing a task preserves its history and creates an identifiable new revision; a task-local interest does not change saved preferences until explicitly selected for reuse. |
| AC04 | Keyword search returns service descriptions with declared capabilities, coverage, input/output examples, authentication, costs/limits, supported content, and readiness. Discovery-only entries cannot be executed as configured connectors. |
| AC05 | A run uses only permitted services; required services are tracked separately. Excluded services are never invoked, and an unavailable required source remains visibly unmet in the delivered report. |
| AC06 | An operator configures one custom website/API source and one custom Python processing module; a task uses their output in a visible table or conclusion with provenance. Invalid configuration returns an actionable validation error. |
| AC07 | Before execution, the plan shows scope, stage allocations, expected requests/model usage, price assumptions or unknowns, timing estimates, acquisition fallback limits, and a delivery reserve. A plan below the minimum feasible delivery effort proposes a smaller scope before running. |
| AC08 | With controlled prices and a fake clock, acquisition and concurrent work cannot consume the reporting reserve. When extra research would exceed the plan, lower-priority expansion is skipped and a report is produced with coverage limits; a cost-triggered pause is not the normal outcome. |
| AC09 | Planned versus measured elapsed time, request counts, token usage, and estimated/known charges appear in the task record. Unknown charges are labeled unknown, not zero, and estimation is distinguished from actual provider billing. |
| AC10 | Automatic mode completes a clear worksheet through reporting without routine stage approvals. Guided mode exposes intermediate work and applies a user revision to affected subsequent work while retaining the prior revision. |
| AC11 | A rendered-page fixture that fails ordinary extraction succeeds through the configured browser fallback; a source that remains unavailable produces an access-gap record rather than disappearing. Fallback attempts use the same source requirement and are included in the plan. |
| AC12 | Every used source capture has an identifier, source/service identity, URL or supplied-origin reference, acquisition method/outcome, retrieval time, available publication/observation time, actual content coverage, and a reference to the saved content. Repeat captures remain distinguishable. |
| AC13 | Text-only, metadata-only, and transcript-containing fixtures remain distinct. A video title alone cannot support a claim about its spoken content. |
| AC14 | Each substantive finding identifies supporting source evidence or a reproducible calculation. Unsupported synthesis is withheld or visibly qualified. Source claims, experiences, opinions, promotions when evidenced, calculations, and unknown sponsorship retain their labels. |
| AC15 | Conflicting and repeated-source fixtures yield visible disagreements and source lineage. Likes/views may be displayed, but do not by themselves make a finding verified or establish representative market demand. |
| AC16 | A structured comparison fixture produces expected numeric values with methods, periods, units/currency, and source references. Missing values are not converted to zero; incompatible quantities are not combined without an explicit, recorded transformation. |
| AC17 | The report opens with purpose-related findings and provides appropriate visuals, evidence, uncertainty, methods, dates, and usage. Sparse or absent evidence produces an explicit insufficient-evidence report without fabricated charts or conclusions. |
| AC18 | Browser, downloadable HTML, and PDF refer to the same saved report revision and agree on key values, conclusions, citations, and qualifications. Exporting does not trigger a second research or analysis run. |
| AC19 | The PDF includes readable static charts, full relevant evidence/methods appendices, selectable Chinese/English text, formulas, page breaks, and long tables. It has no missing glyphs, clipped content, or lost citations in the agreed fidelity fixture. |
| AC20 | The existing topic-to-article entry point still works with a deterministic injected retriever/model configuration, preserving backward compatibility. |
| AC21 | Financial and Chinese AI-market fixture tasks run through the same workflow without domain-specific forks. AI categories include hardware, software, agent skills, workflows, prompt packs, agent systems, and platforms, with overlapping/extensible classification. |
| AC22 | Release evidence contains dated platform access probes, configured-provider cost assumptions plus a measured sample run, and an HTML/PDF fidelity check. Each capability is reported as supported, limited, unavailable, or unverified with observed reasons. |
| AC23 | At least one configured search service, one normally accessible web source, and one catalogue-derived public API have an observed end-to-end retrieval-to-report demonstration. Both Rednote and Bilibili have documented probe outcomes; unsupported platform-wide access is never advertised. |
| AC24 | Export/render failure is shown as a failed deliverable with preserved report content and an actionable retry; it is not mislabeled as successful PDF delivery. |

## Implementation Decisions

- Keep the workbench general. Domain examples configure worksheets, services, processing, and report requirements rather than creating separate finance and market-research products.
- Use the Demand worksheet as shared task context throughout collection, processing, analysis, and writing. Preserve the rationale that a topic alone cannot express useful outcomes.
- Add a local task-workflow facade around the existing STORM runner and its injected retriever/model capabilities. Keep existing topic-oriented use compatible. Reuse existing stage timing, token usage, request counts, callbacks, and bounded runner controls.
- Separate the local browser interface from task execution. Guided and Automatic modes invoke the same workflow; guided review changes interaction checkpoints, not the evidence or reporting rules.
- Persist one local workspace per task with identifiable worksheet/plan/report revisions, source snapshots, structured datasets, evidence/finding references, generated outputs, and usage. Refresh affected work after edits rather than silently mixing revisions.
- Treat catalogue entries and executable integrations as different readiness states. Import a versioned public-apis discovery snapshot and seed executable services with verified capabilities. A catalogue URL is not an API contract.
- Make ordinary source selection a task decision. Custom website/API integration and Python module registration are operator/developer activities. Registered capabilities declare purpose, inputs, outputs, requirements, and estimated resource use.
- Acquire through the appropriate configured API or HTTP path. Use a simple crawler for suitable static pages and Playwright for suitable rendered pages. Record notifications, attempts, content outcomes, and remaining gaps. Browser rendering does not imply platform-wide search, transcript availability, or guaranteed recovery of an unavailable page.
- Retain original captures and structured evidence outside STORM's snippet representation. Pass stable evidence references and relevant text into generation. Repeated URLs, record identities, and captures must not erase provenance or imply independent corroboration.
- Evaluate usefulness against worksheet value criteria and describe evidence quality with inspectable reasons. Do not invent an absolute truth score. Source labels and extraction/transcription uncertainty are retained through synthesis.
- Execute numeric transformations in registered deterministic processors, record their inputs/methods, and use those results for charts. Generated prose may interpret results but cannot invent the underlying numbers.
- Plan the complete deliverable before execution, using configured provider rates and measured stage histories where available. Reserve work for synthesis, visuals, rendering, and checks before optional expansion. Bound requests, fallback attempts, timeouts, concurrency, and generation output sizes against the plan.
- Treat time/cost as planning constraints with visible estimation uncertainty. Feasible scope is established upfront; runtime adaptation reduces lower-priority research and finishes an honest report. Unexpected provider outages or renderer failures remain visible outcomes rather than false completion claims.
- Use a shared structured report bundle for the browser and exports. The working choice is Streamlit for local interaction, Plotly for charts, and Quarto for HTML/PDF publishing, subject to a renderer installation/fidelity check. This adds a report-export capability, not a separate analysis pass.
- Expand relevant interactive evidence into printable appendices and render charts statically for PDF. Preserve Chinese text, original-language evidence, formulas, dates, units, and citations across formats.
- Keep future original-summary-video generation behind the report-output extension contract; R1 preserves the report data it will need, but does not advertise a working video renderer.

## Testing Decisions

The requester approved these testing seams during specification preparation.

- The primary boundary is the complete public local task workflow: worksheet and plan in; saved evidence, analysis, usage, and report artifacts out. Prefer assertions at this boundary to tests of prompts, internal call ordering, private methods, or field-for-field copies of implementation.
- Reuse existing dependency injection for retrieval/models, staged runner execution, callbacks, and usage collection. Supply deterministic source/model fixtures, a fake clock, and a rate card through the workflow boundary. Add only focused contract checks where invalid extension data or numeric transformations require precise diagnosis.
- Add a small browser acceptance set covering worksheet editing, clarification, service selection, guided redirection, task reopening, and report downloads. Business behavior remains covered through the main workflow rather than duplicated across many browser tests.
- Exercise budget completion reserves, parallel request admission, unknown costs, inaccessible required sources, fallback exhaustion, contradictory evidence, duplicates, missing values, incompatible units, failed rendering, and empty-evidence reports.
- Use the same fixture task in guided and automatic execution and compare the final semantic content when inputs are unchanged. Verify that a revision changes affected work and does not overwrite previous evidence.
- Test both financial and AI-market fixtures with the same public workflow. Financial fixtures identify individual bonds separately from bond funds and yield series; the AI fixture distinguishes observed sample signals from wider market inferences.
- Compare browser/HTML/PDF content by report revision, key values, citations, limitations, and evidence references. Inspect representative rendered pages for Chinese glyphs, formula layout, long tables, chart labels, and pagination; avoid fragile whole-document binary snapshots.
- No application test suite was found in the inspected checkout. Existing prior art consists of the injectable retriever, staged runner, callbacks, saved artifacts, and usage counters; existing CI checks formatting and has a manually triggered package build. Add application test execution to CI without activating package publication.
- Live platform probes, real provider billing/usage comparison, and renderer fidelity are separate release-verification activities. Deterministic CI does not require paid keys, platform logins, or availability of Rednote/Bilibili. Unperformed live checks remain unverified rather than silently passing.

## Out of Scope

- Hosted multi-user accounts, tenant management, subscriptions, payments, and an online service marketplace.
- Automatically implementing every public-apis entry or arbitrary user API from a URL alone.
- Platform-wide Rednote/Bilibili indexing, exhaustive social-content collection, or guaranteed access to every post, comment, transcript, or video.
- Full audio transcription and video-frame understanding beyond available text/captions/transcripts.
- Original promotional-video rendering, narration generation, and video publishing in R1; these remain explicitly budgeted future output modules.
- Unrequested scheduled monitoring and universal real-time financial feeds or comprehensive individual-bond coverage.
- General-purpose autonomous installation/execution of unknown modules, and silently learned global preferences.
- Complete market-size or demand estimates derived only from sampled social-media popularity, and unqualified conclusions without supporting evidence.

## Further Notes

### Verification work that remains open

1. **Platform access:** run dated capability probes for Rednote and Bilibili and record which search, page text, metadata, comments, and transcript capabilities actually work through each configured acquisition method. Official merchant/creator integrations do not establish general public-content access. Unsupported capabilities must remain limited/unverified.
2. **Provider costs:** select the initial configured providers, document their current rates/quotas and model/token/request assumptions, and compare a small observed run with the estimate. Do not assert free access, current prices, or a billing guarantee without verification.
3. **Export fidelity:** verify installation and rendering of the chosen report stack with Chinese/English text, formulas, citations, charts, long tables, and appendices. If the renderer fails the check, record the demonstrated issue and evaluate an alternative adapter against the same acceptance fixture.

These are implementation/release checks rather than missing interview answers. They must remain visible in the tickets and release evidence. Numeric task budgets, date ranges, instruments, source selections, output language, and priorities are inputs to each real worksheet, not fixed product-wide assumptions.

### Decision rationale

- General information work is the product; finance was an illustrative scenario and must not narrow the architecture.
- A worksheet helps users discover their intended outcome and keeps it available throughout the workflow.
- The initial local operator-assisted delivery permits human help with clarification and integrations while producing commercial-quality reports.
- Quality and relevance matter more than the volume of collected results; selected sources still require evidence assessment.
- Budget-shaped planning and delivery reserves were explicitly chosen over a default pause when research consumes resources.
- Reports are the first commercial deliverable; optional summary videos reuse established findings rather than drive a separate research process.

### Primary research references

- [Public APIs catalogue](https://github.com/public-apis/public-apis)
- [Xiaohongshu developer documentation](https://open.xiaohongshu.com/document/developer/file/17)
- [Xiaohongshu account scopes](https://openaccount.xiaohongshu.com/docs/scope)
- [Bilibili submission-detail API](https://openhome.bilibili.com/doc/4/d9554788-dcef-f139-6217-b487d41c3826)
- [Playwright Python](https://playwright.dev/python/docs/library)
- [Streamlit](https://github.com/streamlit/streamlit), [Plotly](https://github.com/plotly/plotly.py), [Quarto](https://github.com/quarto-dev/quarto-cli)
- [Quarto PDF publishing](https://quarto.org/docs/output-formats/pdf-basics.html)
- [Plotly static export](https://plotly.com/python/static-image-export/)
