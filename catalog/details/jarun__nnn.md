# jarun/nnn

n³ The unorthodox terminal file manager

## features

- Quality
  - Privacy-aware (no unconfirmed user data collection)
  - POSIX-compliant, follows Linux kernel coding style
  - Highly optimized, static analysis integrated code
- Frugal
  - Typically needs less than 3.5MB resident memory
  - Works with 8 colors (and xterm 256 colors)
  - Disk-IO sensitive (few disk reads and writes)
  - No FPU usage (all integer maths, even for file size)
  - Minimizes screen refresh with fast line redraws
  - Tiny binary (typically around 100KB)
  - 1-column mode for smaller terminals and form factors
  - Hackable - compile in/out features and dependencies
- Portable
  - Language-agnostic plugins
  - Static binary available (no need to install)
  - Minimal library deps, easy to compile
  - No config file, minimal config with sensible defaults
  - Plugin to backup configuration
  - Widely available on many packagers
  - Touch enabled, handheld-friendly shortcuts
  - Unicode support
- Modes
  - Light (default), detail
  - Disk usage analyzer (block/apparent)
  - File picker, (neo)vim plugin
- Navigation
  - Filter with automatic dir entry on unique match
  - *Type-to-nav* (turbo navigation/always filter) mode
  - Jump to an entry with visible relative offset
  - Contexts (_aka_ tabs/workspaces) with custom colors
  - Sessions, bookmarks, mark and visit a dir
  - Remote mounts (needs `sshfs`, `rclone`)
  - Familiar shortcuts (arrows, <kbd>~</kbd>, <kbd>-</kbd>, <kbd>@</kbd>), quick look-up
  - `cd` on quit (*easy* shell integration)
  - Proceed to next file on file open and selection
- Search
  - Instant filtering with *search-as-you-type*
  - Fuzzy, regex (POSIX/PCRE2) and string (default) filters
  - Subtree search plugin to open or edit files
- Sort
  - Ordered pure numeric names by default (visit `/proc`)
  - Case-insensitive version (_aka_ natural) sort
  - By name, access/change/mod (default) time, size, extn
  - Reverse sort
  - Directory-specific ordering
- Mimes
  - Built-in previewer for directory and text files
  - FIFO-based previewer plugins with extensive mime support
  - Open with desktop opener or specify a custom opener
  - File-specific colors (or minimal _dirs in context color_)
  - Icons and Emojis support (customize and compile-in)
  - Plugin for image, video and audio thumbnails
  - Create, list, extract (to), mount (FUSE based) archives
  - Option to open all text files in `$EDITOR`
- Convenience
  - Detailed file stats and mime information
  - Run plugins and custom commands with hotkeys
  - FreeDesktop compliant trash utility integration
  - Cross-dir file/all/range selection
  - Create (with parents), rename, duplicate files and dirs
  - Create new file or directory (tree) on startup
  - Batch renamer for selection or dir
  - List input stream of file paths from stdin or plugin
  - Copy (as), move (as), delete, archive, link selection
  - Easily copy, move paths in system clipboard to current dir
  - Dir updates, notification on `cp`, `mv`, `rm` completion
  - Copy file paths to system clipboard on select
  - Launch apps, run commands, spawn a shell, toggle exe
  - Access context paths/files at prompt or spawned shell
  - Lock terminal after configurable idle timeout
  - Capture and show output of a program in help screen
  - Basic support for screen readers and braille displays

## installation

### Beginners

