# nexu-io/open-design

🎨 Best DeepSeek Harness Design Plugin. The open-source Claude Design alternative. 🖥️ Local-first desktop app. 🖼️ Your coding agent becomes the design engine: prototypes, landing pages, dashboards, sli

## tools

<table>
<tr>
<td width="20%" valign="top"><img src="https://cms-assets.youmind.com/media/1776662673014_nf0taw_HGRMNDybsAAGG88.jpg" alt="Illustrated city food map" /><br/><sub><b>Illustrated city food map</b><br/>Hand-drawn editorial travel poster</sub></td>
<td width="20%" valign="top"><img src="https://cms-assets.youmind.com/media/1777453149026_gd2k50_HHCSvymboAAVscc.jpg" alt="Cinematic elevator scene" /><br/><sub><b>Cinematic elevator scene</b><br/>Single-frame editorial still</sub></td>
<td width="20%" valign="top"><img src="https://cms-assets.youmind.com/media/1777453164993_mt5b69_HHDoWfeaUAEA6Vt.jpg" alt="Cyberpunk anime portrait" /><br/><sub><b>Cyberpunk portrait</b><br/>Profile avatar — neon face text</sub></td>
<td width="20%" valign="top"><img src="https://cms-assets.youmind.com/media/1776661968404_8a5flm_HGQc_KOaMAA2vt0.jpg" alt="3D stone staircase evolution" /><br/><sub><b>3D stone staircase</b><br/>Hewn-stone infographic</sub></td>
<td width="20%" valign="top"><img src="https://cms-assets.youmind.com/media/1777453184257_vb9hvl_HG9tAkOa4AAuRrn.jpg" alt="Glamorous portrait" /><br/><sub><b>Glamorous portrait</b><br/>Editorial studio shot</sub></td>
</tr>
</table>

**93 ready-to-replicate prompts** live in [`prompt-templates/`](prompt-templates/) — preview thumbnails, full prompt body, target model, aspect ratio, and source attribution. One click drops a brief into the composer.

### 5 · Video & HyperFrames — agent-native motion graphics

**[HyperFrames][hyperframes]** is HeyGen's open-source, agent-native video framework, integrated as a first-class citizen in OpenDesign. The agent writes HTML + CSS + GSAP, and HyperFrames renders it to a deterministic MP4 via headless Chrome + FFmpeg. Pair it with **Seedance 2.0** for cinematic t2v / i2v, **Veo 3 / Sora 2 / Kling 2** for routed model variants, and **Suno v5 / Lyria 2** for the audio layer.

<table>
<tr>
<td width="25%" valign="top"><a href="prompt-templates/video/hyperframes-saas-product-promo-30s.json"><img src="https://static.heygen.ai/hyperframes-oss/docs/images/catalog/blocks/app-showcase.png" alt="SaaS promo" /></a><br/><sub><b>30s SaaS product promo</b> · 16:9 · UI 3D reveals</sub></td>
<td width="25%" valign="top"><a href="prompt-templates/video/hyperframes-tiktok-karaoke-talking-head.json"><img src="https://static.heygen.ai/hyperframes-oss/docs/images/catalog/blocks/tiktok-follow.png" alt="TikTok karaoke" /></a><br/><sub><b>TikTok karaoke talking-head</b> · 9:16 · TTS + word-synced captions</sub></td>
<td width="25%" valign="top"><a href="prompt-templates/video/hyperframes-brand-sizzle-reel.json"><img src="https://static.heygen.ai/hyperframes-oss/docs/images/catalog/blocks/logo-outro.png" alt="Brand sizzle reel" /></a><br/><sub><b>30s brand sizzle reel</b> · 16:9 · audio-reactive kinetic type</sub></td>
<td width="25%" valign="top"><a href="prompt-templates/video/hyperframes-data-bar-chart-race.json"><img src="https://static.heygen.ai/hyperframes-oss/docs/images/catalog/blocks/data-chart.png" alt="Bar chart race" /></a><br/><sub><b>Bar chart race</b> · 16:9 · NYT-style data infographic</sub></td>
</tr>
<tr>
<td width="25%" valign="top"><a href="prompt-templates/video/hyperframes-flight-map-route.json"><img src="https://static.heygen.ai/hyperframes-oss/docs/images/catalog/blocks/nyc-paris-flight.png" alt="Flight map" /></a><br/><sub><b>Flight map</b> · 16:9 · Apple-style route reveal</sub></td>
<td width="25%" valign="top"><a href="prompt-templates/video/hyperframes-logo-outro-cinematic.json"><img src="https://static.heygen.ai/hyperframes-oss/docs/images/catalog/blocks/logo-outro.png" alt="Logo outro" /></a><br/><sub><b>4s cinematic logo outro</b> · 16:9 · piece-by-piece assembly + bloom</sub></td>
<td width="25%" valign="top"><a href="prompt-templates/video/hyperframes-money-counter-hype.json"><img src="https://static.heygen.ai/hyperframes-oss/docs/images/catalog/blocks/apple-money-count.png" alt="Money counter" /></a><br/><sub><b>$0 → $10K money counter</b> 

