# aden-hive/hive

Multi-Agent Harness for Production AI

## features

OpenHive is a zero-setup, model-agnostic runtime for **colonies of agents**. A colony is a group of specialized agents that work together to run one business process: a **Queen** — the persistent, client-facing lead — plus however many **worker** agents the job needs. You describe the outcome; the Queen does the work, then grows a colony around it to run that work reliably and at scale.

The mechanism underneath is **one loop controlling many loops**. Hive has a single execution primitive: the Queen *is* an agent loop, and every worker is a **clone** of it — same tools, same model, its own task. There is no graph to compile and no orchestration boilerplate to write. The colony coordinates through a shared ledger and a persistent plan, with crash-safe state, deep observability, and human oversight built into the one primitive every agent shares. See the **[Architecture Overview](docs/architecture/README.md)** for how it works.

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
