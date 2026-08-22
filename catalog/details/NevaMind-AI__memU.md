# NevaMind-AI/memU

Personal memory across agents

## installation

memU works with Codex, Claude Code, Cursor, OpenClaw, Hermes, WorkBuddy, Cola, and more. See [Host adapters](#host-adapters-memory-for-desktop-coding-agents).

**Cross-device · Free · Unlimited · [View online](https://memu.so)**

Get your API key from [memu.so](https://memu.so), then send this message to your agent:

> Read [https://memu.pro/SKILL.md](https://memu.pro/SKILL.md), follow its instructions to install and configure memU, API Key is memu_•••••••••(get Api Key from memu.so).

## Agent support

This matrix lists the currently tested memU integrations by operating system.

- **Memorize** — capture useful session knowledge through a scheduled background task and turn it into reusable memory.
- **Retrieve** — bring relevant memory into a future task.
- **⚠️** — supported with an important limitation; see the user note.

### macOS

| Agent | Mode | Memorize | Retrieve | User note |
| --- | --- | :---: | :---: | --- |
| ChatGPT | ChatGPT(Work mode), codex and VS Code extension | ✅ | ✅ | |
| ChatGPT | Chat | ❌ | ❌ | Chat mode is not currently supported. Please use Work mode. |
| Claude Code | Desktop and CLI | ✅ | ✅ | If the selected model declines the setup steps, retry with **Opus** or another model. Sonnet 5 can occasionally do this. |
| Claude | Chat and Cowork | ❌ | ❌ | |
| Cursor | — | ✅ | ✅ | |
| OpenClaw | — | ✅ | ✅ | Retrieve support has not yet been verified. |
| Hermes Agent | — | ✅ | ✅ | |
| WorkBuddy | — | ✅ | ✅ | |

### Windows

| Agent | Mode | Memorize | Retrieve | User note |
| --- | --- | :---: | :---: | --- |
| ChatGPT | ChatGPT(Work mode), codex and VS Code extension | ✅ | ✅ | |
| ChatGPT | Chat | ❌ | ❌ | Chat mode is not currently supported. Please use Work mode. |
| Claude Code | Desktop and CLI | ✅ | ✅ | If the selected model declines the setup steps, retry with **Opus** or another model. Sonnet 5 can occasionally do this. |
| Claude | Chat and Cowork | ❌ | ❌ | |
| Cursor | — | ✅ | ✅ | |
| OpenClaw | — | ✅ | ✅ | |
| Hermes Agent | — | ✅ | ⚠️ | Use a memU version with Windows `HERMES_HOME` support; older versions may retrieve from the wrong files. |
| WorkBuddy | — | ✅ | ✅ | With Hy3, retrieval may fail. Retry with another model if this happens. |

### Linux

| Agent | Mode | Memorize | Retrieve | User note |
| --- | --- | :---: | :---: | --- |
| Codex | VS Code extension | ❌ | ✅ | |
| Claude Code | CLI | ✅ | ✅ | |
| OpenClaw | 4.23 / 7.1 | ✅ | ✅ | |

Support status reflects the current release and may change as host integrations evolve.

## How it works

![memU memory system architecture](assets/structure-v2.png)

## Automatic skill extraction

Once the scheduled bridging task is installed, memU can turn useful agent history into reusable Markdown skills automatically.

![How memU turns agent history into reusable skills](assets/skill-extraction.png)

1. **Capture new sessions.** The host adapter reads new session history, including messages and tool calls.
2. **Prepare self-evolve jobs.** `prepare` slices each session into a self-contained job with the paths and context the agent needs.
3. **Let the agent decide.** The agent reads related existing skills, then chooses to do nothing, patch an existing skill, or create a new one.
4. **Write readable skill Markdown.** Each skill has a name, description, and reusable workflow, including useful branches, edge cases, and pitfalls.
5. **Commit and index.** `commit` submits changed skill files through `commit_results`; memU embeds the skill name and description and stores it under the `skill` track.
6. **Retrieve it later.** On a similar future task, memU returns the relevant skill so any connected agent can use the learned workflow.

The judgment and synthesis stay inside the agent. `MemoryService` makes no LLM or chat calls; it stores, embeds, and retrieves the skill Markdown the agent prepared.

## Self-hosted

**Private · Single-device · Embedding key required**

To run memU locally with your own storage and embedding provider, send this message to your 

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

### Storage backends

| Provider | DSN | Vector search | Use for |
|---|---|---|---|
| `inmemory` | — | brute-force cosine | tests, throwaway sessions |
| `sqlite` | `sqlite:///path.sqlite3` | brute-force cosine | local/default, single writer |
| `postgres` | `postgresql://...` | pgvector | concurrent access, large stores (`pip install "memu-cli[postgres]"`) |

```python
service = MemoryService(
    database_config={"metadata_store": {"provider": "postgres", "dsn": "postgresql://..."}},
    embedding_profiles={"default": {"provider": "jina"}},
)
```
## License

Apache-2.0


<sub>Partnership Community: <a href="https://linux.do">LINUX DO</a></sub>
