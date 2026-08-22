# aden-hive/hive

Multi-Agent Harness for Production AI

## features

OpenHive is a zero-setup, model-agnostic runtime for **colonies of agents**. A colony is a group of specialized agents that work together to run one business process: a **Queen** — the persistent, client-facing lead — plus however many **worker** agents the job needs. You describe the outcome; the Queen does the work, then grows a colony around it to run that work reliably and at scale.

The mechanism underneath is **one loop controlling many loops**. Hive has a single execution primitive: the Queen *is* an agent loop, and every worker is a **clone** of it — same tools, same model, its own task. There is no graph to compile and no orchestration boilerplate to write. The colony coordinates through a shared ledger and a persistent plan, with crash-safe state, deep observability, and human oversight built into the one primitive every agent shares. See the **[Architecture Overview](docs/architecture/README.md)** for how it works.

## Features

- ✅ Colonies of agents — a Queen spawns worker clones on demand for parallel, long-running work
- ✅ One primitive, many loops — no graph to wire; the Queen grows the colony at runtime
- ✅ Shared tracker ledger + persistent task plan for coordination without a data buffer
- ✅ Queen personas with CEO-style routing and evolving, scoped memory
- ✅ Crash-safe park/resume, cost enforcement, and out-of-band human-in-the-loop (Sentinel)
- ✅ Zero Setup — no technical configuration required
- ✅ General Compute Use and Browser Use with Native Extension
- ✅ Custom Model Support

Visit [adenhq.com](https://adenhq.com) for complete documentation, examples, and guides.

Visit [HoneyComb](http://honeycomb.open-hive.com/) to see what jobs are being automated by AI. It’s a stock market for jobs, driven by our community’s AI agent progress. You can long and short jobs (with no real money but compute token)based on how much you think a job is going to be replaced by AI.

https://github.com/user-attachments/assets/bf10edc3-06ba-48b6-98ba-d069b15fb69d


## Who Is Hive For?

Hive is the multi-agent harness layer for teams moving AI agents from prototype to production. Single agents like Openclaw and Cowork can finish personal jobs pretty well but lack the rigor to fulfil business processes. 

Hive is a good fit if you:

- Want AI agents that **execute real business processes**, not demos
- Need a **runtime that handles state, recovery, and parallel execution** at scale
- Need **adaptive agents that improve over time** through reflexion, memory, and learned skills
- Require **human-in-the-loop control**, observability, and cost limits
- Plan to run agents in **production** where uptime, cost, and auditability matter

Hive may not be the best fit if you’re only experimenting with simple agent chains or one-off scripts.

## When Should You Use Hive?

Use Hive when the bottleneck is no longer the model but the harness around it:

- Long-running agents that need **state persistence and crash recovery**
- Production workloads requiring **cost enforcement, observability, and audit trails**
- Agents that **improve over time** through reflexion, scoped memory, and learned skills
- Parallel, multi-agent work coordinated through a **shared tracker ledger and persistent plan**
- A framework that **scales with model improvements** rather than fighting them

## Quick Links

- **[Documentation](https://docs.adenhq.com/)** - Complete guides and API reference
- **[Self-Hosting Guide](https://docs.adenhq.com/getting-started/quickstart)** - Deploy Hive on your infrastructure
- **[Changelog](https://github.com/aden-hive/hive/releases)** - Latest updates and releases
- **[Roadmap](docs/roadmap.md)** - Upcoming features and plans
- **[Report Issues](https://github.com/aden-hive/hive/issues)** - Bug reports and feature requests
- **[Contributing](CONTRIBUTING.md)** - How to contribute and submit PRs

## requirements

- Python 3.11+ for agent development
- An LLM provider that powers the agents
- **ripgrep (optional, recommended on Windows):** The `terminal_rg` / `terminal_glob` search tools use ripgrep for faster file search. If not installed, a Python fallback is used. On Windows: `winget install BurntSushi.ripgrep` or `scoop install ripgrep`

> **Windows Users:** Native Windows is supported via `quickstart.ps1` and `hive.ps1`. Run these in PowerShell 5.1+. WSL is also an option but not required.

## installation

> **Note**
> Hive uses a `uv` workspace layout and is not installed with `pip install`.
> Running `pip install -e .` from the repository root will create a placeholder package and Hive will not function correctly.
> Please use the quickstart script below to set up the environment.

```bash
# Clone the repository
git clone https://github.com/aden-hive/hive.git
cd hive

# Run quickstart setup (macOS/Linux)
./quickstart.sh

# Windows (PowerShell)
.\quickstart.ps1
```

This sets up:

- **framework** - Core agent runtime and colony runtime (in `core/.venv`)
- **aden_tools** - MCP tools for agent capabilities (in `tools/.venv`)
- **credential store** - Encrypted API key storage (`~/.hive/credentials`)
- **LLM provider** - Interactive default model configuration, including Hive LLM and OpenRouter
- All required Python dependencies with `uv`

- Finally, it will open the Hive interface in your browser

> **Tip:** To reopen the dashboard later, run `hive open` from the project directory.

### Build Your First Agent

Type the agent you want to build in the home input box. The queen is going to ask you questions and work out a solution with you.

<img width="2500" height="1214" alt="Image" src="https://github.com/user-attachments/assets/1ce19141-a78b-46f5-8d64-dbf987e048f4" />

### Use Template Agents

Click "Try a sample agent" and check the templates. You can run a template directly or choose to build your version on top of the existing template.

### Run Agents

Now you can run an agent by selecting the agent (either an existing agent or example agent). You can click the Run button on the top left, or talk to the queen agent and it can run the agent for you.

<img width="2549" height="1174" alt="Screenshot 2026-03-12 at 9 27 36 PM" src="https://github.com/user-attachments/assets/7c7d30fa-9ceb-4c23-95af-b1caa405547d" />

## Integration

<a href="https://github.com/aden-hive/hive/tree/main/tools/src/aden_tools/tools"><img width="100%" alt="Integration" src="https://github.com/user-attachments/assets/a1573f93-cf02-4bb8-b3d5-b305b05b1e51" /></a>
Hive is built to be model-agnostic and system-agnostic.

- **LLM flexibility** - Hive Framework supports Anthropic, OpenAI, OpenRouter, Hive LLM, and other hosted or local models through LiteLLM-compatible providers.
- **Business system connectivity** - Hive Framework is designed to connect to all kinds of business systems as tools, such as CRM, support, messaging, data, file, and internal APIs via MCP.
