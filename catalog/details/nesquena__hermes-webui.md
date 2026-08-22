# nesquena/hermes-webui

Hermes WebUI: The best way to use Hermes Agent from the web or from your phone!

## features

Most AI tools reset every session. They don't know who you are, what you worked on, or what
conventions your project follows. You re-explain yourself every time.

Hermes retains context across sessions, runs scheduled jobs while you're offline, and gets
smarter about your environment the longer it runs. It uses your existing Hermes agent setup,
your existing models, and requires no additional configuration to start.

What makes it different from other agentic tools:

- **Persistent memory** — user profile, agent notes, and a skills system that saves reusable
  procedures; Hermes learns your environment and does not have to relearn it
- **Self-hosted scheduling** — cron jobs that fire while you're offline and deliver results to
  Telegram, Discord, Slack, Signal, email, and more
- **10+ messaging platforms** — the same agent available in the terminal is reachable from your phone
- **Self-improving skills** — Hermes writes and saves its own skills automatically from experience;
  no marketplace to browse, no plugins to install
- **Provider-agnostic** — OpenAI, Anthropic, Google, DeepSeek, OpenRouter, and more
- **Orchestrates other agents** — can spawn Claude Code or Codex for heavy coding tasks and bring
  the results back into its own memory
- **Self-hosted** — your conversations, your memory, your hardware

**vs. the field** *(landscape is actively shifting — see [docs/why-hermes.md](docs/why-hermes.md) for the full breakdown)*:

| | OpenClaw | Claude Code | Codex CLI | OpenCode | Hermes |
|---|---|---|---|---|---|
| Persistent memory (auto) | Yes | Partial† | Partial | Partial | Yes |
| Scheduled jobs (self-hosted) | Yes | No‡ | No | No | Yes |
| Messaging app access | Yes (15+ platforms) | Partial (Telegram/Discord preview) | No | No | Yes (10+) |
| Web UI (self-hosted) | Dashboard only | No | No | Yes | Yes |
| Self-improving skills | Partial | No | No | No | Yes |
| Python / ML ecosystem | No (Node.js) | No | No | No | Yes |
| Provider-agnostic | Yes | No (Claude only) | Yes | Yes | Yes |
| Open source | Yes (MIT) | No | Yes | Yes | Yes |

† Claude Code has CLAUDE.md / MEMORY.md project context and rolling auto-memory, but not full automatic cross-session recall  
‡ Claude Code has cloud-managed scheduling (Anthropic infrastructure) and session-scoped `/loop`; no self-hosted cron

**The closest competitor is OpenClaw** — both are always-on, self-hosted, open-source agents
with memory, cron, and messaging. The key differences: Hermes writes and saves its own skills
automatically as a core behavior (OpenClaw's skill system centers on a community marketplace);
Hermes is more stable across updates (OpenClaw has documented release regressions and ClawHub
has had security incidents involving malicious skills); and Hermes runs natively in the Python
ecosystem. See [docs/why-hermes.md](docs/why-hermes.md) for the full side-by-side.

---

## installation

Run the repo bootstrap:

```bash
git clone https://github.com/nesquena/hermes-webui.git hermes-webui
cd hermes-webui
python3 bootstrap.py
```

Or keep using the shell launcher:

```bash
./start.sh
```

For self-hosted VM or homelab installs, `ctl.sh` wraps the common daemon lifecycle commands without requiring `fuser` or `pkill`:

```bash
./ctl.sh start              # background daemon, PID at ~/.hermes/webui.pid
./ctl.sh status             # PID, uptime, bound host/port, log path, /health
./ctl.sh logs --lines 100   # tail ~/.hermes/webui.log
./ctl.sh restart
./ctl.sh stop
```

`ctl.sh start` runs the bootstrap in foreground/no-browser mode behind the daemon wrapper, writes logs to `~/.hermes/webui.log`, and respects `.env` plus inline overrides such as `HERMES_WEBUI_HOST=0.0.0.0 ./ctl.sh start`.

> **Stopping the server.** Each launch method has its own stop path because only `ctl.sh start` writes a PID file (`~/.hermes/webui.pid`):
>
> | Launch method | How to stop |
> |---|---|
> | `python3 bootstrap.py` | **Ctrl-C** in the terminal (runs in the foreground) |
> | `./ctl.sh start` | `./ctl.sh stop` (sends SIGTERM, waits, then SIGKILL) |
> | Detached `bootstrap.py` (no `--foreground`) or `./start.sh` | Find the PID via `lsof -i :8787` (or `ss -tlnp`) and `kill` it |
>
> `./ctl.sh stop` cannot stop a server launched by `bootstrap.py` or `start.sh` directly — it only manages processes it started itself.

> **How chat runs by default.** WebUI runs the Hermes agent in-process, reading
> your `HERMES_HOME` config directly. It does not connect to an external
> Hermes/agent OpenAI-compatible API server to run chat. `HERMES_API_URL` is only
> read by the Tasks/cron health probe and does not route chat.
>
> Two options if you run an external endpoint:
>
> 1. **Use its models as a chat provider** (supported today): add it in
>    **Settings → Providers** as a custom OpenAI-compatible provider with
>    `base_url = http://127.0.0.1:8642/v1` and your bearer token.
> 2. **Route chat through a Hermes Gateway API server** (supported today via
>    `HERMES_WEBUI_CHAT_BACKEND=gateway`): see [`docs/advanced-chat-setup.md`](docs/advanced-chat-setup.md).
>    Full agent-loop delegation is not yet shipped; tracked in [#1925](https://github.com/nesquena/hermes-webui/issues/1925).

## configuration

- **Hermes Control Center** (sidebar launcher button) -- Conversation tab (export/import/clear), Preferences tab (model, send key, theme, language, all toggles), System tab (version, password)
- Send key: Enter (default) or Ctrl/Cmd+Enter
- Show/hide CLI sessions toggle (enabled by default)
- Token usage display toggle (off by default, also via `/usage` command)
- Control Center always opens on the Conversation tab; resets on close
- Unsaved changes guard -- discard/save prompt when closing with unpersisted changes
- Cron completion alerts -- toast notifications and unread badges scoped to the active profile on the Tasks tab and session sidebar
- Background agent error alerts -- banner when a non-active session encounters an error

## tools

- Type `/` in the composer for autocomplete dropdown
- Plain skills match case-insensitive keywords in their name or description; built-in, agent/plugin, and bundle commands keep prefix matching and take precedence over a same-slug skill
- Built-in: `/help`, `/clear`, `/compress [focus topic]`, `/compact` (alias), `/model <name>`, `/workspace <name>`, `/new`, `/usage`, `/theme`
- Arrow keys navigate, Tab/Enter select, Escape closes
- Unrecognized commands pass through to the agent
