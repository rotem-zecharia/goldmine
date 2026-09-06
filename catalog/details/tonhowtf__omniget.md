# tonhowtf/omniget

Download Udemy and Hotmart courses, YouTube videos, music and books — 1,800+ sites, no terminal. Free open-source desktop app for Windows, macOS and Linux, with a built-in course player, PDF/EPUB read

## features

You bought a course and want it on your disk before the platform pulls it. You keep a yt-dlp cheat sheet because the flags never stick. You have one site for Instagram stories, another for X videos, a Chrome extension for Pinterest, a Python script for subtitles, and none of them remember your login.

OmniGet puts all of that behind one text box. Paste a link, see a preview with quality options, click download. The same window then plays the course, reads the PDF, transcribes the audio and backs up the Pinterest board. yt-dlp and FFmpeg install themselves and stay updated, so there is nothing to configure and no terminal to open.

<p align="center">
  <img src="assets/readme/workflow.svg" alt="How OmniGet works: paste a link or press the hotkey, OmniGet detects the site and fetches with yt-dlp or a native extractor, the file lands in your folder and opens in the built-in player, reader or tools." width="100%" />
</p>

### How it compares

| | OmniGet | yt-dlp alone | Single-site web downloaders | Paid course downloaders |
|---|---|---|---|---|
| Sites | Courses, Instagram, X, Pinterest, Bilibili, Telegram, torrents natively, plus 1,800+ through yt-dlp | 1,800+ | One | One or two platforms |
| Setup | Download one file, open it | Python, PATH, FFmpeg, flags | None | Installer, license key |
| Logged-in content | Cookies from your browser through the extension | Manual `--cookies` export | Rarely | Sometimes |
| Queue | Resume, retry with backoff, rules, followed channels | One command at a time | No | Varies |
| After the download | Player, reader, flashcards, notes, 108 tools | Files | Files, often re-encoded | Files |
| Price and license | Free, GPL-3.0 | Free, Unlicense | Free with ads | Subscription |

yt-dlp is the engine OmniGet runs on, and OmniGet would not exist without it. If you live in a terminal and only want files, yt-dlp alone is the right tool.

---

## installation

