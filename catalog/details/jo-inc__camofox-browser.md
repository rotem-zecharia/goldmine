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

railway link
railway up
```

Set secrets via the Railway dashboard or CLI:
```bash
railway variables set CAMOFOX_API_KEY="your-generated-key"
```

## configuration

Browser behavior can be tuned in `camofox.config.json`:

```json
{
  "newPageTimeoutMs": 10000

## tools

Two subprocesses may be spawned: (1) the Camoufox browser engine (core functionality, `lib/launcher.js`), (2) yt-dlp for YouTube transcript extraction (optional, `plugins/youtube/youtube.js`). Both are isolated in dedicated files separate from route handlers.
