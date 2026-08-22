# d-kimuson/claude-code-viewer

A full-featured web-based Claude Code client that provides complete interactive functionality for managing Claude Code projects

## tools

> [!WARNING]
> As of April 2026, Anthropic's [Terms of Service](https://code.claude.com/docs/en/legal-and-compliance#authentication-and-credential-use) prohibit using the Agent SDK to **send chat messages** with a subscription account. While Anthropic's X/Twitter announcements suggested personal use may be acceptable, the boundary between permitted and prohibited use remains ambiguous.
>
> In response, **chat sending, session resuming, permission approval, and `AskUserQuestion`** have been made opt-in.
>
> Note that real-time conversation log viewing, session history browsing, Git operations, and all other read-oriented features are implemented independently of the Agent SDK and remain fully available regardless of your authentication mode. You can start a Claude Code session from the CLI (or the built-in terminal) and watch it live in Claude Code Viewer without any restrictions.

### Choosing Your Authentication Mode

On first launch (or from the Settings screen), you will be prompted to select your authentication method:

- **API Key** (default) — Uses the Anthropic API directly. All features, including chat sending, are fully available.
- **Subscription** — Opts out of Agent SDK chat features. The chat input switches to a copy mode: configure your session options in the form, then click the **Copy** button to get the equivalent `claude` CLI command with the corresponding arguments already set. Paste and run it in any terminal to start or resume your session. Once the session is running, Claude Code Viewer will display the conversation in real-time as usual.

### Built-in Terminal

Claude Code Viewer includes an integrated terminal emulator accessible via the **panel at the bottom of the screen**. Open it, paste the copied command, and launch Claude Code without ever leaving the browser.

---

## Introduction

Claude Code Viewer is a web-based Claude Code client focused on **comprehensive session log analysis**. It preserves and organizes all conversation data through strict schema validation and a progressive disclosure UI that reveals details on demand.

**Core Philosophy**: Zero data loss + Effective organization + Remote-friendly design

## requirements

- **Node.js**: Version 22.13.0 or later
- **Claude Code**: v1.0.125 or later
- **Operating Systems**: macOS and Linux (Windows is not supported)

## installation

### Quick Start (CLI)

Run directly from npm without installation:

```bash
npx @kimuson/claude-code-viewer@latest --port 3400
```

Alternatively, install globally:

```bash
npm install -g @kimuson/claude-code-viewer
claude-code-viewer --port 3400
```

The server will start on port 3400 (or the default port 3000). Open `http://localhost:3400` in your browser to access the interface.

**Available Options:**

```bash
claude-code-viewer [options]

Options:
  -p, --port <port>                Port to listen on (default: 3000)
  -h, --hostname <hostname>        Hostname to listen on (default: localhost)
  -v, --verbose                    Enable verbose debug logging
  -P, --password <password>        Password for authentication
  -e, --executable <executable>    Path to Claude Code executable
  --claude-dir <claude-dir>        Path to Claude directory
  --api-only                       Run in API-only mode without Web UI
  --base-path <path>               URL base path to serve the app under
```

### Remote Access via Tailscale (Mobile / PWA)

