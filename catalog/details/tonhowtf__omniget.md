# tonhowtf/omniget

Download Udemy and Hotmart courses, YouTube videos, music and books — 1,800+ sites, no terminal. Free open-source desktop app for Windows, macOS and Linux, with a built-in course player, PDF/EPUB read

## installation

Pick your system, download the latest release, and open it. There is no installer to click through and no admin rights are needed.

<table>
  <tr>
    <th>Platform</th>
    <th>How to install</th>
  </tr>
  <tr>
    <td><strong>Windows</strong></td>
    <td>
      <a href="https://github.com/tonhowtf/omniget/releases/latest"><img alt="Download OmniGet for Windows" src="https://img.shields.io/badge/Windows-Portable_EXE-0078D6?style=for-the-badge&logo=windows&logoColor=white" height="38"></a>
      <br/>
      <sub>Download the <code>.exe</code> from Releases and double click it. It is portable, so it runs from anywhere. There is also an <code>.msi</code> installer, and <code>winget install -e --id tonhowtf.OmniGet</code> if you prefer the command line.</sub>
    </td>
  </tr>
  <tr>
    <td><strong>macOS</strong></td>
    <td>
      <a href="https://github.com/tonhowtf/omniget/releases/latest"><img alt="Download OmniGet for macOS" src="https://img.shields.io/badge/macOS-DMG-000000?style=for-the-badge&logo=apple&logoColor=white" height="38"></a>
      <br/>
      <sub>Open the <code>.dmg</code> and drag OmniGet into your Applications folder. Read the first launch note below.</sub>
    </td>
  </tr>
  <tr>
    <td><strong>Linux</strong></td>
    <td>
      <a href="https://github.com/tonhowtf/omniget/releases/latest"><img alt="Download OmniGet for Linux as deb, rpm or AppImage" src="https://img.shields.io/badge/Linux-deb_·_rpm_·_AppImage-FFAA33?style=for-the-badge&logo=linux&logoColor=white" height="38"></a>
      <br/>
      <sub>Debian and Ubuntu: download the <code>.deb</code>. Fedora and openSUSE: the <code>.rpm</code>. Everything else: the <code>.AppImage</code>. x86_64 and ARM64 builds are both published.</sub>
    </td>
  </tr>
</table>

<sub><strong>AppImage on Debian 12+ or Ubuntu 24.04+:</strong> those releases ship without FUSE 2, which AppImage needs. If <code>./omniget.AppImage</code> fails with a libfuse error, run <code>sudo apt install libfuse2</code>, or start it with <code>./omniget.AppImage --appimage-extract-and-run</code>. The <code>.deb</code> avoids this entirely.</sub>

### ⚠️ Please read this before the first launch

OmniGet is open source and is not signed with a paid certificate, so the first time you open it your system may warn you. This is expected, and the steps below clear it for good. Your files stay local either way.

**macOS (this is the big one, the app will not open on the first try).** macOS Gatekeeper blocks unsigned apps. After you move OmniGet to Applications, open Terminal and run these two lines:

```bash
xattr -cr /Applications/omniget.app
codesign --force --deep --sign - /Applications/omniget.app
```

Then open OmniGet normally. You only do this once.

**Windows.** SmartScreen may show a blue warning on the first run. Click **More info**, then **Run anyway**. This is standard for open source apps without a paid code signing certificate.

### Portable mode, for a USB stick or a locked-down PC

Create an empty file named `portable.txt` (or `.portable`) next to the `.exe` and relaunch. OmniGet then keeps settings, the database, cookies, plugins, caches, and the bundled yt-dlp and FFmpeg in a `data` folder beside the executable. Nothing is written to `AppData\Roaming` or any other user folder, so the whole install travels on the stick. Without that file, OmniGet uses the standard per-user data directory.

Free and open source under GPL-3.0. Updates run quietly in the background. The bundled tools (yt-dlp and FFmpeg) install themselves, and yt-dlp is verified by SHA256 before it runs. Plugins install on first launch and update themselves too, with nothing for you to configure.

---

## One keypress, and it is downloading

This is the part people fall in love with. Copy any link, a YouTube video, a tweet, a Discord message, a track, a magnet, then press the global hotkey **`Ctrl+Shift+D`** (**`Cmd+Shift+D`** on macOS). OmniGet reads your clipboard and downloads it in the background. You do n
