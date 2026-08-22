# hyperfield/yt-channel-downloader

A Qt GUI app that makes it easy to selectively download multiple videos at once from Youtube and other platforms channels.

## features

- **Fetch & Replace / Fetch & Add**: Replace the current list or append newly fetched items to it.
- **Search Within Fetched Items**: Filter the current list by title with the built-in search field.
- **Fetch Video Listings**: Input a YouTube video, playlist, or channel URL and get a list of matching items.
- **Selective Download**: Choose exactly which videos you want to download, or select all at once.
- **Quality Control**: Specify video/audio quality or opt to download only the associated audio track.
- **Download Marking**: Keeps track of downloaded files for easier management.
- **Size & Time Estimates**: Preview total download size and ETA before starting, with cancelable calculations.
- **Large-List Handling**: Channels can be fetched in batches with `Fetch Next`, and playlists use configurable fetch limits to keep fetching responsive.
- **Thumbnail Previews & Downloads**: See thumbnails as soon as items are fetched, and save them with your downloads.
- **Playlist Downloads**: Download all or some videos from a playlist URL.
- **Channel Downloads**: Download all or some videos from a channel URL.
- **Single Video or Audio Downloads**: Paste any supported link (YouTube, Vimeo, Twitch, SoundCloud, Facebook, Instagram, Twitter/X, TikTok, Udemy*, Reddit, and more via yt-dlp) and download it. Bulk channel and playlist fetching remains YouTube-only.
- **Runtime Detection**: Get guided prompts if an optional JavaScript runtime for yt-dlp is missing.
- **Browser-Cookie Login for Restricted YouTube Content**: Reuse a signed-in browser profile for private, age-restricted, or premium YouTube content.

\*Some providers (for example, Udemy or other premium services) still require valid browser cookies or provider-specific credentials. The in-app browser-cookie login flow is primarily intended for restricted YouTube downloads.

### Coming Soon

- Download history tracking
- [Suggest a feature!](https://github.com/hyperfield/yt-channel-downloader/issues)

## installation

### Install from PyPI

The easiest way to get the desktop app is straight from PyPI. Make sure FFmpeg is installed (see below), then run:

```bash
pip install yt-channel-downloader
```

If you don't have `pip`, you can use `python -m pip` instead.

The package depends on `yt-dlp[default]`, so the Python install will also pull in yt-dlp's recommended companion components such as `yt-dlp-ejs`. You still need an external JavaScript runtime like Deno or Node.js installed separately on your system for the best YouTube support.

If `yt-dlp` is already present in your Python environment, upgrade it alongside the app. `pip install yt-channel-downloader` can otherwise keep an older `yt-dlp` that still satisfies the dependency floor but no longer works reliably against recent YouTube player changes.

To update the app to the latest version from PyPI:

```bash
pip install --upgrade yt-channel-downloader yt-dlp
yt-channel-downloader
```

### Install the .deb (Debian/Ubuntu)

1. Download the latest `.deb` from the releases page (or build one with `./scripts/create_binary.sh` then `./scripts/create_deb.sh`).
2. Install it with `apt` so dependencies are resolved:

```bash
sudo apt install ./yt-channel-downloader_<version>_<arch>.deb
```

3. Launch with:

```bash
yt-channel-downloader
```

### MacOS or Linux (from source)

`ffmpeg` is needed for the app to work correctly, so make sure you have it on your system. Check in your terminal emulator if `ffmpeg` is installed:

    ffmpeg -version

#### How to install `ffmpeg` on MacOS or Linux

You can download it from [FFmpeg's official site](https://ffmpeg.org/download.html) or install it from a repository according to your OS distribution.

On MacOS with [Homebew](https://brew.sh/):

    brew install ffmpeg

On Debian/Ubuntu:

    sudo apt update
    sudo apt install ffmpeg

On Fedora:

    sudo dnf install ffmpeg

On Arch Linux:

    sudo pacman -S ffmpeg

#### Recommended: JavaScript runtime (improves YouTube format coverage)

yt-dlp can use a JavaScript runtime to parse YouTube player code; having one installed reduces missing formats and silences runtime warnings. The Python dependency install includes yt-dlp's `default` extras, but it does not install an external runtime for you. Install any of:

- **Node.js** via your package manager:
  - Debian/Ubuntu: `sudo apt update && sudo apt install nodejs npm`
  - Fedora: `sudo dnf install nodejs npm`
  - Arch Linux: `sudo pacman -S nodejs npm`
  - macOS (Homebrew): `brew install node`
- **Deno** (alternative runtime): see install instructions at [deno.com](https://deno.com/)

#### Install YT Channel Downloader

##### Clone the repository

    git clone https://github.com/hyperfield/yt-channel-downloader.git

##### Navigate into the directory

    cd yt-channel-downloader

##### Create a virtual environment

    python3 -m venv .venv

##### Activate the virtual environment

For `bash`/`zsh`:

    source .venv/bin/activate

For `fish`:

    source .venv/bin/activate.fish

##### Install the project in editable mode

    pip install -e .

##### Run the program

    yt-channel-downloader

To deactivate the virtual environment after usage, type

    deactivate

### Windows

`ffmpeg` is needed for the app to work correctly, so make sure you have it on your system. Open the command line (`CMD`) and type

    ffmpeg -version

to check if it's on your system.

#### How to install `ffmpeg` on Windows

1. **Download `ffmpeg`**:
   - Visit the official [FFmpeg download page](https://ffmpeg.org/download.html).
   - Alternatively, you can use this direct link: [Download FFmpeg for Windows](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip).

2. **Extract the files**:
   - Extract the downloaded archive to a directory, such as `C:\ffmpeg`.

3. **Add `ffmpeg` to your system PATH**:
   - Open the Start menu and search for "Environment Variables".
   - Select "Edit the system environment variables".
   - In the "System Properties" window, click on the 
