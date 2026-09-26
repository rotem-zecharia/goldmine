# alexta69/metube

Self-hosted video downloader for YouTube and other sites (web UI for yt-dlp)

## installation

```bash
docker run -d -p 8081:8081 -v /path/to/downloads:/downloads ghcr.io/alexta69/metube
```

Or with Docker Compose:

```yaml
services:
  metube:
    image: ghcr.io/alexta69/metube
    container_name: metube
    restart: unless-stopped
    ports:
      - "8081:8081"
    volumes:
      - /path/to/downloads:/downloads
```

Then open `http://<host>:8081` in your browser. Images are multi-arch (amd64/arm64), and also published on Docker Hub as `alexta69/metube`.

## configuration

MeTube is configured with environment variables: `-e NAME=value` on the `docker run` command line, or the `environment:` section in Compose. Defaults are the Docker image's; outside Docker, the directories default to the working directory.

### Runtime and permissions

| Variable | Default | Description |
| :--- | :--- | :--- |
| `PUID` / `PGID` | `1000` | User and group MeTube runs as and writes files with. Legacy `UID`/`GID` also work. |
| `UMASK` | `022` | Umask for the files MeTube creates. |
| `CHOWN_DIRS` | `true` | Make `PUID:PGID` the owner of the download, state and temp directories at startup. With `false`, MeTube's user must already have access. |
| `LOGLEVEL` | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` or `NONE`. |
| `ENABLE_ACCESSLOG` | `false` | Log every HTTP request. |
| `DEFAULT_THEME` | `auto` | UI theme: `light`, `dark`, or `auto` to follow the system. |

### Downloads

| Variable | Default | Description |
| :--- | :--- | :--- |
| `MAX_CONCURRENT_DOWNLOADS` | `3` | Downloads that run at once; the rest wait their turn. |
| `DEFAULT_OPTION_PLAYLIST_ITEM_LIMIT` | `0` | Default for the **Items Limit** field: how many entries of a playlist or channel to download (`0` = all). |
| `CLEAR_COMPLETED_AFTER` | `0` | Seconds before finished and failed downloads leave the Completed list (`0` = never). |
| `DELETE_FILE_ON_TRASHCAN` | `false` | Also delete the file from disk when its entry is removed from Completed. |
| `SUBSCRIPTION_DEFAULT_CHECK_INTERVAL` | `60` | Default minutes between checks of a [subscription](https://github.com/alexta69/metube/wiki/Subscriptions). |
| `SUBSCRIPTION_SCAN_PLAYLIST_END` | `50` | Newest entries fetched each time a subscription is checked. |
| `SUBSCRIPTION_MAX_SEEN_IDS` | `50000` | Video IDs remembered per subscription, to bound the state file's size. |

### Directories

| Variable | Default | Description |
| :--- | :--- | :--- |
| `DOWNLOAD_DIR` | `/downloads` | Where downloads are saved. |
| `AUDIO_DOWNLOAD_DIR` | same as `DOWNLOAD_DIR` | Where audio-only downloads are saved, to keep them apart from video. |
| `TEMP_DIR` | `/downloads` | Where files are written while downloading. An SSD or `tmpfs` is faster, but on a RAM disk interrupted downloads can't resume. |
| `STATE_DIR` | `/downloads/.metube` | Where MeTube keeps its queue, history, subscriptions and uploaded cookies. |
| `CUSTOM_DIRS` | `true` | Show a **Download Folder** field under Advanced Options, to save into a subfolder of the download directory. |
| `CREATE_CUSTOM_DIRS` | `true` | Let that field create folders that don't exist yet. |
| `CUSTOM_DIRS_EXCLUDE_REGEX` | `(^\|/)[.@].*$` | Folders left out of the field's suggestions; the default hides names starting with `.` or `@`. Empty hides none. |
| `DEFAULT_FOLDER` | | Folder the field starts with, relative to the download directory. Requires `CUSTOM_DIRS`. |
| `DOWNLOAD_DIRS_INDEXABLE` | `false` | Serve browsable listings of the download directories. |

### File naming

Templates use [yt-dlp's output template syntax](https://github.com/yt-dlp/yt-dlp/blob/master/README.md#output-template). How MeTube applies them is explained in [Output templates](https://github.com/alexta69/metube/wiki/Output-templates).

| Variable | Default | Description |
| :--- | :--- | :--- |
| `OUTPUT_TEMPLATE` | `%(title)s.%(ext)s` | Filename for downloads. |
| `OUTPUT_TEMPLATE_PLAYLIST` | `%(playlist_title)s/%(title)s.%(ext)s` | Filename for items added from a playlist. Empty means `OUTPUT_TEMPLATE`. |
| `OUTPUT_TEMPLATE_CHANNEL` | `%(channel)s/%(title)s.%(ext)s` | Filename for items added from a channel. Empty means `OUTPUT_TEMPLATE`. |
| `OUTPUT_TEMPLATE_CHAPTER` | `%(title)s - %(section_number)02d - %(section_title)s.%(ext)s` | Default filename for each chapter when **Split by chapters** is on. |

### yt-dlp

| Variable | Default | Description |
| :--- | :--- | :--- |
| `YTDL_OPTIONS` | `{}` | Options for every download, as a JSON object — see [yt-dlp options](#yt-dlp-options).
