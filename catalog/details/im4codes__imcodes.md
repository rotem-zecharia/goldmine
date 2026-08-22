# im4codes/imcodes

The IM for agents. Shared Agent Context & Memory, supervised execution, and cross-agent audit across AI providers.

## tools

IM.codes exposes a daemon-managed stdio MCP server to supported SDK-backed providers. Agents get one runtime-scoped tool surface for memory, agent-to-agent messaging, and scheduled follow-ups, without raw auth tokens or ad hoc shell commands.

- **Memory recall and provenance.** `search_memory` searches the caller-bound memory namespace for prior work, project history, decisions, preferences, bugs, commits, deployments, and previously discussed context. `list_memory_summaries` retrieves recent compact summaries without a query. Results include compact refs plus `projectionId` values; `get_memory_sources` expands a relevant hit into provenance snippets when the model needs exact prior instructions, bug details, commit/deployment context, or source evidence.
- **Memory writes.** `save_observation` stores useful facts, decisions, or implementation notes as user-private memory candidates; `save_preference` stores stable user preferences through the explicit preference path.
- **Agent messaging.** `send_list_targets` lists sibling sessions in the current project, and `send_message` sends scoped messages, optional file path references, reply requests, or broadcasts through the same guarded `imcodes send` pipeline.
- **Cron scheduling.** `cron_create`, `cron_list`, `cron_update`, and `cron_delete` manage future structured sends for reminders, recurring checks, delegated reviews, or scheduled Team follow-ups, with target/session/project fields and optional expiration/timezone data.
- **Runtime-bound identity and safety.** Tool calls are bound to the current IM.codes session, project, user, and server at runtime. Agents cannot forge namespace, user, server, token, or routing fields; memory, Send, and Cron all remain behind their underlying feature gates plus MCP kill switches.
- **Operational visibility.** The Shared Context UI reports MCP readiness per managed provider, tool-family gate state, degraded reasons, update time, and recent daemon-redacted tool calls so you can tell whether the model really has Memory, Send, and Cron available.

## installation

```bash
npm install -g imcodes
```

## requirements

- macOS or Linux (tested on both)
- **Windows (experimental)**: Native support via ConPTY (built-in on Windows 10+). Just `npm install -g imcodes` — no extra software needed. WSL also works.
- Node.js >= 22
- Terminal multiplexer: [tmux](https://github.com/tmux/tmux) (Linux/macOS). Windows uses ConPTY (auto-detected, built-in).
- At least one AI coding agent: [Claude Code](https://github.com/anthropics/claude-code) (CLI or SDK), [Codex](https://github.com/openai/codex) (CLI or SDK), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [OpenClaw](https://openclaw.com), or [Qwen](https://github.com/QwenLM/qwen-agent)
