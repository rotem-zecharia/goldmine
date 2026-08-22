# mediago-dev/mediago

Cross-platform video downloader — sniff and grab m3u8/HLS streams, Bilibili, YouTube and more. Desktop + Docker + 🦞.

## tools

MediaGo exposes a full HTTP API — scripts, automation tools and other
apps can create download tasks, query progress and manage the list
directly. The browser extension uses this same API to talk to the desktop
app; anyone else can tap in too.

### 🎞️ Built-in format conversion

After a download finishes, convert it to another format or quality
without leaving MediaGo. No more opening a separate tool for ffmpeg.

### 🐳 One-line Docker deployment

Headless install on your server, then access the web UI from anywhere on
the same network:

```shell
docker run -d --name mediago -p 8899:8899 -v /path/to/mediago:/app/mediago caorushizi/mediago:3.5.0
```

Available on [Docker Hub](https://hub.docker.com/r/caorushizi/mediago) and GHCR (`ghcr.io/caorushizi/mediago`) — same image, pick whichever registry is faster for you. Supports both Intel / AMD (amd64) and ARM (arm64). On the desktop build,
MediaGo listens on both `127.0.0.1` and your LAN IP out of the box, so
phones and tablets on the same Wi-Fi can open the web UI too.

## 📷 Screenshots

![Home](./images/home_en.png)

![Home — dark mode](./images/home-dark_en.png)

![Settings](./images/settings_en.png)

![Resource extraction](./images/browser_en.png)

## 📥 Download

### v3.5.0 (stable)

- [Windows — installer](https://github.com/caorushizi/mediago/releases/download/v3.5.0/mediago-community-setup-win32-x64-3.5.0.exe)
- [Windows — portable](https://github.com/caorushizi/mediago/releases/download/v3.5.0/mediago-community-portable-win32-x64-3.5.0.exe)
- [macOS — Apple Silicon (arm64)](https://github.com/caorushizi/mediago/releases/download/v3.5.0/mediago-community-setup-darwin-arm64-3.5.0.dmg)
- [macOS — Intel (x64)](https://github.com/caorushizi/mediago/releases/download/v3.5.0/mediago-community-setup-darwin-x64-3.5.0.dmg)
- [Linux (deb)](https://github.com/caorushizi/mediago/releases/download/v3.5.0/mediago-community-setup-linux-amd64-3.5.0.deb)
- [**Docker Hub**](https://hub.docker.com/r/caorushizi/mediago): `docker run -d --name mediago -p 8899:8899 -v /path/to/mediago:/app/mediago caorushizi/mediago:3.5.0`
- **GHCR**: `docker run -d --name mediago -p 8899:8899 -v /path/to/mediago:/app/mediago ghcr.io/caorushizi/mediago:3.5.0`

Browsing older releases? See the [GitHub Releases page](https://github.com/caorushizi/mediago/releases).

### 🪄 One-click Docker deployment via BT Panel

1. Install [BT Panel](https://www.bt.cn/new/download.html?r=dk_mediago) using the official script.
2. Log in to the panel, click **Docker** in the sidebar and finish the
   Docker service setup (just follow the prompts).
3. Find **MediaGo** in the app store, click **Install**, configure your
   domain, and you're done.

## 📝 What's new in v3.5.0

- **🌐 Browser extension** — sniff videos on any site, send to MediaGo
  in one click
- **🎬 YouTube + 1000+ sites** — powered by yt-dlp
- **🦞 OpenClaw Skill** — download videos via AI coding assistants
- **🔌 HTTP API** — integrate with scripts, automation and third-party tools
- **🎞️ In-app format conversion** — choose output format and quality
- **🐳 Simpler Docker deployment** — mount a single folder, multi-arch images on GHCR
- **⚡ Faster startup** — backend rewrite, lower memory footprint, built-in video player

## 🧑‍💻 Development from source

Repository workflows use [Task](https://taskfile.dev/) v3.51.1. Install the
fixed version on macOS, Linux, or Windows (PowerShell) with a Go toolchain,
make sure the Go binary directory is on `PATH`, and verify it before running
repository commands:

```shell
go install github.com/go-task/task/v3/cmd/task@v3.51.1
task --version
```

From the repository root, the primary clone-and-start flow is:

```shell
git clone https://github.com/caorushizi/mediago.git
cd mediago
task setup
task dev:all
```

`task setup` installs the Node workspace and the runtime tools needed by the
application. Their only version source is `scripts/deps-versions.json`; Task
does not automatically upgrade them. Running `pnpm install` alone installs
onl
