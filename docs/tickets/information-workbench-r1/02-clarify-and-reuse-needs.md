# T02: Clarify vague needs and reuse saved worksheets

## Parent

[Information Workbench R1 specification](https://github.com/Moskataza/storm/issues/1)

## What to build

A requester begins with a vague interest. The conversation offers relevant directions, asks the questions that determine the purpose, and updates an editable worksheet. An operator can do this collaboratively with the requester. The resulting worksheet can drive the existing task-to-report demonstration and be reused later without silently changing lasting preferences.

## Acceptance criteria

- [ ] A vague-request fixture produces alternative directions and asks for the missing purpose rather than inventing a goal.
- [ ] Answers and direct form edits update the same visible worksheet; minor defaults and remaining questions are identified.
- [ ] A clear-enough worksheet can proceed through the existing task flow; an unresolved purpose remains visible for clarification.
- [ ] Save/reopen/reuse preserve revision history and task-local requirements.
- [ ] A preference becomes reusable only through an explicit selection; a one-task interest does not change unrelated tasks.
- [ ] Chinese and English worksheet content round-trips without the old topic-only language restriction.
- [ ] Workflow tests exercise vague-to-clear and reuse/isolation behavior with model fixtures; a browser check covers conversation-to-form editing.

## Specification coverage

AC01, AC02, AC03; Chinese/English input portion of AC19.

## Blocked by

- T01: Deliver a replayable worksheet-to-report task.

## Demonstration

Start with an unclear AI interest, clarify market-learning questions, run the fixture report, and reuse the worksheet for a second task with isolated preferences.
