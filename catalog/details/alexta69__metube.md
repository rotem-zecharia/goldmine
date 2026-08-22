# alexta69/metube

Self-hosted video downloader for YouTube and other sites (web UI for yt-dlp)

## configuration

Certain values can be set via environment variables, using the `-e` parameter on the docker command line, or the `environment:` section in Docker Compose.

### 🏠 Runtime & Permissions

* __PUID__: User under which MeTube will run. Defaults to `1000` (legacy `UID` also supported).
* __PGID__: Group under which MeTube will run. Defaults to `1000` (legacy `GID` also supported).
* __UMASK__: Umask value used by MeTube. Defaults to `022`.
* __DEFAULT_THEME__: Default theme to use for the UI, can be set to `light`, `dark`, or `auto`. Defaults to `auto`.
* __LOGLEVEL__: Log level, can be set to `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`, or `NONE`. Defaults to `INFO`.
* __ENABLE_ACCESSLOG__: Whether to enable access log. Defaults to `false`.

### ⬇️ Download Behavior

* __MAX_CONCURRENT_DOWNLOADS__: Maximum number of simultaneous downloads allowed. For example, if set to `5`, then at most five downloads will run concurrently, and any additional downloads will wait until one of the active downloads completes. Defaults to `3`.
* __DELETE_FILE_ON_TRASHCAN__: if `true`, downloaded files are deleted on the server, when they are trashed from the "Completed" section of the UI. Defaults to `false`.
* __DEFAULT_OPTION_PLAYLIST_ITEM_LIMIT__: Maximum number of playlist items that can be downloaded. Defaults to `0` (no limit).
* __SUBSCRIPTION_DEFAULT_CHECK_INTERVAL__: Default minutes between automatic checks for each subscription. Defaults to `60`.
* __SUBSCRIPTION_SCAN_PLAYLIST_END__: Maximum playlist/channel entries to fetch per subscription check (newest-first). Defaults to `50`.
* __SUBSCRIPTION_MAX_SEEN_IDS__: Cap on stored video IDs per subscription to limit state file growth. Defaults to `50000`.
* __CLEAR_COMPLETED_AFTER__: Number of seconds after which completed (and failed) downloads are automatically removed from the "Completed" list. Defaults to `0` (disabled).

### 📁 Storage & Directories

* __DOWNLOAD_DIR__: Path to where the downloads will be saved. Defaults to `/downloads` in the Docker image, and `.` otherwise.
* __AUDIO_DOWNLOAD_DIR__: Path to where audio-only downloads will be saved, if you wish to separate them from the video downloads. Defaults to the value of `DOWNLOAD_DIR`.
* __CUSTOM_DIRS__: Whether to enable downloading videos into custom directories within the __DOWNLOAD_DIR__ (or __AUDIO_DOWNLOAD_DIR__). When enabled, a **Download Folder** field appears under **Advanced Options**, where the directory for each download can be specified. Defaults to `true`.
* __CREATE_CUSTOM_DIRS__: Whether to support automatically creating directories within the __DOWNLOAD_DIR__ (or __AUDIO_DOWNLOAD_DIR__) if they do not exist. When enabled, the download directory selector supports free-text input, and the specified directory will be created recursively. Defaults to `true`.
* __CUSTOM_DIRS_EXCLUDE_REGEX__: Regular expression to exclude some custom directories from the folder field's suggestions. Empty regex disables exclusion. Defaults to `(^|/)[.@].*$`, which means directories starting with `.` or `@`.
* __DEFAULT_FOLDER__: Custom directory to pre-select in the download folder field, relative to __DOWNLOAD_DIR__ (or __AUDIO_DOWNLOAD_DIR__), for when most downloads go to the same place. It is only a starting value — the field stays editable, so any other folder can still be picked per download. Requires __CUSTOM_DIRS__; ignored with a warning otherwise. Defaults to empty, i.e. the base download directory.
* __DOWNLOAD_DIRS_INDEXABLE__: If `true`, the download directories (__DOWNLOAD_DIR__ and __AUDIO_DOWNLOAD_DIR__) are indexable on the web server. Defaults to `false`.
* __STATE_DIR__: Path to where MeTube will store its persistent state files (`queue.json`, `pending.json`, `completed.json`, `subscriptions.json`). Defaults to `/downloads/.metube` in the Docker image, and `.` otherwise.
* __TEMP_DIR__: Path where intermediary download files will be saved. Defaults to `/downloads` in the Docker image, and `.` otherwise.
  * Set this

## features

MeTube development relies on community contributions. If you need additional features, please submit a PR. Create an issue first to discuss the implementation before writing code — MeTube's scope is deliberately narrow: it downloads well and stops once the file is written. Features that improve the download itself are welcome; post-download file management (tag editing, metadata lookups, library organization) is out of scope regardless of implementation quality — see [AGENTS.md](AGENTS.md) for the full policy. Feature requests without an accompanying PR are unlikely to be fulfilled.

## 🛠️ Building and running locally

Make sure you have Node.js 22+ and Python 3.13 installed.

```bash

## installation

cd ui
curl -fsSL https://get.pnpm.io/install.sh | sh -
pnpm install
pnpm run build
# install python dependencies
cd ..
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
# run
uv run python3 app/main.py
```

A Docker image can be built locally (it will build the UI too):

```bash
docker build -t metube .
```

Note that if you're running the server in VSCode, your downloads will go to your user's Downloads folder (this is configured via the environment in `.vscode/launch.json`).