Claude Code Viewer works great as a persistent server you access from your phone. A convenient approach is to run it on a always-on machine and expose it over [Tailscale](https://tailscale.com/) with HTTPS:

1. **Set up HTTPS on your Tailscale node** following the [Tailscale HTTPS certificates guide](https://tailscale.com/docs/how-to/set-up-https-certificates).
2. **Start Claude Code Viewer** bound to all interfaces with a password:

   ```bash
   claude-code-viewer --hostname 0.0.0.0 --port 3400 --password your-secret
   ```

3. **Access from your phone** via the Tailscale HTTPS URL (e.g. `https://your-machine.ts.net:3400`).

Claude Code Viewer is a **PWA (Progressive Web App)**. On mobile, tap "Add to Home Screen" to get an app-like experience with an optimized UI and push notifications when sessions complete.

### Reverse Proxy Sub-Path

Use `--base-path` (or `CCV_BASE_PATH`) when serving Claude Code Viewer below a URL prefix:

```bash
claude-code-viewer --hostname 127.0.0.1 --port 3400 --base-path /ccv
```

Configure the reverse proxy to preserve the prefix when forwarding requests. The UI, API, SSE connection, terminal WebSocket, authentication cookies, PWA manifest, and service worker will then use `/ccv`:

```nginx
location /ccv/ {
  proxy_pass http://127.0.0.1:3400;
  proxy_http_version 1.1;
  proxy_buffering off;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection "upgrade";
  proxy_set_header Host $host;
}
```

The base path accepts nested URL-safe segments such as `/tools/ccv`. Values containing traversal segments, backslashes, query strings, fragments, spaces, or percent-encoding are rejected.

## configuration

### Command-Line Options and Environment Variables

Claude Code Viewer can be configured using command-line options or environment variables. Command-line options take precedence over environment variables.

| Command-Line Option             | Environment Variable        | Description                                                                                                                                                                                                                                                                                                    | Default       |
| ------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `-p, --port <port>`             | `PORT`                      | Port number for Claude Code Viewer to run on                                                                                                                                                                                                                                                                   | `3000`        |
| `-h, --hostname <hostname>`     | `HOSTNAME`                  | Hostname to listen on for remote access                                                                                                                                                                                                                                                                        | `localhost`   |
| `-v, --verbose`                 | —                           | Enable verbose debug logging. Outputs detailed server-side logs to stderr for troubleshooting                                                                                                                                                                                                                  | (unset)       |
| `-P, --password <password>`     | `CCV_PASSWORD`              | Password for authentication. When set, enables password-based authentication to protect access to Claude Code Viewer. All `/api` routes (except login, logout, check, config, and version endpoints) require authentication. If not set, authentication is disabled and the application is publicly accessible | (none)        |
| `-e, --executable <executable>` | `CCV_CC_EXECUTABLE_PATH`    | Path to Claude Code installation. If not set, uses system PATH installation, or falls back to bundled version from dependencies                                                                                                                                                                                | (auto-detect) |
| `--claude-dir <claude-dir>`     | `CCV_GLOBAL_CLAUDE_DIR`     | Path to Claude directory where session logs are stored                                                                                                                                                                                                                                                         | `~/.claude`   |
| `--terminal-disabled`           | `CCV_TERMINAL_DISABLED`     | Disable the in-app terminal panel when set to `1`/`true` (env) or when the flag is present (CLI)                                                                                                                                                                                                               | (unset)       |
| `--terminal-shell <path>`       | `CCV_TERMINAL_SHELL`        | Shell executable for terminal sessions (e.g. `/bin/zsh`)                                                                                                                                                                                           

## features

| Feature                 | Description                                                                                                                                                                                                                                                                                                                                                              |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| View Chat Logs          | View Claude Code session logs in real-time through the web UI. Supports historical logs as it uses standard Claude Code logs (~/.claude/projects/...) as the data source                                                                                                                                                                                                 |
| Search Conversations    | Full-text search across conversations with `⌘K` (macOS) or `Ctrl+K` (Linux). Search within a specific project or across all projects. Features fuzzy matching, prefix search, and keyboard navigation (↑↓ to navigate, Enter to select)                                                                                                                                  |
| In-page Find            | Jump to any text in the current conversation with a configurable hotkey (`Ctrl+F` / `Command+F`). Cycles through all matches with keyboard navigation                                                                                                                                                                                                                    |
| Start Conversations     | Start Claude Code sessions directly from Claude Code Viewer. Enjoy core functionality like file/command completion, pause/resume, and tool approval through a superior web experience                                                                                                                                                                                    |
| Resume Sessions         | Resume conversations directly from existing session logs                                                                                                                                                                                                                                                                                                                 |
| Continue Sessions       | Claude Code Viewer provides advanced session process control. Sessions started through Claude Code Viewer remain alive (unless aborted), allowing you to continue conversations without resuming (no session-id reassignment)                                                                                                                                            |
| Create Projects         | Create new projects from Claude Code Viewer. Select a directory through the web UI to execute the `/init` command and begin project setup                                                                                                                                                                                                                                |
| Session Options Toolbar | Inline toolbar above the chat input for configuring per-project session options: model selection, thinking effort (low/medium/high/max), permission mode, and system prompt preset. Settings persist per project                                                                                                                                                         |
| Voice Input             | Dictate messages directly in the chat input using the built-in