Pick your system. Every build is published on the [Releases page](https://github.com/tonhowtf/omniget/releases/latest). Updates arrive inside the app.

<table>
  <tr>
    <th align="left">System</th>
    <th align="left">What to download</th>
    <th align="left">Other ways</th>
  </tr>
  <tr>
    <td><b>Windows 10 / 11</b></td>
    <td><code>omniget_x.y.z_x64-setup.exe</code> (installer)<br/><code>omniget_x.y.z_x64-portable.exe</code> (no install, runs from anywhere)<br/><code>omniget_x.y.z_x64_en-US.msi</code> (for IT deployments)</td>
    <td><code>winget install -e --id tonhowtf.OmniGet</code></td>
  </tr>
  <tr>
    <td><b>macOS 10.15+</b></td>
    <td><code>omniget_x.y.z_aarch64.dmg</code> for Apple Silicon (M1 and later)<br/><code>omniget_x.y.z_x64.dmg</code> for Intel Macs</td>
    <td><code>brew install --cask tonhowtf/tap/omniget</code></td>
  </tr>
  <tr>
    <td><b>Linux</b></td>
    <td><code>.deb</code> for Debian and Ubuntu (amd64 and arm64)<br/><code>.rpm</code> for Fedora, openSUSE and RHEL family (x86_64 and aarch64)<br/><code>.AppImage</code> for everything else (amd64 and aarch64)</td>
    <td>AppImage self-updates through the <code>.zsync</code> files</td>
  </tr>
</table>

### The first launch warning, and how to clear it

OmniGet is not signed with a paid certificate, so each system shows a warning the first time. This is normal for open source desktop apps and you handle it once.

**Windows.** SmartScreen shows a blue box. Click **More info**, then **Run anyway**.

**macOS.** Gatekeeper refuses to open the app and may say it is "damaged". After you drag OmniGet into Applications, open Terminal (Spotlight, type "Terminal") and paste these two lines:

```bash
xattr -cr /Applications/omniget.app
codesign --force --deep --sign - /Applications/omniget.app
```

Then open OmniGet from Launchpad as usual.

**Linux, AppImage on Debian 12+ or Ubuntu 24.04+.** Those releases ship without FUSE 2, which AppImage needs. If the file fails with a libfuse error, run `sudo apt install libfuse2`, or launch it with `./omniget.AppImage --appimage-extract-and-run`. The `.deb` avoids this entirely.

### Portable mode

Create an empty file named `portable.txt` (or `.portable`) next to the Windows `.exe` and relaunch. Settings, the database, cookies, plugins, caches, yt-dlp and FFmpeg all move to a `data` folder next to the executable. Nothing touches `AppData`, so the whole install fits on a USB stick.

---

## Your first download in one minute

1. Open OmniGet. The setup screen asks for your language and theme, then installs yt-dlp and FFmpeg with one click. yt-dlp is checked against its SHA-256 before it runs.
2. Copy any link: a YouTube video, an Instagram reel, an X post, a Pinterest board, a magnet, a direct file URL.
3. Paste it in the box on the home screen. OmniGet detects the site and shows the title, thumbnail and available qualities. Pick one and press Enter.

The Downloads page shows speed, phase and ETA read straight from the downloader, so a stalled download looks stalled instead of frozen at "3 seconds left". Interrupted downloads resume where they stopped. Rate-limited sites get retried with backoff, and connections per site adapt on their own, so YouTube gets up to 16 parallel fragments while a site that answers 429 gets fewer. When a Python 3.10 or newer is present, yt-dlp runs as a zipapp on it and starts in under a second instead of unpacking the bundled binary on every launch.

<p align="center">
  <img src="assets/readme/downloads.png" alt="OmniGet Downloads page with an active 4K YouTube download showing phase, speed, ETA and the exact yt-dlp command, plus queued and finished items" width="900" />
</p>

### Skip the window entirely

Copy a link anywhere on your system and press **Ctrl+Shift+D** (**Cmd+Shift+D** on macOS). OmniGet reads the clipboard and starts the download in the background. A second hotkey, **Ctrl+Shift+M**, grabs audio only, so a YouTube link becomes an MP3 without opening anything. It

## tools

Tools is the part of OmniGet that grew beyond downloading. Each tile is one job: an isolated Rust command with JSON in and JSON out, which is also what lets AI agents drive them through the built-in MCP server. The hub has a search box that understands English and Portuguese ("legenda" finds subtitle tools) and a platform filter, and tools that only run on Windows say so on the tile and stay hidden elsewhere.

<p align="center">
  <img src="assets/readme/tools.png" alt="OmniGet Tools hub with 16 categories: YouTube, Speech and subtitles, Video editing, Instagram, X, Pinterest, Spotify, PDF, Documents, Images, System, Files, Downloads, Automation, Phone and AI" width="900" />
</p>

Status legend: no mark means ready, **beta** means it works but has not been tested against every account type, **planned** means the tile exists so you can see where things are going and does nothing yet.

<table>
  <tr>
    <td><img src="assets/readme/tools-instagram.png" alt="Instagram tools in OmniGet: download post, bulk download, reel audio, stories, highlights, story viewers, profile viewer, HD avatar, profile download, unfollowers, fans, mutuals, who unfollowed, ghost followers, whitelist, data export, analytics, compare profiles, hashtag explorer, comments, likers, giveaway picker, publish and schedule" /></td>
    <td><img src="assets/readme/tools-x.png" alt="X / Twitter tools in OmniGet: download post, unroll thread, post to image, profile X-ray, profile media, advanced search, export bookmarks, who doesn't follow back, your X archive and Grok" /></td>
  </tr>
  <tr>
    <td><img src="assets/readme/tools-pinterest.png" alt="Pinterest tools in OmniGet: download pin, board backup, profile backup, search without AI or ads, similar pins, find the source, duplicates, color palette, offline gallery and keyword ideas" /></td>
    <td><img src="assets/readme/tools-speech.png" alt="Speech and subtitles tools in OmniGet: transcribe with whisper.cpp, text to speech, translate subtitles, dub from subtitles, and planned voice cloning, voice design, vocal isolation and dictation" /></td>
  </tr>
</table>

### YouTube (11)

- **Download video.** Paste a link and pick quality, format and subtitles. Same engine as the home screen.
- **Metadata.** Save the info, description and thumbnail without the video.
- **Thumbnails.** Browse every cover image and save it at any resolution.
- **Subtitles.** Download subtitles, or merge two languages into one bilingual file.
- **Comments and chapters.** Fetch comments or chapter markers, filter them, export JSON or CSV.
- **Live chat.** Save the chat replay of a stream as JSON or CSV.
- **Subtitle workshop.** Edit, translate and re-time SRT, VTT and ASS files with a waveform, two-point sync, find and replace, an auto fix, and AI grammar and translation.
- **SponsorBlock.** See sponsor, intro and outro segments and get the yt-dlp flags to skip them.
- **Dislikes.** Likes, dislikes and rating from Return YouTube Dislike.
- **Real thumbnail.** The frames the CDN already has at 25, 50 and 75 percent, instead of the clickbait cover.
- **Force H.264.** A switch in the browser extension that keeps YouTube on H.264 instead of VP9 and AV1, for machines that stutter on newer codecs.

### Speech and subtitles (8)

- **Transcribe.** Audio or video to subtitles with whisper.cpp, offline. Models download on demand, Metal acceleration on macOS.
- **Text to speech.** Natural voices from Microsoft Edge, free, with a synced subtitle file.
- **Translate subtitles.** Translate an SRT with your AI provider or a LibreTranslate server, keeping the timing.
- **Dub from subtitles.** Turn an SRT into a voice track that fits each line and optionally replace the video's audio. *beta*
- **Clone a voice**, **Design a voice** and **Isolate vocals** through a VoiceStudio install running on your machine. *beta*
- **Dictation.** Press a global shortcut, speak, and whisper types the text where your cursor is. *beta*

### Video editing (6)

- **Cut a clip
