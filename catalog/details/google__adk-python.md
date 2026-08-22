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

### Stable Release (Recommended)

You can install the latest stable version of ADK using `pip`:

```bash
pip install google-adk
```

**Requirements:** Python 3.10+.

For transitive dependency protection, we recommend to install with our companion
constraints files (for python 3.10 to 3.14).

Choose the constraints file matching your Python version:

```bash
# For example, for Python 3.10
curl -o constraints-3.10.txt https://raw.githubusercontent.com/google/adk-python/main/constraints-3.10.txt
pip install google-adk -c constraints-3.10.txt
rm constraints-3.10.txt
```

To install optional integrations, you can use the following command:

```bash
pip install "google-adk[extensions]"
```

The release cadence is roughly bi-weekly.

### Development Version

Bug fixes and new features are merged into the main branch on GitHub first. If you need access to changes that haven't been included in an official PyPI release yet, you can install directly from the main branch:

```bash
pip install git+https://github.com/google/adk-python.git@main
```

Note: The development version is built directly from the latest code commits. While it includes the newest fixes and features, it may also contain experimental changes or bugs not present in the stable release. Use it primarily for testing upcoming changes or accessing critical fixes before they are officially released.

## Quick Start

> **Beginner Note:** ADK applications are built using two main classes:
> **`Agent`** (defines an AI's instructions, tools, and behavior) and
> **`Workflow`** (orchestrates agents and tasks in a graph-based flow).

### Agent

```python
from google.adk import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant. Greet the user warmly.",
)
```

### Workflow

```python
from google.adk import Agent, Workflow

generate_fruit_agent = Agent(
    name="generate_fruit_agent",
    instruction="Return the name of a random fruit. Return only the name.",
)

generate_benefit_agent = Agent(
    name="generate_benefit_agent",
    instruction="Tell me a health benefit about the specified fruit.",
)

root_agent = Workflow(
    name="root_agent",
    edges=[("START", generate_fruit_agent, generate_benefit_agent)],
)
```

### Run Locally

```bash
# Interactive CLI
adk run path/to/my_agent

# Web UI (supports multi-agent directories or pointing directly to a single agent folder)
adk web path/to/agents_dir
```

### Development UI

A built-in development UI to help you test, evaluate, debug, and showcase your agent(s).

[![ADK Web UI](https://raw.githubusercontent.com/google/adk-python/main/assets/adk-web-dev-ui.png)](https://youtu.be/TEjqk0eeNy8)

[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch%20ADK%20Web%20Demo-FF0000?style=flat&logo=youtube&logoColor=white)](https://youtu.be/TEjqk0eeNy8)

### Evaluate Agents

```bash
adk eval \
    samples_for_testing/hello_world \
    samples_for_testing/hello_world/hello_world_eval_set_001.evalset.json
```

## 📚 Documentation

- **Getting Started**: https://google.github.io/adk-docs/
- **Guides**: See
  [`docs/guides/`](https://github.com/google/adk-python/tree/main/docs/guides)
  for task-oriented walkthroughs of agents, tools, events, plugins, and
  workflows.
- **Samples**: See
  [`contributing/samples/`](https://github.com/google/adk-python/tree/main/contributing/samples)
  for runnable example agents.

## 🤝 Contributing

We welcome contributions from the community! Whether it's bug reports, feature requests, documentation improvements, or code contributions, please see our:

- [General contribution guideline and flow](https://google.github.io/adk-docs/contributing-guide/).
- [Code Contributing Guidelines](./CONTRIBUTING.md) to get started.

## Community Repo

We have the [adk-python-community repo](https://github.com/google/adk-python-community) that is home to a growing ecosystem of community-contributed tools, third-party
service integrations, and de
