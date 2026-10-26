# T04: Select described services and report from a real public API

## Parent

[Information Workbench R1 specification](https://github.com/Moskataza/storm/issues/1)

## What to build

A requester searches the service catalogue, reads useful capability descriptions, selects permitted and required services, and receives a report containing information from a configured search provider and a catalogue-derived public API. Ordinary requesters use ready services without configuring integrations. Discovery entries remain visibly distinct from executable capabilities.

## Acceptance criteria

- [ ] Searchable catalogue entries show coverage, suitable tasks, input/output examples, authentication requirements, costs/limits, content types, provenance of the catalogue entry, and readiness.
- [ ] Import a reproducible public-apis snapshot; catalogue entries do not become executable merely because they have URLs.
- [ ] Optional selections define permitted sources, and must-use selections become tracked requirements; excluded services are never called.
- [ ] Configure and test one working search provider and at least one public API chosen from the catalogue after checking its current official documentation and access conditions.
- [ ] A task retrieves through those selected services, shows source-attributed results in the report, and includes their observed usage in its plan/ledger.
- [ ] Document the chosen providers' current rates/quotas, date checked, assumptions, unknowns, and a measured sample call/run. Preserve this as the first provider-cost verification record.
- [ ] Credentials are referenced through local provider configuration and do not appear in saved worksheets or reports.
- [ ] Deterministic workflow/browser checks cover search, selection, readiness, source exclusion, and unknown/disabled providers; live verification remains separately labeled.

## Specification coverage

AC04, AC05 selection, API portion of AC12, provider-cost portion of AC22, configured provider/API portion of AC23.

## Blocked by

- T03: Plan and finish an automatic report within its budget.

## Demonstration

Search for a service, inspect its description, select required/optional sources, and produce a budgeted report using a verified live public API with visible provenance and usage.
