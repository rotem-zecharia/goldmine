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

## features

> **In April 2026, Anthropic released Claude Design — the first time an LLM stopped writing prose and started delivering design artifacts directly.** It went viral. But it stayed closed-source, paid-only, cloud-only, locked to Anthropic's model, Anthropic's skills, Anthropic's surface. No checkout, no self-host, no Vercel deploy, no swap-in-your-own-agent.

OpenDesign (OD) is the open-source alternative. Same loop, same artifact-first mental model, none of the lock-in:

- 🤖 **Agent-native, model-agnostic.** We don't ship an agent. The `claude` / `codex` / `cursor-agent` / `copilot` / `hermes` / `kimi` already on your `PATH` are the design engine. Swap with one click.
- 🧠 **Brand-grade by default.** Every render reads the active package's `DESIGN.md` as the core brand contract. 151 design-system packages ship with the repo; legacy packages may be `DESIGN.md`-only, while newer packages can add `manifest.json`, `tokens.css`, components, assets, and provenance. Drop a folder in, the picker finds it.
- 🖥️ **Local-first, BYOK at every layer.** Native desktop apps for macOS (Apple Silicon + Intel) and Windows (x64). Linux AppImage on the optional release lane. Product analytics and session replay are consent-gated; scrubbed safety and reliability telemetry is always on. Before describing daemon data paths, contributors and operators MUST read `AGENTS.md` → **Daemon data directory contract**. This README MUST NOT restate it.
- 🌍 **Composable on four planes.** **Plugins** carry runnable workflows · functional **skills** carry agent behavior · **design templates** carry rendering blueprints · **design systems** carry the brand. All four use portable, versionable directories that anyone can author and publish.
- 🔁 **Refresh an existing codebase.** Hand a `git` repo + `DESIGN.md` to the agent and it refactors your real components to the brand spec. Dedicated plugins migrate Figma / Pencil workflows into React / Next.js / Vue code.
- 🔒 **Privacy by conviction.** Everything runs where your data lives — your laptop, your team's server, your Vercel project. When the network is needed, the BYOK proxy is SSRF-guarded.

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
