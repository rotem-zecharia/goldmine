# dcostenco/prism-coder

Persistent session memory for AI coding agents — local-first, with on-device inference, associative recall, and drift detection. Works with Claude Code, Cursor, and Codex.

## installation

Prism also ships as a plugin, which registers the MCP server and the startup
skill for you.

**Claude Code** — from the community marketplace:

```bash
/plugin marketplace add anthropics/claude-plugins-community
/plugin install synalux-prism@claude-community
```

**Codex** — this repository is itself a plugin marketplace:

```bash
codex plugin marketplace add dcostenco/prism-coder
codex plugin add synalux-prism@prism
```

The plugin registers `prism-mcp` via `npx -y prism-mcp-server`. If you already
configured Prism by hand — `prism connect` writes an `mcp_servers.prism-mcp`
entry — you have that server twice under one key. Install the plugin **or**
run `prism connect`, not both.

### What `prism connect` changes about host subagents

`connect` steers bounded work to `prism_infer` on your machine rather than to
host-spawned agents. What it writes differs per host, and **it does not disable
subagents everywhere** — Claude Code keeps them and is pointed at an economy
model instead. Prism's local workers stay available over MCP in every case.

| Host | Setting written | Effect |
|---|---|---|
| Claude Code | `env.CLAUDE_CODE_SUBAGENT_MODEL = "sonnet"` in `~/.claude/settings.json` | Subagents stay **enabled**, pinned to an economy model. Fan-out is discouraged by policy text, not by config |
| Gemini CLI | `experimental.enableAgents = false` in `~/.gemini/settings.json` | Subagents **off**. Gemini exposes one boolean, so that is all there is to set |
| Codex | `features.multi_agent = false` in `$CODEX_HOME/config.toml` (default `~/.codex`), plus a bounded fallback: 2 threads, depth 1, cheap subagent model, 900s cap | Subagents **off**, with a bounded profile underneath so a deliberate re-enable lands somewhere sane |

Two things worth knowing:

- **`experimental` is Gemini's namespace, not ours.** Prism is not enabling
  anything experimental — it writes `false` to a flag Gemini already defines at
  that path. Writing anywhere else would have no effect.
- **That namespace is by definition temporary.** If Gemini promotes
  `enableAgents` out of `experimental`, Prism keeps writing the old path, Gemini
  reads the new one, and host subagents quietly turn back on. Nothing errors and
  the settings file still looks correct. If you see host subagents running while
  `enableAgents` reads `false`, check whether the key has moved before assuming
  `connect` failed to write it.

Both writes are idempotent in the sense that a host already configured this way
is left untouched — but they are **re-applied on every `prism connect` run**,
not only on `--refresh`. If you deliberately re-enable host subagents, the next
`connect` will turn them off again. Keep them on by not re-running `connect`,
or by re-enabling after each run.

---

<details>
<summary>Release history (optional)</summary>

## What's New in v20.12.1

- **`prism connect --refresh` now converges every registration it owns**, not
  just the top-level one — directory-scoped entries could otherwise keep
  launching an old build indefinitely.
- **`prism update` checks the installed package**, not the CLI that happens to
  be running, so it can no longer report "current" while the install is stale.
- **The opt-in scheduled updater can actually start** — the LaunchAgent now
  carries a PATH that includes node and npm.

## What's New in v20.12.0

- **Prism now tells you when it's out of date.** Session startup shows a
  one-line update notice when a newer release exists — cache-backed, at most
  one registry check per day, silent offline. `PRISM_NO_UPDATE_CHECK=1`
  opts out.
- **Hands-free updates, if you want them.** `prism autoupdate enable` sets up
  a daily `prism update --if-idle`: it updates only the global npm package,
  defers while any Prism server is running, and never touches host
  configuration — that stays behind a visible `prism connect`.

## What's New in v20.11.1

- **Saving memory never gets refused.** The save path used to reject
  `session_save_ledger`/`save_handoff` c

