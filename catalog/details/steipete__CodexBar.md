# steipete/CodexBar

Show usage stats for OpenAI Codex and Claude Code, without having to login.

## requirements

- macOS 14+ (Sonoma)

### GitHub Releases
Download: <https://github.com/steipete/CodexBar/releases>

### Homebrew
```bash
brew install --cask codexbar
```

### CLI Tarballs (macOS/Linux)
Homebrew formula (Linux today):
```bash
brew install steipete/tap/codexbar
```
Arch Linux AUR package:
```bash
yay -S codexbar-cli
```
Or download release tarballs from GitHub Releases:
- macOS: `CodexBarCLI-v<tag>-macos-arm64.tar.gz`, `CodexBarCLI-v<tag>-macos-x86_64.tar.gz`
- Linux (glibc): `CodexBarCLI-v<tag>-linux-aarch64.tar.gz`, `CodexBarCLI-v<tag>-linux-x86_64.tar.gz`
- Linux (static musl): `CodexBarCLI-v<tag>-linux-musl-aarch64.tar.gz`, `CodexBarCLI-v<tag>-linux-musl-x86_64.tar.gz`

### First run
- Open Settings → Providers and enable what you use.
- Install/sign in to the provider sources you rely on: CLIs, browser sessions, OAuth/device flow, API keys, local app files, or provider apps depending on the provider.
- Optional: Settings → Providers → Codex → OpenAI cookies (Automatic or Manual) to add dashboard extras.

## tools

Provider toggles and API keys live in the resolved CodexBar config file. New installs use
`~/.config/codexbar/config.json`; existing `~/.codexbar/config.json` installs still load from the legacy path. You can
script the same provider list that Settings → Providers uses:

```bash
codexbar config providers
codexbar config enable --provider grok
codexbar config disable --provider cursor
```

For API-key providers, store a key without opening Settings:

```bash
printf '%s' "$ELEVENLABS_API_KEY" | codexbar config set-api-key --provider elevenlabs --stdin
```

`set-api-key` trims the piped value, stores it with restrictive config-file permissions, and enables the provider by default. Use `--no-enable` to only save the key, or `--api-key <key>` for one-off local scripts where shell history is not a concern.
See [CLI configuration](docs/cli-configuration.md) for the full flow.

## Providers

