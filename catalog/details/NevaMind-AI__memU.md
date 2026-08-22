# NevaMind-AI/memU

Personal memory across agents

## installation

memU works with Codex, Claude Code, Cursor, OpenClaw, Hermes, WorkBuddy, Cola, and more. See [Host adapters](#host-adapters-memory-for-desktop-coding-agents).

**Cross-device · Free · Unlimited · [View online](https://memu.so)**

Get your API key from [memu.so](https://memu.so), then send this message to your agent:

> Read [https://memu.pro/SKILL.md](https://memu.pro/SKILL.md), follow its instructions to install and configure memU, API Key is memu_•••••••••(get Api Key from memu.so).

## configuration

Values resolve in order: process env → `~/.memu/config.env` → default. memU
supports Local and Cloud memory backends, selected by `MEMU_MEMORY_MODE`; an
unset mode remains Local for backward compatibility.

For Local / self-hosted installations, every CLI flag has a matching variable:

| Setting | Env var | Default |
|---|---|---|
| Store | `MEMU_DB` | `./data/memu.sqlite3` (CLI); **required** for host adapters |
| Embedding provider | `MEMU_EMBED_PROVIDER` | `openai` (also: `jina`, `voyage`, `doubao`, `openrouter`); legacy `MEMU_LLM_PROVIDER` still read |
| API key | `MEMU_API_KEY` | the provider's env var, e.g. `OPENAI_API_KEY` |
| Embedding model | `MEMU_EMBED_MODEL` | the provider's default |
| Base URL | `MEMU_BASE_URL` | the provider's default |

Run `<binary> doctor` to display the resolved mode and verify the same retrieval
path the host uses.