## configuration

`prism connect` now reads Claude, Cursor, Gemini, and Codex configuration
through a single verified file snapshot, preventing another process from
swapping a file between Prism's safety check and its read. Supported symlinked
dotfiles still work, while dangling or planted symlinks fail loudly instead of
being followed or overwritten. This release also carries the patched
dependencies and cross-platform release checks introduced in v20.2.5.

Cloud fallback is now documented consistently as Gemini 3.6 Flash. Plan
ceilings govern automatic `prism_infer` routing; direct use of any downloaded
model through local Ollama remains free on every tier.

---

## What's New in v20.2.4

### Reliable Session Memory That Shows Work, Not Greetings
Greeting-only assistant replies are skipped before ledger writes. Existing
greeting rows are filtered at read time across native startup, MCP context, and
`prism load --json`, while entries containing decisions, TODOs, changed files,
or non-session events remain visible. Historical rows are not destructively
deleted. If Synalux has a transient startup failure, Prism displays one bounded
local last-good snapshot and clearly labels it; permanent authorization or
validation failures still fail loud, and later writes remain cloud-routed.

---

## What's New in v20.2.2

### One Local-First Workflow Across Every Agent
`prism connect` now installs one orchestration contract for Claude Code,
Claude Desktop, Cursor, Gemini CLI, and Codex. Bounded delegated work goes to
`session_task_route` and the local `prism_infer` worker first; routine work must
not create background host agents. Local workers can receive the active
project's dashboard-configured quick, standard, or deep memory and select a
RAM-safe 2B/4B/9B/27B model at call time. The router forwards complexity but
does not choose the model; `prism_infer` owns the final decision using memory
and context fit, installed models, live RAM, entitlements, and explicit caller
overrides.

Codex and Gemini native agent fan-out are disabled during connect. Codex keeps
a two-thread, one-level Terra/low fallback profile if the developer explicitly
re-enables native agents later. Claude Code keeps native agents as a last-resort
path but pins their model to Sonnet. Cursor and Claude Desktop do not expose a
supported global subagent-policy file, so they receive the identical workflow
through Prism's MCP server instructions. `prism_infer` safety boundaries and
the host's final verification responsibility are unchanged.

### Subscription-Tier Skills Arrive Before the First Host Launch
`prism connect` now downloads the authoritative Synalux skill manifest and
materializes entitled packages in the native `~/.agents/skills` directory
before the command exits. Codex therefore sees the current skillset on its
first launch instead of requiring a second restart. Prism rechecks the same
snapshot at MCP startup, session load, and every five minutes—without host
lifecycle hooks.

On the first user turn, Prism's native skill, MCP metadata, and managed host
instructions request one `session_bootstrap({})` call. Prism then uses the
dashboard's developer name, Auto-Load Projects, and quick, standard, or deep
setting. The response stays focused on greeting and session state because tier
skills are already present in the host's native skill directory.

Hook-free MCP can provide and prioritize that ready-to-display block, but the
host model still owns the final assistant message and may summarize it. Prism
does not claim a deterministic verbatim greeting on third-party chat surfaces;
that would require a host lifecycle hook, launcher, extension, or Prism-owned
panel. Context loading itself remains complete even when a host shortens the
visible reply.

Free accounts receive only the public hook-free `prism-startup` package; the MCP
server still supplies a compact, non-proprietary safety and evidence contract.
Authenticated paid accounts receive the protected behavioral and engineering
pack

## requirements

External contributions now require signing the [Individual CLA](./CLA.md). The CLA check is merge-blocking on the `main` branch.

---

</details>

## features

Your AI agent forgets everything between sessions. Prism fixes that — and adds verification, drift detection, and multi-agent coordination on top.

### Mind Palace — persistent memory that survives across sessions

Every conversation feeds a persistent store. The next session loads the right context automatically — no re-explaining.

