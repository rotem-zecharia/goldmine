# im4codes/imcodes

The IM for agents. Shared Agent Context & Memory, supervised execution, and cross-agent audit across AI providers.

## tools

IM.codes exposes a daemon-managed stdio MCP server to supported SDK-backed providers. Agents get one runtime-scoped tool surface for memory, agent-to-agent messaging, and scheduled follow-ups, without raw auth tokens or ad hoc shell commands.

- **Memory recall and provenance.** `search_memory` searches the caller-bound memory namespace for prior work, project history, decisions, preferences, bugs, commits, deployments, and previously discussed context. `list_memory_summaries` retrieves recent compact summaries without a query. Results include compact refs plus `projectionId` values; `get_memory_sources` expands a relevant hit into provenance snippets when the model needs exact prior instructions, bug details, commit/deployment context, or source evidence.
- **Memory writes.** `save_observation` stores useful facts, decisions, or implementation notes as user-private memory candidates; `save_preference` stores stable user preferences through the explicit preference path.
- **Agent messaging.** `send_list_targets` lists sibling sessions in the current project, and `send_message` sends scoped messages, optional file path references, reply requests, or broadcasts through the same guarded `imcodes send` pipeline.
- **Cron scheduling.** `cron_create`, `cron_list`, `cron_update`, and `cron_delete` manage future structured sends for reminders, recurring checks, delegated reviews, or scheduled Team follow-ups, with target/session/project fields and optional expiration/timezone data.
- **Runtime-bound identity and safety.** Tool calls are bound to the current IM.codes session, project, user, and server at runtime. Agents cannot forge namespace, user, server, token, or routing fields; memory, Send, and Cron all remain behind their underlying feature gates plus MCP kill switches.
- **Operational visibility.** The Shared Context UI reports MCP readiness per managed provider, tool-family gate state, degraded reasons, update time, and recent daemon-redacted tool calls so you can tell whether the model really has Memory, Send, and Cron available.

## Supervised Execution & Auto Audit

IM.codes can drive supported agent sessions turn by turn — a supervisor with your own instructions evaluates each completed turn at the idle boundary and decides to auto-continue, hand back, or trigger an audit loop, instead of you typing "continue" every round.

- **Per-session Auto modes.** Configure `off`, `supervised`, or `supervised_audit` per session instead of forcing one policy everywhere.
- **Completion checks at the idle boundary.** When a turn finishes, IM.codes can classify it as `complete`, `continue`, or `ask_human`, then dispatch the next continue prompt inside the same session.
- **Fail-closed automation.** Auto supervision stays visible in the timeline/footer, uses structured decisions, and returns control to you on timeout, invalid output, or bad config instead of silently guessing.
- **Optional audit → rework loop.** In `supervised_audit`, a completed turn can automatically enter an audit pipeline and send a rework brief back into the same session before control returns.
- **Global defaults seed new sessions.** Set your default supervisor backend, model, and timeout once. New `supervised` / `supervised_audit` sessions snapshot them at enable time, and each session can still override backend/model/timeout and audit mode individually.
- **Two-layer custom supervision instructions.** Keep a global supervision persona alongside a per-session addition. By default the two are concatenated (`global`, blank line, then `session`); tick the session's **Override global** checkbox to ignore the global value for that one session. Unlike backend/model/timeout, the global value is re-read on every dispatch, so editing it takes effect on already-enabled sessions without a re-enable.
- **Built for real IM.codes workflows.** Auto supervision understands OpenSpec work, Team discussion/review flows, and `imcodes send`-style cross-agent coordination as valid agent

## features

### Private Aliases

Save owner-scoped reusable text snippets and insert them from the composer by typing `;` or selecting a `;;(name)` marker. The message keeps the marker visible while IM.codes resolves and delivers the value out of band. Agents can create, search, edit, and resolve aliases through managed MCP tools; bulk listings expose metadata only, so one call cannot dump every stored value into model context.

### Controlled Nodes

