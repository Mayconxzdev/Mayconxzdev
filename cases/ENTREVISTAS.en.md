# Interview preparation: defensible experience

This guide reflects **the author's reported experience**, not an independent technical interview or verified employer impact.

## Incident: duplicated database during AI-assisted development

**Situation:** a coding agent created a second copy of an existing database, which led to duplication in the application.

**Reported action:** I compared the filenames and file dates to identify the newer copy and used that analysis to resolve the issue.

**Reported result:** the issue was resolved. No independent commit, trace or specific test log for this incident is published.

**Technical follow-up:** filenames and timestamps provide clues; I would verify the active database path and contents before treating them as authoritative. I do not claim I ran PRAGMA database_list or a particular backup procedure in the original incident.

## Deployment and training

I encountered different Windows computer setups and investigated compatibility issues. I also helped users learn the software and supported changes after deployment. I have not published measured time savings or success rates for those activities.

## ArsenalMind

I can demonstrate the complete local setup, including capability research and communication of selected versus invoked tools. The public Python module can be independently tested; the complete local MCP journey has not been independently reproduced in this repository.

## AI-assisted engineering

I learned programming fundamentals before using AI coding agents. I use agents to speed up research and implementation, while checking decisions, code and results. I may take longer to implement certain changes without AI support. My work is better presented as software engineering with applied AI, integrations and operational troubleshooting than as senior independent expertise in every language mentioned.

## Before an interview

- Choose the role-specific resume.
- Prepare a synthetic demo with actual calls, outputs and a controlled failure.
- Explain personal contributions and co-authorship separately.
- Give a truthful problem/action/outcome example.
- Be prepared to explain and modify one function unaided.
- Avoid unsupported claims about AI evals, production MLOps and spoken-English proficiency.

[Profile](../README.en.md) · [ArsenalMind live demo](DEMO_ENTREVISTA.en.md)
