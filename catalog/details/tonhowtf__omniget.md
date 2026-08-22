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
