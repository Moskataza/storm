# T04: Select described services and report from a real public API

## Parent

[Information Workbench R1 specification](https://github.com/Moskataza/storm/issues/1)

## What to build

A requester searches the service catalogue, reads useful capability descriptions, selects permitted and required services, and receives a report containing information from the configured SEC EDGAR public submissions/XBRL connector. Ordinary requesters use ready services without configuring integrations. Discovery entries remain visibly distinct from executable capabilities.

## Acceptance criteria

- [ ] Searchable catalogue entries show coverage, suitable tasks, input/output examples, authentication requirements, costs/limits, content types, provenance of the catalogue entry, and readiness.
- [ ] Import a reproducible public-apis snapshot with commit/date and attribution; catalogue entries do not become executable merely because they have URLs.
- [ ] Optional selections define permitted sources, and must-use selections become tracked requirements; excluded services are never called.
- [ ] Configure SEC EDGAR as the first live reference connector with provider-neutral contracts; additional verified connectors remain individually callable. A dedicated search service or second API is not required for R1.
- [ ] A task retrieves through those selected services, shows source-attributed results in the report, and includes their observed usage in its plan/ledger.
- [ ] Expose dated rate/quota assumptions and unknown costs in the connector description and task ledger; T10 owns actual provider-cost verification.
- [ ] Credentials are referenced through local provider configuration and do not appear in saved worksheets or reports.
- [ ] Deterministic workflow/browser checks cover search, selection, readiness, source exclusion, and unknown/disabled providers; live verification remains separately labeled.

- [ ] The LLM may search/discover services and call permitted verified connectors through approved collection tools. Unverified recommendations, excluded services, and unknown endpoint calls cannot execute. Record tool provenance and usage.

## Specification coverage

AC04, AC05 selection, API portion of AC12, provider-cost metadata supporting AC22, configured provider/API portion of AC23.

## Blocked by

- T03: Plan and finish an automatic report within its budget.

## Demonstration

Search for a service, inspect its description, select required/optional sources, and produce a budgeted report using a verified live public API with visible provenance and usage.
