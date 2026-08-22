# AeternaLabsHQ/pullmd

Self-hosted URL- and file-to-Markdown service for humans and AI agents - web pages, documents, images, audio, YouTube. PWA + REST + MCP + Claude Code skill, Reddit-aware, refreshable share links.

## installation

Pre-built multi-arch images (`linux/amd64`, `linux/arm64`) live on Docker
Hub. Drop the compose file somewhere and run:

```bash
mkdir pullmd && cd pullmd
curl -O https://raw.githubusercontent.com/AeternaLabsHQ/pullmd/main/docker-compose.yml
docker compose up -d
# → http://localhost:3000
```

That's it. No `.env` needed: every variable has a sensible default
and PullMD listens on port `3000`. Add a `.env` next to the compose
file to override anything (see [Configuration](#configuration)).

## configuration

```yaml
services:
  pullmd:
    image: aeternalabshq/pullmd:latest
    container_name: pullmd
    restart: unless-stopped
    ports:
      - "${PORT:-3000}:3000"
    environment:
      - PUBLIC_URL=${PUBLIC_URL:-http://localhost:${PORT:-3000}}
      - TRAFILATURA_URL=http://trafilatura:8001/extract
      - PLAYWRIGHT_URL=http://playwright:8002/render
      - MARKITDOWN_URL=http://markitdown:8003/convert
      - CACHE_DB=/data/cache.db
    volumes:
      - ./data:/data
    networks:
      - pullmd-internal
    depends_on:
      - trafilatura
      - playwright
      - markitdown

  trafilatura:
    image: aeternalabshq/pullmd-trafilatura:latest
    container_name: pullmd-trafilatura
    restart: unless-stopped
    networks:
      - pullmd-internal

  playwright:
    image: aeternalabshq/pullmd-playwright:latest
    container_name: pullmd-playwright
    restart: unless-stopped
    networks:
      - pullmd-internal

  markitdown:
    image: aeternalabshq/pullmd-markitdown:latest
    container_name: pullmd-markitdown
    restart: unless-stopped
    mem_limit: ${MARKITDOWN_MEM_LIMIT:-1g}
    networks:
      - pullmd-internal

networks:
  pullmd-internal:
    driver: bridge
```

> **Abridged for readability** — the [`docker-compose.yml` in the repo](./docker-compose.yml)
> additionally passes every optional `.env` variable through to the
> containers (Reddit credentials, auth, media/OCR keys, YouTube options,
> output shaping). Use the `curl -O` command above rather than copying
> this block, or `.env` overrides beyond the basics won't reach the
> containers.

> **Note:** the Playwright sidecar adds **~3.7 GB** to your image cache
> (Chromium + Firefox + WebKit binaries from the official Playwright
> base image). It's optional — leave `PLAYWRIGHT_URL` unset and the
> `playwright` service block off, and PullMD silently degrades to
> static extraction with a fallback note in the metadata.

> **Note:** the MarkItDown sidecar is optional. Leave `MARKITDOWN_URL` unset
> and remove the `markitdown` service block to disable document conversion.
> Web-page URLs always work without it.

> **Mirror on GHCR:** `ghcr.io/aeternalabshq/{pullmd,pullmd-trafilatura,pullmd-playwright,pullmd-markitdown}`.
> Replace the `image:` lines if you prefer GitHub's registry.

### Behind Traefik

For deployments behind Traefik with TLS, use `docker-compose.traefik.yml`
instead. Same images, but with Traefik labels and the `proxy` external
network. Set `HOST_DOMAIN` in `.env`:

```bash
curl -O https://raw.githubusercontent.com/AeternaLabsHQ/pullmd/main/docker-compose.traefik.yml
echo "HOST_DOMAIN=pullmd.example.com" > .env
docker compose -f docker-compose.traefik.yml up -d
```

### Local development (no Docker)

```bash
git clone https://github.com/AeternaLabsHQ/pullmd.git
cd pullmd
npm install
npm start             # http://localhost:3000
npm test              # node --test
```

---

## Configuration

All variables go in `.env` (copy from `.env.example`):

> **v3.0.0 output format change:** the markdown body is clean by default - just `# Title` followed by content. The source URL, fetch date, and all extraction metadata remain in the YAML frontmatter unchanged - the body no longer duplicates them. Set `PULLMD_SOURCE_HEADER=true` to restore the old inline header. Use `PULLMD_FRONTMATTER_FIELDS` to pick which frontmatter fields are emitted (handy for trimming tokens in agent pipelines).

| Variable               | Required | Purpose                                                                                              |
| ---------------------- | -------- | ---------------------------------------------------------------------------------------------------- |
| `HOST_DOMAIN`          | Traefik variant only | Public hostname without scheme. Used by Traefik routing and as fallback for `PUBLIC_URL`. Unused by the default compose. |
| `PUBLIC_URL`           | no       | Full public origin embedded in `/help` and the skill zip. Defaults to `https://${HOST_DOMAIN}

## tools

| Endpoint               | Returns                                                                          |
| ---------------------- | -------------------------------------------------------------------------------- |
| `GET /api?url=…`       | Markdown (or JSON / plain text via `format=`). Also handles direct links to documents (PDF, Office, EPUB, …) when the markitdown sidecar is configured. |
| `GET /api/stream?url=…`| Server-Sent Events stream of extraction-stage status, ending in a `result` event. Used by the PWA. |
| `POST /api/html`       | Convert a local/raw HTML document (body = HTML, max 10 MB). Never cached — no history entry, no share link. |
| `POST /api/file`       | Convert an uploaded document (raw file bytes in body; set `Content-Type` to the file's MIME type; filename via `X-Filename` header or `?filename=`; max 25 MB). Returns Markdown. Requires the markitdown sidecar (`MARKITDOWN_URL`) for document types (PDF, Office, EPUB, ...); image and audio uploads instead use the `PULLMD_VISION_*` / `PULLMD_STT_*` tier (no markitdown container needed). |
| `GET /s/:id`           | Cached Markdown by share id; refreshes from source if > 1 h old.                 |
| `GET /api/history`     | Recent conversions (JSON).                                                       |
| `GET /api/archive`     | Paginated full archive.                                                          |
| `GET /api/storage`     | Cache size / hit-rate stats.                                                     |
| `GET /api/stats`       | Extraction telemetry (sources, quality, latency). `?window=-7 days`.             |
| `GET /api/config`      | Which optional tiers this instance has enabled (auth mode, markitdown, vision, STT, PDF OCR, YouTube). The PWA reads it to show or hide controls. |
| `GET /api/recipes/status` | Which [site recipes](#site-recipes) loaded, which were rejected, and any frontmatter fields dropped by the allowlist. |
| `POST /mcp`            | Streamable-HTTP MCP endpoint (3 tools: `read_url`, `get_share`, `list_recent`). |
| `GET /pullmd.zip`      | Claude Code skill bundle, with this instance's URL baked in (`/web-reader.zip` redirects here). |
| `GET /help`            | Bilingual user/agent setup guide.                                                |

### `/api` parameters

| Param           | Default | Notes                                                                              |
| --------------- | ------- | ---------------------------------------------------------------------------------- |
| `url`           | —       | Required.                                                                          |
| `comments`      | `true`  | Include Reddit / Hacker News comments. Ignored for other URLs.                     |
| `comment_depth` | `3`     | Max nesting depth (1–10). Applies to Reddit and Hacker News.                       |
| `comment_limit` | none    | Max top-level comments (uncapped by default).                                      |
| `frontmatter`   | `false` | Prepend YAML metadata.                                                             |
| `format`        | `md`    | `text` strips Markdown; `json` returns structured response.                        |
| `nocache`       | `false` | Bypass the 1-hour cache.                                                           |
| `render`        | auto    | `force` → always render via Playwright. `skip` → never render. Bypasses cache.     |
| `extractor`     | auto    | Force `readability` / `trafilatura` / `playwright` and skip the quality pick. Bypasses cache. |
| `pdf`           | —       | `ocr` → route PDFs through the [OCR tier](#high-quality-pdf-ocr). Bypasses cache.  |
| `yt_timecodes` / `yt_chunk` | see [YouTube](#youtube-transcripts) | Transcript format overrides. Bypass cache when set. |
| `lang`          | `de`    | Comments-section header language (`de` or `en`).                                   |
| `query`         | —       | Set this when 
