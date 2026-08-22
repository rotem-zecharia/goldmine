# jo-inc/camofox-browser

Stealth headless browser for AI agents — bypass Cloudflare, bot detection, and anti-scraping. Drop-in Puppeteer/Playwright replacement.

## features

- **C++ Anti-Detection** - bypasses Google, Cloudflare, and most bot detection
- **Element Refs** - stable `e1`, `e2`, `e3` identifiers for reliable interaction
- **Token-Efficient** - accessibility snapshots are ~90% smaller than raw HTML
- **Runs on Anything** - lazy browser launch + idle shutdown keeps memory at ~40MB when idle. Designed to share a box with the rest of your stack -- Raspberry Pi, $5 VPS, shared infra.
- **Session Isolation** - separate cookies/storage per user
- **Cookie Import** - inject Netscape-format cookie files for authenticated browsing
- **File Upload** - attach files from a configured upload directory without a native OS dialog
- **Proxy + GeoIP** - route traffic through residential proxies with automatic locale/timezone
- **Structured Logging** - JSON log lines with request IDs for production observability
- **YouTube Transcripts** - extract captions from any YouTube video via yt-dlp, no API key needed
- **Search Macros** - `@google_search`, `@youtube_search`, `@amazon_search`, `@reddit_subreddit`, and 10 more
- **Snapshot Screenshots** - include a base64 PNG screenshot alongside the accessibility snapshot
- **Large Page Handling** - automatic snapshot truncation with offset-based pagination
- **Download Capture** - capture browser downloads and fetch them via API (optional inline base64)
- **DOM Image Extraction** - list `<img>` src/alt and optionally return inline data URLs
- **Deploy Anywhere** - Docker, Fly.io, Railway
- **VNC Interactive Login** - log into sites visually via noVNC, export storage state for agent reuse
- **OpenAPI Docs** - auto-generated spec at [`/openapi.json`](http://localhost:9377/openapi.json) and interactive docs at [`/docs`](http://localhost:9377/docs)
- **Structured Extract** - `POST /tabs/:tabId/extract` with a JSON Schema that maps properties to snapshot refs via `x-ref`
- **Session Tracing** - opt-in per-session Playwright trace capture (screenshots + DOM snapshots + network) with API endpoints to list, fetch, and delete trace zips
- **Telemetry** - automatic [anonymized crash/hang telemetry](lib/reporter.js#L28-L290) via GitHub Issues. Identifies which sites cause failures and common failure patterns. Private domains are HMAC-hashed, paths/params stripped, tokens/IPs redacted. Opt-out with `CAMOFOX_CRASH_REPORT_ENABLED=false`.

## requirements

| Dependency | Purpose | Install |
|-----------|---------|---------|
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | YouTube transcript extraction (fast path) | `pip install yt-dlp` or `brew install yt-dlp` |

The Docker image includes yt-dlp. For local dev, install it for the `/youtube/transcript` endpoint. Without it, the endpoint falls back to a slower browser-based method.

## installation

### OpenClaw Plugin

```bash
openclaw plugins install @askjo/camofox-browser
```

**Tools:** `camofox_create_tab`  |  `camofox_snapshot`  |  `camofox_click`  |  `camofox_type`  |  `camofox_navigate`  |  `camofox_scroll`  |  `camofox_screenshot`  |  `camofox_close_tab`  |  `camofox_list_tabs`  |  `camofox_import_cookies`

### Standalone

Run from npm:

```bash
npx @askjo/camofox-browser
```

Or from source:

```bash
git clone https://github.com/jo-inc/camofox-browser
cd camofox-browser
npm install
npm start  # downloads Camoufox on first run (~300MB)
```

Default port is `9377`. See [Environment Variables](#environment-variables) for all options.

> **Note:** the postinstall script unsets `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD` for itself before fetching the Camoufox binary. Without that override, an exported `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1` (common when Playwright is configured to use system Chrome) would silently skip the binary download and crash the server at runtime.
>
> **External Camoufox executable:** set `CAMOUFOX_EXECUTABLE=/path/to/camoufox-bin` before `npm install` and when starting the server to skip the bundled download and launch that executable. Compatibility aliases are `CAMOUFOX_EXECUTABLE_PATH` and `CAMOFOX_EXECUTABLE_PATH`. This is useful for NixOS paths such as `/nix/store/.../camoufox-bin`; the executable must come from a Camoufox bundle that includes `properties.json`, `version.json`, and `fontconfig/`.
>
> **Air-gapped or custom binary management:** prefer `CAMOUFOX_EXECUTABLE` when you already have a Camoufox bundle. Otherwise disable the auto-fetch with `npm install --ignore-scripts` (skips lifecycle scripts for *every* dependency -- bluntest option) or, more surgically, `npm install --omit=optional` plus a manual `npx camoufox-js fetch` step against your mirror. Note that `PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm install` no longer skips the Camoufox download (the postinstall sanitizes the env locally); use `--ignore-scripts` or `CAMOUFOX_EXECUTABLE` for that.

### Docker

The included `Makefile` auto-detects your CPU architecture and pre-downloads Camoufox + yt-dlp binaries outside the Docker build, so rebuilds are fast (~30s vs ~3min).

```bash
# Build and start (auto-detects arch: aarch64 on M1/M2, x86_64 on Intel)
make up

# Stop and remove the container
make down

# Force a clean rebuild (e.g. after upgrading VERSION/RELEASE)
make reset

# Just download binaries (without building)
make fetch

# Override arch or version explicitly
make up ARCH=x86_64
make up VERSION=135.0.1 RELEASE=beta.24
```

#### Windows

On Windows, `make` is not available. Use the included `build.ps1` PowerShell script instead:

```powershell
# Build and start
.\build.ps1 up

# Stop and remove the container
.\build.ps1 down

# Build image only
.\build.ps1 build

# Force a clean rebuild
.\build.ps1 reset

# Download binaries only (without building)
.\build.ps1 fetch

# Override architecture
.\build.ps1 up -Arch x86_64
.\build.ps1 up -Arch aarch64
```

> **Note:** PowerShell 7+ (`pwsh`) is recommended but `powershell.exe` (Windows PowerShell 5.1) also works. The script requires Docker Desktop for Windows with the WSL2 backend.
>
> **Line endings:** This project includes a `.gitattributes` file that forces Unix (`LF`) line endings for `.sh` files. If you've already cloned the repo and get `sh: not found` or `set: Illegal option -` errors during `docker build`, run:
> ```powershell
> Get-ChildItem -Recurse *.sh | ForEach-Object { (Get-Content $_) -join "`n" + "`n" | Set-Content $_ -NoNewline }
> ```
> This converts shell scripts to LF line endings. Future clones will handle this automatically thanks to `.gitattributes`.

> **WARNING: Do not run `docker build` directly.** The Dockerfile uses bind mounts to pull pre-downloaded binaries from `dist/`. Always use `make up` (or `make fetch` then `make build`) -- it downloads the binaries first.

### Fly.io

For Fly.io or other remote CI, you'll need a Dockerfile that downloads binaries at

## tools

### Cookie Import

Import cookies from your browser into Camoufox to skip interactive login on sites like LinkedIn, Amazon, etc.

#### Setup

**1. Generate a secret key:**

```bash
# macOS / Linux
openssl rand -hex 32
```

**2. Set the environment variable before starting OpenClaw:**

```bash
export CAMOFOX_API_KEY="your-generated-key"
openclaw start
```

The same key is used by both the plugin (to authenticate requests) and the server (to verify them). Both run from the same environment -- set it once.

> **Why an env var?** The key is a secret. Plugin config in `openclaw.json` is stored in plaintext, so secrets don't belong there. Set `CAMOFOX_API_KEY` in your shell profile, systemd unit, Docker env, or Fly.io secrets.

> **Cookie import is disabled by default.** If `CAMOFOX_API_KEY` is not set, the server rejects all cookie requests with 403.

**3. Export cookies from your browser:**

Install a browser extension that exports Netscape-format cookie files (e.g., "cookies.txt" for Chrome/Firefox). Export the cookies for the site you want to authenticate.

**4. Place the cookie file:**

```bash
mkdir -p ~/.camofox/cookies
cp ~/Downloads/linkedin_cookies.txt ~/.camofox/cookies/linkedin.txt
```

The default directory is `~/.camofox/cookies/`. Override with `CAMOFOX_COOKIES_DIR`.

**5. Ask your agent to import them:**

> Import my LinkedIn cookies from linkedin.txt

The agent calls `camofox_import_cookies` -> reads the file -> POSTs to the server with the Bearer token -> cookies are injected into the browser session. Subsequent `camofox_create_tab` calls to linkedin.com will be authenticated.

#### How it works

```
~/.camofox/cookies/linkedin.txt          (Netscape format, on disk)
        |
        v
camofox_import_cookies tool              (parses file, filters by domain)
        |
        v  POST /sessions/:userId/cookies
        |  Authorization: Bearer <CAMOFOX_API_KEY>
        |  Body: { cookies: [Playwright cookie objects] }
        v
camofox server                           (validates, sanitizes, injects)
        |
        v  context.addCookies(...)
        |
Camoufox browser session                 (authenticated browsing)
```

- `cookiesPath` is resolved relative to the cookies directory -- path traversal outside it is blocked
- Max 500 cookies per request, 5MB file size limit
- Cookie objects are sanitized to an allowlist of Playwright fields

### Session Persistence

By default, camofox persists each user's cookies and localStorage to `~/.camofox/profiles/`. Sessions survive browser restarts -- log in once (via cookies or VNC), and subsequent sessions restore the authenticated state automatically.

```
~/.camofox/
|-- cookies/          # Bootstrap cookie files (Netscape format)
\-- profiles/         # Persisted session state (auto-managed)
    \-- <hashed-userId>/
        \-- storage_state.json
```

Override the directory with `CAMOFOX_PROFILE_DIR` or set `"profileDir"` in the persistence plugin config. To disable persistence, set `"persistence": { "enabled": false }` in `camofox.config.json`.

By default, storage state contains cookies and localStorage only. To also persist IndexedDB, set `"indexedDB": true` in the persistence plugin config. This captures all serializable IndexedDB records—not only authentication data—and may make snapshots significantly larger and checkpoints slower.

### Session Tracing

Capture a Playwright trace of every action in a session: page screenshots, DOM snapshots, network requests, and console output. Output is a single `.zip` file you can open in Playwright's built-in Trace Viewer.

Opt-in per session by passing `trace: true` when opening the first tab:

```bash
curl -X POST http://localhost:9377/tabs \
  -H 'Content-Type: application/json' \
  -d '{"userId":"agent1","sessionKey":"task1","url":"https://example.com","trace":true}'
```

The trace is written when the session closes. Close the session to flush it, then list, fetch, and view:

```bash
# Close the session to flush the trace


## configuration

Browser behavior can be tuned in `camofox.config.json`:

```json
{
  "newPageTimeoutMs": 10000
}
```

`newPageTimeoutMs` controls how long tab creation waits for Firefox to create a page. If the context is unresponsive, Camofox replaces only that user's context and retries once. The default is 10 seconds.

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `CAMOFOX_PORT` | Server port | `9377` |
| `PORT` | Server port (fallback, for platforms like Fly.io, Railway) | `9377` |
| `CAMOFOX_BIND_HOST` | Optional server bind host. Set to `127.0.0.1` for loopback-only access or `0.0.0.0` for IPv4 on all interfaces. When unset, Node uses its default all-interface binding. | - |
| `CAMOFOX_API_KEY` | Enable cookie import endpoint (disabled if unset) | - |
| `CAMOFOX_ADMIN_KEY` | Required for `POST /stop` | - |
| `CAMOFOX_ACCESS_KEY` | If set, all routes (except `/health`, cookie import, and `/stop`) require `Authorization: Bearer <key>`. Lets you safely expose the server beyond loopback. | - |
| `CAMOFOX_EVALUATE_MAX_BODY_SIZE` | Max JSON request body size for `POST /tabs/:tabId/evaluate`; other JSON routes remain limited to `100kb`. | `1mb` |
| `CAMOUFOX_EXECUTABLE` | External Camoufox executable to use instead of downloading/launching the bundled cache. Must point to a Camoufox bundle with sibling resources. | - |
| `CAMOUFOX_EXECUTABLE_PATH` | Compatibility alias for `CAMOUFOX_EXECUTABLE` | - |
| `CAMOFOX_EXECUTABLE_PATH` | Compatibility alias for `CAMOUFOX_EXECUTABLE` | - |
| `CAMOFOX_DISABLE_DEFAULT_ADDONS` | Set to `1`/`true` to skip downloading and launching the default uBlock Origin (UBO) addon. Useful for deployments where the addons.mozilla.org download is unreliable or unwanted (a failed download otherwise leaves a broken addon cache that blocks startup). | `0` |
| `CAMOFOX_COOKIES_DIR` | Directory for cookie files | `~/.camofox/cookies` |
| `CAMOFOX_UPLOADS_DIR` | Directory allowed for `POST /tabs/:tabId/upload` file attachments. Paths outside it, including symlink escapes, are rejected. | `~/.camofox/uploads` |
| `CAMOFOX_PROFILE_DIR` | Directory for persisted session profiles | `~/.camofox/profiles` |
| `CAMOFOX_TRACES_DIR` | Directory for session trace zips | `~/.camofox/traces` |
| `CAMOFOX_TRACES_MAX_BYTES` | Max size per trace, removed on next startup if exceeded | `52428800` (50MB) |
| `CAMOFOX_TRACES_TTL_HOURS` | Traces older than this are swept on startup | `24` |
| `MAX_SESSIONS` | Max concurrent browser sessions | `50` |
| `MAX_TABS_PER_SESSION` | Max tabs per session | `10` |
| `SESSION_TIMEOUT_MS` | Session inactivity timeout | `1800000` (30min) |
| `BROWSER_IDLE_TIMEOUT_MS` | Kill browser when idle (0 = never) | `300000` (5min) |
| `CAMOFOX_INTERACTIVE` | Interactive browser mode: `desktop` opens a real local Camoufox window; `off` keeps normal headless behavior | `off` |
| `HANDLER_TIMEOUT_MS` | Max time for any handler | `30000` (30s) |
| `MAX_CONCURRENT_PER_USER` | Concurrent request cap per user | `3` |
| `MAX_OLD_SPACE_SIZE` | Node.js V8 heap limit (MB) | `128` |
| `PROXY_STRATEGY` | Proxy mode: `backconnect` (rotating sticky sessions) or blank (single endpoint) | - |
| `PROXY_PROVIDER` | Provider name for session format (e.g. `decodo`) | `decodo` |
| `PROXY_HOST` | Proxy hostname or IP (simple mode) | - |
| `PROXY_PORT` | Proxy port (simple mode) | - |
| `PROXY_USERNAME` | Proxy auth username | - |
| `PROXY_PASSWORD` | Proxy auth password | - |
| `PROXY_BACKCONNECT_HOST` | Backconnect gateway hostname | - |
| `PROXY_BACKCONNECT_PORT` | Backconnect gateway port | `7000` |
| `PROXY_COUNTRY` | Target country for proxy geo-targeting | - |
| `PROXY_STATE` | Target state/region for proxy geo-targeting | - |
| `TAB_INACTIVITY_MS` | Close tabs idle longer than this | `300000` (5min) |
| `CAMOFOX_CRASH_REPORT_ENABLED` | Enable anonymized crash/hang telemetry (`false` to disable) | `true` |
| `CAMOFOX_CRASH_REPORT_URL` | Telemetry endpoint ([self-hosted endpoint](
