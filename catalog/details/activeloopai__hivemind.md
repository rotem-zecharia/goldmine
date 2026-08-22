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

## limitations

- **Trajectory export for fine-tuning.** Because traces are stored in Deeplake's tensor format, they're export-ready as PyTorch datasets. Teams running their own open-source models can fine-tune on their org's accumulated trajectories. A handful of advanced customers are already doing this against the trajectories their Claude Code and Codex agents generated.
- **GPU-accelerated dense retrieval at scale.** Local CPU embeddings already ship via the optional nomic-embed daemon (see [Semantic search](#semantic-search-optional)). Next: GPU-accelerated vector search over the full trace store, on by default.
- **Skill versioning and review.** Pre-release human review for codified skills before they propagate org-wide, for teams that want a curation step.
- **More agents.** If your team uses an agent that isn't on the supported-assistants list above, open an issue.
