# screenpipe/screenpipe

YC (S26) / Open Computer History / Continuously record your company computer work, map your workflows, help you find work worth automating, and power your agents' context

## installation

[Download the desktop app](https://screenpipe.com/how-to-install?download=1) for macOS, Windows, or Linux. Available features depend on your [plan](https://screenpipe.com/pricing).

or run the CLI:

```
npx screenpipe record
```

then 

```bash
npx screenpipe setup
# or
claude mcp add screenpipe -- npx -y screenpipe-mcp@latest
```

then ask claude `what did i see in the last 5 mins?` or `summarize today conversations` or `create a pipe that updates linear every time i work on task X`

<details>
<summary>🤖 CLI-only setup for coding agents</summary>

If Claude Code, Codex, Gemini CLI, Cursor, or another coding agent is working from this repository, give it this instruction:

> Read the [screenpipe CLI skill](crates/screenpipe-core/assets/skills/screenpipe-cli/SKILL.md) before operating screenpipe. Set up always-on local capture, verify capture freshness and storage, then query my history without relying on the desktop app.

To install the screenpipe skills and MCP configuration into every supported agent detected on your computer, run:

```bash
npx screenpipe setup
```

The skill covers the recorder-first service default, explicit API-only server mode, human and JSON status, local search, safe read-only SQLite access, pipes, and connections.

</details>


## specs

- captures full accessibility tree, OCR as fallback, transcription, speakers, keyboard inputs, app switches
- CPU: approximately 5-20%; varies with hardware, capture settings, transcription, and AI workloads
- RAM: approximately 0.5-3 GB for capture; local models and additional workloads can use more
- Storage: varies with activity, displays, audio, capture settings, and retention. Measure a representative day on your device before sizing storage.
- filters (window, app, chrome extensions, passwords, proprietary AI PII model)
- optional encryption at rest
- Local capture and search work offline after setup. Cloud AI, sync, and connected services require network access.

---

<p align="center">
    <a href="https://docs.screenpi.pe">docs</a> ·
    <a href="https://screenpi.pe/team">enterprise</a> ·
    <a href="https://discord.gg/screenpipe">discord</a> ·
    <a href="https://twitter.com/screenpipe">x</a> ·
    <a href="https://www.youtube.com/@screen_pipe">youtube</a> ·
    <a href="https://www.reddit.com/r/screen_pipe">reddit</a>
</p>

## Repository guide

Start with [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and contribution
requirements. Agents should also read [AGENTS.md](AGENTS.md); [CLAUDE.md](CLAUDE.md)
points to the same instructions.

| Directory | Contents |
| --- | --- |
| `apps/` | Desktop app and the Workflows web host |
| `crates/` | Rust capture, storage, engine, and service crates |
| `packages/` | SDK, CLI distribution, MCP server, browser extension, and shared UI |
| `docs/` | Contributor guides, product/design guidance, testing, and architecture specs |
| `evals/` | Coding-agent regression evaluations |
| `infra/` | Build runners and deployment infrastructure |
| `scripts/` | Repository development and maintenance tools |

### Documentation for humans and agents

- [Onboarding](docs/ONBOARDING.md): walkthrough from setup to a first contribution.
- [Vision](docs/VISION.md): product priorities and scope.
- [Design](docs/DESIGN.md): interface principles and visual conventions.
- [Testing](docs/TESTING.md): regression checklists and validation guidance.
- [Coverage](docs/COVERAGE.md): generated E2E and core engine coverage summary.
- [Native builds](docs/macos-dev-builds.md): supported build and test commands.
- [App publication](docs/human-only-app-publication.md): release and publication boundaries.

The root [package.json](package.json) exposes `@screenpipe/workflows-ui` for projects
that install this repository as a Git dependency. It forwards exports to
[`packages/workflows-ui`](packages/workflows-ui), where the implementation lives;
it is not a root JavaScript workspace or app. In-repo apps depend on that package
directly. Keep the t

## features

### Event-driven screen capture
Instead of recording every second, screenpipe listens for meaningful events — app switches, clicks, typing pauses, scrolling — and captures a screenshot only when something actually changes. Each capture pairs a screenshot with the accessibility tree (the structured text the OS already knows about: buttons, labels, text fields). If accessibility data isn't available (e.g. remote desktops, games), it falls back to OCR. This gives you maximum data quality with minimal CPU and storage — no more processing thousands of identical frames.

### Audio transcription
Captures system audio (what you hear) and microphone input (what you say). Real-time speech-to-text using Whisper (Large-V3-Turbo) running locally on your device, or Deepgram for cloud transcription. Speaker identification and diarization. Works with any audio source — Zoom, Google Meet, Teams, or any other application.

On macOS 14.4+, you can exclude specific apps from system-audio capture by listing their bundle IDs in `~/.screenpipe/audio-exclusions.json`. Enable Experimental CoreAudio System Audio in Settings → Recording first; the picker UI only appears once that flag is on.

```json
{ "excluded_apps": [{ "bundle_id": "com.spotify.client", "name": "Spotify" }] }
```

The exclusion list hot-reloads — edits to the file and excluded apps launching/quitting are picked up on the engine's existing 500 ms tap-rebuild loop without restarting screenpipe. Override the file path with `SCREENPIPE_AUDIO_EXCLUSIONS_PATH` for testing. Note: this requires the "System Audio Recording Only" TCC permission in System Settings → Privacy & Security → Screen & System Audio Recording.

### AI-powered search
Natural language search across accessibility-first screen text, OCR fallback text, and audio transcriptions. Filter by application name, window title, browser URL, date range. Full-text keyword search (SQLite FTS5) under the hood. Returns screenshots and audio clips alongside text results.

### Timeline view
Visual timeline of your entire screen history. Scroll through your day like a DVR. Click any moment to see the full screenshot and extracted text. Play back audio from any time period.

### Plugin system (Pipes)
Pipes are scheduled AI agents defined as markdown files. Each pipe is a `pipe.md` with a prompt and schedule — screenpipe runs an AI coding agent (like pi or claude-code) that queries your screen data, calls APIs, writes files, and takes actions. Built-in pipes include:
- **meeting-summary**: Summarizes the meeting that just ended and patches the note back onto the meeting record
- **day-recap**: Today's accomplishments, key moments, and unfinished work
- **standup-update**: What you did, what's next, and any blockers
- **time-breakdown**: Where your time went, by app, project, and category
- **ai-prompt-journal**: Captures every prompt you send to AI tools, saved to Obsidian or local markdown
- **video-export**: Create a video of your recent screen activity

Developers can create pipes by writing a markdown file in `~/.screenpipe/pipes/`.

#### Pipe data permissions
Each pipe supports YAML frontmatter fields that give admins deterministic, OS-level control over what data AI agents can access:
- **App & window filtering**: `allow-apps`, `deny-apps`, `deny-windows` (glob patterns)
- **Content type control**: restrict to `ocr`, `audio`, `input`, or `accessibility`
- **Time & day restrictions**: e.g. `time-range: 09:00-18:00`, `days: Mon,Tue,Wed,Thu,Fri`
- **Endpoint gating**: `allow-raw-sql: false`, `allow-frames: false`

Enforced at three layers — skill gating (AI never learns denied endpoints), agent interception (blocked before execution), and server middleware (per-pipe cryptographic tokens). Not prompt-based. Deterministic.

### MCP server (Model Context Protocol)
screenpipe runs as an MCP server, allowing AI assistants to query your screen history:
- Works with Claude Desktop, Cursor, VS Code (Cline, Continue), and any MCP-compatible client


## tools

Full REST API running on localhost (default port 3030). Endpoints for searching screen content, audio, frames. Raw SQL access to the underlying SQLite database. JavaScript/TypeScript SDK available.

## Privacy and security

- **Local capture storage**: Screen frames, audio, transcripts, and the search index are stored on your device by default. Cloud AI, transcription, sync, integrations, exports, and enterprise storage can send data off-device. See the [cloud and telemetry FAQ](#does-screenpipe-send-my-data-to-the-cloud).
- **Source-available**: fully auditable codebase; personal, non-commercial use permitted.
- **Local AI support**: Use a supported local model such as Ollama for inference on your device. Configure transcription, sync, integrations, and telemetry separately to control other network traffic.
- **No account required**: Core application works without any sign-up.
- **You own your data**: Export, delete, or back up at any time.
- **Optional encrypted sync**: End-to-end encrypted sync between devices (zero-knowledge encryption).
- **AI data permissions**: Per-pipe YAML-based access control — deterministic enforcement at the OS level, not prompt-based. Three enforcement layers prevent AI agents from accessing unauthorized data.

## How screenpipe compares to alternatives

| Feature | screenpipe | Rewind / Limitless | Microsoft Recall | Granola |
|---------|-----------|-------------------|-----------------|---------|
| Source-available | ✅ fully auditable | ❌ | ❌ | ❌ |
| Platforms | macOS, Windows, Linux | macOS, Windows | Windows only | macOS only |
| Data storage | Local by default; optional cloud and team storage | Cloud required | Local (Windows) | Cloud |
| Multi-monitor | ✅ All monitors | ❌ Active window only | ✅ | ❌ Meetings only |
| Audio transcription | ✅ Local Whisper | ✅ | ❌ | ✅ Cloud |
| Developer API | ✅ Full REST API + SDK | Limited | ❌ | ❌ |
| Plugin system | ✅ Pipes (AI agents) | ❌ | ❌ | ❌ |
| AI model choice | Any (local or cloud) | Proprietary | Microsoft AI | Proprietary |
| Team deployment | ✅ Central config, AI permissions | ❌ | ❌ | ❌ |
| Pricing | Free and paid plans; custom Enterprise pricing | Subscription | Bundled with Windows | Subscription |

## Pricing

The desktop app has **Free**, **Basic**, and **Business** plans. Use the [current pricing page](https://screenpipe.com/pricing) for rates, monthly versus annual billing, capacity options, and included features.

Business includes personal device sync and team seat management; shared context across teammates is not currently included. **Enterprise pricing is scoped per deployment**, including seats, duration, storage, support, and implementation work. Request a [deployment proposal](https://screenpipe.com/enterprise) for the total cost and included services.

Source builds are governed by [LICENSE.md](LICENSE.md), which permits personal, non-commercial use, nonprofit/educational/research use, and a limited organizational evaluation. Commercial use requires a commercial license. Official builds have separate terms under the [Terms of Service](https://screenpipe.com/terms) and the applicable subscription or app license.

Existing lifetime licenses remain valid; new lifetime purchases are no longer sold.

## Integrations

- **AI coding assistants**: Cursor, Claude Code, Cline, Continue, OpenCode, Gemini CLI
- **AI chat assistants**: ChatGPT (via MCP), Claude Desktop (via MCP), any MCP-compatible client
- **Note-taking**: Obsidian, Notion
- **Local AI**: Ollama, any OpenAI-compatible model server
- **Automation**: Custom pipes (scheduled AI agents as markdown files)

## Teams & enterprise

screenpipe Teams lets organizations deploy AI agents across their team with full control over what AI can access. See [screenpi.pe/team](https://screenpi.pe/team).

- **Central config management**: Push capture settings (app filters, schedules, URL rules) to every device from an admin dashboard.
- **Shared pipes**: Deploy AI workflows (auto-standups, meeting
