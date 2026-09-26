# farion1231/cc-switch

A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode, OpenClaw, Grok Build & Hermes Agent. Only official website: ccswitch.io

## features

AI coding tools like Claude Code, Codex, and Gemini CLI each have their own configuration format. Switching API providers means hand-editing JSON, TOML, YAML, or `.env` files, and MCP, Skills, and prompts have to be maintained separately in every tool.

**CC Switch** brings all of this into a single desktop app: pick a preset, enter your key, and switch in one click, without losing your existing configuration.

- **One App, Ten Tools** — Claude Code, Claude Desktop, Codex, Gemini CLI, Grok Build, OpenCode, OpenClaw, Hermes, Pi, and MiniMax Code
- **No More Manual Editing** — 90+ provider presets including AWS Bedrock, NVIDIA NIM, and community relays
- **Use GPT in Claude Code, Claude in Codex** — Built-in local routing automatically converts between Anthropic, OpenAI, and Gemini API formats, with automatic failover
- **Centralized MCP, Skills & Prompts** — Add MCP servers and Skills once, then choose which tools to sync them to; prompts are maintained separately for each tool
- **Usage & Quotas at a Glance** — Track token usage and spending even without local routing; subscription quotas and balances show right on provider cards and in the tray
- **Cross-Platform** — Native desktop app for Windows, macOS, and Linux, built with Tauri 2

## Screenshots

|                  Main Interface                   |                  Add Provider                  |
| :-----------------------------------------------: | :--------------------------------------------: |
| ![Main Interface](assets/screenshots/main-en.png) | ![Add Provider](assets/screenshots/add-en.png) |

## requirements

- **Windows**: Windows 10 and above
- **macOS**: macOS 12 (Monterey) and above
- **Linux**: x86_64 or ARM64 with glibc 2.35+ and WebKitGTK 4.1 — e.g. Ubuntu 22.04+, Debian 12+, and recent Fedora releases; RHEL / Rocky / Alma 8–9 are not supported yet

### Windows Users

Download the latest `CC-Switch-v{version}-Windows.msi` installer or `CC-Switch-v{version}-Windows-Portable.zip` portable version from the [Releases](../../releases) page. On Windows on ARM, download `CC-Switch-v{version}-Windows-arm64.msi` or `CC-Switch-v{version}-Windows-arm64-Portable.zip`.

### macOS Users

**Method 1: Install via Homebrew (Recommended)**

```bash
brew install --cask cc-switch
```

Update:

```bash
brew upgrade --cask cc-switch
```

**Method 2: Manual Download**

Download `CC-Switch-v{version}-macOS.dmg` (recommended) or `.zip` from the [Releases](../../releases) page. It's a Universal build that runs natively on both Apple Silicon and Intel Macs.

> **Note**: CC Switch for macOS is code-signed and notarized by Apple. You can install and open it directly.

### Arch Linux Users

**Install via paru (Recommended)**

```bash
paru -S cc-switch-bin
```

### Linux Users

Download the latest Linux build from the [Releases](../../releases) page:

- `CC-Switch-v{version}-Linux-x86_64.deb` / `-Linux-arm64.deb` (Debian/Ubuntu)
- `CC-Switch-v{version}-Linux-x86_64.rpm` / `-Linux-arm64.rpm` (Fedora and other RPM distros that ship WebKitGTK 4.1)
- `CC-Switch-v{version}-Linux-x86_64.AppImage` / `-Linux-arm64.AppImage` (any distro meeting the requirements above)

> **Flatpak**: Not included in official releases. You can build it yourself from the `.deb` — see [`flatpak/README.md`](flatpak/README.md) for instructions.

## tools

1. **Add Provider**: Click "Add New Provider" (the + button) in the toolbar → Choose a preset or create a custom configuration
2. **Switch Provider**:
   - Main UI: Select provider → Click "Enable" (for OpenCode, OpenClaw, Hermes, and MiniMax Code the button is "Add"; these four tools and Pi are coexist-mode tools, so you can add several providers at once)
   - System Tray: Click provider name directly (Claude Code, Codex, Gemini CLI, and Grok Build only)
3. **Takes Effect**: Claude Code needs no restart; for Codex, Gemini CLI, and Grok Build, restart your terminal or the CLI tool; for Claude Desktop, restart the app itself (see FAQ)
4. **Back to Official Login**: Switch to the built-in official provider in the list (e.g. "Claude Official"), restart the tool, then follow its login/OAuth flow
5. **Local Routing (optional)**: To use OpenAI- or Gemini-format providers in Claude Code, or to use Claude in Codex, you need to turn on local routing. In "Settings → Routing → Local Routing", turn on "Routing Master Switch", then turn on the tool you need under "Routing Enabled". To toggle it right from the top of the main page, turn on "Show Routing Toggle on Main Page"

### MCP, Prompts, Skills, Projects & Sessions

- **MCP**: Click "MCP Management" → Add servers via templates or custom config (or "Import Existing") → Toggle sync for each tool
- **Prompts**: Click "Prompts" → Create prompts with the Markdown editor → Enable one to write it to that tool's prompt file
- **Skills**: Click "Skills" → "Discover Skills" → Search skills.sh or browse GitHub repos → One-click install to supported tools
- **Projects**: On the Claude Code, Claude Desktop, or Codex page, open the project switcher at the top of the main page → "New project" to save the current configuration; later, pick it from the switcher to switch the whole setup at once
- **Sessions**: Click "Session Manager" → Browse, search, and restore each tool's conversation history

> **Note**: On first launch, CC Switch automatically imports your existing Claude Code, Codex, Gemini CLI, and Grok Build configuration as a provider named `default` and adds an official provider for each of these tools and Claude Desktop, so nothing you had configured is lost.

For detailed guides on every feature, check out the **[User Manual](docs/user-manual/en/README.md)**, covering provider management, MCP/Prompts/Skills, local routing & failover, and more.
