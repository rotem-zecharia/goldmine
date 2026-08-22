# jooapa/jammer

light-weight CLI music player with Soundcloud, Youtube, Rss, Midi Support for Win, Linux & OSX

## installation

### Install

#### macOS / Linux (Homebrew)
```bash
brew tap jooapa/jammer && brew trust jooapa/jammer && brew install jammer
```

#### Manual Download
GitHub latest [Release](https://github.com/jooapa/jammer/releases/latest)  
*Linux version of Jammer requires fuse2. Ubuntu 22.04 or newer install `apt install libfuse2 ffmpeg`*

### Update existing

```bash
jammer --update
```

## tools

*when using **Soundcloud** or **Youtube** **links** do not forget to use **`https://`** at the start.*

```bash
# examples of how to use
jammer
jammer [song] ... [folder]
jammer https://soundcloud.com/username/track-name
jammer https://soundcloud.com/username/sets/playlist-name
jammer https://youtube.com/watch?v=video-id
jammer https://youtube.com/playlist?list=playlist-id
jammer https://raw.githubusercontent.com/jooapa/jammer/main/npc_music/616845.mp3
jammer https://raw.githubusercontent.com/jooapa/jammer/main/example/terraria.jammer
jammer https://anchor.fm/s/101ec0f34/podcast/rss
jammer "path/to/song.mp3"

jammer     --start        # opens jammer folder
jammer     --update       # checks for updates and installs
jammer -h, --help         # show help
jammer -D                 # debug mode
jammer -v, --version      # show version

## these commands are for the playlists in the <jammer/playlists> folder
jammer -p, --play       <name>                # play playlist
jammer -c, --create     <name>                # create playlist
jammer -d, --delete     <name>                # delete playlist
jammer -a, --add        <name> <song> ...     # add song to playlist
jammer -r, --remove     <name> <song> ...     # remove song from playlist
jammer -s, --show       <name>                # show songs in playlist
jammer -l, --list                             # list all playlists

jammer -f, --flush                            # deletes all the songs in songs folder
jammer -gp, --get-path                        # get the path to the <jammer/songs> folder
jammer -hm, --home                            # play all songs from the <jammer/songs> folder
jammer -so, --songs                           # open <jammer/songs> folder
```

### Interactive controls

- Press `C` to open Settings, then use Up/Down to move the `>` cursor and Enter or Space to select. Page Up/Page Down and Left/Right move between pages; Escape goes back.
- Press `Tab` to open the quick playlist switcher. It starts on the current playlist and uses the same arrow-and-Enter controls.
- Default controls can be changed in `<JammerPath>/KeyData.ini`.

#### Example of making a playlist in cli

```bash
jammer -c new_playlist
jammer -a new_playlist "https://www.youtube.com/playlist?list=PLnaJlq-zKc0WUXhwhSowwJdpe1fZumJzd"
jammer -p new_playlist
```

### Supported formats

Jammer **supports** the following audio formats: ***.mp3***, ***.ogg***, ***.wav***, ***.mp2***, ***.mp1***, ***.aiff***, ***.aif***, ***.mod***, ***.mo3***, ***.s3m***, ***.xm***, ***.it***, ***.aac***, ***.adts***, ***.mp4***, ***.m4a***, ***.m4b***, ***.mid***, ***.midi***, ***.rmi***, ***.kar***

- **JAMMER** Jammer playlist
- **FOLDER** Folder/Directory (support playing all audio files within a folder)
- **YOUTUBE** Youtube video/playlist
- **SOUNDCLOUD** Soundcloud song/playlist
- **RSS** RSS feed

### MIDI support

Jammer supports playing ***.mid***, ***.midi***, ***.rmi***, ***.kar*** files. To play, you need to have a SoundFont file ***.sf2***, ***.sf3***, ***.sfz***, ***sf2pack***

Here is one sf2 file you can use [ChoriumRevA.SF2](https://www.un4seen.com/download.php?x/ChoriumRevA), *This is BASS's recommended SoundFont file.*

To change the SoundFont file, press `G` (default keybind).

`Link to a soundFont by path`: This will link the SoundFont file by path. **This will not copy the SoundFont file to the <jammer/soundfonts>.**

`Import soundfont by path`: **This will copy the SoundFont file to the `<jammer/soundfonts>`.**

Will show all the SoundFont files in the `<jammer/soundfonts>` folder.

### RSS

Jammer supports playing audio from RSS feeds. You can add an RSS feed by the url. Then you can open the rss, and it will show all the audio files in the feed.

### Streams

Streams are filtered views of your Jammer playlists that allow you to play specific subsets of songs based on tags or properties.

Currently available stream:

#### Favorites Stream (`fav` / `favorites`)

The favorites stream plays only son

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

### M3U and M3U8 Support

Jammer supports m3u and m3u8 playlists. You can play them but with pretty limited functionality.

m3u files can be played just by opening them with Jammer. But cannot be opened with the `--play`, `-p` command from the `<jammer/playlists>` folder. You can `Save as` (default keybind `Alt + S`) the m3u file, Thus creating a JAMMER playlist to `<jammer/playlists>` folder.

Starting the m3u or m3u8 file with `#EXTM3U` and example of the m3u of all the features that are supported.

```m3u
#EXTM3U

#EXTINF:0,Lady Gaga - Telephone ft. Beyoncé
https://www.youtube.com/watch?v=Zwnvgz3ey78
#EXTINF:0,Epic Music 
/home/user/epic music/epic_music.mp3

/tmp/secret_klinoff.mp3
```

## Language support

The bundled translations are synchronized for the currently supported languages:

- English
- Finnish (*[antonako1](https://github.com/antonako1)*)
- Portuguese (*[Natanaelfelixx](https://github.com/Natanaelfelixx)*)

Missing bundled files are copied automatically into `<JammerPath>/locales`. Create a new
translation by copying an existing `.ini` file from `locales/` and translating it.

## Soundcloud Client ID

soundcloud every now and then changes the client id, which is not cool, so this allows change allows the user to change it :)
You can change the client id by going to the settings and changing the client id.

### how to get the id

- open up the [soundcloud.com](https://soundcloud.com/discover)
- open the inspect element -> Network tab
- start playing some random song
- you start to see some entries in the network tab. you should see some thing like `me?client_id=wDSKS1Bp8WmdlRPkZ7NQXGs67PMXl2Nd`

Or use Settings → Integrations → Fetch SoundCloud client ID. Jammer fetches the public
SoundCloud JavaScript assets over HTTP; it does not download or launch a browser.
If a SoundCloud track download fails, Jammer automatically attempts to fetch the newest
client ID and retries the download once before showing the final failure.

## Spotify Playlist Import

Jammer uses [SpotifyAPI-NET](https://johnnycrazy.github.io/SpotifyAPI-NET/) to import
track metadata from Spotify playlists that you own or collaborate on. It uses the
Authorization Code flow with PKCE, so a client secret is neither requested nor stored.

1. Create an application in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard).
2. Add this exact redirect URI to the application: `http://127.0.0.1:5543/callback/`.
3. In Jammer, open Settings → Integrations → Spotify application client ID and paste the
   application's client ID. You can alternatively set `SPOTIFY_CLIENT_ID`.
4. Select Authorize Spotify. Jammer opens Spotify in your browser and waits for the local
   callback.
5. Select Import or update Spotify playlists, then choose one playlist or Update all
   imported playlists.

The integration requests only `playlist-read-private` and `playlist-read-collaborative`.
The refreshable authorization is stored in `<JammerPath>/spotify-auth.json`; on Unix-like
systems the file is restricted to the current user. Disconnect Spotify deletes that file.

Each imported track is initially stored in its `.j

## limitations

Perfect app, no issues.