Enroll another machine as a restricted controlled node without turning it into a full IM.codes source server. Type `^` to autocomplete a target or insert `^^(name)` directly, then authorized agents can run scoped remote commands, transfer individual files, or invoke typed Computer Use tools on that node. Execution remains owner-gated and revocable, controlled nodes stay out of normal server/session lists, and each enrolled machine receives independent credentials. Download links expire, but a newly downloaded installer can be kept and reused to enroll multiple machines.

### Windows Remote Desktop

Capable Windows controlled nodes expose a continuous H.264 remote desktop to authorized Owners and Participants. The browser and native worker negotiate a direct WebRTC route first and use TURN UDP/TCP only as fallback; video and mouse/keyboard data never pass through the application Server. Control is the default mode, multiple authorized controllers are allowed, and each viewer can switch independently to View mode. Display tabs support a context menu (right-click, keyboard context-menu key, or mobile long-press) for 720p, 1080p, 1440p, and 4K modes. Mobile includes pinch/drag navigation plus a zoomed virtual-mouse mode with edge pan, left/middle/right buttons, and wheel scrolling.

macOS and Linux controlled nodes are supported soon; today the feature is offered only by capable Windows nodes, and a node that cannot serve it simply does not advertise the capability.

The Windows package is a signed, prebuilt worker: controlled nodes do not install compilers or media dependencies. Capture uses DXGI Desktop Duplication and encoding uses a low-latency Media Foundation H.264 transform. Hardware encoding is preferred when it passes its runtime gate; the qualified Windows software transform keeps integrated-only, AMD, NVIDIA-without-NVENC, and headless systems eligible without a GPU-vendor requirement. A signed on-demand virtual display is used only when no presentable real display exists and is removed after the last session. Protected video, the lock screen, and UAC secure desktop are intentionally not bypassed.

Operators should expose TURN TCP and UDP on `TURN_PORT` (default `3479`) and UDP relay ports `TURN_RELAY_MIN_PORT`–`TURN_RELAY_MAX_PORT` (defaults `49160`–`49200`), set `TURN_HOST`, `TURN_EXTERNAL_IP`, and a strong `TURN_SHARED_SECRET`, and monitor relay bandwidth. `IMCODES_REMOTE_DESKTOP_ENABLED=0` is the fail-closed kill switch for new sessions; omitting it enables the feature only when the node advertises a verified worker. Revocation, execution disable, browser/daemon loss, lease expiry, local Stop, or worker failure closes input and releases pressed keys/buttons. Existing Computer Use, exec, heartbeat, and file-transfer functions remain available when remote desktop is disabled.

Troubleshooting starts with the panel's bounded route/RTT/FPS/bitrate/encoder diagnostics and the node's worker health status. A missing capability means the signed worker or manifest did not verify; `media_unavailable` usually means no presentable desktop or compliant encoder; repeated TURN use means direct ICE is unavailable. Roll back with the normal controlled-node upgrade path—the installer restores the prior node, worker, manifest, and only the exact IM.codes virtual-display package added by that attempt.

### Computer Use & Browser Automation

