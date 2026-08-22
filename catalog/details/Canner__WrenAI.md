# Canner/WrenAI

GenBI (Generative BI) for AI agents, an open-source, governed text-to-SQL through an open context layer that turns natural-language questions into trusted dashboards, charts, and SQL across 20+ data s

## features

- **Generative BI, end to end.** Wren does **governed text-to-SQL** — and goes beyond it: generate the answer, deploy the dashboard, share the URL, all driven by the agents you already use.
- **Knowledge management built in.** Business meaning, approved definitions, and proven examples are captured as a reviewable, version-controlled **semantic layer (MDL)**, not buried in prompts.
- **Open by default.** Open-sourced core, SDK, and skills under the Apache-2.0 license.
- **Correctness as primitives.** Rich schema retrieval, dry-plan validation, structured errors with hints, value profiling, eval runner. The agent orchestrates; the trace lives in its reasoning.
- **Governed execution, reviewable context.** Dry-plan validation, row limits, and structured errors keep agent-generated SQL inside guardrails, and every definition and example lives in Git — reviewable, versioned, diff-able. (Row/column-level security and access control are Cloud / self-hosted — see [Open core: OSS vs. Cloud / self-hosted](#open-core-oss-vs-cloud--self-hosted).)
- **Sits on top of your existing stack.** Warehouse, transformation pipelines, your existing semantic layer. Not another tool to maintain.

## installation

WrenAI is **agent-driven by design**: install the CLI, install a one-file
discovery stub for your AI client, then let your AI agent drive the rest.
Workflow guides live inside the CLI itself and are served on demand, so
content always matches the installed version.
