# jooapa/jammer

light-weight CLI music player with Soundcloud, Youtube, Rss, Midi Support for Win, Linux & OSX

## installation

#### macOS / Linux (Homebrew)
```bash
brew tap jooapa/jammer && brew trust jooapa/jammer && brew install jammer
```

#### Manual Download
GitHub latest [Release](https://github.com/jooapa/jammer/releases/latest)  
*Linux version of Jammer requires fuse2. Ubuntu 22.04 or newer install `apt install libfuse2 ffmpeg`*

## tools

*when using **Soundcloud** or **Youtube** **links** do not forget to use **`https://`** at the start.*

```bash

## configuration

You can customize Jammer's storage locations using these environment variables:

- `JAMMER_CONFIG_PATH` - Path to the configuration directory
- `JAMMER_SONGS_PATH` - Path to the songs storage directory
- `JAMMER_PLAYLISTS_PATH` - Path to the playlists directory
- `JAMMER_YTDLP_BIN` - Path to an externally managed yt-dlp executable
- `SPOTIFY_CLIENT_ID` - Optional override for the Spotify developer application client ID

Without an override, Jammer uses centralized paths below `<JammerPath>`: `songs`,
`playlists`, `tools`, `downloads`, `cache`, `locales`, `soundfonts`, and `themes`.

**Examples:**

Windows:
```powershell
$env:JAMMER_SONGS_PATH = "D:\Music\JammerSongs"
$env:JAMMER_CONFIG_PATH = "D:\AppData\Jammer"
```

Linux/macOS:
```bash
export JAMMER_SONGS_PATH="/mnt/music/jammer_songs"
export JAMMER_CONFIG_PATH="/home/user/.config/jammer"
```

## limitations

Perfect app, no issues.