- [Codex](docs/codex.md) — OAuth API or local Codex CLI, plus optional OpenAI web dashboard extras.
- [OpenAI](docs/openai.md) — Admin API key usage/cost graphs with legacy credit-balance fallback.
- [Azure OpenAI](docs/azure-openai.md) — API key, endpoint, and deployment validation probe.
- [Claude](docs/claude.md) — OAuth API, browser cookies, or CLI PTY fallback; session and weekly usage where available.
- [Cursor](docs/cursor.md) — Browser session cookies for plan + usage + billing resets.
- [OpenCode](docs/opencode.md) — Browser cookies for workspace subscription usage.
- [OpenCode Go](docs/opencode.md) — Usage API, browser fallback, and local SQLite cost history.
- [Alibaba Coding Plan](docs/alibaba-coding-plan.md) — Web cookies or API key for coding-plan quotas.
- [Alibaba Token Plan](docs/alibaba-token-plan.md) — Bailian browser/manual cookies for token-plan credits.
- [Qwen Cloud](docs/qwen-cloud.md) — 5-hour and weekly individual Token Plan usage via browser/manual cookies.
- [Gemini](docs/gemini.md) — OAuth-backed quota API using Gemini CLI credentials (no browser cookies).
- [Antigravity](docs/antigravity.md) — Local language server probe, `agy` CLI HTTPS source, and Google OAuth fallback (experimental).
- [Droid](docs/factory.md) — Browser cookies + WorkOS token flows for Factory usage + billing.
- [Copilot](docs/copilot.md) — GitHub device flow + Copilot internal usage API.
- [Devin](docs/devin.md) — Chrome localStorage session or manual Bearer token for daily and weekly quotas.
- [z.ai](docs/zai.md) — API token for personal/team quota, MCP, 5-hour, and hourly usage windows.
- [Manus](docs/manus.md) — Browser `session_id` auth for credit balance, monthly credits, and daily refresh tracking.
- [MiniMax](docs/minimax.md) — API token, cookie header, or browser cookies for coding-plan usage.
- [T3 Chat](docs/t3chat.md) — Browser cookies capture for Base and Overage usage buckets.
- [ZoomMate](docs/zoommate.md) — Chrome cookie auto-import or manual cURL capture for credits usage.
- [Kimi](docs/kimi.md) — Auth token (JWT from `kimi-auth` cookie) for weekly quota + 5‑hour rate limit.
- [Kilo](docs/kilo.md) — API token with CLI-auth fallback for Kilo Pass usage.
- [Kiro](docs/kiro.md) — CLI-based usage; monthly credits + bonus credits.
- [Vertex AI](docs/vertexai.md) — Google Cloud gcloud OAuth with token cost tracking from local Claude logs.
- [Augment](docs/augment.md) — Augment CLI or browser cookies for credits tracking and usage monitoring.
- [Amp](docs/amp.md) — Browser cookie-based authentication with Amp Free usage tracking.
- [Ollama](docs/ollama.md) — API key access plus browser cookies for Ollama Cloud usage windows.
- [Synthetic](docs/synthetic.md) — API key quota endpoint for rolling five-hour, weekly token, and search-hourly usage.
- [JetBrains AI](docs/jetbrains.md) — Local XML-based quota from JetBrains IDE configuration; monthly credits tracking.
- [Warp](docs/warp.md) — API token for GraphQL request limits and monthly credits.
- [ElevenLabs](docs/elevenlabs.md) — API key for character credits and voice slot usage.
- [OpenRo

## features

- Multi-provider menu bar with per-provider toggles (Settings → Providers).
- Provider-specific usage meters with reset countdowns.
- Optional Codex web dashboard enrichments (code review remaining, usage breakdown, credits history).
- Inline spend and usage charts for API-backed providers such as OpenAI, Claude Admin API, OpenRouter, LiteLLM, z.ai, MiniMax, Mistral, and AWS Bedrock.
- Configurable cost-usage scans for Codex + Claude, plus reused chart UI for supported provider histories. Codex history uses a WAL-enabled SQLite store capped at 25,000 retained session entries and 256 MiB.
- A persistent Settings → Usage & Spend view for local 7/30-day estimates, grouped by native currency and limited to providers that expose cost history.
- Provider status polling with incident badges in the menu and icon overlay.
- Merge Icons mode to combine providers into one status item + switcher.
- Display controls for provider icons, labels, bars, reset-time style, and highest-usage auto-selection.
- Fresh installs default to Adaptive refresh. Existing users keep every valid stored choice, while legacy unset or
  invalid preferences resolve to 5 minutes. Manual and fixed 1m, 2m, 5m, 15m, and 30m alternatives remain available.
- Bundled CLI (`codexbar`) for scripts and CI (including `codexbar cost --provider codex`, `claude`, or `both` for local cost usage); macOS and Linux CLI builds available.
- WidgetKit widgets for supported providers.
- Localized app and website with a shared 21-language catalog, automatic website detection, persistent pickers, and RTL support.
- Optional session quota notifications and weekly-reset confetti.
- Privacy-first: on-device parsing by default; browser cookies are opt-in and reused (no passwords stored).

## Privacy note
Wondering if CodexBar scans your disk? It doesn’t crawl your filesystem; it reads a small set of known locations (browser cookies/local storage, provider config files, local JSONL logs) when the related features are enabled. Plain Adaptive refresh never inspects local agent activity. The separate Adaptive (agent-aware) option asks before inspecting the running-process list (including command lines) to identify Codex/Claude and reading bounded known-session metadata. Declining returns to plain Adaptive. When allowed with Agent Sessions hidden, CodexBar retains only the latest activity time and discards session paths and identities. Provider tokens and token-account settings live in the CodexBar config file with restrictive file permissions. See the discussion and audit notes in [issue #12](https://github.com/steipete/CodexBar/issues/12).

## macOS permissions (why they’re needed)
- **Full Disk Access (optional)**: only required to read Safari cookies/local storage for web-based providers. If you don’t grant it, use another supported browser, manual cookies/API keys, OAuth, or CLI/local sources where that provider supports them.
- **Keychain access (prompted by macOS)**:
  Chromium cookie import needs the browser’s Safe Storage item, and an explicitly enabled Claude OAuth repair may
  read Claude Code’s own Keychain item. Background CodexBar paths fail or skip instead of requesting authorization;
  a user-initiated import or repair can still show the macOS prompt. **Settings → Advanced → Disable Keychain
  access** blocks CodexBar-owned Keychain operations and browser decryption, but cannot constrain provider-owned CLIs
  that CodexBar launches. Manual cookie headers, API keys, and file-backed sources remain alternatives where
  supported. See [Keychain prompts](docs/keychain-prompts.md) for Allow Once vs. Always Allow, recurring grants, and
  safe troubleshooting.
- **Files & Folders prompts (folder/volume access)**: CodexBar launches provider CLIs and local probes for some providers. If those helpers read a project directory or external drive, macOS may ask CodexBar for that folder/volume (e.g., Desktop or an external volume). This is driven by the helper’s working directory, not backgroun

## installation

- Clone the repo and open it in Xcode or run the scripts directly.
- Launch once, then toggle providers in Settings → Providers.
- Install/sign in to provider sources you rely on (CLIs, browser cookies, OAuth/device flow, API keys, or local app/config files).
- Optional: set OpenAI cookies (Automatic or Manual) for Codex dashboard extras.

## Build from source
Requires macOS 14+ and Swift 6.2+.

```bash
./Scripts/package_app.sh        # builds CodexBar.app in-place with ad-hoc signing
open CodexBar.app
```

Dev loop:
```bash
./Scripts/compile_and_run.sh
./Scripts/compile_and_run.sh --test  # also run the sharded test suite before packaging/relaunching
make check                           # SwiftFormat + SwiftLint
make docs-list                       # list docs with frontmatter summaries
```

CLI install:
```bash
# after installing CodexBar.app in /Applications
./bin/install-codexbar-cli.sh
```

## Related
- ✂️ [Trimmy](https://github.com/steipete/Trimmy) — “Paste once, run once.” Flatten multi-line shell snippets so they paste and run.
- 🧳 [MCPorter](https://mcporter.dev) — TypeScript toolkit + CLI for Model Context Protocol servers.
- 🧿 [oracle](https://askoracle.dev) — Ask the oracle when you're stuck. Invoke GPT-5 Pro with a custom context and files.

## Looking for a Windows version?
- [Win-CodexBar](https://github.com/Finesssee/Win-CodexBar)

## Linux desktop integration?
- [codexbar-waybar](https://github.com/Marouan-chak/codexbar-waybar) — Waybar custom module + GTK4 popover for Hyprland / Sway / other Wayland compositors, built on top of the bundled Linux CLI.
- [codexbar-cosmic-applet](https://github.com/andrew-verde/codexbar-cosmic-applet) — Native COSMIC (System76) desktop panel applet with a tab per provider, pace projections, and cost/token stats, built on top of the bundled Linux CLI.
- [Codexbar GNOME](https://extensions.gnome.org/extension/9841/codexbar/) — GNOME Shell extension that brings CodexBar usage into the desktop panel.
- [codexbar-cinnamon-applet](https://github.com/jacobcalvert/codexbar-cinnamon-applet) — Linux Mint Cinnamon panel applet powered by CodexBar's JSON output.
- [noctalia-codex-usage](https://github.com/rayoplateado/noctalia-codex-usage) — Noctalia/Quickshell plugin that shows Codex 5-hour and weekly usage limits, built on top of the bundled Linux CLI.
- [KodexBar](https://github.com/tylxr59/KodexBar) — KDE Plasma widget that shows CodexBar usage in the Plasma panel, built on top of the bundled Linux CLI.
- [codexbar-plasmoid](https://github.com/psimaker/codexbar-plasmoid) — KDE Plasma 6 widget for CodexBar's meter icon, provider switcher, quota windows, pace, credits, local cost, and status, powered by the bundled Linux CLI.
- [CodexBar Plasma](https://github.com/Lucenx9/codexbar-plasma) — KDE Plasma 6 widget with multi-provider views, account selection, cost history, notifications, configurable providers, and installable `.plasmoid` releases, powered by the bundled Linux CLI.
- [CodexBar Meter](https://github.com/noctalia-dev/community-plugins/tree/main/codexbar-meter) — Noctalia v5 bar widget and panel showing every enabled provider's quota windows, credits, and pace, installable from Noctalia's plugin store, built on the bundled Linux CLI.

## Status bar & terminal integration
- [showy-quota](https://github.com/enieuwy/showy-quota) — always-on AI plan quota strips for SketchyBar, tmux, and Zellij (standalone WASM plugin), built on `codexbar serve` / the bundled CLI.
- [AI Usage Limits](https://github.com/lenadweb/stream-deck-ai-limits) — Elgato Stream Deck integration for macOS: shows a selected CodexBar provider, account, and configurable quota or payload metrics on keys and Stream Deck+ dials, using local `codexbar serve`.

## Credits
Inspired by [ccusage](https://github.com/ryoppippi/ccusage) (MIT), specifically the cost usage tracking.

## License
MIT • Peter Steinberger ([steipete](https://twitter.com/steipete))
