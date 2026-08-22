# vzhd1701/gridplayer

Play videos side-by-side

## features

- Cross-platform (Linux, Mac, and Windows)
- Support for any video and audio format (VLC)
- Support for (almost) any streaming
  URLs ([streamlink](https://streamlink.github.io/plugins.html) + [yt-dlp](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md))
- Hardware & software video decoding
- Control video aspect, playback speed, zoom
- Set loop fragments with frame percision
- Configurable grid layout
- Easy swap videos with drag-n-drop
- Playlist retains settings for each video

## Translation

GridPlayer now supports internationalization! Anyone with a handful of free time and
desire to support this project is [welcome to contribute](https://crowdin.com/project/gridplayer).
No coding skills or special software required, all dialogs are well documented and
there are not many strings to translate.

Huge thanks to [every contributor](https://github.com/vzhd1701/gridplayer#translations)!

## installation

### Windows

[![Download Windows Installer](https://raw.githubusercontent.com/vzhd1701/gridplayer/master/resources/public/dl_windows_installer.png)](https://github.com/vzhd1701/gridplayer/releases/download/v0.5.5/GridPlayer-0.5.5-win64-install.exe)
[![Download Windows Portable](https://raw.githubusercontent.com/vzhd1701/gridplayer/master/resources/public/dl_windows_portable.png)](https://github.com/vzhd1701/gridplayer/releases/download/v0.5.5/GridPlayer-0.5.5-win64-portable.zip)

Via [scoop](https://scoop.sh/):

```shell
scoop install gridplayer
```

**Compatible with Windows 7, 8, 10, 11.**

### Linux

[![Get it from the Flathub](https://raw.githubusercontent.com/vzhd1701/gridplayer/master/resources/public/dl_flathub.png)](https://flathub.org/apps/details/com.vzhd1701.gridplayer)
[![Get it from the Snap Store](https://raw.githubusercontent.com/vzhd1701/gridplayer/master/resources/public/dl_snap.png)](https://snapcraft.io/gridplayer)
[![Download AppImage](https://raw.githubusercontent.com/vzhd1701/gridplayer/master/resources/public/dl_appimage.png)](https://github.com/vzhd1701/gridplayer/releases/download/v0.5.5/GridPlayer-0.5.5-x86_64.AppImage)

**For better system integration install via Flathub.**

#### Note on AppImage

The AppImage was built using Ubuntu Focal Fossa libraries, so compatibility is Ubuntu 20+.

You may need to set execute permissions on AppImage file in order to run it:

```shell
chmod +x GridPlayer-0.5.5-x86_64.AppImage
```

### MacOS

[![Download DMG](https://raw.githubusercontent.com/vzhd1701/gridplayer/master/resources/public/dl_dmg.png)](https://github.com/vzhd1701/gridplayer/releases/download/v0.5.5/GridPlayer.0.5.5_arm64.dmg)

**DMG image is not signed and targets Apple Silicon (`arm64`).** You will have to add an exception to run this app.

- [How to open an app that hasn’t been notarized or is from an unidentified developer](https://support.apple.com/en-euro/HT202491)
- [Open a Mac app from an unidentified developer](https://support.apple.com/guide/mac-help/open-a-mac-app-from-an-unidentified-developer-mh40616/mac)

If you get "GridPlayer is damaged and can't be opened" error, run this command in the Terminal app:

```shell
sudo xattr -rd com.apple.quarantine /Applications/GridPlayer.app
```

### Install with [UV](https://docs.astral.sh/uv/)

```shell
uv tool install gridplayer
```

**Python 3.10 or later required.**

This type of installation will also require VLC installed (Windows & Mac) or a `vlc` package (Linux) present in your
system.
Please refer to [VLC official page](https://www.videolan.org/vlc/) for instructions on how to install it.

Some distros (e.g. Ubuntu) might also require `libxcb-xinerama0` package.

### From source

```shell
uv tool install git+https://github.com/vzhd1701/gridplayer.git
```

The same notes about the Python version and external packages from above apply here.

## Video Decoder settings

GridPlayer supports two video output modes:

- Hardware (default) mode uses available GPU to render video. This mode offers high performance and is a recommended
  mode.
- Software mode is entirely independent of GPU and only uses the CPU to render video. This mode may cause a high CPU
  load with high-resolution videos.

Due to libvlc software library limitations, video decoding is split into parallel processes. You can control how many
videos are handled by a single decoder process using the "Videos per process" setting. Setting this option too high may
cause a high CPU load and application freeze. The optimal value is 4 videos per process.

There is also "Hardware SP" mode. It handles video decoding within the same process in which GridPlayer runs. It is not
recommended to use with many videos (>4-6) because it may cause high CPU load and application freeze.

Due to OS inter-process restrictions, "Hardware SP" is the only available hardware mode in macOS.

## limitations

### Linux (Snap): Error when opening a file from the mounted disk

You need to allow GridPlayer snap to access removable storage devices via Snap Store or by running:

```shell
sudo snap connect gridplayer:removable-media
```

### Linux (Snap): mounted drives are not visible in file selection dialog

You will also see following error if you run GridPlayer from terminal:

```shell
GLib-GIO-WARNING **: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
```

To fix this, you need to allow GridPlayer snap to access system mount information and disk quotas via Snap Store or by
running:

```shell
sudo snap connect gridplayer:mount-observe
```

### Linux: black screen issue when using hardware decoder

If no compositor is running, GridPlayer switches the overlay to opaque automatically. If the overlay is still a black
screen, switch on "Opaque overlay (fix black screen)" checkbox in settings.

Depending on the window manager, the overlay might be a bit glitchy with the hardware decoder. Enabling compositor might
help.

## Geting help

If you found a bug or have a feature request,
please [open a new issue](https://github.com/vzhd1701/gridplayer/issues/new/choose).

If you have a question about the program or have difficulty using it, you are welcome
to [the discussions page](https://github.com/vzhd1701/gridplayer/discussions). You can also mail me directly, I'm always
happy to help.

## Attributions

This software was build using

- **Python** by [Python Software Foundation](https://www.python.org/)
  - Licensed under *Python Software Foundation License*
- **Qt** by [Qt Project](https://www.qt.io/)
  - Licensed under *GPL 2.0, GPL 3.0, and LGPL 3.0*
- **VLC** by [VideoLAN](https://www.videolan.org/)
  - Licensed under *GPL 2.0 or later*

### Python packages

- **PyQt** by [Riverbank Computing](https://riverbankcomputing.com/)
  - Licensed under *Riverbank Commercial License and GPL v3*
- **python-vlc** by [Olivier Aubert](https://github.com/oaubert/python-vlc)
  - Licensed under *GPL 2.0 and LGPL 2.1*
- **pydantic** by [Samuel Colvin](https://github.com/samuelcolvin/pydantic)
  - Licensed under *MIT License*
- **streamlink** by [Christopher Rosell, Streamlink Team](https://github.com/streamlink/streamlink)
  - Licensed under *BSD-2-Clause License*
- **yt-dlp** by [Contributors](https://github.com/yt-dlp/yt-dlp)
  - Licensed under *Unlicense License*

### Graphics

- **Hack Font** by [Source Foundry](http://sourcefoundry.org/hack/)
  - Licensed under *MIT License*
- **Basic Icons** by [Icongeek26](https://www.flaticon.com/authors/icongeek26)
  - Licensed under *Flaticon License*
- **Suru Icons** by [Sam Hewitt](https://snwh.org/)
  - Licensed under *Creative Commons Attribution-Share Alike 4.0*
- **Clean App Download Buttons** by [Tony Thomas](https://medialoot.com/item/clean-app-download-buttons/)
  - Licensed under *MediaLoot License*
- **Flag Icons** by [Panayiotis Lipiridis](https://github.com/lipis/flag-icons)
  - Licensed under *MIT License*

## Translations

<!-- CROWDIN-CONTRIBUTORS-START -->

<table>
  <tbody>
    <tr>
      <td align="center" valign="top">
        <a href="https://crowdin.com/profile/VenusGirl"><img alt="logo" style="width: 64px" src="https://crowdin-static.cf-downloads.crowdin.com/avatar/14432528/medium/3284b34db4ef3cda16835c5a18c797d0.jpg" />
          <br />
          <sub><b>VenusGirl</b></sub></a>
        <br />
        <sub><b>886 words</b></sub>
        <br /><sub><b><code title="Korean">ko</code></b></sub>
      </td>
      <td align="center" valign="top">
        <a href="https://crowdin.com/profile/LOUIS_Sylvain"><img alt="logo" style="width: 64px" src="https://crowdin-static.cf-downloads.crowdin.com/avatar/14983555/medium/af7d7ab185011ffda0bd01b41fc05ccf.png" />
          <br />
          <sub><b>Sylvain LOUIS</b></sub>
          <br />
          <sub><b>(LOUIS_Sylvain)</b></sub></a>
        <br />
        <sub><b>886 words</b></sub>
        <br /><sub><b>
