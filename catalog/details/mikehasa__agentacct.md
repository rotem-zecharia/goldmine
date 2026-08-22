# mikehasa/agentacct

See what your coding agents did and what it cost. Breaks each task down into work steps — tools used, files changed, tests run, time and tokens spent. Local-first dashboard for Claude Code, Codex, Ope

## installation

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
