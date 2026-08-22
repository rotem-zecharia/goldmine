# osaurus-ai/osaurus

Own your AI. The native macOS harness for AI agents -- any model, persistent memory, autonomous execution, cryptographic identity. Built in Swift. Fully offline. Open source.

## installation

```bash
brew install --cask osaurus
```

Or download the latest `.dmg` from [Releases](https://github.com/osaurus-ai/osaurus/releases/latest). After installing, launch from Spotlight (`⌘ Space` → "Osaurus") or the CLI:

```bash
osaurus ui       # Open the chat UI
osaurus serve    # Start the server
osaurus status   # Check status
```

> Requires macOS 15.5+ and Apple Silicon.

## Agents

Agents are the core of Osaurus. Each one gets its own prompts, memory, and visual theme -- a research assistant, a coding partner, a file organizer, whatever you need. Tools and skills are automatically selected via RAG search based on the task at hand -- no manual configuration needed. Everything else in the harness exists to make agents smarter, faster, and more capable over time.

Agents can also opt into a private local database and a single self-scheduled next run -- see [Agent DB & Self-Scheduling](docs/AGENT_DB.md). Local storage is plaintext by default (protected by FileVault) with opt-in SQLCipher encryption -- see [Storage](docs/STORAGE.md).

### Agent Loop

Every chat is an agent loop. Pick a working folder and the agent gets file, search, and git tools. Toggle the sandbox and it gets shell access in an isolated sandbox. The model writes a markdown todo list, executes against it, and closes out with a verified summary -- all in the same chat window. See the [Agent Loop Guide](docs/AGENT_LOOP.md).

### Sandbox

Agents execute code in an isolated Linux VM powered by Apple's [Containerization](https://developer.apple.com/documentation/containerization) framework. Full dev environment -- shell, Python, Node.js, compilers, package managers -- with zero risk to your Mac.

Each agent gets its own Linux user and home directory. The VM connects back to Osaurus (inference, memory, secrets) via a vsock bridge -- sandboxed but not disconnected. Extend with simple JSON plugin recipes, no Xcode or code signing required.

```
┌────────────────┐       ┌────────────────────────────┐
│    Osaurus     │       │   Linux VM (Alpine)        │
│                │       │                            │
│  Sandbox Mgr ──┼───────┤→ /workspace  (VirtioFS)    │
│  Host API   ←──┼─vsock─┤→ osaurus-host bridge       │
│                │       │                            │
│                │       │  agent-alice  (Linux user) │
│                │       │  agent-bob    (Linux user) │
└────────────────┘       └────────────────────────────┘
```

> The Linux VM requires macOS 26+ (Tahoe). On earlier versions Osaurus falls back to a native macOS Seatbelt sandbox: commands run on your Mac under `sandbox-exec` confinement, with writes limited to the sandbox workspace, `pip`/`npm` installs (no `apk`), and all-or-nothing network access instead of per-domain allowlists. See the [Sandbox Guide](docs/SANDBOX.md) for configuration, built-in tools, and plugin authoring.

### Memory

Three layers -- identity, pinned facts, and per-session episodes -- plus a transcript fallback. Agents distill conversations once at session end (not on every turn), score what matters by salience, and surface at most one compact slice per request based on what you're actually asking. A background consolidator decays, merges, and evicts so memory stays sharp instead of bloating. Most turns inject ~800 tokens or less; many inject zero. See the [Memory Guide](docs/MEMORY.md).

### Privacy Filter

When you send to a cloud model, an on-device classifier — OpenAI's `openai/privacy-filter` (Apache-2.0, 1.5B params / 50M active sparse-MoE), served via the MLX conversion `mlx-community/openai-privacy-filter-bf16` (~2.8 GB) — detects names, emails, phones, URLs, addresses, dates, account numbers, and free-form secrets, alongside deterministic regex for SSN, credit cards, IBAN, AWS keys, GitHub tokens, and your own custom patterns. Each detection is shown in a review sheet with a scrubbed preview before sending; approved entities are swapped for stable `[PERSON_1]` / `[EMAIL_2]` placeholders, and streaming rep

## tools

```bash
osaurus tools install osaurus.calendar   # Install from registry
osaurus tools list                       # List installed
osaurus tools create MyPlugin --swift    # Create a plugin
osaurus tools dev com.acme.my-plugin     # Dev with hot reload
```

20+ native plugins: Mail, Calendar, Vision, XLSX, PPTX, Music, Git, Filesystem, Fetch, and more. (Web search, browsing, and macOS control are core Osaurus capabilities now — no plugin needed.) Plugins target the v3 host API surface — register HTTP routes, serve web apps, persist data in SQLite, dispatch agent tasks, and call inference through any model. Older v1/v2 plugins continue to load unchanged. See the [Plugin Authoring Guide](docs/plugins/README.md).

Document attachments keep structure where the file format exposes it: CSV/TSV tables, XLSX workbooks, PPTX decks, PDF page anchors, and rich document sections are parsed through the document adapter registry before they reach the agent.

## More

**Skills & Methods** -- Skills import reusable AI capabilities from GitHub repos or files, compatible with [Agent Skills](https://agentskills.io/). Full Claude plugins (skills, scheduled agents, slash commands, MCP providers, and `CLAUDE.md` context) can be imported from any GitHub repo and managed as a single bundle. Methods are learned workflows that agents save and reuse over time. All are automatically selected via RAG search -- no manual configuration needed. See [Skills Guide](docs/SKILLS.md) and [Claude Plugins](docs/CLAUDE_PLUGINS.md).

**Automation** -- Schedules run recurring tasks in the background. Watchers monitor folders and trigger agents on file changes.

**Voice** -- On-device transcription via FluidAudio on Apple's Neural Engine. Voice input in chat, VAD mode with wake-word activation, and a global hotkey to transcribe into any app. No audio leaves your Mac. See [Voice Input Guide](docs/VOICE_INPUT.md).

**Shortcuts, Spotlight & Siri** -- Osaurus ships App Intents, so "Ask Osaurus" and "Run Osaurus Agent" are available system-wide the moment you install -- no setup. Ask your active agent and get the reply inline, or kick off a custom agent in the background. See [App Intents Guide](docs/APP_INTENTS.md).

**Developer Tools** -- Server explorer, MCP tool inspector, inference monitoring, plugin debugging. See [Developer Tools Guide](docs/DEVELOPER_TOOLS.md). For the inference scheduler, model leases, continuous-batching engine, and feature flags that tune them, see [Inference Runtime](docs/INFERENCE_RUNTIME.md).

## Telemetry

Osaurus collects **anonymous, aggregated usage analytics** via [Aptabase](https://aptabase.com), an [open-source](https://github.com/aptabase/aptabase), privacy-first analytics project. We collect this only to understand broad user trends and preferences (how the app is used and where people run into friction) so we can make it better. It **never** includes your chats, prompts, files, model outputs, or keys. There are no accounts or device profiles, so events aren't tied to you.

For the exact, exhaustive list of every event and property we capture — and an explicit list of what we never collect — see [Telemetry & KPIs](docs/TELEMETRY.md).

### Crash reporting

**Crash and app-hang reporting** via [Sentry](https://sentry.io) is a **separate, independent** switch from usage analytics. Unlike analytics it's **opt-out** — on by default and active from launch — because crash reports carry no personal information and are what let us fix real bugs; you can turn it off anytime in **Settings → Privacy → Send Crash Reports**. It's limited to crash and hang diagnostics — no performance tracing, profiling, failed-request capture, network breadcrumbs, screenshots, or personal information; we drop the user object and device hostname from every event, on top of disabling PII. It needs a DSN to be configured, so like analytics it's off by default in source builds.

### Local development

Telemetry is **off by default in source builds**: with no key, the S