<p align="center">
  <img src="docs/mind-palace-dashboard-v20.8-full.png" alt="Mind Palace Dashboard — full page: session ledger, memory analytics, lifecycle controls, background scheduler" width="700" />
</p>

The dashboard shows your current project state, pending TODOs, intent health, and a neural knowledge graph — all built automatically from your agent sessions.

### Export — read the record outside the agent

`session_export_memory` writes your memory out as plain files you can read,
diff, and commit. Nothing goes through a model to produce it.

```
markdown   human-readable — drop it in a PR to show what the agent actually did
json       machine-readable — import into another Prism instance
vault      zipped Markdown with YAML frontmatter and [[wikilinks]] (Obsidian, Logseq)
```

This is the surface to reach for when you want to answer "did the agent verify
this, or is it claiming it did?" — the export is a record you review after the
fact, in a diff or a pull request, rather than a live view you have to go and
open. The same data is available from the dashboard's **Export ZIP** and
**Export Vault** buttons.

### Knowledge Graph — semantic + keyword + graph search

Ask "what did I decide about the auth flow last month?" and get an answer with citations, combining vector similarity, full-text search, and graph traversal.

<p align="center">
  <img src="docs/knowledge-graph.jpg" alt="Knowledge Graph — 190 keywords, 47 edges, 12 projects visualized" width="500" />
</p>

### Session History — immutable audit trail

Every session is logged with files changed, decisions made, and TODOs. Search, filter, and replay any past session.

<p align="center">
  <img src="docs/session-ledger.jpg" alt="Session Ledger — 93 sessions, 847 decisions logged across 12 projects" width="700" />
</p>

### Inference Metrics — see where your tokens go

Every `prism_infer` call tracks which model handled it (local Ollama vs cloud) and how many tokens were consumed. When you save a session, Prism shows a summary:

```
📊 Inference Metrics (this session):
  Total calls: 12 — Local: 10 (83%) | Cloud: 2 (17%)
  Prompt tokens: 7,840 evaluated / 8,420 submitted est.
  Completion tokens: 3,150
  Cloud tokens saved (est.): 11,570 — token volume handled locally instead of cloud
  Avg latency: 1,240ms
  By model:
    prism-coder:27b: 6 calls, 7,200 tokens, avg 1,800ms
    prism-coder:9b: 4 calls, 2,870 tokens, avg 620ms
    synalux-27b: 2 calls, 1,500 tokens, avg 1,100ms
```

**Cloud tokens saved** is the honest routing metric — it accrues only when local Ollama handles a call that would otherwise have gone to Synalux cloud inference. A compact version appears inline after every 5th `prism_infer` call: `📊 local 10 (83%) · cloud 2 (17%) · ~11,570 tok · avg 1,240ms · 11,570 cloud tok saved`.

Local calls use actual Ollama token counts (`prompt_eval_count` / `eval_count` from Ollama); cloud calls use char/4 estimates. Metrics are tracked locally — no portal dependency, no env vars, works offline. Per-call data is also forwarded to the Synalux portal as best-effort analytics (independent of the display).

### Session Drift Detection

Long agent sessions can wander from their original goal. `session_detect_drift` compares current work against the stated goal and returns `on_track / minor_drift / major_drift` so the agent can self-correct.

### Behavioral Verification — catch bad edits before they happen

AI agents apply patterns from checklists without understanding the real-world impact. The `verify_behavior` tool challenges the agent with a scenario it must answer **before** editing — forcing it to think through what the end user wi

## tools

| Feature | Prism Coder | Ollama | LM Studio | Mem0 | Zep |
|---|:---:|:---:|:---:|:---:|:---:|
| Local inference cascade | ✅ | ✅ runtime | ✅ app | — | — |
| Cloud fallback | ✅ optional | — | ◐ provider-dependent | ◐ | ◐ |
| Persistent memory | ✅ | — | ◐ project context | ✅ | ✅ |
| Knowledge/tool integration | ✅ MCP + ingestion | ◐ APIs | ◐ integrations | ✅ SDK/API | ✅ SDK/API |
| MCP server | ✅ native | — | ◐ client integration | ◐ client integration | ◐ client integration |

