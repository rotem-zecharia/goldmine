# jackwener/OpenCLI

Make Any Website into CLI & Use your logged-in browser by AI agent.

## installation

### 1. Install OpenCLI

For desktop use, start with **OpenCLIApp**. It bundles the OpenCLI runtime,
keeps the managed `opencli` command installed, and gives you a system tray UI
for setup, diagnostics, updates, browser-login keepalive, and Web → Markdown.

**Option A — OpenCLIApp (recommended for macOS / Windows):**
Download the latest app from <https://opencli.info/download>, install it, then
open the app once and use the System page to install or repair the `opencli`
command.

**Option B — npm global install (CLI-only / CI / servers):**
OpenCLI requires **Node.js >= 20** when installed through npm.

```bash
node --version
npm install -g @jackwener/opencli
```

### 2. Install the Browser Bridge Extension

OpenCLI connects to Chrome/Chromium through a lightweight Browser Bridge extension plus a small local daemon. The daemon auto-starts when needed.

**Option A — Chrome Web Store (recommended):**
Install **OpenCLI** from the [Chrome Web Store](https://chromewebstore.google.com/detail/opencli/ildkmabpimmkaediidaifkhjpohdnifk).

**Option B — Manual install:**
1. Download the latest `opencli-extension-v{version}.zip` from the GitHub [Releases page](https://github.com/jackwener/opencli/releases).
2. Unzip it, open `chrome://extensions`, and enable **Developer mode**.
3. Click **Load unpacked** and select the unzipped folder.

### 3. Verify the setup

```bash
opencli doctor
```

### 4. Optional: name your Chrome profile

Each Chrome profile runs its own OpenCLI extension instance. If you use multiple Chrome profiles, list the connected profiles and assign local aliases:

```bash
opencli profile list
opencli profile rename <contextId> work
opencli profile use work
opencli --profile work browser main state
```

With only one connected profile, OpenCLI uses it automatically. With multiple connected profiles and no default, OpenCLI asks you to choose instead of guessing.

## tools

```bash
opencli list
opencli hackernews top --limit 5
opencli bilibili hot --limit 5
```

## For Humans

Use OpenCLI directly when you want a reliable command instead of a live browser session:

- `opencli list` shows every registered command.
- `opencli <site> <command>` runs a built-in or generated adapter.
- `opencli external register mycli` exposes a local CLI through the same discovery surface.
- `opencli doctor` helps diagnose browser connectivity.

## Extending OpenCLI

If you want to add your own commands, start with the [Extending OpenCLI guide](./docs/guide/extending-opencli.md). README keeps this short; the guide covers the directory layout, source-control model, and install commands.

| Need | Recommended path |
|------|------------------|
| Keep personal website commands in your own Git repo | `opencli plugin create` + `opencli plugin install file://...` |
| Quickly draft a private local adapter | `opencli browser init <site>/<command>` in `~/.opencli/clis/` |
| Modify an official adapter locally | `opencli adapter eject <site>` + `opencli adapter reset <site>` |
| Publish or install third-party commands | `opencli plugin install github:user/repo` |
| Wrap an existing local binary | `opencli external register <name>` |

## For AI Agents

OpenCLI's browser commands are designed to be used by AI Agents — not run manually. Install skills into your AI agent (Claude Code, Cursor, etc.), and the agent operates websites on your behalf using your logged-in Chrome session.

## configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENCLI_PROFILE` | — | Browser Bridge profile alias/contextId to use when multiple Chrome profiles are connected |
| `OPENCLI_WINDOW` | command default | Set to `foreground` or `background` to override Browser Bridge window placement. Browser-backed commands also accept `--window <foreground\|background>`. |
| `OPENCLI_BROWSER_CONNECT_TIMEOUT` | `45` | Seconds to wait for browser connection |
| `OPENCLI_BROWSER_COMMAND_TIMEOUT` | `60` | Seconds to wait for a single browser command |
| `OPENCLI_CDP_ENDPOINT` | — | Chrome DevTools Protocol endpoint for remote browser or Electron apps |
| `OPENCLI_CDP_TARGET` | — | Filter CDP targets by URL substring (e.g. `detail.1688.com`) |
| `OPENCLI_VERBOSE` | `false` | Enable verbose logging (`-v` flag also works) |
| `DEBUG_SNAPSHOT` | — | Set to `1` for DOM snapshot debug output |

`opencli browser *` requires an explicit `<session>` positional, uses a foreground browser window by default, and keeps that session's tab lease until `opencli browser <session> close` or idle cleanup. Browser-backed adapters use a background adapter window and release one-shot tab leases by default. Interactive adapters can declare `siteSession: 'persistent'` to keep a stable site tab for continuity; pass `--site-session ephemeral` for a one-shot tab.
