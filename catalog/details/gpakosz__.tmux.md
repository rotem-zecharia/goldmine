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

Troubleshooting
---------------

  - **I believe something's not quite right**

    Please make sure no tmux client or server process is currently running.

    Then launch tmux with:
    ```
    $ tmux -f /dev/null -L test
    ```

    Which launches a new tmux client/server pair without loading any
    configuration.

    If the issue is still reproducing, please reach out to the tmux project for
    support.

    Otherwise, please open an issue describing what doesn't work and I'll do my
    best to address it.

  - **I tried to use `set`, `bind` and `unbind` in my `.local` customization
    file, but Oh my tmux! overwrites my preferences**

    When that happens append `#!important` to the line:

    ```
    bind c new-window -c '#{pane_current_path}' #!important
    ```

    ```
    set -g default-terminal "screen-256color" #!important
    ```

  - **Status line is broken and/or gets duplicated at the bottom of the screen**

    This could happen on Linux when the distribution provides a version of glib
    that received Unicode 9.0 upgrades (glib `>= 2.50.1`) while providing a
    version of glibc that didn't (glibc `< 2.26`). Typically VTE-based terminal
    emulators rely on glib's `g_unichar_iswide()` function while tmux relies on
    glibc's `wcwidth()` function. When these two functions disagree, display
    gets messed up. You may also configure `LC_CTYPE` to use a `UTF-8` locale.

    This can also happen on macOS when using iTerm2 and "Use Unicode version 9
    character widths" is enabled in `Preferen

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

Bindings
--------

tmux may be controlled from an attached client by using a key combination of a
prefix key, followed by a command key. This configuration uses `C-a` as a
secondary prefix while keeping `C-b` as the default prefix. In the following
list of key bindings:
  - `<prefix>` means you have to either hit <kbd>Ctrl</kbd> + <kbd>a</kbd> or <kbd>Ctrl</kbd> + <kbd>b</kbd>
  - `<prefix> c` means you have to hit <kbd>Ctrl</kbd> + <kbd>a</kbd> or <kbd>Ctrl</kbd> + <kbd>b</kbd> followed by <kbd>c</kbd>
  - `<prefix> C-c` means you have to hit <kbd>Ctrl</kbd> + <kbd>a</kbd> or <kbd>Ctrl</kbd> + <kbd>b</kbd> followed by <kbd>Ctrl</kbd> + <kbd>c</kbd>

This configuration uses the following bindings:

  - `<prefix> e` opens the `.local` customization file copy with the editor
    defined by the `VISUAL` or `EDITOR` environment variable (defaults to `vim`
    when empty)
  - `<prefix> r` reloads the configuration
  - `C-l` clears both the screen **and** the tmux history

  - `<prefix> C-c` creates a new session
  - `<prefix> C-f` lets you switch to another session by name
  - `<prefix> BTab` brings you to the last active session

  - `<prefix> C-h` and `<prefix> C-l` let you navigate windows left/right
    (default `<prefix> n` is unbound and `<prefix

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

### Enabling the Powerline look

Powerline originated as a status-line plugin for Vim. Its popular eye-catching
look is based on the use of special symbols:

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/user-attachments/assets/55afd317-150b-42f0-9ef3-fa619be7b160">
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/user-attachments/assets/55afd317-150b-42f0-9ef3-fa619be7b160">
    <img alt="Powerline symbols" src="https://github.com/user-attachments/assets/55afd317-150b-42f0-9ef3-fa619be7b160">
  </picture>
</p>

To make use of these symbols, there are several options:

  - Use a font that already bundles those: this is the case for the [Source Code
    Pro][source code pro] font
  - Use a [pre-patched font][powerline patched fonts]
  - Use your preferred font along with the standalone [Powerline font][powerline
    font] (that only contains the Powerline symbols): [this highly depends on
    your operating system and your terminal emulator][terminal support], for
    instance here's a screenshot of iTerm2 configured to use
    `PowerlineSymbols.otf` for non-ASCII symbols:
    <p align="center">
      <picture>
        <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/553208/62243890-8232f500-b3de-11e9-9b8c-51a5d38bdaa8.png">
        <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/553208/62243890-8232f500-b3de-11e9-9b8c-51a5d38bdaa8.png">
        <img alt="iTerm2 + Powerline font" src="https://user-images.githubusercontent.com/553208/62243890-8232f500-b3de-11e9-9b8c-51a5d38bdaa8.png">
      </picture>
    </p>

[source code pro]: https://github.com/adobe-fonts/source-code-pro/releases/latest
[powerline patched fonts]: https://github.com/powerline/fonts
[powerline font]: https://github.com/powerline/powerline/raw/develop/font/PowerlineSymbols.otf
[terminal support]: http://powerline.readthedocs.io/en/master/usage.html#usage-terminal-emulators

Then edit your `.local` customization file copy (with `<prefix> e`) and adjust
the following variables:

```
tmux_conf_theme_left_separator_main='\uE0B0'
tmux_conf_theme_left_separator_sub='\uE0B1'
tmux_conf_theme_right_separator_main='\uE0B2'
tmux_conf_theme_right_separator_sub='\uE0B3'
```

The [Powerline manual] contains further details on how to install fonts
containing the Powerline symbols.

[Powerline manual]: http://powerline.readthedocs.org/en/latest/installation.html#fonts-installation

### Configuring the status line

Edit your `.local` customization file copy (`<prefix> e`) and adjust the
`tmux_conf_theme_status_left` and `tmux_conf_theme_status_right` variables to
your liking.

This configuration supports the following builtin variables:

  - `#{battery_bar}`: horizontal battery charge bar
  - `#{battery_hbar}`: 1 character wide, horizontal battery charge bar
  - `#{battery_vbar}`: 1 character wide, vertical battery charge bar
  - `#{battery_percentage}`: battery percentage
  - `#{battery_status}`: is battery charging or discharging?
  - `#{circled_window_index}`: circled window number (from ⓪ to ⑳)
  - `#{circled_session_name}`: circled session number (from ⓪ to ⑳)
  - `#{hostname}`: SSH/Mosh aware hostname information
  - `#{hostname_full}`: SSH/Mosh aware fully qualified hostname
  - `#{hostname_ssh}`: SSH/Mosh aware hostname information, blank
