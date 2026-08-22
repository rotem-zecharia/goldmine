# d-kimuson/claude-code-viewer

A full-featured web-based Claude Code client that provides complete interactive functionality for managing Claude Code projects

## tools

> [!WARNING]
> As of April 2026, Anthropic's [Terms of Service](https://code.claude.com/docs/en/legal-and-compliance#authentication-and-credential-use) prohibit using the Agent SDK to **send chat messages** with a subscription account. While Anthropic's X/Twitter announcements suggested personal use may be acceptable, the boundary between permitted and prohibited use remains ambiguous.
>
> In response, **chat sending, session resuming, permission approval, and `AskUserQuestion`** have been made opt-in.
>
> Note that real-time conversation log viewing, session history browsing, Git operations, and all other read-oriented features are implemented independently of the Agent SDK and remain fully available regardless of your authentication mode. You can start a Claude Code session from the CLI (or the built-in terminal) and watch it live in Claude Code Viewer without any restrictions.

## requirements

- **Node.js**: Version 22.13.0 or later
- **Claude Code**: v1.0.125 or later
- **Operating Systems**: macOS and Linux (Windows is not supported)

## installation

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

## configuration

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