## features

> **In April 2026, Anthropic released Claude Design — the first time an LLM stopped writing prose and started delivering design artifacts directly.** It went viral. But it stayed closed-source, paid-only, cloud-only, locked to Anthropic's model, Anthropic's skills, Anthropic's surface. No checkout, no self-host, no Vercel deploy, no swap-in-your-own-agent.

OpenDesign (OD) is the open-source alternative. Same loop, same artifact-first mental model, none of the lock-in:

- 🤖 **Agent-native, model-agnostic.** We don't ship an agent. The `claude` / `codex` / `cursor-agent` / `copilot` / `hermes` / `kimi` already on your `PATH` are the design engine. Swap with one click.
- 🧠 **Brand-grade by default.** Every render reads the active package's `DESIGN.md` as the core brand contract. 151 design-system packages ship with the repo; legacy packages may be `DESIGN.md`-only, while newer packages can add `manifest.json`, `tokens.css`, components, assets, and provenance. Drop a folder in, the picker finds it.
- 🖥️ **Local-first, BYOK at every layer.** Native desktop apps for macOS (Apple Silicon + Intel) and Windows (x64). Linux AppImage on the optional release lane. Product analytics and session replay are consent-gated; scrubbed safety and reliability telemetry is always on. Before describing daemon data paths, contributors and operators MUST read `AGENTS.md` → **Daemon data directory contract**. This README MUST NOT restate it.
- 🌍 **Composable on four planes.** **Plugins** carry runnable workflows · functional **skills** carry agent behavior · **design templates** carry rendering blueprints · **design systems** carry the brand. All four use portable, versionable directories that anyone can author and publish.
- 🔁 **Refresh an existing codebase.** Hand a `git` repo + `DESIGN.md` to the agent and it refactors your real components to the brand spec. Dedicated plugins migrate Figma / Pencil workflows into React / Next.js / Vue code.
- 🔒 **Privacy by conviction.** Everything runs where your data lives — your laptop, your team's server, your Vercel project. When the network is needed, the BYOK proxy is SSRF-guarded.

### Comparison

| | Claude Design | Figma | Lovable / v0 / Bolt | **OpenDesign** |
|---|---|---|---|---|
| Open source | ❌ | ❌ | ❌ | **✅ Apache-2.0** |
| Self-host / desktop | ❌ | ❌ | ❌ | **✅ macOS + Windows + Docker + Vercel web** |
| Agent-native (runs in your CLI) | Anthropic only | ❌ | Cloud agent only | **✅ 25 CLIs + BYOK** |
| Brand-grade `DESIGN.md` | Proprietary | Theme JSON | Limited tokens | **✅ 151 systems shipped** |
| Skills / plugins / templates | Closed | Plugin store | Closed | **✅ 100+ functional skills · rendering templates · 277 plugins** |
| HyperFrames (HTML→MP4) | ❌ | ❌ | ❌ | **✅ First-class** |
| Refresh an existing repo to brand | ❌ | ❌ | ❌ | **✅ via agent + `DESIGN.md`** |
| Minimum billing | Pro / Max / Team | Pro / Org | Pro / Team | **BYOK · any compatible endpoint** |

---

## configuration

The fastest way to use OpenDesign. No Node, no pnpm, no clone.

