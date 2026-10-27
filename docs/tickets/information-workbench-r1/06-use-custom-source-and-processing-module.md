# T06: Use a custom source and Python processing module in a report

## Parent

[Information Workbench R1 specification](https://github.com/Moskataza/storm/issues/1)

## What to build

An operator registers a custom website/API integration and a Python processing capability, declares the required configuration and input/output contract, and uses both in an ordinary worksheet task. The processing result becomes visible in a table, chart input, or conclusion while keeping its source and method references.

## Acceptance criteria

- [ ] Registered capabilities declare purpose, supported task roles, inputs, outputs, configuration requirements, and resource assumptions.
- [ ] A custom API can be configured with endpoint, parameters, credential reference, and response mapping; complex sources can supply an operator-registered Python connector.
- [ ] The catalogue exposes the configured custom source's actual capabilities and readiness, and ordinary users can select it without API setup.
- [ ] A task invokes a custom deterministic processor on source data and carries source IDs, inputs, units, method/version, and computed results into its report artifacts.
- [ ] Missing configuration, incompatible processor input, and invalid output produce actionable task-visible errors and preserved evidence rather than silent corruption.
- [ ] Add a second module in the demonstration without changing core task-workflow logic; future analyzer/renderer roles use the same registration approach.
- [ ] Public-workflow contract tests exercise valid registration, missing credentials/configuration, malformed responses, and incompatible processor inputs.

- [ ] Only operator-approved modules installed before tasks in the storm Conda environment may run. A task never installs packages, executes untrusted code, or turns an LLM-discovered endpoint into a connector without verification. Validate both successful calls and rejected requests.

## Specification coverage

AC06, custom source portion of AC12, processor foundation of AC16.

## Blocked by

- T04: Select described services and report from a real public API.

## Demonstration

Register a small custom source and a comparison processor, select them for a worksheet, and show their attributed calculation in the resulting report.
