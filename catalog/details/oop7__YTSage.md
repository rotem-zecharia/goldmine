# oop7/YTSage

Modern YouTube downloader with a clean PySide6 interface. Download videos in any quality, extract audio, fetch subtitles, sponsorBlock, and view video metadata. Built with yt-dlp for reliable performa

## features

YTSage is designed for users who want a **simple yet powerful YouTube downloader**. Unlike other tools, it offers:

- A modern and clean PySide6 interface
- One-click downloads for video, audio, and subtitles
- Advanced features like SponsorBlock, subtitle merging, and playlist selection
- Optional Generic Mode for sites supported by yt-dlp beyond YouTube
- Cross-platform support and easy installation

<a id="features"></a>

## installation

Install YTSage via PyPI:

```bash
pip install ytsage
```

<details>
<summary>🔄 Update existing installation</summary>

```bash
pip install --upgrade ytsage
```

</details>

Then launch the application:

```bash
ytsage
```

You can also open YTSage with a video or playlist URL prefilled and analyzed immediately:

```bash
ytsage "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

## tools

<details>
<summary>🎯 Basic Usage</summary>

1. **Launch YTSage**
2. **Paste YouTube URL** (or use "Paste URL" button)
3. **Click "Analyze"**
4. **Select Format:**
   - `Video` for video downloads
   - `Audio Only` for audio extraction
5. **Choose Options:**
   - Enable Subtitles and select language
   - Enable Subtitle Merging
   - Save Thumbnail
   - Remove Sponsored Segments
   - Save Description
   - Embed Chapters
6. **Select Output Directory**
7. **Click "Download"**

> 💡 Default download directory is the user's "Downloads" folder.

</details>

<details>
<summary>📋 Playlist Download</summary>

1. **Paste Playlist URL**
2. **Click "Analyze"**
3. **Select videos from the playlist selector (optional, defaults to all)**
4. **Choose desired format/quality**
5. **Click "Download"**

> 💡 The application automatically handles the download queue, and you can export playlist entries as `.txt`, `.csv`, `.m3u`, or `.json`.

</details>

<details>
<summary>🌍 Generic Mode for Non-YouTube Sites</summary>

Use Generic Mode when you want YTSage to accept URLs from sites supported by yt-dlp, such as Dailymotion, CBC Gem, TikTok, and others.

How to use it:

1. Open `Download Settings`.
2. Toggle on `Generic Mode`.
3. Paste a supported video or playlist URL that is not from YouTube.
4. Click `Analyze`.
5. Choose a format and download as usual.

Notes:

- Generic mode only changes the URL validation inside YTSage. The target site must still be supported by your installed version of yt-dlp.
- Some sites require cookies, login sessions, proxy, or extra yt-dlp arguments depending on the extractor.
- If a site fails, update yt-dlp from the built-in updater tab first before reporting an issue.

</details>

<details>
<summary>🧰 Media & Download Options</summary>

- **Subtitle Options:** Filter languages and embed subtitles into the video file.
- **Subtitle Merging:** Merge subtitles into the video file for hardcoded/burned-in subtitles.
- **Save Description:** Save the video description as a text file.
- **Save Thumbnail:** Save the video thumbnail as an image file.
- **Embed Chapters:** Embed chapter markers as metadata for compatible video players.
- **Remove Sponsored Segments:** Remove sponsored segments from the video using SponsorBlock.
- **Trim Video:** Download only specific parts of a video by specifying time ranges in `HH:MM:SS` format.

</details>

<details>
<summary>⚙️ Output & File Settings</summary>

- **Speed Limiter:** Limit download speed, e.g., `500K` for 500 KB/s.
- **Save Download Path:** Saves the default download path for future downloads. Available in **Download Settings → Download Path**.
- **Default Video Resolution:** Set your preferred default video resolution for auto-selection (e.g., 1080p, 720p). Available in **Download Settings → Default Video Resolution**.
- **Default Subtitle Languages:** Set default subtitle languages for auto-selection (comma-separated, e.g., `en,es`). Available in **Download Settings → Default Subtitle Languages**.
- **Output Filename Format:** Customize the output filename format using variables like `%(title)s`, `%(uploader)s`, `%(playlist_index)s`, and `%(resolution)s`. Available in **Download Settings → Filename Format**.
- **Force Output Format:** Force video downloads into a specific container format like `mp4`, `webm`, or `mkv`. Available in **Download Settings → Output Format Settings**.
- **Audio Format Conversion:** Convert audio-only downloads into preferred formats such as `AAC`, `MP3`, `FLAC`, `WAV`, `Opus`, `M4A`, `Vorbis`, or `Best`. Available in **Download Settings → Audio Format Settings**.
- **Audio Normalization:** Standardize volume for audio-only downloads using EBU R128.
- **Concurrent Connections:** Dramatically increase download speed by downloading files in multiple fragments simultaneously. Available in **Download Settings → General → Concurrent Connections** (Default is 1, maximum recommended is 8-10 to avoid IP throttling).

</details>

<details>
<summary>🌐 Access & Ne