### Pricing

Prism's current published tiers are listed below. Competitor pricing is
usage- and plan-dependent, so consult the provider directly: [GitHub
Copilot](https://github.com/features/copilot/plans), [Cursor](https://cursor.com/en-US/pricing),
and [Amazon Q Developer](https://aws.amazon.com/q/developer/pricing/).

---

## Plans

All on-device models are free to run locally via Ollama on every tier. A subscription gates **cloud** features, higher automatic-routing ceilings, and increased limits. On-device models run through your Ollama regardless of plan; the ceiling applies only to cloud inference and automatic `prism_infer` routing.

| | **Free** | **Standard** $19/mo | **Advanced** $49/mo | **Enterprise** $99/mo |
|---|---|---|---|---|
| Seats | 1 | 1 | up to 5 | up to 25 |
| Automatic `prism_infer` ceiling | up to 4b | up to 9b | up to 27b | up to 27b |
| Cloud inference | -- | ✅ | ✅ | ✅ (priority) |
| Cloud Coder (Web IDE) | -- | ✅ | ✅ | ✅ (priority) |
| Cloud search | -- | ✅ | ✅ | ✅ |
| Max output tokens | 512 | 1,024 | 2,048 | 4,096 |
| Cloud fallback | -- | Gemini 3.6 Flash | Gemini 3.6 Flash | Gemini 3.6 Flash (priority) |
| Grounding verifier (fact-check AI output) | -- | ✅ | ✅ | ✅ |
| Memory sync (cloud) | -- | ✅ | ✅ | ✅ |
| Knowledge / session memory | limited | unlimited | unlimited | unlimited |
| Analytics dashboard | -- | ✅ | ✅ | ✅ |
| HIPAA BAA | -- | -- | -- | ✅ |

14-day free trial on paid plans. 25+ seats: [contact sales](https://synalux.ai/support)

---

## How agents use it

Prism exposes 40+ MCP tools. The core memory loop:

| Tool | What it does |
|---|---|
| `session_bootstrap` | Hook-free first-turn greeting and dashboard-configured context |
| `session_load_context` | Explicit project reload or older-server startup fallback |
| `session_save_ledger` | Append an immutable session log entry |
| `session_save_handoff` | Save live state for the next session |
| `knowledge_search` | Semantic + keyword search over all memories |
| `query_memory_natural` | Memory-first Q&A with a grounded live-source fallback on paid tiers |
| `session_detect_drift` | Detect when a session has drifted from its goal |
| `verify_behavior` | Pre-edit scenario challenge — catch bad changes before they happen |
| `knowledge_ingest` | Teach Prism a codebase or document |
| `prism_infer` | Local-first inference (route/chat/code modes, thinking, cloud escalation) |
| `inference_metrics` | Session delegation or persisted MCP + VS Code panel local/cloud stats |

### `query_memory_natural` — memory first, current sources when needed

Ask one natural-language question instead of choosing separate memory, search,
scrape, and inference tools. Prism searches its accumulated project memory
first. If no useful evidence exists, paid tiers run one bounded Synalux search
(Firecrawl, Gemini 3.6 Google Search grounding, then legacy Brave fallback),
resolve and preserve the source URLs, scrape the leading page, and ask a
RAM-safe local Prism Coder model to answer from that evidence. The paid-tier
Gemini 3.6 verifier checks the draft before it is served. Reserved or uncertain
clinical content never enters the web-grounded local path; it follows Prism's
cloud-or-refuse safety boundary.

### `prism_infer` — local-first inference with cloud escalation

```typescript
prism_infer({
    prompt: "Write a binary search in Python",
    mode: "code",        // "route" | "chat" | "code"
    think: true,          // enable <think> reasoning (default: true for chat/code)
    model_
