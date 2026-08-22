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

## limitations

[https://github.com/electerm/electerm/wiki/Know-issues](https://github.com/electerm/electerm/wiki/Know-issues)
