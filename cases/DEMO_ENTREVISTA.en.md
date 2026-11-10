# ArsenalMind: technical demonstration guide

This is a **live interview walkthrough**, not a claim of an independently certified MCP deployment. The complete ArsenalMind installation is private; the [Capability Watch module](../samples/arsenalmind-capability-watch/README.md) is the independently runnable public subset.

## Scenario: research tooling for a website redesign

Ask a coding agent to compare design tools, including a candidate such as ScrollCraft. The goal is to demonstrate how a candidate is discovered, evaluated, called and checked.

| Step | What to show | Evidence |
| --- | --- | --- |
| Setup | Client, ArsenalMind version, synthetic demo project | Sanitised environment summary |
| Task | Original request and constraints | Input and acceptance criteria |
| Plan | Selected skills, reasons and availability | Capability-router plan with explicit statuses |
| Research | Candidates and rejected alternatives | Research links and decision rationale |
| Actual call | One real MCP/CLI invocation | Tool response, status and invocation identifier |
| Output | Artefact, change diff and trade-offs | Observable result in a synthetic project |
| Verification | Test command, exit status and a failure case | Real logs and screenshots where relevant |
| Review | Limitations and unresolved issues | Accurate execution summary |

The user reports that the local capability router distinguishes planned, mentioned and actually invoked skills. That feature can be demonstrated live, but the documentation alone does not independently verify a specific invocation.

## Adversarial cases

- No matching skill exists: report the gap rather than claiming use.
- A discovered tool fails licensing/security checks: do not install it automatically.
- An MCP call fails: show the error rather than silently reporting success.
- Input contains customer data: switch to synthetic fixtures.
- A with/without-ArsenalMind comparison must use comparable tasks and measurements.

The public Capability Watch code and offline tests are inspectable today. Full MCP traces, end-to-end evaluation and performance gains require a separate test record.

[Case study](ARSENALMIND.en.md) · [Profile](../README.en.md)
