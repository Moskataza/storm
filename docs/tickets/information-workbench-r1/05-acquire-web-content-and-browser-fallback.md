# T05: Acquire web evidence with browser fallback and honest access gaps

## Parent

[Information Workbench R1 specification](https://github.com/Moskataza/storm/issues/1)

## What to build

A worksheet selects websites as sources. The task acquires suitable static content through HTTP/simple crawling and uses Playwright when rendered content needs a browser. A failed required source triggers a visible notification and bounded fallback attempts, then an explicit report gap if still inaccessible. The same source remains required throughout acquisition.

## Acceptance criteria

- [ ] An accessible page produces saved content, stable capture identity, source URL, acquisition method/outcome, retrieval/publication metadata when available, and evidence references used by a report.
- [ ] A rendered-page fixture succeeds through the configured browser path after ordinary extraction fails; source status and acquired content are validated rather than treating navigation alone as success.
- [ ] HTTP errors, empty content, exhausted fallbacks, and inaccessible pages remain visible; they are not silently dropped or represented as successful full-content retrieval.
- [ ] Requests, crawl extent, browser attempts, timeouts, and concurrency fit the task plan and delivery reserve.
- [ ] Available text/captions/transcripts are distinguished from metadata-only captures; a title alone does not establish a video's spoken claims.
- [ ] Run dated Rednote and Bilibili capability probes, recording each attempted method and supported/limited/unavailable/unverified status for search, text, metadata, comments, and transcripts. Do not claim platform-wide coverage from a single successful page.
- [ ] At least one normally accessible real web source completes acquisition-to-report; failed social-platform probes still leave a demonstrable gap report and documented capability limits.
- [ ] Fixture workflow tests verify static success, rendered fallback, required-source failure, content coverage, and budget-bounded attempts without live platform dependencies.

## Specification coverage

AC05 failures, AC11, AC12, AC13, platform-access portion of AC22, web/platform portion of AC23.

## Blocked by

- T04: Select described services and report from a real public API.

## Demonstration

Show one rendered-page fallback success and one inaccessible required source in the same report, then present the dated Rednote/Bilibili capability records.
