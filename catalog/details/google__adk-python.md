# google/adk-python

An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

## features

- **Workflow Runtime**: A graph-based execution engine for composing
  deterministic execution flows for agentic apps, with support for routing,
  fan-out/fan-in, loops, retry, state management, dynamic nodes,
  human-in-the-loop, and nested workflows.

- **Task API**: Structured agent-to-agent delegation with multi-turn task
  mode, single-turn controlled output, mixed delegation patterns,
  human-in-the-loop, and task agents as workflow nodes.

- **Modular Multi-Agent Systems**: Design scalable applications by composing
  multiple specialized agents into flexible hierarchies.

- **Rich Tool Ecosystem**: Utilize pre-built tools, custom functions,
  OpenAPI specs, MCP tools or integrate existing tools to give agents diverse
  capabilities, all for tight integration with the Google ecosystem.

- **Code-First Development**: Define agent logic, tools, and orchestration
  directly in Python for ultimate flexibility, testability, and versioning.

- **Agent Config**: Build agents without code. Check out the
  [Agent Config](https://google.github.io/adk-docs/agents/config/) feature.

- **Tool Confirmation**: A [tool confirmation flow (HITL)](https://google.github.io/adk-docs/tools/confirmation/) that can guard tool execution with explicit confirmation and custom input.

- **Deploy Anywhere**: Easily containerize and deploy agents on Cloud Run or
  scale seamlessly with Vertex AI Agent Engine.

## installation

> **Beginner Note:** ADK applications are built using two main classes:
> **`Agent`** (defines an AI's instructions, tools, and behavior) and
> **`Workflow`** (orchestrates agents and tasks in a graph-based flow).
