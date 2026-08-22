# alexta69/metube

Self-hosted video downloader for YouTube and other sites (web UI for yt-dlp)

## configuration

Certain values can be set via environment variables, using the `-e` parameter on the docker command line, or the `environment:` section in Docker Compose.

## features

MeTube development relies on community contributions. If you need additional features, please submit a PR. Create an issue first to discuss the implementation before writing code — MeTube's scope is deliberately narrow: it downloads well and stops once the file is written. Features that improve the download itself are welcome; post-download file management (tag editing, metadata lookups, library organization) is out of scope regardless of implementation quality — see [AGENTS.md](AGENTS.md) for the full policy. Feature requests without an accompanying PR are unlikely to be fulfilled.

## installation

cd ui
curl -fsSL https://get.pnpm.io/install.sh | sh -
pnpm install
pnpm run build
