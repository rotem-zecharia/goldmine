# activeloopai/hivemind

Hivemind turns your traces into reusable skills across agents

## installation

One command, all your agents.

**macOS / Linux**

```bash
curl -fsSL https://deeplake.ai/hivemind.sh | sh
```

**Windows** — in PowerShell:

```powershell
irm https://deeplake.ai/hivemind.ps1 | iex
```

**Any platform, via npm** — for CI and Dockerfiles, or where policy blocks
piping a downloaded script to a shell. Skips the checks the installers do, so
Node 22+ and a writable npm prefix are on you:

```bash
npm i -g @deeplake/hivemind && hivemind install
```

The installer detects every supported assistant on your machine (table below), wires up the hooks, and shows a one-line consent prompt before opening a browser for sign-in. Restart your assistants after install.

**Headless / CI installs:** pass an API token instead of using the browser flow:

```bash
HIVEMIND_TOKEN=<your-token> hivemind install
# or
hivemind install --token <your-token>
```

Get a token from your account settings on https://deeplake.ai. With no token in a non-interactive shell, the install completes with hooks but skips sign-in; run `hivemind login` later to enable shared memory.

**Install for a specific assistant only:**

```bash
hivemind install --only claude
hivemind claude install    # equivalent
hivemind codex install
hivemind claw install
hivemind cursor install
hivemind hermes install
hivemind pi install
hivemind claude_cowork install   # Alpha
```

**Check what's wired up:**

```bash
hivemind status
```

**Supported assistants:**

| Platform         | Integration                                      | Auto-capture | Auto-recall |
|------------------|--------------------------------------------------|--------------|-------------|
| **Claude Code**  | Marketplace plugin                               | ✅           | ✅          |
| **OpenClaw**     | Native extension                                 | ✅           | ✅          |
| **Codex**        | Hooks (`hooks.json`)                             | ✅           | ✅          |
| **Cursor**       | Hooks (`hooks.json` 1.7+)                        | ✅           | ✅          |
| **Hermes Agent** | Shell hooks (`config.yaml`) + skill + MCP server | ✅           | ✅          |
| **pi**           | Extension API (`pi.on(...)`) + skill + AGENTS.md | ✅           | ✅          |
| **Claude Cowork** 🅰️ | MCP server (Claude Desktop)                  | 🅰️ Alpha¹    | ✅          |

🅰️ **Claude Cowork is Alpha.** Auto-recall (the `hivemind_search` / `read` / `index` tools) is solid. ¹Auto-capture covers **Local Agent Mode** sessions only — those write a transcript we can tail; plain desktop-chat turns leave no readable local trace and aren't captured ([why](#claude-cowork-alpha)).

### Alternative install paths

<details>
  <summary><b>Claude Code plugin marketplace</b></summary>

If you prefer Claude Code's native plugin marketplace:

```
/plugin marketplace add activeloopai/hivemind
/plugin install hivemind
/reload-plugins
/hivemind:login
```

Auto-updates on each session start. Manual update: `/hivemind:update`.
</details>

<details>
  <summary><b>OpenClaw ClawHub</b></summary>

```
openclaw plugins install clawhub:hivemind
```

Then type `/hivemind_login` in chat, click the auth link, and sign in.

#### Commands

| Command | Description |
|---------|-------------|
| `/hivemind_login` | Sign in via device flow |
| `/hivemind_capture` | Toggle capture on/off |
| `/hivemind_whoami` | Show current org and workspace |
| `/hivemind_orgs` | List organizations |
| `/hivemind_switch_org <name>` | Switch organization |
| `/hivemind_workspaces` | List workspaces |
| `/hivemind_switch_workspace <id>` | Switch workspace |
| `/hivemind_update` | Check for plugin updates |

Auto-recall and auto-capture are enabled by default. Data is stored in the same `sessions` table as Claude Code and Codex.

#### Coexistence with `memory-core`

Hivemind runs **alongside** OpenClaw's built-in `memory-core` plugin. It does **not** claim the memory slot, so `memory-core`'s dreaming cron (`"0 3 * * *"`) and other memory-slot-dependent jobs keep

## features

### 🔍 Natural search

Just ask your agent naturally:

```
"What was Emanuele working on?"
"Search traces for authentication bugs we've solved"
"What did we decide about the API design?"
"Show me skills my team has codified for handling migrations"
```

### 🔒 Privacy controls

Disable capture entirely:

