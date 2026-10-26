# Information Workbench R1 continuation record

## Current phase and next action

The requester approved the shared design at Q23 and explicitly authorized committing the previously local-only design documentation. The design commit is **f76730c**, `docs: record agreed information workbench design`, on local main.

The requester then invoked to-spec and to-tickets, requested a first-release specification and complete demonstrable slices with dependencies, and asked to preserve the conversation through their creation before compaction.

**Specification published:** [Moskataza/storm #1](https://github.com/Moskataza/storm/issues/1), `Specification: Information Workbench R1`, open with ready-for-agent. The requester approved the proposed testing seams through an asynchronous answer before publication. A readback confirmed that the issue body matches the local specification and contains 44 user stories and AC01–AC24.

**Ticket proposals:** ten complete local drafts, with acceptance criteria, demonstrations, specification coverage and direct blockers. Their graph and AC01–AC24 coverage were checked. The requester has been asked asynchronously to approve granularity/dependencies or request merges/splits. **Ticket issues have not been published; approval is pending.**

Next action: read any pending answer to the ticket-breakdown question. If approved, publish T01–T10 in dependency order as ready-for-agent sub-issues of #1 and set native GitHub blocking relationships. If changes were requested, revise the concrete drafts and graph, then obtain approval. Update the tracker manifest and this record with the real issue numbers/URLs. Do not change or close the parent specification body.

Implementation has not started. The task is specification and ticket planning; do not begin building the application merely because tickets become ready.

## Tool and mode limits

The active collaboration mode remains Default. No tool for changing the UI collaboration mode or triggering manual compaction is exposed. This limitation was disclosed; work has stayed limited to documentation, specification, and tickets. Preserve this record if the host compacts automatically. Do not claim that a mode transition or manual compaction occurred.

## Repository and permissions

- Workspace: /home/kataz/projects/storm.
- GitHub account: Moskataza; fork and issue tracker: Moskataza/storm.
- origin points to the fork; upstream points to stanford-oval/storm. Local main tracks origin/main.
- The original repository allowed only read access; the fork has administrative/write access. Issues are enabled and the five default triage labels exist.
- Before tracker work, read docs/agents/issue-tracker.md; before triage, read docs/agents/triage-labels.md. Read docs/agents/domain.md, GLOSSARY.md and applicable ADRs before code exploration.
- AGENTS.md remains local/excluded. The requester previously wanted docs/GLOSSARY local-only, but explicitly reversed that instruction for design documentation in the latest phase. The design docs are now tracked by f76730c. Local ignore entries still hide newly created docs until explicitly added; tracked docs changes are visible normally.
- An unrelated untracked .omc/ directory exists. Leave it alone.
- GitHub networking and writes to .git require escalated execution in this environment. Previously approved prefixes include gh api, gh issue create, git add, and git commit; use normal approval mechanics as required rather than bypassing restrictions.
- No git push has been requested or performed for these documentation commits.

## Agreed design and rationale

1. **General information work:** collect, analyze, process and write according to the requester's needs. Finance was an example, not the product boundary. The requester explicitly corrected a premature finance-only interpretation.
2. **Demand worksheet plus conversation:** help users discover what they want to understand, decide or produce. Record purpose, priority questions, scope, value/completion criteria, processing needs, audience/language, outputs, depth and time/cost allowances. Suggest directions for vague requests and make minor defaults visible.
3. **Initial local operator-assisted delivery:** the operator can spend human time helping a requester clarify needs and complete work. The first release is not a hosted multi-user service, but can retrieve online information.
4. **Guided and Automatic modes:** use the same workflow. Guided review permits inspecting evidence and redirecting the task; Automatic mode executes a clear worksheet without routine stage approvals. Save task revisions and explicit reusable preferences.
5. **Service selection prioritizes quality:** searchable optional service descriptions explain capabilities, coverage, input/output examples, authentication, costs/limits and readiness. Selected services are permitted sources; must-use sources are tracked requirements. Ordinary requesters should not need to configure APIs.
6. **Extensible integrations:** use public-apis to discover services, not as a universal execution API. Operators/developers can configure custom websites/APIs and add Python connector, processor, analyzer and renderer modules.
7. **Acquisition fallback:** notify when a required source is inaccessible and try appropriate Playwright or simple-crawler acquisition within the plan. Keep remaining gaps visible. Do not silently substitute a different source or claim content that was not obtained.
8. **Evidence quality:** distinguish source claims, experiences, opinions, identifiable promotions, unknown sponsorship, and calculated results. Preserve sources, dates, methods, units and uncertainty. Likes/views are contextual signals. Repeated/derived posts are not independent confirmation.
9. **Budget correction:** the requester rejected a default budget-triggered pause. Plan the whole work upfront to fit time/cost, reserve analysis/reporting/export effort, and adapt lower-priority research to deliver a report with explicit coverage limits. Unknown prices and estimate uncertainty remain visible.
10. **Commercial reports first:** clear browser overview, expandable evidence/methods, charts/tables/formulas where useful, and client-ready HTML/PDF from the same saved findings/data. Working stack: local Streamlit, Plotly, Quarto; export fidelity remains to verify.
11. **Optional original summary video:** derived from report findings, charts, captions and narration for promotion, not merely a collection of source clips. It must be explicitly requested and budgeted. Original video rendering is deferred beyond R1.
12. **Initial input modalities:** accessible text, structured data and available captions/transcripts. Full audio/visual understanding is a later module.
13. **Generality validation:** financial information work plus Chinese AI-market learning using Rednote/Bilibili where obtainable. AI offerings span hardware, software, agent skills, workflows, prompt packs, agent systems and platforms; categories overlap and can expand. This is market learning, not merely purchase recommendations.

## Documents

- GLOSSARY.md: canonical terminology, including requester/operator, worksheet, task plan/budget, finding and AI offering.
- docs/adr/0001-demand-worksheet-as-shared-task-context.md: why a worksheet guides all stages rather than only a topic.
- docs/adr/0002-plan-for-completed-deliverables-within-budget.md: upfront planning, delivery reserve and completion rather than a default cost pause.
- docs/worksheets/system-design.yaml: complete agreed design and proposed implementation defaults.
- docs/worksheets/ai-market-study.yaml: example worksheet; per-task date range, priorities, actual limits and language are runtime inputs.
- docs/specs/information-workbench-r1.md: exact local copy of published specification #1.
- docs/specs/information-workbench-r1-tracker.yaml: authoritative local publication/reference and dependency manifest.
- docs/tickets/information-workbench-r1/README.md: numbered proposal, graph explanation and acceptance coverage.
- docs/tickets/information-workbench-r1/01-replayable-worksheet-report.md through 10-demonstrate-release-across-two-domains.md: complete ticket drafts.

## Ticket dependencies

| Draft | End-to-end slice | Direct blockers |
| --- | --- | --- |
| T01 | Replayable worksheet-to-report task | None |
| T02 | Clarification and needs reuse | T01 |
| T03 | Budgeted automatic report completion | T01 |
| T04 | Described service selection and live public API | T03 |
| T05 | HTTP/browser acquisition and access-gap reporting | T04 |
| T06 | Custom source and Python processing | T04 |
| T07 | Evidence-qualified analysis and visuals | T01 |
| T08 | Guided redirection with preserved history | T02, T03, T07 |
| T09 | Matching browser/HTML/PDF client artifacts | T03, T07 |
| T10 | Cross-domain demonstration and release evidence | T05, T06, T08, T09 |

The immediate implementation frontier would be T01 after ticket publication and an explicit instruction to begin implementation. T02/T03/T07 become independent after T01. No implementation issue currently exists to claim.

## Testing and release verification

Approved testing boundary: complete public task workflow, with injected sources/models, controlled rates and fake clock; assert saved findings/data/evidence, usage and report outcomes. Use a small browser set for editing, service selection, redirection, reopening and downloads. Avoid testing generated wording or private implementation details.

There was no application test suite in the inspected checkout. Existing CI checks Black formatting and has a manually triggered package build/publish workflow. T01 adds application tests without activating package publication.

Keep these three checks open and explicit:

1. **Platform access:** Rednote official merchant/account documentation and Bilibili own-submission metadata access do not establish arbitrary public search, comments, transcripts or platform-wide collection. Record actual dated probes and capability outcomes. Browser/crawler fallback is a method to test, not a guarantee.
2. **Provider costs:** verify selected provider rates/quotas, model/request assumptions and actual measured usage. Distinguish estimates, unknowns and provider billing. Do not invent numeric budgets for real requester tasks.
3. **Export fidelity:** check the chosen stack's installation, static chart export, Chinese/English fonts, formulas, citations, long tables, page breaks and evidence appendices. Browser/HTML/PDF must use the same report revision; do not rerun analysis for export.

Other deferred scope: hosted accounts/payments, universal automatic API onboarding, exhaustive social indexing, general realtime/comprehensive bond feeds, full audiovisual analysis, video generation, unrequested scheduled monitoring and silently learned global preferences.

## Code facts already established

- STORMWikiRunner accepts custom rm, wraps Retriever, and internally constructs concrete generation modules. Add a narrow workbench adapter rather than a broad rewrite.
- knowledge_storm/storm_wiki/engine.py:128 has bounded scope/concurrency controls; :174 the runner constructor; :341 the staged public run entry.
- knowledge_storm/interface.py:288 adapts retriever output with url/title/description/snippets; Information.meta preserves extra references. :485 records stage time, token usage and retrieval counts retrospectively.
- knowledge_storm/utils.py:674 performs HTTP acquisition; :684 extracts text; :695 currently excludes tables/comments and failures disappear. Preserve structured source records and failed attempts in the new workbench path.
- Source merging currently groups by URL; keep capture IDs and structured evidence outside snippets to avoid losing repeat captures/lineage.
- The current demo accepts only a topic and escapes dollar signs in article rendering. New worksheet/multilingual/formula handling must not inherit those restrictions.

## Invoked skills and publication requirements

- to-spec: /home/kataz/.codex/plugins/cache/mattpocock/mattpocock-skills/1.3.1/skills/engineering/to-spec/SKILL.md. Synthesize without another interview; check testing seams (approved), then publish a ready-for-agent specification (done: #1).
- to-tickets: /home/kataz/.codex/plugins/cache/mattpocock/mattpocock-skills/1.3.1/skills/engineering/to-tickets/SKILL.md. Propose complete vertical slices; obtain breakdown approval; then publish and set blocking edges. Pending approval is mandatory, not inferred.
- Grilling/domain-modeling produced the shared understanding and documentation; the requester already confirmed it. Do not restart the interview.
- Keep human-facing explanations concise. If waiting because of a skill requirement, name/link the exact skill and quote its approval instruction.

## Final continuation checklist

- Read pending ticket-breakdown response.
- Publish only approved implementation tickets, replacing draft IDs with real issue references; attach sub-issues and native dependencies as documented.
- Update publication manifest, ticket index, and this record with actual references and next action.
- Validate draft/remote content, required labels, graph and acceptance coverage.
- Preserve this record before any host-driven context compaction; disclose that no manual compaction tool is available.
