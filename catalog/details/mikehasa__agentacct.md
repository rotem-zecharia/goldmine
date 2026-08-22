# mikehasa/agentacct

See what your coding agents did and what it cost. Breaks each task down into work steps — tools used, files changed, tests run, time and tokens spent. Local-first dashboard for Claude Code, Codex, Ope

## installation

### The macOS app — no Python required

The signed, notarized **macOS app** bundles everything. Download the `.dmg` from the [latest release](https://github.com/mikehasa/agentacct/releases/latest), drag agentacct to Applications, and open it — on first launch it installs the bundled CLI, instruments the coding agents it finds, and shows your Work Receipts in a native window. Requires macOS 14+.

### The CLI

Requires Python >= 3.11 on macOS or Linux; Windows is supported only via WSL.

```bash
pipx install agentacct
agentacct onboard   # once per machine (global by default)
agentacct tui       # the live terminal dashboard
```

No `pipx` yet? Install it first with `brew install pipx` (macOS) or `python3 -m pip install --user pipx` — or skip pipx entirely and use `uv tool install agentacct`. See [INSTALL.md](INSTALL.md) for a plain-`venv` fallback.

`onboard` installs agentacct once per machine (global by default, writing zero files into your repo): it detects your local coding-agent logs, sets up a global store, and runs a first usage sync. Then run **`agentacct tui`** for the live terminal dashboard (onboarding also starts the managed background sync plus a local JSON API on `http://127.0.0.1:8765` — the machine-readable lane native shells and scripts poll). Open a **new** agent session in any repo — MCP servers and hooks bind at session start, so the session that ran onboarding cannot become the first recorded Task. (Prefer a per-repo install? Run `agentacct onboard --scope project` instead.)

### Let your coding agent install it

Paste this into your coding agent:

```text
Install and set up agentacct — a local-first tool that reads my
coding-agent logs read-only and shows honest token usage and cost.

Run `pipx install agentacct`
(or `pipx install git+https://github.com/mikehasa/agentacct`),
then `agentacct onboard` (installs once per machine, global by default, zero
files written into the repo), then tell me to run `agentacct tui`.

Observe-only: never store, request, or echo any API key; all state stays local
on this machine. Don't modify my global client config without showing the exact
command first.
```

The agent then follows [INSTALL.md](INSTALL.md), the canonical runbook: the global install, the manual per-client setup, and the full per-client capability matrix. `agentacct setup prompt --agent <client>` prints the same prompt.

Want to look around before touching your real data? `agentacct demo` runs a safe local walkthrough in a throwaway temporary store — no provider keys, no paid API calls.

The managed runtime is controlled with `agentacct start` / `status` / `stop` / `repair`; all state lives in the global store (by default `~/.local/state/agentacct/state`; older global stores under `~/.agent-sentinel-global/state` are still recognized). A `--scope project` install keeps its state in the repo's `.agent-sentinel/` directory instead (gitignored; the directory keeps its pre-rename spelling for data compatibility).

### Uninstall

```bash
agentacct stop                 # stop the managed sync + local API (owned processes only)
agentacct uninstall-autostart  # only if you installed autostart
pipx uninstall agentacct
```

Then remove what onboarding added. For a global install (the default): delete the global store (`~/.local/state/agentacct/state` — keep it if you want the history) and the agentacct entries in your user config (`~/.claude.json`, the merged blocks in `~/.claude/settings.json`, the `~/.claude/hooks/` wrapper, and `~/.codex/config.toml`). For a `--scope project` install: delete that repo's `.agent-sentinel/` directory (that project's local ledger) and the agentacct entries onboarding added to `.mcp.json` / `.claude/settings.local.json` / `~/.codex/config.toml`. If you installed the standing instruction block, remove it first with `agentacct setup instructions --agent <client> --user --remove`.

## The terminal dashboard

Prefer the terminal? `agentacct tui` is the full dashboard in your shell — usage 