1. [Install](https://github.com/jarun/nnn/wiki/Usage#installation) `nnn`, preferbly using the package manager.
2. Run the following command to generate (and optionally add to your rc file) a shell function to start with.
   ```sh
   sh -c "$(curl -Ls https://raw.githubusercontent.com/jarun/nnn/master/misc/quickstart.sh)"
   ```

Use the shell function name you chose to run `nnn` with your preferred configuration.

### Power users

1. [Install](https://github.com/jarun/nnn/wiki/Usage) `nnn` and the dependencies you need.
2. The desktop opener is default. Use `-e` to open text files in the terminal. Optionally [open detached](https://github.com/jarun/nnn/wiki/Basic-use-cases#detached-text).
3. Configure [cd on quit](https://github.com/jarun/nnn/wiki/Basic-use-cases#configure-cd-on-quit).
4. [Sync subshell](https://github.com/jarun/nnn/wiki/Basic-use-cases#sync-subshell-pwd) `$PWD` to `nnn`.
5. [Install plugins](https://github.com/jarun/nnn/tree/master/plugins#installation).
6. Use `-x` to sync selection to clipboard, show notis on `cp`, `mv`, `rm` and set xterm title.
7. For a CLI-only environment, set [`NNN_OPENER`](https://github.com/jarun/nnn/wiki/Usage#configuration) to [`nuke`](https://github.com/jarun/nnn/blob/master/plugins/nuke). Use option `-c`.
8. Bid `ls` goodbye! `alias ls='nnn -de'` :sunglasses:
9. Visit the [Live previews](https://github.com/jarun/nnn/wiki/Live-previews) and [Troubleshooting](https://github.com/jarun/nnn/wiki/Troubleshooting) Wiki pages.

Don't memorize! Arrows, <kbd>/</kbd>, <kbd>q</kbd> suffice. <kbd>Tab</kbd> creates and/or cycles contexts. <kbd>?</kbd> lists shortcuts.

[![](https://github.com/user-attachments/assets/e93f7571-8b8d-4703-bef1-93fc804adf7d)](https://www.youtube.com/embed/-knZwdd1ScU)

[![Wiki](https://img.shields.io/badge/RTFM-nnn%20Wiki-crimson?maxAge=2592000)](https://github.com/jarun/nnn/wiki)

## Videos

- [nnn file manager on Termux (Android)](https://www.youtube.com/embed/AbaauM7gUJw)
- [NNN File Manager](https://www.youtube.com/embed/1QXU4XSqXNo)
- [This Week in Linux 114 - TuxDigital](https://www.youtube.com/watch?v=5W9ja0DQjSY&t=2059s)
- [nnn file manager basics - Linux](https://www.youtube.com/embed/il2Fm-KJJfM)
- [I'M GOING TO USE THE NNN FILE BROWSER! 😮](https://www.youtube.com/embed/U2n5aGqou9E)
- [NNN: Is This Terminal File Manager As Good As People Say?](https://www.youtube.com/embed/KuJHo-aO_FA)
- [nnn - A File Manager (By Uoou, again.)](https://www.youtube.com/embed/cnzuzcCPYsk)

## Elsewhere

- [AddictiveTips](https://www.addictivetips.com/ubuntu-linux-tips/navigate-linux-filesystem/)
- [ArchWiki](https://wiki.archlinux.org/index.php/Nnn)
- [FOSSMint](https://www.fossmint.com/nnn-linux-terminal-file-browser/)
- [gHacks Tech News](https://www.ghacks.net/2019/11/01/nnn-is-an-excellent-command-line-based-file-manager-for-linux-macos-and-bsds/)
- Hacker News [[1](https://news.ycombinator.com/item?id=18520898)] [[2](https://news.ycombinator.com/item?id=19850656)]
- [It's FOSS](https://itsfoss.com/nnn-file-browser-linux/)
- [Linux Format Issue 265; Manage files with nnn](https://linuxformat.com/archives?issue=265)
- LinuxLinks [[1](https://www.linuxlinks.com/nnn-fast-and-flexible-file-manager/)] [[2](https://www.linuxlinks.com/bestconsolefilemanagers/)] [[3](https://www.linuxlinks.com/excellent-system-tools-nnn-portable-terminal-file-manager/)]
- [Linux Magazine; FOSSPicks](https://www.linux-magazine.com/Issues/2017/205/FOSSPicks/(offset)/15)
- [Make Tech Easier](https://www.maketecheasier.com/nnn-file-manager-terminal/)
- [Opensource.com](https://opensource.com/article/22/12/linux-file-manager-nnn)
- [Open Source For You](https://www.opensourceforu.com/2019/12/nnn-this-feature-rich-terminal-file-manager-will-enhance-your-productivity/)
- [PCLinuxOS Magazine Issue June 2021](https://pclosmag.com/html/Issues/202106/page08.html)
- [Suckless Rocks](https://suckless.org/rocks/)
- [Ubuntu Full Circle Magazine Issue 135; Review: nnn](https://fullcirclemagazine
