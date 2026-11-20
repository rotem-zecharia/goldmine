# ruvnet/ruflo

🌊 The original agent harness. Deploy intelligent multi-player swarms, coordinate autonomous workflows, and build conversational AI systems. Features adaptive memory, self-learning intelligence, federa

## installation

**macOS / Linux / WSL / Git-Bash:**

```bash
# One-line install (POSIX shells only — see Windows note below)
curl -fsSL https://cdn.jsdelivr.net/gh/ruvnet/ruflo@main/scripts/install.sh | bash
```

**All platforms (including native Windows PowerShell / cmd):**

```bash
# Interactive setup wizard — runs identically on every platform
npx ruflo@latest init wizard

# Quick non-interactive init
# npx ruflo@latest init

# Or install globally
npm install -g ruflo@latest
```

> 💡 **Windows users:** the `curl ... | bash` form needs a POSIX shell (Git-Bash, WSL, MSYS). The `npx ruflo@latest init wizard` line works natively in PowerShell and cmd. If you hit an `'bash' is not recognized` error, use the `npx` line instead — both end up running the same init flow.

### <img src="docs/assets/readme/icons/network.svg" width="28" height="28" alt=""> MCP Server

```bash
# Add Ruflo as an MCP server in Claude Code
claude mcp add claude-flow -- npx ruflo@latest mcp start
```

For static inspection of local applications and binaries, see the [ruRE plugin guide](plugins/ruflo-rure/README.md).

---

**Grok Build:** `npx ruflo init --grok` writes the project host surface (`.grok/`, the team bus, and the operator guide) and nothing outside the project; add `--dry-run` to preview. Setup, the `spawn_subagent` contract, the optional status row, and what to re-check when Grok updates: [the Grok operator guide](v3/@claude-flow/cli/templates/grok/docs/README.md).

</details>

## Mission Control

<p align="center"><img src="docs/assets/readme/console.svg" alt="Mission Control console overview" width="100%"></p>

Open `/ruflo` in Claude Code to monitor agent work, inspect a run, or give Claude permission to operate the console.

If you use the console, open the agent’s log and compare its actions with the diff and test result from your first task.

| Task | What you can do |
| --- | --- |
| Monitor work | Track workflows, agents, models, token use, and cost. [Workflow demo with sample data](docs/assets/ruflo-console-workflows.svg) |
| Inspect a run | Search logs and results, triage failures, replay a run, and compare outcomes. |
| Customize the console | Preview Orbital, switch among six palettes, save a theme, or import its JSON. [38 second renderer replay](https://raw.githubusercontent.com/ruvnet/ruflo/main/docs/assets/ruflo-console-theme-compact.svg) · [Theme Studio guide](plugins/ruflo-console/README.md) |
| Control Claude’s access | Choose a permission level and approval mode in **Settings → Claude control**. Review each action in the live log. [Permission details](v3/docs/adr/ADR-444-claude-controls-the-console.md) |

### Install and open the console

Use Claude Code **2.1.287 or later**. Review mods before installing them because they run with your account’s permissions.

```text
/plugin marketplace add ruvnet/ruflo
/plugin install ruflo-console@ruflo
/plugin install ruflo-mods@ruflo
/reload-plugins
```

Open `/plugin` to check the active mods, then `/ruflo` to launch the console. For a project initialized through the CLI, run `npx ruflo init` and restart Claude Code before opening `/ruflo`.

<details>
<summary>Console mods and catalog</summary>

| Mod | Purpose |
| --- | --- |
| `ruflo-console` | Opens the console beside Claude Code. |
| `ruflo-mods` | Routes prompts and enforces policy in process. |
| `ruflo-swarm` | Adds a pane showing the swarm. |
| `ruflo-ruos` | Adds the ruOS status segment. |

Open `/ruflo market` to inspect plugins, mods, and skills. The catalog asks for confirmation before installing, enabling, disabling, or updating an item.

</details>

<a id="console-walkthrough"></a>

### Create a mission with Claude

The default is **read + ask**. Available levels are `read`, `write`, `manage`, and `full`, with `ask` or `auto` approval. Actions above the selected level are refused. Network, spending, and destructive actions require confirmation even in `auto`.

1. In **Settings → Claude control**, select **write + ask**.
2. Ask Claude, “Cr
