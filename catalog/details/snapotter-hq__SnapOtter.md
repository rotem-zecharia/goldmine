# snapotter-hq/SnapOtter

Open-source, self-hosted file-processing tool. Convert, compress, OCR, transcribe & run local AI across image, video, audio, PDF & documents, via UI, REST API & pipelines. Your files never leave your 

## installation

One command, that's it.

```bash
docker run -d --name SnapOtter -p 1349:1349 -v SnapOtter-data:/data snapotter/snapotter:latest
```

Open [http://localhost:1349](http://localhost:1349) and log in with `admin` / `admin`. That's the whole install.

For the production Compose stack, NVIDIA GPU acceleration, and configuration, see [Deployment](#deployment) below.

## features

- **200+ tools across 5 modalities:**
  - **Image (107):** resize, crop, compress, convert, watermark, color adjust, beautify screenshots, generate memes, vectorize, GIF tools, find duplicates, passport photos, plus dedicated format converters (JPG to PNG, HEIC to JPG, WebP to PNG, image to PDF, and more). Supports 55+ input formats (including 23 camera RAW formats) and 17 output formats
  - **Video (57):** convert, compress, trim, resize, crop, merge, video-to-GIF, extract audio, stabilize, change FPS, burn/extract subtitles, plus dedicated converters (MOV to MP4, MKV to MP4, MP4 to MP3, and more)
  - **Audio (27):** convert, trim, normalize, volume, fade, pitch shift, silence removal, noise reduction, merge/split, waveform, plus dedicated converters (M4A to MP3, AAC to MP3, OGG to WAV, and more)
  - **PDF (29):** merge, split, compress, convert, protect/unlock, redact, sign, watermark, page numbers, OCR, plus PDF to JPG/PNG/TIFF
  - **Files (23):** CSV/JSON/XML/YAML conversion, CSV merge/split, Excel to CSV, chart maker, ZIP create/extract
- **Image editor:** Free layer-based editor with brushes, shapes, adjustments, filters, curves, and keyboard shortcuts. Runs in your browser and processes on your hardware
- **Local AI:** Remove backgrounds, upscale images, restore and colorize old photos, erase objects, blur faces, enhance faces, extract text (OCR from images and PDFs), transcribe audio, auto-generate video subtitles, expand canvas, and fix transparency. All on your hardware, no internet required. Built-in Fast OCR adds about 25 MiB to the official image; the optional accuracy pack installs on demand
- **OIDC / SSO:** Login with Google, GitHub, Okta, or any OpenID Connect provider
- **21 languages:** English, Arabic, Chinese (Simplified & Traditional), Dutch, French, German, Hindi, Indonesian, Italian, Japanese, Korean, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian, Vietnamese. RTL support for Arabic
- **Pipelines:** Chain tools into reusable workflows, 20 steps by default (`MAX_PIPELINE_STEPS`). Import/export as JSON. Batch size is unlimited in the published image and 100 from a source build (`MAX_BATCH_SIZE`)
- **REST API:** Every tool available via API with API key auth. Interactive docs at `/api/docs`
- **Self-hosted:** one `docker run` for a single-container quick start (embedded Postgres 17 + Redis 8), or the same Postgres 17 + Redis 8 as a Compose stack for production. No external SaaS dependencies
- **Multi-arch:** Runs on AMD64 and ARM64 (Intel, Apple Silicon, Raspberry Pi)
- **Privacy first:** Your files never leave your network. Basic analytics help us catch bugs and improve tools. Disable them at build time with `SNAPOTTER_ANALYTICS=off` or at runtime with the in-app admin opt-out ([Here's how to do it](https://docs.snapotter.com/guide/deployment.html#analytics))

## Deployment

The [Quick Start](#quick-start) one-liner above is all most people need. For production, run the 3-container Compose stack (app + Postgres 17 + Redis 8). Save this as `compose.yaml`:

```yaml
services:
  snapotter:
    image: snapotter/snapotter:latest
    ports: ["1349:1349"]
    environment:
      DATABASE_URL: postgres://snapotter:snapotter@postgres:5432/snapotter
      REDIS_URL: redis://redis:6379
    volumes:
      - SnapOtter-data:/data
    depends_on: [postgres, redis]
    restart: unless-stopped
  postgres:
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: snapotter
      # Change this for any non-local deployment.
      POSTGRES_PASSWORD: snapotter
      POSTGRES_DB: snapotter
    volumes: ["SnapOtter-pgdata:/var/lib/postgresql/data"]
    restart: unless-stopped
  redis:
    image: redis:8-alpine
    volumes: ["SnapOtter-redisdata:/data"]
    restart: unless-stopped
volumes:
  SnapOtter-data:
  SnapOtter-pgdata:
  SnapOtter-redisdata:
```

Then start the stack:

```bash
docker compose up -d
```

<details>
<summary><sub>Have an NVIDIA GPU? Click here for CUDA acceleration.</sub></sum