Supported SDK agents can control desktop apps through typed Computer Use tools. The cross-platform desktop-app path integrates [Open Computer Use](https://github.c

## installation

```bash
npm install -g imcodes
```

## Quick Start

> **Self-hosting is strongly recommended.** The shared instance at `app.im.codes` is for testing only — it comes with no uptime guarantees, may be rate-limited, and could be targeted. This is a personal project with no commercial support. For anything beyond evaluation, deploy the server on your own infrastructure.

Use [app.im.codes](https://app.im.codes) for evaluation, or self-host for anything real.

```bash
imcodes bind https://app.im.codes/bind/<api-key>
```

This binds your machine, starts the daemon, registers it as a system service, and brings the machine into the web/mobile dashboard.

### OpenClaw Connect

If OpenClaw is running locally, connect IM.codes to the OpenClaw gateway on the daemon machine:

```bash
imcodes connect openclaw
```

What this does:

- connects to `ws://127.0.0.1:18789` by default
- reuses the OpenClaw gateway token automatically from `~/.openclaw/openclaw.json`
- syncs OpenClaw sessions and child sessions into IM.codes so they appear as transport-backed sessions/sub-sessions
- saves the IM.codes-side connection config to `~/.imcodes/openclaw.json`
- restarts the daemon so OpenClaw transport sessions can reconnect automatically

Common variants:

```bash
imcodes connect openclaw --url ws://127.0.0.1:18789
OPENCLAW_GATEWAY_TOKEN=... imcodes connect openclaw
imcodes connect openclaw --url wss://gateway.example.com
```

Notes:

- remote non-TLS `ws://` URLs require `--insecure`
- use `imcodes disconnect openclaw` to remove the saved config and drop the connection
- this flow has only been tested on macOS

## Self-Host

### One-Command Setup

Deploy server + daemon on a single machine. Requires Docker and a domain with DNS pointing to the server.

```bash
npm install -g imcodes
mkdir imcodes && cd imcodes
imcodes setup --domain imc.example.com
```

This generates all config, starts PostgreSQL + server + Caddy with automatic HTTPS, creates the admin account, and binds the local daemon — all in one step. Credentials are printed at the end.

To connect additional machines:

```bash
npm install -g imcodes
imcodes bind https://imc.example.com/bind/<api-key>
```

### Manual Setup

If you prefer to configure manually:

```bash
git clone https://github.com/im4codes/imcodes.git && cd imcodes
./gen-env.sh imc.example.com        # generates .env with random secrets, prints admin password
docker compose up -d
```

The generated `docker-compose.yml` already uses `pgvector/pgvector:pg18` for PostgreSQL.

Login at `https://your-domain` with `admin` and the printed password. Bind your dev machine with `imcodes bind`.

## Windows (experimental)

Windows is natively supported via [ConPTY](https://devblogs.microsoft.com/commandline/windows-command-line-introducing-the-windows-pseudo-console-conpty/) (built-in on Windows 10+). No WSL required.

### Install & Bind (Windows)

```cmd
npm install -g imcodes
imcodes bind https://app.im.codes/bind/<api-key>
```

### Upgrade (Windows)

```cmd
imcodes upgrade
```

Or upgrade remotely from the web dashboard (sends upgrade command to the daemon).

### Troubleshooting (Windows)

If the daemon stops after an auto-upgrade, regenerate the launch chain:

```cmd
imcodes repair-watchdog
```

This rewrites the watchdog script and scheduled task with the current Node.js and imcodes paths. Needed after Node.js version switches (nvm, fnm) or if the daemon won't restart after upgrade.

If `imcodes` is "not recognized as internal or external command" after upgrade, the npm global directory may not be on your PATH. Fix it:

```cmd
npm prefix -g
```

Copy the output path and add it to your PATH:

```cmd
setx PATH "<npm-prefix-path>;%PATH%"
```

Then open a **new** terminal window.

Check the daemon watchdog log for errors:

```
%USERPROFILE%\.imcodes\watchdog.log
```

## requirements

- macOS or Linux (tested on both)
- **Windows (experimental)**: Native support via ConPTY (built-in on Windows 10+). Just `npm install -g imcodes` — no extra software needed. WSL also works.
- Node.js >= 22
- Terminal multiplexer: [tmux](https://github.com/tmux/tmux) (Linux/macOS). Windows uses ConPTY (auto-detected, built-in).
- At least one AI coding agent: [Claude Code](https://github.com/anthropics/claude-code) (CLI or SDK), [Codex](https://github.com/openai/codex) (CLI or SDK), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [OpenClaw](https://openclaw.com), or [Qwen](https://github.com/QwenLM/qwen-agent)

## About

This is a personal project. I haven't written any code myself — it was built almost entirely by [Claude Code](https://github.com/anthropics/claude-code), with significant contributions from [Codex](https://github.com/openai/codex) and [Gemini CLI](https://github.com/google-gemini/gemini-cli).

## Disclaimer

IM.codes is an independent open-source project and is not affiliated with, endorsed by, or sponsored by Anthropic, OpenAI, Google, Alibaba, OpenClaw, or any other company whose products are mentioned. All product names, trademarks, and registered trademarks are the property of their respective owners.

## License

[MIT](LICENSE)

© 2026 [IM.codes](https://im.codes)
