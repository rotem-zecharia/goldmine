# gpakosz/.tmux

Oh my tmux! My self-contained, pretty & versatile tmux configuration made with 💛🩷💙🖤❤️🤍

## installation

**Requirements:**

  - tmux **`>= 2.6`** running on Linux, macOS, FreeBSD, OpenBSD, Windows
    (WSL or Cygwin — not recommended)
  - awk, perl (optionally with Time::HiRes support for sub-second timestamps),
    grep, and sed
  - Outside of tmux, the `TERM` environment variable must be set to
    `xterm-256color`

⚠️ Before installing, you may want to backup your existing configuration.

You can install Oh my tmux! at any of the following locations:
- `~`
- `$XDG_CONFIG_HOME/tmux`
- `~/.config/tmux`

**Automatic installation**

Copy the following command and paste it into your terminal.
```
curl -fsSL "https://github.com/gpakosz/.tmux/raw/refs/heads/master/install.sh#$(date +%s)" | bash
```

**Manual installation in `~`**
```
$ cd
$ git clone --single-branch https://github.com/gpakosz/.tmux.git
$ ln -s -f .tmux/.tmux.conf
$ cp .tmux/.tmux.conf.local .
```

**Manual installation in `$XDG_CONFIG_HOME/tmux`**
```
$ git clone --single-branch https://github.com/gpakosz/.tmux.git "/path/to/oh-my-tmux"
$ mkdir -p "$XDG_CONFIG_HOME/tmux"
$ ln -s /path/to/oh-my-tmux/.tmux.conf "$XDG_CONFIG_HOME/tmux/tmux.conf"
$ cp /path/to/oh-my-tmux/.tmux.conf.local "$XDG_CONFIG_HOME/tmux/tmux.conf.local"
```

**Manual installation in `~/.config/tmux`**
```
$ git clone --single-branch https://github.com/gpakosz/.tmux.git "/path/to/oh-my-tmux"
$ mkdir -p ~/.config/tmux
$ ln -s /path/to/oh-my-tmux/.tmux.conf ~/.config/tmux/tmux.conf
$ cp /path/to/oh-my-tmux/.tmux.conf.local ~/.config/tmux/tmux.conf.local
```
⚠️ When installing in `$XDG_CONFIG_HOME/tmux` or `~/.config/tmux`, the
configuration file names don't have a leading `.` character.

🚨 **You should never alter the main `.tmux.conf` or `tmux.conf` file. If you do,
you're on your own. Instead, every customization should happen in your
`.tmux.conf.local` or `tmux.conf.local` customization file copy.**

If you're a Vim user, setting the `VISUAL` or `EDITOR` environment variable to
`vim` will enable and further customize the `vi-style` key bindings (see tmux
manual).

If you're new to tmux, I recommend reading the [tmux getting started
guide][getting-started], as well as the [tmux 3: Productive Mouse-Free
Development][bhtmux3] book by [@bphogan].

Now proceed to [adjust] your `.local` customization file copy.

[getting-started]: https://github.com/tmux/tmux/wiki/Getting-Started
[bhtmux3]: https://pragprog.com/titles/bhtmux3/tmux-3/
[@bphogan]: https://bphogan.com/
[adjust]: #configuration

## features

- `C-a` acts as secondary prefix, while keeping default `C-b` prefix
  - Visual theme inspired by [Powerline][]
  - [Maximize any pane to a new window with `<prefix> +`][maximize-pane]
  - Mouse mode toggle with `<prefix> m`
  - Laptop battery status line information
  - Uptime status line information
  - Optional highlight of focused pane
  - Configurable new sessions, windows and panes behavior (to optionally retain
    the current path)
  - SSH/Mosh aware username and hostname status line information
  - SSH/Mosh aware pane splitting (with automatic reconnection to the remote
    server)
  - Copy to OS clipboard (needs `xsel`, `xclip`, or `wl-copy` on Linux)
  - Support for `\uXXXX` (BMP) and `\UXXXXXXXX` (supplementary plane) Unicode
    escapes
  - [PathPicker][] integration, if available
  - [Urlscan][] (preferred) or [Urlview][] integration, if available

[maximize-pane]: http://pempek.net/articles/2013/04/14/maximizing-tmux-pane-new-window/
[PathPicker]: https://facebook.github.io/PathPicker/
[Urlview]: https://packages.debian.org/stable/misc/urlview
[Urlscan]: https://github.com/firecat53/urlscan

The "Maximize any pane to a new window with `<prefix> +`" feature is different
from the builtin `resize-pane -Z` command, as it allows you to further split a
maximized pane. It's also more flexible by allowing you to maximize a pane to a
new window, then change window, then go back and the pane is still in maximized
state in its own window. You can then minimize a pane by using `<prefix> +`
either from the source window or the maximized window.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://cloud.githubusercontent.com/assets/553208/9890858/ee3c0ca6-5c02-11e5-890e-05d825a46c92.gif">
    <source media="(prefers-color-scheme: dark)" srcset="https://cloud.githubusercontent.com/assets/553208/9890858/ee3c0ca6-5c02-11e5-890e-05d825a46c92.gif">
    <img alt="Maximizing a pane" src="https://cloud.githubusercontent.com/assets/553208/9890858/ee3c0ca6-5c02-11e5-890e-05d825a46c92.gif">
  </picture>
</p>

Mouse mode allows you to set the active window, set the active pane, and resize
panes. It also switches automatically to copy-mode when you select text.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://cloud.githubusercontent.com/assets/553208/9890797/8dffe542-5c02-11e5-9c06-a25b452e6fcc.gif">
    <source media="(prefers-color-scheme: dark)" srcset="https://cloud.githubusercontent.com/assets/553208/9890797/8dffe542-5c02-11e5-9c06-a25b452e6fcc.gif">
    <img alt="Mouse mode" src="https://cloud.githubusercontent.com/assets/553208/9890797/8dffe542-5c02-11e5-9c06-a25b452e6fcc.gif">
  </picture>
</p>

## configuration

While this configuration tries to bring sane default settings, you may want to
customize it further to your needs.

🚨 Again, you should never alter the main `.tmux.conf` or `tmux.conf` file.
If you do, you're on your own.

Please refer to the sample `.local` customization file to know more about the
variables that allow you to alter different behaviors. Upon successful
installation, pressing `<prefix> e` will open your `.local` customization file
copy with the editor defined by the `VISUAL` or `EDITOR` environment variable
(defaults to `vim` when empty).