```bash
HIVEMIND_CAPTURE=false claude
```

Disable capture for a specific directory tree (persistent, travels with the repo) by dropping a `.hivemind` file with `{ "collect": false }`. See [Per-directory config](#per-directory-config-hivemind).

Enable debug logging:

```bash
HIVEMIND_DEBUG=1 claude
```

## ⚠️ Data collection notice

This plugin captures session activity and stores it in your Deeplake workspace:

| Data                  | What's captured                    |
|-----------------------|------------------------------------|
| User prompts          | Every message you send             |
| Tool calls            | Tool name + full input             |
| Tool responses        | Full tool output                   |
| Assistant responses   | The agent's final response         |
| Subagent activity     | Subagent tool calls and responses  |
| Codified skills       | Patterns extracted from traces     |

**All users in your Deeplake workspace can read this data.** That's the design. Shared capability requires shared substrate. A DATA NOTICE is displayed at the start of every session. Workspace-level isolation prevents data leakage between orgs.

## configuration

| Variable                  | Default                   | Description                                |
|---------------------------|---------------------------|--------------------------------------------|
| `HIVEMIND_TOKEN`          | _(none)_                  | API token (auto-set by login)              |
| `HIVEMIND_ORG_ID`         | _(none)_                  | Organization ID (auto-set by login)        |
| `HIVEMIND_WORKSPACE_ID`   | `default`                 | Workspace name                             |
| `HIVEMIND_API_URL`        | `https://api.deeplake.ai` | API endpoint                               |
| `HIVEMIND_TABLE`          | `memory`                  | SQL table for summaries and virtual FS     |
| `HIVEMIND_SESSIONS_TABLE` | `sessions`                | SQL table for per-event session capture    |
| `HIVEMIND_MEMORY_PATH`    | `~/.deeplake/memory`      | Path that triggers interception            |
| `HIVEMIND_CAPTURE`        | `true`                    | Set to `false` to disable capture          |
| `HIVEMIND_CAPTURE_ONLY_CLI` | _(none)_                | Set to `true` to capture only interactive CLI sessions. Sessions spawned by the Claude Agent SDK (Python/TypeScript) are skipped; their `CLAUDE_CODE_ENTRYPOINT` is `sdk-py` / `sdk-ts`, so they fail the substring check for `cli`. |
| `HIVEMIND_SKILLIFY_EVERY_N_TURNS` | `20`              | Assistant turns between auto skill-mining attempts. Lower = more frequent mining (cheaper sessions, noisier output); higher = fewer attempts on longer histories. |
| `HIVEMIND_SUMMARY_EVERY_N_MSGS` | `50`                | Captured events between periodic session summaries. The first summary of a session runs at 10 events regardless. Raise it to cut background summary runs. |
| `HIVEMIND_SUMMARY_EVERY_HOURS` | `2`                  | Time-based summary cadence, used when at least one new event has arrived since the last summary. |
| `HIVEMIND_WIKI_WORKER`    | _(none)_                  | Set to `1` to disable the background session-summary worker entirely (no `claude -p` summary runs). Also set automatically inside the worker as a recursion guard. Capture and recall keep working. |
| `HIVEMIND_GRAPH_ON_STOP`  | _(none)_                  | Set to `0` to disable the code-graph rebuild that runs on `Stop` / `SessionEnd`. |
| `HIVEMIND_EMBEDDINGS`     | `true`                    | Set to `false` to force lexical-only mode  |
| `HIVEMIND_PROACTIVE_RECALL_DISABLED` | _(none)_       | Set to `1` to disable **proactive recall** (auto-searching team memory on each recall-worthy prompt and injecting a relevant snippet into the agent's context). On by default. Does **not** affect capture or the agent's own grep/skill recall. Alt form: `HIVEMIND_PROACTIVE_RECALL=0`. |
| `HIVEMIND_RECALL_MIN_OVERLAP` | `2`                   | Proactive recall (lexical mode): min distinct prompt keywords a summary must share to be injected. Higher = stricter. |
| `HIVEMIND_RECALL_TIMEOUT_MS` | `1000`                 | Proactive recall: hard cap on the synchronous search path; on timeout it skips rather than delay the turn. |
| `HIVEMIND_DEBUG`          | _(none)_                  | Set to `1` for verbose hook debug logs     |

## Per-directory config (`.hivemind`)

The variables above set **one global identity** for the whole machine. A `.hivemind` file lets a specific directory tree override that: either **route** it to a different org/workspace, or **opt out** of capture entirely.

Routing is symmetric — a routed directory both writes its traces to that workspace **and reads memory from it**. Sessions started under it search, recall, and browse `~/.deeplake/memory` in the routed workspace, and `hivemind whoami` reports it.

Drop a `.hivemind` JSON file at the root of the tree you want to configure:

```json
{
  "orgId": "acme-corp",
  "workspaceId": "client-work",
  "collect": true
}
```

| Field         | Effect                                                                        |
|---------------|-----

## limitations

- **Trajectory export for fine-tuning.** Because traces are stored in Deeplake's tensor format, they're export-ready as PyTorch datasets. Teams running their own open-source models can fine-tune on their org's accumulated trajectories. A handful of advanced customers are already doing this against the trajectories their Claude Code and Codex agents generated.
- **GPU-accelerated dense retrieval at scale.** Local CPU embeddings already ship via the optional nomic-embed daemon (see [Semantic search](#semantic-search-optional)). Next: GPU-accelerated vector search over the full trace store, on by default.
- **Skill versioning and review.** Pre-release human review for codified skills before they propagate org-wide, for teams that want a curation step.
- **More agents.** If your team uses an agent that isn't on the supported-assistants list above, open an issue.

## Security & storage

### Tenant isolation & encryption

- TLS between every agent and Deep Lake. AES-256 on the bytes once they land. Your cloud credentials live in Deep Lake's vault, and Hivemind never sees the raw keys.
- Org and workspace boundaries enforced at the storage layer, not just the API. Sessions never share a row, a partition, or an index with another workspace.
- Disable capture per session with `HIVEMIND_CAPTURE=false`. Delete a workspace and the underlying objects go with it.

### Code-level controls

- SQL values escaped with `sqlStr()`, `sqlLike()`, `sqlIdent()`
- ~70 allowlisted builtins run in the virtual FS; unrecognized commands are denied
- Credentials stored with mode `0600`, config dir with mode `0700`
- Device flow login: no tokens in environment or code

### Bring your own cloud (BYOC)

Hivemind Cloud is the default. When that isn't enough, point Hivemind at storage in your own cloud. We handle the orchestration, data never leaves your perimeter.

| Provider                   | Status     | Setup                                                  |
|----------------------------|------------|--------------------------------------------------------|
| Google Cloud Storage       | Available  | [docs](https://docs.deeplake.ai/latest/guide/gcs/)     |
| Azure Blob Storage         | Available  | [docs](https://docs.deeplake.ai/latest/guide/azure/)   |
| Amazon S3                  | Available  | [contact us](https://deeplake.ai/hivemind#security)    |
| S3-compatible on-prem      | On request | [contact us](https://deeplake.ai/hivemind#security)    |

## Who builds Hivemind

Hivemind is built and maintained by [Activeloop](https://activeloop.ai), the open-source team behind [Deeplake](https://github.com/activeloopai/deeplake), backed by Y Combinator.

We run Hivemind ourselves, all day, across Claude Code, OpenClaw, Codex, and Cursor. Every benchmark number above came from our own internal eval against the LoCoMo public benchmark. If you're running coding agents at a team or org and want to talk through your setup, drop us a line: [hello@activeloop.ai](mailto:hello@activeloop.ai).

## Got questions?

Setup, BYOC, agent integrations, or workflow. Come ask in the community:

<p align="center">
  <a href="https://join.slack.com/t/hubdb/shared_invite/zt-35zr0yil0-lnzJcQhACsBlB7~3lufrCg"><img src="https://img.shields.io/badge/Join_us_on-Slack-4A154B?logo=slack&logoColor=white&style=for-the-badge" alt="Join us on Slack"></a>
</p>

## Development

```bash
git clone https://github.com/activeloopai/hivemind.git
cd hivemind
npm install
npm run build     # tsc + esbuild → harnesses/claude-code/bundle/ + harnesses/codex/bundle/ + cursor/bundle/ + harnesses/openclaw/dist/ + mcp/bundle/ + bundle/cli.js
npm test          # vitest
```

Test locally with Claude Code:

```bash
claude --plugin-dir claude-code
```

Interactive shell against Deeplake:

```bash
npm run shell
```

## Star history

<p align="center">
  <a href="https://star-history.com/#activeloopai/hivemind&Date">
    <img src="https://api.star-history.com/svg?repos=activeloopai/hivemind&type=Date" alt="Sta
