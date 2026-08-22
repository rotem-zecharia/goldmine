# yt-dlp/yt-dlp

A feature-rich command-line audio/video downloader

## installation

<!-- MANPAGE: BEGIN EXCLUDED SECTION -->
[![Windows](https://img.shields.io/badge/-Windows_x64-blue.svg?style=for-the-badge&logo=windows)](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe)
[![Unix](https://img.shields.io/badge/-Linux/BSD-red.svg?style=for-the-badge&logo=linux)](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp)
[![MacOS](https://img.shields.io/badge/-MacOS-lightblue.svg?style=for-the-badge&logo=apple)](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos)
[![PyPI](https://img.shields.io/badge/-PyPI-blue.svg?logo=pypi&labelColor=555555&style=for-the-badge)](https://pypi.org/project/yt-dlp)
[![Source Tarball](https://img.shields.io/badge/-Source_tar-green.svg?style=for-the-badge)](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.tar.gz)
[![Other variants](https://img.shields.io/badge/-Other-grey.svg?style=for-the-badge)](#release-files)
[![All versions](https://img.shields.io/badge/-All_Versions-lightgrey.svg?style=for-the-badge)](https://github.com/yt-dlp/yt-dlp/releases)
<!-- MANPAGE: END EXCLUDED SECTION -->

You can install yt-dlp using [the binaries](#release-files), [pip](https://pypi.org/project/yt-dlp) or one using a third-party package manager. See [the wiki](https://github.com/yt-dlp/yt-dlp/wiki/Installation) for detailed instructions


<!-- MANPAGE: BEGIN EXCLUDED SECTION -->
## RELEASE FILES

#### Recommended

File|Description
:---|:---
[yt-dlp](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp)|Platform-independent [zipimport](https://docs.python.org/3/library/zipimport.html) binary. Needs Python (recommended for **Linux/BSD**)
[yt-dlp.exe](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe)|Windows (Win8+) standalone x64 binary (recommended for **Windows**)
[yt-dlp_macos](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_macos)|Universal MacOS (10.15+) standalone executable (recommended for **MacOS**)

#### Alternatives

File|Description
:---|:---
[yt-dlp_linux](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux)|Linux (glibc 2.17+) standalone x86_64 binary
[yt-dlp_linux.zip](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux.zip)|Unpackaged Linux (glibc 2.17+) x86_64 executable (no auto-update)
[yt-dlp_linux_aarch64](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux_aarch64)|Linux (glibc 2.17+) standalone aarch64 binary
[yt-dlp_linux_aarch64.zip](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux_aarch64.zip)|Unpackaged Linux (glibc 2.17+) aarch64 executable (no auto-update)
[yt-dlp_linux_armv7l.zip](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_linux_armv7l.zip)|Unpackaged Linux (glibc 2.31+) armv7l executable (no auto-update)
[yt-dlp_musllinux](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_musllinux)|Linux (musl 1.2+) standalone x86_64 binary
[yt-dlp_musllinux.zip](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_musllinux.zip)|Unpackaged Linux (musl 1.2+) x86_64 executable (no auto-update)
[yt-dlp_musllinux_aarch64](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_musllinux_aarch64)|Linux (musl 1.2+) standalone aarch64 binary
[yt-dlp_musllinux_aarch64.zip](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_musllinux_aarch64.zip)|Unpackaged Linux (musl 1.2+) aarch64 executable (no auto-update)
[yt-dlp_x86.exe](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_x86.exe)|Windows (Win8+) standalone x86 (32-bit) binary
[yt-dlp_win_x86.zip](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_win_x86.zip)|Unpackaged Windows (Win8+) x86 (32-bit) executable (no auto-update)
[yt-dlp_arm64.exe](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_arm64.exe)|Windows (Win10+) standalone ARM64 binary
[yt-dlp_win_arm64.zip](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp_win_ar

## requirements

Python versions 3.10+ (CPython) and 3.11+ (PyPy) are supported. Other versions and implementations may or may not work correctly.

<!-- Python 3.5+ uses VC++14 and it is already embedded in the binary created
<!x-- https://www.microsoft.com/en-us/download/details.aspx?id=26999 --x>
On Windows, [Microsoft Visual C++ 2010 SP1 Redistributable Package (x86)](https://download.microsoft.com/download/1/6/5/165255E7-1014-4D0A-B094-B6A430A6BFFC/vcredist_x86.exe) is also necessary to run yt-dlp. You probably already have this, but if the executable throws an error due to missing `MSVCR100.dll` you need to install it manually.
-->

While all the other dependencies are optional, `ffmpeg`, `ffprobe`, `yt-dlp-ejs` and a supported JavaScript runtime/engine are highly recommended

### Strongly recommended

* [**ffmpeg** and **ffprobe**](https://www.ffmpeg.org) - Required for [merging separate video and audio files](#format-selection), as well as for various [post-processing](#post-processing-options) tasks. License [depends on the build](https://www.ffmpeg.org/legal.html)

    Since ffmpeg is such an important dependency, we provide our own builds at [yt-dlp/FFmpeg-Builds](https://github.com/yt-dlp/FFmpeg-Builds). In the past, patches were applied to these builds in order to fix common issues for yt-dlp users, but currently our builds are equivalent to upstream ffmpeg. See [the readme](https://github.com/yt-dlp/FFmpeg-Builds#patches-applied) for details

    **Important**: What you need is ffmpeg *binary*, **NOT** [the Python package of the same name](https://pypi.org/project/ffmpeg)

* [**yt-dlp-ejs**](https://github.com/yt-dlp/ejs) - Required for full YouTube support. Licensed under [Unlicense](https://github.com/yt-dlp/ejs/blob/main/LICENSE), bundles [MIT](https://github.com/davidbonnet/astring/blob/main/LICENSE) and [ISC](https://github.com/meriyah/meriyah/blob/main/LICENSE.md) components.

    A JavaScript runtime/engine like [**deno**](https://deno.land) (recommended), [**node.js**](https://nodejs.org), [**bun**](https://bun.sh), or [**QuickJS**](https://bellard.org/quickjs/) is also required to run yt-dlp-ejs. See [the wiki](https://github.com/yt-dlp/yt-dlp/wiki/EJS).

### Networking
* [**certifi**](https://github.com/certifi/python-certifi)\* - Provides Mozilla's root certificate bundle. Licensed under [MPLv2](https://github.com/certifi/python-certifi/blob/master/LICENSE)
* [**brotli**](https://github.com/google/brotli)\* or [**brotlicffi**](https://github.com/python-hyper/brotlicffi) - [Brotli](https://en.wikipedia.org/wiki/Brotli) content encoding support. Both licensed under MIT <sup>[1](https://github.com/google/brotli/blob/master/LICENSE) [2](https://github.com/python-hyper/brotlicffi/blob/master/LICENSE) </sup>
* [**websockets**](https://github.com/aaugustin/websockets)\* - For downloading over websocket. Licensed under [BSD-3-Clause](https://github.com/aaugustin/websockets/blob/main/LICENSE)
* [**requests**](https://github.com/psf/requests)\* - HTTP library. For HTTPS proxy and persistent connections support. Licensed under [Apache-2.0](https://github.com/psf/requests/blob/main/LICENSE)

#### Impersonation

The following provide support for impersonating browser requests. This may be required for some sites that employ TLS fingerprinting.

* [**curl_cffi**](https://github.com/lexiforest/curl_cffi) (recommended) - Python binding for [curl-impersonate](https://github.com/lexiforest/curl-impersonate). Provides impersonation targets for Chrome, Edge and Safari. Licensed under [MIT](https://github.com/lexiforest/curl_cffi/blob/main/LICENSE)
  * Can be installed with the `curl-cffi` extra, e.g. `pip install "yt-dlp[default,curl-cffi]"`
  * Currently included in most builds *except* `yt-dlp` (Unix zipimport binary) and `yt-dlp_x86` (Windows 32-bit)


### Metadata

* [**mutagen**](https://github.com/quodlibet/mutagen)\* - For `--embed-thumbnail` in certain formats. Licensed under [GPLv2+](https://github.com/quodlibet/mutagen/blob/maste

## tools

<!-- MANPAGE: BEGIN EXCLUDED SECTION -->
    yt-dlp [OPTIONS] [--] URL [URL...]

Tip: Use `CTRL`+`F` (or `Command`+`F`)  to search by keywords
<!-- MANPAGE: END EXCLUDED SECTION -->

<!-- Auto generated -->

## configuration

-h, --help                      Print this help text and exit
    --version                       Print program version and exit
    -U, --update                    Update this program to the latest version
    --no-update                     Do not check for updates (default)
    --update-to [CHANNEL]@[TAG]     Upgrade/downgrade to a specific version.
                                    CHANNEL can be a repository as well. CHANNEL
                                    and TAG default to "stable" and "latest"
                                    respectively if omitted; See "UPDATE" for
                                    details. Supported channels: stable,
                                    nightly, master
    -i, --ignore-errors             Ignore download and postprocessing errors.
                                    The download will be considered successful
                                    even if the postprocessing fails
    --no-abort-on-error             Continue with next video on download errors;
                                    e.g. to skip unavailable videos in a
                                    playlist (default)
    --abort-on-error                Abort downloading of further videos if an
                                    error occurs (Alias: --no-ignore-errors)
    --list-extractors               List all supported extractors and exit
    --extractor-descriptions        Output descriptions of all supported
                                    extractors and exit
    --use-extractors NAMES          Extractor names to use separated by commas.
                                    You can also use regexes, "all", "default"
                                    and "end" (end URL matching); e.g. --ies
                                    "holodex.*,end,youtube". Prefix the name
                                    with a "-" to exclude it, e.g. --ies
                                    default,-generic. Use --list-extractors for
                                    a list of extractor names. (Alias: --ies)
    --default-search PREFIX         Use this prefix for unqualified URLs. E.g.
                                    "gvsearch2:python" downloads two videos from
                                    google videos for the search term "python".
                                    Use the value "auto" to let yt-dlp guess
                                    ("auto_warning" to emit a warning when
                                    guessing). "error" just throws an error. The
                                    default value "fixup_error" repairs broken
                                    URLs, but emits an error if this is not
                                    possible instead of searching
    --ignore-config                 Don't load any more configuration files
                                    except those given to --config-locations.
                                    For backward compatibility, if this option
                                    is found inside the system configuration
                                    file, the user configuration is not loaded.
                                    (Alias: --no-config)
    --no-config-locations           Do not load any custom configuration files
                                    (default). When given inside a configuration
                                    file, ignore all previous --config-locations
                                    defined in the current file
    --config-locations PATH         Location of the main configuration file;
                                    either the path to the config or its
                                    containing directory ("-" for stdin). Can be
                                    used multiple times and inside other
                                    configuration files
    --plugin-dirs DIR               Path to an additional directory to search
                                    for plugins. This option 

## features

* Forked from [**yt-dlc@f9401f2**](https://github.com/blackjack4494/yt-dlc/commit/f9401f2a91987068139c5f757b12fc711d4c0cee) and merged with [**youtube-dl@a08f2b7**](https://github.com/ytdl-org/youtube-dl/commit/a08f2b7e4567cdc50c0614ee0a4ffdff49b8b6e6) ([exceptions](https://github.com/yt-dlp/yt-dlp/issues/21))

* **[SponsorBlock Integration](#sponsorblock-options)**: You can mark/remove sponsor sections in YouTube videos by utilizing the [SponsorBlock](https://sponsor.ajay.app) API

* **[Format Sorting](#sorting-formats)**: The default format sorting options have been changed so that higher resolution and better codecs will be now preferred instead of simply using larger bitrate. Furthermore, you can now specify the sort order using `-S`. This allows for much easier format selection than what is possible by simply using `--format` ([examples](#format-selection-examples))

* **Merged with animelover1984/youtube-dl**: You get most of the features and improvements from [animelover1984/youtube-dl](https://github.com/animelover1984/youtube-dl) including `--write-comments`, `BiliBiliSearch`, `BilibiliChannel`, Embedding thumbnail in mp4/ogg/opus, playlist infojson etc. See [#31](https://github.com/yt-dlp/yt-dlp/pull/31) for details.

* **YouTube improvements**:
    * Supports Clips, Stories (`ytstories:<channel UCID>`), Search (including filters)**\***, YouTube Music Search, Channel-specific search, Search prefix (`ytsearch:`)**\***, Mixes, and Feeds (`:ytfav`, `:ytwatchlater`, `:ytsubs`, `:ythistory`, `:ytrec`, `:ytnotif`)
    * Fix for [n-sig based throttling](https://github.com/ytdl-org/youtube-dl/issues/29326) **\***
    * Download livestreams from the start using `--live-from-start` (*experimental*)
    * Channel URLs download all uploads of the channel, including shorts and live

* **Cookies from browser**: Cookies can be automatically extracted from all major web browsers using `--cookies-from-browser BROWSER[+KEYRING][:PROFILE][::CONTAINER]`

* **Download time range**: Videos can be downloaded partially based on either timestamps or chapters using `--download-sections`

* **Split video by chapters**: Videos can be split into multiple files based on chapters using `--split-chapters`

* **Multi-threaded fragment downloads**: Download multiple fragments of m3u8/mpd videos in parallel. Use `--concurrent-fragments` (`-N`) option to set the number of threads used

* **New and fixed extractors**: Many new extractors have been added and a lot of existing ones have been fixed. See the [changelog](Changelog.md) or the [list of supported sites](supportedsites.md)

* **New MSOs**: Philo, Spectrum, SlingTV, Cablevision, RCN etc.

* **Subtitle extraction from manifests**: Subtitles can be extracted from streaming media manifests. See [commit/be6202f](https://github.com/yt-dlp/yt-dlp/commit/be6202f12b97858b9d716e608394b51065d0419f) for details

* **Multiple paths and output templates**: You can give different [output templates](#output-template) and download paths for different types of files. You can also set a temporary path where intermediary files are downloaded to using `--paths` (`-P`)

* **Portable Configuration**: Configuration files are automatically loaded from the home and root directories. See [CONFIGURATION](#configuration) for details

* **Output template improvements**: Output templates can now have date-time formatting, numeric offsets, object traversal etc. See [output template](#output-template) for details. Even more advanced operations can also be done with the help of `--parse-metadata` and `--replace-in-metadata`

* **Other new options**: Many new options have been added such as `--alias`, `--print`, `--concat-playlist`, `--wait-for-video`, `--retry-sleep`, `--sleep-requests`, `--convert-thumbnails`, `--force-download-archive`, `--force-overwrites`, `--break-match-filters` etc

* **Improvements**: Regex and other operators in `--format`/`--match-filters`, multiple `--postprocessor-args` and `--downloader-args`, faster
