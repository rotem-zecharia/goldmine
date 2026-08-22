# electerm/electerm

📻Terminal/ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice client(Linux, Mac, Windows, Android, HarmonyOS)

## features

- Works as a terminal/file manager or ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice client
- Support Window 7+(X64/ARM64), HarmonyOS，Android, Mac OS 10.15+(x64/arm64), Linux(x64/arm64/Loong64 new world & old world), even old Linux with glibc 2.17+ like UOS/Kylin/Ubuntu 18.04 etc
- Global hotkey to toggle window visibility (similar to guake, default is `ctrl + 2`)
- Multi platform(linux, mac, win)
- 🇺🇸 🇨🇳 🇧🇷 🇷🇺 🇪🇸 🇫🇷 🇹🇷 🇭🇰 🇯🇵 🇸🇦 🇩🇪 🇰🇷 🇮🇩 🇵🇱 Multi-language support([electerm-locales](https://github.com/electerm/electerm-locales), contributions/fixes welcome)
- Double click to directly edit (small) remote files.
- Auth with publicKey + password.
- Support Zmodem(rz, sz).
- Support ssh tunnel.
- Support [Trzsz](https://github.com/trzsz/trzsz)(trz/tsz), similar to rz/sz, and compatible with tmux.
- Transparent window(Mac, win).
- Terminal background image.
- Global/session proxy.
- Quick commands
- UI/terminal theme
- Sync bookmarks/themes/quick commands to github/gitee secret gist/webdav/custom server/electerm cloud
- Quick input to one or all terminals.
- AI assistant integration (supporting [DeepSeek](https://www.deepseek.com), OpenAI, and any other AI APIs) to help with command suggestions, script writing, and explaining selected terminal content, create bookmarks/themes
- MCP (Model Context Protocol) widget for AI assistants and external tools integration - see [MCP Widget Usage Guide](https://github.com/electerm/electerm/wiki/MCP-Widget-Usage-Guide)
- Deep link support: Open connections with URLs like `telnet://192.168.2.31:34554` or `ssh://user@host:22` - see [Deep link support wiki](https://github.com/electerm/electerm/wiki/Deep-link-support)
- Command line usage: check [wiki](https://github.com/electerm/electerm/wiki/Command-line-usage)

## installation

- For Mac user: `brew install --cask electerm`
- With snap: `sudo snap install electerm --classic`
- For some Linux distribution, you can find it from OS default App store(Ubuntu, Deepin, Mint...).
- For some linux OS, the `rpm`, `deb`, or `snap` release may not work, you can try the `tar.gz` or `.appImage` release.
- For Windows users, you can install it from [windows store](https://www.microsoft.com/store/apps/9NCN7272GTFF), command-line installer [winget](https://github.com/microsoft/winget-cli) and [scoop](https://github.com/lukesampson/scoop) is also recommended:

```powershell
# winget https://github.com/microsoft/winget-cli
winget install electerm.electerm

# scoop https://github.com/lukesampson/scoop
scoop bucket add dorado https://github.com/chawyehsu/dorado
scoop install dorado/electerm
```

- Install from Debian repository (for Debian/Ubuntu-based systems) with `apt` command

Check [https://repos.electerm.org/deb](https://repos.electerm.org/deb)

- Install from npm

```bash
npm i -g electerm

```

## Upgrade

- Auto upgrade: When a new version is released, you will get an upgrade notification after you start electerm again. You can then click the upgrade button to upgrade.
- Download: Just download the latest edition, reinstall.
- Npm: If you install from npm, just run `npm i -g electerm` again.
- If use Snap or some other distribution system, these systems may provide upgrades.

## limitations

[https://github.com/electerm/electerm/wiki/Know-issues](https://github.com/electerm/electerm/wiki/Know-issues)

## Troubleshoot

[https://github.com/electerm/electerm/wiki/Troubleshoot](https://github.com/electerm/electerm/wiki/Troubleshoot)

## Discussion

[![Discord](https://img.shields.io/badge/Discord-Join-blue?logo=discord)](https://discord.gg/855W7g8EVd)

[Discussion board](https://github.com/electerm/electerm/discussions)

![electerm-wechat-group-qr.jpg](https://electerm.org/electerm-wechat-group-qr.jpg)

## Support

Would love to hear from you, please tell me what you think, [submit an issue](https://github.com/electerm/electerm/issues), [Start a new discussion](https://github.com/electerm/electerm/discussions/new), [create/fix language files](https://github.com/electerm/electerm-locales) or create pull requests, all welcome.

## Sponsor this project

github sponsor

[https://github.com/sponsors/electerm](https://github.com/sponsors/electerm)

kofi

[https://ko-fi.com/zhaoxudong](https://ko-fi.com/zhaoxudong)

wechat donate

[![wechat donate](https://electerm.org/electerm-wechat-donate.png)](https://github.com/electerm)

TRON TRN20

[![TRN20 donate](https://github.com/electerm/electerm-resource/blob/master/static/images/trn20.png?raw=true)]

Address: TXk3pQNmQu1vihH76RaEFnK9wg13x4LLCZ

## Dev

```bash
# May only works in Linux