- **macOS** (Apple Silicon · Intel x64) → [**open-design.ai**](https://open-design.ai/?utm_source=github&utm_medium=referral&utm_content=readme_download_macos) or [GitHub Releases](https://github.com/nexu-io/open-design/releases)
- **Windows** (x64) → [**open-design.ai**](https://open-design.ai/?utm_source=github&utm_medium=referral&utm_content=readme_download_windows) or [GitHub Releases](https://github.com/nexu-io/open-design/releases)
- **Linux** (AppImage, optional lane) → [GitHub Releases](https://github.com/nexu-io/open-design/releases)

After install: the app auto-detects every coding-agent CLI on your `PATH`, loads 100+ functional skills, the separate rendering-template catalog, and 151 design systems, and lets you type a brief in the entry view.

## installation

You can use OpenDesign without ever opening the GUI — call it as a skill, plugin, or MCP server inside Claude Code, Codex, Cursor, Copilot, OpenClaw, Antigravity, Hermes, Kimi, and more.

If you installed the macOS desktop app via the DMG or Homebrew cask, your shell
may still resolve `od` to Apple's built-in `/usr/bin/od` octal-dump utility. In
that case, open **Settings → MCP server** in the desktop app and copy the
client-specific snippet; it uses absolute paths and does not rely on the bare
`od` command.

```bash
# One-line install into the agent you're using:
od mcp install <agent>
# <agent> = claude | codex | reasonix | raven | cursor | copilot | openclaw
#         | antigravity | pi | vibe | hermes | cline | kimi | kiro
#         | trae | opencode

# Hosted equivalent for curl-based setup:
curl -fsSL https://open-design.ai/install.sh | sh -s <agent>
```

`install.sh` is a thin shell wrapper around `od mcp install`; it exists so the
hosted URL returns shell instead of the landing-page HTML fallback and fails
fast if your shell resolves a non-Open-Design `od` binary.

> **macOS / WSL2 users:** `/usr/bin/od` is a system octal-dump command and can
> shadow OpenDesign's `od` command. Desktop-app users should prefer the
> **Settings → MCP server** snippet; WSL2 users should follow the
> [`WSL2 setup guide`](docs/wsl-setup.md) first.

Then, inside the agent:

```
> Use open-design to generate a landing page with the Linear design system
```

In a filesystem-backed local CLI run, the agent composes the selected functional skill or design template with your `DESIGN.md`, writes the canonical project files, and OpenDesign previews those files. A BYOK/plain-API run without filesystem tools instead returns one complete `<artifact>` block.

### 🐳 Run with Docker

```bash
git clone https://github.com/nexu-io/open-design.git
cd open-design/deploy
cp .env.example .env
echo "OD_API_TOKEN=$(openssl rand -hex 32)" >> .env
docker compose up -d
# open http://127.0.0.1:7456
```

If the browser asks for credentials, use `open-design` as the username and the
`OD_API_TOKEN` value from `deploy/.env` as the password. This keeps Docker bridge
traffic authenticated without requiring host networking. API clients can keep
using `Authorization: Bearer <OD_API_TOKEN>`.

### 🚀 Deploy on Sealos

[![Deploy on Sealos](https://sealos.io/Deploy-on-Sealos.svg)](https://sealos.io/products/app-store/open-design/)

The Sealos App Store template runs the published OpenDesign Docker image with persistent workspace storage and Basic Auth on the public proxy. For custom public or shared Docker deployments, follow the reverse-proxy and `OPEN_DESIGN_ALLOWED_ORIGINS` guidance in [`deploy/README.md`](deploy/README.md#local-compose).

### 🧑‍💻 Run from source

```bash
git clone https://github.com/nexu-io/open-design.git
cd open-design
corepack enable && pnpm install
pnpm tools-dev run web
```

Open the URL printed by `tools-dev`; development ports are allocated dynamically unless you pass explicit port flags.

Node `~24`, pnpm `10.33.x`. WSL2 users, see [`docs/wsl-setup.md`](docs/wsl-setup.md); native Windows users, see [`docs/windows-troubleshooting.md`](docs/windows-troubleshooting.md). Full quickstart, env vars, and packaged build flow → [`QUICKSTART.md`](QUICKSTART.md).

### A full workflow — from brief to artifact

`brief → plugin → direction → design system → artifact → handoff → memory`

1. **A PM submits a brief.** The plugin picker offers landing page · pitch deck · dashboard · social post · PM spec · OKR scorecard…
2. **A designer (or the agent) locks the direction.** No brand? Pick from 5 curated directions. Have a brand? Drop a screenshot / URL → the agent connects GitHub, imports Figma, and codifies a reusable `DESIGN.md`.
3. **The agent creates the first deliverable.** Plugin + functional skill or design template + `DESIGN.md` are bound. Filesystem-backed CLI runs write canonical project files and the preview follows them; BYOK/plain-API runs without file too

## limitations

- [x] Daemon + 27 runtime definitions across 26 distinct coding-agent CLI executables + skill/design-template registries + design-system catalog
- [x] Web app + chat + question form + 5-direction picker + todo progress + sandboxed preview
- [x] 100+ functional skills · separate rendering-template catalog · 151 design-system packages · 5 visual directions · 5 device frames
- [x] SQLite-backed projects · conversations · messages · tabs · templates
- [x] Multi-provider BYOK proxy (`/api/proxy/{anthropic,openai,azure,google,ollama,senseaudio}/stream`) with OpenAI-compatible presets including Atlas Cloud + SSRF guard
- [x] Claude Design ZIP import (`/api/import/claude-design`)
- [x] Sidecar protocol + Electron desktop + IPC automation
- [x] Artifact lint API + 5-dim self-critique pre-emit gate
- [x] **0.8.0** — plugin marketplace infrastructure (261 official plugins, manifest spec, per-agent install scripts)
- [x] **0.9.0** — OpenDesign Cloud (official model service built into the app: zero config, one-click sign-in)
- [x] **0.10.0** — the all-in-one design workspace: the whole craft loop in one window (references → material → interactive editing → motion → handoff)
- [x] **0.11.0** — _The Bazaar_: built in the open — a community marketplace of plugins and design systems anyone can pick from and contribute to
- [x] **0.12.0** — _Brand-backed Design System_: turn the brand you already own into a reusable, portable `DESIGN.md` system
- [x] **0.13.0** — _Stay in Flow_: native session resume, faster model picking, and export straight to screenshot-backed PPTX / PDF
- [x] Packaged Electron builds — macOS (Apple Silicon + Intel) + Windows (x64) + Linux AppImage (optional lane)
- [ ] Comment-mode surgical edits — partially shipped; reliable targeted patching in progress
- [ ] AI-emitted tweaks panel UX — not yet implemented
- [ ] `npx od init` to scaffold a project with `DESIGN.md`
- [ ] Plugin SDK + `od plugin {add,list,remove,test,publish}` CLI
- [ ] Figma / Pencil → React / Next / Vue migration plugins (alpha)
- [ ] Refresh-existing-codebase plugin (point at a git repo + `DESIGN.md`)

Phased delivery → [`docs/roadmap.md`](docs/roadmap.md).

---

## Community

Real people behind every channel.

- 💬 **Discord** — daily chat, plugin sharing, questions → [**discord.gg/mHAjSMV6gz**](https://discord.gg/mHAjSMV6gz)
- 🐦 **X / Twitter** — release notes, milestones, behind the scenes → [**@OpenDesignHQ**](https://x.com/OpenDesignHQ)
- 🗣️ **GitHub Discussions** — deep Q&A, RFCs, "show your work" → [**Discussions**](https://github.com/nexu-io/open-design/discussions)
- 🐛 **GitHub Issues** — bug reports, feature requests → [**Issues**](https://github.com/nexu-io/open-design/issues)

The [`good-first-issue`](https://github.com/nexu-io/open-design/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) and [`help-wanted`](https://github.com/nexu-io/open-design/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) labels are the easiest way in.

---

## Contributing

OpenDesign keeps moving because contributors — designers, engineers, prompt authors — keep showing up. Many of the most-used skills, design systems, and plugins were written by people outside the core team.

### 🎯 Where to start (max leverage, min change)

| Want to ship… | How | Where |
|---|---|---|
| A new functional **skill** | Drop a folder with `SKILL.md` + optional `assets/` + `references/` | [`skills/`](skills/) · spec in [`docs/skills-protocol.md`](docs/skills-protocol.md) |
| A new rendering **design template** | Add a renderable `SKILL.md` bundle | [`design-templates/`](design-templates/) |
| A new **design system** | Drop a package centered on `DESIGN.md`; add `manifest.json`, `tokens.css`, components, assets, or provenance when needed | [`design-systems/<brand>/`](design-systems/) |
| A new **plugin** | Drop `open-design.json` + the type-specific payload under a category folder | [`plugins/community/`](plugins/community/) · spec in [`plugins/spec/SPEC.md`](plugins/sp
