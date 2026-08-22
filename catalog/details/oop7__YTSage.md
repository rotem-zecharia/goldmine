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
## ✨ Features

<div align="center">

| Core Features | Advanced Features | Extra Features |
|-----------------------------------|-----------------------------------------|------------------------------------|
| 🎥 Format Table | 🚫 SponsorBlock Integration | 🎞️ FPS/HDR Display |
| 🎵 Audio Extraction | 📝 Subtitle Selection & Merging | 🔄 Auto Update yt-dlp |
| ✨ Simple UI | 💾 Save Description & Thumbnail | 🛠️ FFmpeg/yt-dlp/Deno Detection |
| 📋 Playlist Support & Selector | 🚀 Speed Limiter | ⚙️ Custom Commands |
| 📑 Chapter Integration | ✂️ Video Section Trimming | 🍪 Login with Cookies |
| 📜 Download History | 🔄 Version Channel Selection | 🌐 Proxy Support |
| 🎚️ Audio Format Conversion | 🎬 Video Format Settings | 🆙 Built-in Updater Tab |
| 🌍 Generic Mode | 🔊 Audio Normalization (EBU R128) | 🌍 Localized in 16 Languages |
| 💾 Playlist Export | ⚙️ Default Quality & Subtitles | |
</div>

<a id="installation"></a>

## installation

### ⚡ Quick Install (Recommended)

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

### 📦 Pre-built Executables

> [👉 Download Latest Release](https://github.com/oop7/YTSage/releases/latest)

#### 🪟 Windows

| Format | Description |
|--------|-------------|
| ![Windows EXE](https://img.shields.io/badge/Windows-EXE-0078D6?style=for-the-badge&logo=windows&logoColor=white) | Standard Installer |
| ![Windows FFmpeg](https://img.shields.io/badge/Windows-FFmpeg-0078D6?style=for-the-badge&logo=windows&logoColor=white) | With FFmpeg Included |
| ![Windows Portable](https://img.shields.io/badge/Windows-Portable-0078D6?style=for-the-badge&logo=windows&logoColor=white) | Portable version, no installation needed |
| ![Windows Portable FFmpeg](https://img.shields.io/badge/Windows-Portable%20FFmpeg-0078D6?style=for-the-badge&logo=windows&logoColor=white) | Portable with FFmpeg, zipped |

<details>
<summary>🛠️ Installation Steps</summary>

1. **EXE Installer (`.exe`)**: Double-click the file and follow the setup wizard.
2. **Portable Version (`.zip`)**: Extract the archive to your desired location and launch `ytsage.exe`.
3. **FFmpeg Included**: Choose versions with FFmpeg included if you don't have FFmpeg installed on your system.
</details>

#### 🐧 Linux

| Format | Description |
|--------|-------------|
| ![Linux DEB](https://img.shields.io/badge/Linux-DEB-FCC624?style=for-the-badge&logo=linux&logoColor=black) | Debian Package |
| ![Linux AppImage](https://img.shields.io/badge/Linux-AppImage-FCC624?style=for-the-badge&logo=linux&logoColor=black) | AppImage, Portable |
| ![Linux RPM](https://img.shields.io/badge/Linux-RPM-FCC624?style=for-the-badge&logo=linux&logoColor=black) | RPM Package |
| ![Flathub](https://img.shields.io/badge/Linux-Flatpak-FCC624?style=for-the-badge&logo=flathub&logoColor=black) | Flatpak Bundle |

<details>
<summary>🛠️ Installation Steps</summary>

- **DEB (`.deb`)**:
  ```bash
  sudo dpkg -i ytsage_*.deb
  sudo apt-get install -f # Fix missing dependencies if needed
  ```
- **RPM (`.rpm`)**:
  ```bash
  sudo rpm -i ytsage-*.rpm
  ```
- **AppImage (`.AppImage`)**:
  ```bash
  chmod +x YTSage-*.AppImage
  ./YTSage-*.AppImage
  ```
- **Flatpak**: Follow instructions on Flathub or run:
  ```bash
  flatpak install flathub io.github.oop7.ytsage
  ```
</details>

#### 🍎 macOS

| Format | Description |
|--------|-------------|
| ![macOS ARM64 APP](https://img.shields.io/badge/macOS-ARM64%20APP-000000?style=for-the-badge&logo=apple&logoColor=white) | Zipped Application for Apple Silicon |
| ![macOS ARM64 DMG](https://img.shields.io/badge/macOS-ARM64%20DMG-000000?style=for-the-badge&logo=apple&logoColor=white) | Disk Image Installer for Apple Silicon |

<details>
<summary>🛠️ Installation Steps</summary>

- **DMG Installer (`.dmg`)**: Double-click to mount, then drag `YTSage.app` to your Applications folder.
- **Application Archive (`.zip`)**: Extract the zip and move `YTSage.app` to your Applications folder.

*Note: If you encounter an "Application is damaged" error, see the macOS troubleshooting section below.*
</details>

---

<details>
<summary>💻 Manual Source Installation</summary>

### 1. Clone the repository

```bash
git clone https://github.com/oop7/YTSage.git
cd YTSage
```

### 2. Install dependencies

#### ⚡ Using uv

```bash
uv pip install .
```

#### 📦 Or using standard pip

```bash
pip install .
```

### 3. Run the application

```bash
python -m ytsage.main
```

</details>

<a id="screenshots"></a>
## 📸 Screenshots

<div align="center">
<table>
  <tr>
    <td><img src="branding/screenshots/Download-Settings.png" alt="Download Settings" width="400"/></td>
    <td><img src="branding/screen

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
