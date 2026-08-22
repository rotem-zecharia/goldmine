# EKKOLearnAI/hermes-studio

Web dashboard for Hermes Agent — multi-platform AI chat, session management, scheduled jobs, usage analytics

## features

| Area | What Hermes Studio does |
| --- | --- |
| Agent chat | Runs Hermes Agent conversations with streaming responses, tool traces, generated-file previews, persistent local sessions, and standalone desktop chat windows. |
| Local control plane | Manages profiles, providers, models, credentials, memory, skills, plugins, logs, and runtime settings from one dashboard. |
| Automation | Builds executable visual workflows and configures platform channels, cron jobs, Kanban tasks, group-chat rooms, and MCP servers around the same Hermes profiles. |
| Workspace tools | Provides a file browser, web terminal, Desktop Agent Browser, voice input/output, coding-agent runners, device discovery, Journey graph, and performance views. |
| Distribution | Ships as a desktop app for Windows/macOS/Linux, an npm CLI package, and a Docker image. |

## tools

- Total token usage breakdown (input / output)
- Session count with daily average
- Estimated cost tracking & cache hit rate
- Model usage distribution chart
- 30-day daily trend (bar chart + data table)

## configuration

These variables configure Hermes Web UI, its local Hermes runtime integration, and development/preview helpers. Provider API keys and Hermes Agent settings are normally managed through Hermes profiles; environment variables here are process-level overrides.

| Variable | Default | Description |
| --- | --- | --- |
| `PORT` | `8648` | Web UI listen port. |
| `BIND_HOST` | `0.0.0.0` | Web UI bind host. Set `::` explicitly for IPv6. |
| `HERMES_LAN_ADVERTISE_URL` | unset | Reachable Studio origin used in App LAN QR codes. Set this to the Docker host's LAN URL when Studio is opened through `localhost`, for example `http://192.168.1.20:6060`. |
| `HERMES_APP_ENTITLEMENT_REQUIRED` | `true` | Require a valid cloud-signed App entitlement before accepting a LAN App relay connection. Set `false` only for temporary compatibility diagnostics. |
| `HERMES_APP_ENTITLEMENT_PUBLIC_KEY` | built in | Optional PEM public-key override for RS256 App entitlements. The expected issuer is `hermes-studio-server` and audience is `ekko-studio`. |
| `HERMES_WEB_UI_HOME` | `~/.hermes-web-ui` | Web UI data home for auth token, credentials, logs, DB, and default uploads. `HERMES_WEBUI_STATE_DIR` is also supported as a compatibility alias. |
| `HERMES_WEBUI_STATE_DIR` | unset | Compatibility alias for `HERMES_WEB_UI_HOME`. |
| `HERMES_WEB_UI_DISABLE_MCP_AUTOINJECT` | unset | Disable startup injection of the managed `hermes-studio` MCP server into Hermes profile configs. |
| `HERMES_WEB_UI_ALLOW_TRANSIENT_MCP_AUTOINJECT` | unset | Allow managed MCP injection when `HERMES_WEB_UI_HOME` is under a temporary directory, such as Version Preview runtimes. |
| `UPLOAD_DIR` | `$HERMES_WEB_UI_HOME/upload` | Upload root override. Files are stored below profile-scoped subdirectories. |
| `CORS_ORIGINS` | same host only | Comma- or space-separated cross-origin allowlist for HTTP, Socket.IO, and WebSocket requests. Set `*` only when you intentionally need legacy wildcard CORS. |
| `AUTH_TOKEN` | auto-generated | Explicit bearer token. If unset, Web UI creates one under `HERMES_WEB_UI_HOME`. |
| `AUTH_JWT_SECRET` | `AUTH_TOKEN` | JWT signing secret override for username/password sessions. |
| `HERMES_WEB_UI_AUTH_JWT_EXPIRES_IN` | `30d` | Username/password session JWT lifetime. Accepts seconds or `s`/`m`/`h`/`d` suffixes, for example `12h` or `7d`. |
| `PROFILE` | `default` | Startup/default Hermes profile. Runtime requests use the profile selected by the frontend and authorized for the current account. |
| `LOG_LEVEL` | `info` | Server log level. |
| `BRIDGE_LOG_LEVEL` | `$LOG_LEVEL` or `info` | Bridge log level. |
| `MAX_DOWNLOAD_SIZE` | `200MB` | Maximum file download size. |
| `MAX_EDIT_SIZE` | `10MB` | Maximum editable file size. |
| `WORKSPACE_BASE` | current user's home directory | Base directory for workspace browsing. |
| `HERMES_HOME` | platform default | Hermes data home. Windows uses `%LOCALAPPDATA%\hermes`; macOS/Linux uses `~/.hermes`. |
| `HERMES_BIN` | `hermes` | Custom Hermes CLI binary path. |
| `HERMES_AGENT_ROOT` | auto-discovered | Hermes Agent source checkout containing `run_agent.py`. |
| `HERMES_AGENT_BRIDGE_PYTHON` | auto-discovered | Python interpreter used to launch the agent bridge. |
| `HERMES_AGENT_BRIDGE_UV` | auto-discovered | `uv` executable used to launch the agent bridge when available. |
| `UV` | auto-discovered | Fallback `uv` executable path. |
| `PYTHON` | auto-discovered | Fallback Python executable for the agent bridge. |
| `HERMES_AGENT_BRIDGE_ENDPOINT` | platform default | Agent bridge broker endpoint. Windows defaults to `tcp://127.0.0.1:18765`; macOS/Linux defaults to `ipc:///tmp/hermes-agent-bridge.sock`. |
| `HERMES_AGENT_BRIDGE_TIMEOUT_MS` | `120000` | Timeout for Node requests to the bridge broker. |
| `HERMES_AGENT_BRIDGE_CONNECT_RETRY_MS` | `5000` | Short retry window for connecting to the bridge socket. |
| `HERMES_AGENT_BRIDGE_STARTUP_TIMEOUT_MS` | `120000` | Timeout while waiting for the Python bridge to become ready. |
|
