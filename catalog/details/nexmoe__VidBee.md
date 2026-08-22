# nexmoe/VidBee

Download video and audio from YouTube , TikTok , Twitter , Instagram , Facebook , Twitch , Bilibili , and 1000+ sites—or import local media. Create searchable transcripts on your computer, then summar

## installation

VidBee is currently under active development, and feedback is welcome for any [issue](https://github.com/nexmoe/VidBee/issues) encountered.

[📥 Download VidBee](https://vidbee.org/download/) | [📚 Documentation](https://vidbee.org/docs/)

> [!IMPORTANT]
>
> **Star Us**, You will receive all release notifications from GitHub without any delay ~

If VidBee is useful to you, sharing it is one of the best ways to support the project.

> [!IMPORTANT]
>
> When you post about VidBee on **X** or **Threads**, please mention **@nexmoe** so I can see it and help amplify it:
> - X: [@nexmoe](https://x.com/nexmoe)
> - Threads: [@nexmoe](https://www.threads.com/@nexmoe)

## configuration

Subscribe to RSS feeds and let VidBee check for new items and add them to your download queue. Each subscription can use its own rules, so regular releases do not need the same manual setup every time.

- Turn automatic downloads on or keep new items ready for manual review.
- Filter feed items by keywords, add automatic tags, and download only the latest item when you do not want the backlog.
- Choose a custom directory and filename template for each subscription.
- See whether each feed item is queued, downloading, completed, failed, or still waiting.

![VidBee RSS subscriptions and queued feed items](screenshots/rss-framed.webp)

## tools

This monorepo now includes:

- `packages/downloader-core`: Shared yt-dlp/ffmpeg download core
- `apps/api`: Fastify API server with oRPC and SSE events
- `apps/web`: TanStack Start web client using oRPC

Run locally:

```bash
pnpm run start:web
```

This command starts `apps/api` and `apps/web` together.

Run with Docker:

```bash
docker compose up -d --build
```

Run with GitHub Container Registry images:

```yaml
services:
  api:
    image: ghcr.io/nexmoe/vidbee-api:latest
    environment:
      VIDBEE_API_HOST: 0.0.0.0
      VIDBEE_API_PORT: 3100
      VIDBEE_DOWNLOAD_DIR: /data/downloads
      VIDBEE_HISTORY_STORE_PATH: /data/vidbee/vidbee.db
    ports:
      - "3100:3100"
    volumes:
      # Replace the named volume with /path/on/your/NAS:/data/downloads
      # when downloaded files must be directly visible on the host.
      - vidbee-downloads:/data/downloads
      - vidbee-data:/data/vidbee
    restart: unless-stopped

  web:
    image: ghcr.io/nexmoe/vidbee-web:latest
    depends_on:
      - api
    ports:
      - "3000:3000"
    restart: unless-stopped

volumes:
  vidbee-downloads:
  vidbee-data:
```

Stop services:

```bash
docker compose down
```

Optional env vars (via `.env`):

```bash
VIDBEE_API_PORT=3100
VIDBEE_WEB_PORT=3000
