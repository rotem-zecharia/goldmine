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

## installation

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
