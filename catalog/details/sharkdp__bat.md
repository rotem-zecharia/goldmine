# sharkdp/bat

A cat(1) clone with wings.

## tools

#### `fzf`

You can use `bat` as a previewer for [`fzf`](https://github.com/junegunn/fzf). To do this,
use `bat`'s `--color=always` option to force colorized output. You can also use `--line-range`
option to restrict the load times for long files:

```bash
fzf --preview "bat --color=always --style=numbers --line-range=:500 {}"
```

For more information, see [`fzf`'s `README`](https://github.com/junegunn/fzf#preview-window).

#### `find` or `fd`

You can use the `-exec` option of `find` to preview all search results with `bat`:

```bash
find … -exec bat {} +
```

If you happen to use [`fd`](https://github.com/sharkdp/fd), you can use the `-X`/`--exec-batch` option to do the same:

```bash
fd … -X bat
```

#### `ripgrep`

With [`batgrep`](https://github.com/eth-p/bat-extras/blob/master/doc/batgrep.md), `bat` can be used as the printer for [`ripgrep`](https://github.com/BurntSushi/ripgrep) search results.

```bash
batgrep needle src/
```

#### `tail -f`

`bat` can be combined with `tail -f` to continuously monitor a given file with syntax highlighting.

```bash
tail -f /var/log/pacman.log | bat --paging=never -l log
```

Note that we have to switch off paging in order for this to work. We have also specified the syntax
explicitly (`-l log`), as it can not be auto-detected in this case.

#### `git`

You can combine `bat` with `git show` to view an older version of a given file with proper syntax
highlighting:

```bash
git show v0.6.0:src/main.rs | bat -l rs
```

#### `git diff`

You can combine `bat` with `git diff` to view lines around code changes with proper syntax
highlighting:
```bash
batdiff() {
    git diff --name-only --relative --diff-filter=d -z | xargs -0 bat --diff
}
```
If you prefer to use this as a separate tool, check out `batdiff` in [`bat-extras`](https://github.com/eth-p/bat-extras).

If you are looking for more support for git and diff operations, check out [`delta`](https://github.com/dandavison/delta).

#### `xclip`

The line numbers and Git modification markers in the output of `bat` can make it hard to copy
the contents of a file. To prevent this, you can call `bat` with the `-p`/`--plain` option or
simply pipe the output into `xclip`:
```bash
bat main.cpp | xclip
```
`bat` will detect that the output is being redirected and print the plain file contents.

#### `man`

`bat` can be used as a colorizing pager for `man`, by setting the
`MANPAGER` environment variable:

```bash
export MANPAGER="bat -plman"
man 2 select
```
(on some older Debian or Ubuntu releases, the executable is named `batcat` instead of `bat`)

If you prefer to have this bundled in a new command, you can also use [`batman`](https://github.com/eth-p/bat-extras/blob/master/doc/batman.md).

Note that the [Manpage syntax](assets/syntaxes/02_Extra/Manpage.sublime-syntax) is developed in this repository and still needs some work.

#### `prettier` / `shfmt` / `rustfmt`

The [`prettybat`](https://github.com/eth-p/bat-extras/blob/master/doc/prettybat.md) script is a wrapper that will format code and print it with `bat`.

#### Highlighting `--help` messages

You can use `bat` to colorize help text: `$ cp --help | bat -plhelp`

You can also use a wrapper around this:

```bash
# in your .bashrc/.zshrc/*rc
alias bathelp='bat --plain --language=help'
help() {
    "$@" --help 2>&1 | bathelp
}
```

Then you can do `$ help cp` or `$ help git commit`.

When you are using `zsh`, you can also use global aliases to override `-h` and `--help` entirely:

```bash
alias -g -- -h='-h 2>&1 | bat --language=help --style=plain'
alias -g -- --help='--help 2>&1 | bat --language=help --style=plain'
```

For `fish`, you can use abbreviations:

```fish
abbr -a --position anywhere -- --help '--help | bat -plhelp'
abbr -a --position anywhere -- -h '-h | bat -plhelp'
```

This way, you can keep on using `cp --help`, but get colorized help pages.

> [!TIP]
> To remove these abbreviations later, run:
> ```fish
> abbr -e -- --help
> abbr -e -- -h
> ```
> The `--` before the abbre

## installation

<!--

Installation instructions need to:
* be for widely used systems
* be non-obvious
* be from somewhat official sources

-->

[![Packaging status](https://repology.org/badge/vertical-allrepos/bat-cat.svg?columns=3&exclude_unsupported=1)](https://repology.org/project/bat-cat/versions)

### On Ubuntu (using `apt`)
*... and other Debian-based Linux distributions.*

`bat` is available on [Ubuntu since 20.04 ("Focal")](https://packages.ubuntu.com/search?keywords=bat&exact=1) and [Debian since August 2021 (Debian 11 - "Bullseye")](https://packages.debian.org/bullseye/bat).

If your Ubuntu/Debian installation is new enough you can simply run:

```bash
sudo apt install bat
```

**Important**: On some older Ubuntu/Debian releases, the executable is installed as `batcat` instead of `bat` (due to [a name
clash with another package](https://github.com/sharkdp/bat/issues/982)). On newer releases, the executable is available as `bat`. If `bat --version` does not work after installation, try `batcat --version` instead. You can set up a `bat -> batcat` symlink or alias to prevent any issues that may come up because of this and to be consistent with other distributions:
``` bash
mkdir -p ~/.local/bin
ln -s /usr/bin/batcat ~/.local/bin/bat
```

an example alias for `batcat` as `bat`:
```bash
alias bat="batcat"
```

### On Ubuntu (using most recent `.deb` packages)
*... and other Debian-based Linux distributions.*

If the package has not yet been promoted to your Ubuntu/Debian installation, or you want
the most recent release of `bat`, download the latest `.deb` package from the
[release page](https://github.com/sharkdp/bat/releases) and install it via:

```bash
sudo dpkg -i bat_0.18.3_amd64.deb  # adapt version number and architecture
```

### On Alpine Linux

You can install [the `bat` package](https://pkgs.alpinelinux.org/packages?name=bat)
from the official sources, provided you have the appropriate repository enabled:

```bash
apk add bat
```

### On Arch Linux

You can install [the `bat` package](https://www.archlinux.org/packages/extra/x86_64/bat/)
from the official sources:

```bash
pacman -S bat
```

### On Fedora

You can install [the `bat` package](https://packages.fedoraproject.org/pkgs/rust-bat/bat/) from the official sources:

```bash
dnf install bat
```

### On Gentoo Linux

You can install [the `bat` package](https://packages.gentoo.org/packages/sys-apps/bat)
from the official sources:

```bash
emerge sys-apps/bat
```

### On FreeBSD

You can install a precompiled [`bat` package](https://www.freshports.org/textproc/bat) with pkg:

```bash
pkg install bat
```

or build it on your own from the FreeBSD ports:

```bash
cd /usr/ports/textproc/bat
make install
```

### On OpenBSD

You can install `bat` package using [`pkg_add(1)`](https://man.openbsd.org/pkg_add.1):

```bash
pkg_add bat
```

### Via nix

You can install `bat` using the [nix package manager](https://nixos.org/nix):

```bash
nix-env -i bat
```

### On openSUSE

You can install `bat` with zypper:

```bash
zypper install bat
```

### Via snap package

There is currently no recommended snap package available.
Existing packages may be available, but are not officially supported and may contain [issues](https://github.com/sharkdp/bat/issues/1519).

### On macOS (or Linux) via Homebrew

You can install `bat` with [Homebrew](https://formulae.brew.sh/formula/bat):

```bash
brew install bat
```

### On macOS via MacPorts

Or install `bat` with [MacPorts](https://ports.macports.org/port/bat/summary):

```bash
port install bat
```

### On Windows

There are a few options to install `bat` on Windows. Once you have installed `bat`,
take a look at the ["Using `bat` on Windows"](#using-bat-on-windows) section.

#### Prerequisites

You will need to install the [Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist#latest-microsoft-visual-c-redistributable-version)

#### With WinGet

You can install `bat` via [WinGet](https://learn.micros

## configuration

`bat` can also be customized with a configuration file. The location of the file is dependent
on your operating system. To get the default path for your system, call
```bash
bat --config-file
```

Alternatively, you can use `BAT_CONFIG_PATH` or `BAT_CONFIG_DIR` environment variables to point `bat`
to a non-default location of the configuration file or the configuration directory respectively:
```bash
export BAT_CONFIG_PATH="/path/to/bat/bat.conf"
export BAT_CONFIG_DIR="/path/to/bat"
```

A default configuration file can be created with the `--generate-config-file` option.
```bash
bat --generate-config-file
```

There is also now a systemwide configuration file, which is located under `/etc/bat/config` on
Linux and Mac OS and `C:\ProgramData\bat\config` on windows. If the system wide configuration
file is present, the content of the user configuration will simply be appended to it.

### Format

The configuration file is a simple list of command line arguments. Use `bat --help` to see a full list of possible options and values. In addition, you can add comments by prepending a line with the `#` character.

Example configuration file:
```bash
# Set the theme to "TwoDark"
--theme="TwoDark"

# Show line numbers, Git modifications and file header (but no grid)
--style="numbers,changes,header"

## limitations

--italic-text=always

# Use C++ syntax for Arduino .ino files
--map-syntax "*.ino:C++"
```

## Using `bat` on Windows

`bat` mostly works out-of-the-box on Windows, but a few features may need extra configuration.

## requirements

You will need to install the [Visual C++ Redistributable](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads) package.

### Paging

Windows only includes a very limited pager in the form of `more`. You can download a Windows binary
for `less` [from its homepage](http://www.greenwoodsoftware.com/less/download.html) or [through
Chocolatey](https://chocolatey.org/packages/Less). To use it, place the binary in a directory in
your `PATH` or [define an environment variable](#using-a-different-pager). The [Chocolatey package](#on-windows) installs `less` automatically.

### Colors

Windows 10 natively supports colors in both `conhost.exe` (Command Prompt) and PowerShell since
[v1511](https://en.wikipedia.org/wiki/Windows_10_version_history#Version_1511_(November_Update)), as
well as in newer versions of bash. On earlier versions of Windows, you can use
[Cmder](http://cmder.app/), which includes [ConEmu](https://conemu.github.io/).

**Note:** Old versions of `less` do not correctly interpret colors on Windows. To fix this, you can add the optional Unix tools to your PATH when installing Git. If you don’t have any other pagers installed, you can disable paging entirely by passing `--paging=never` or by setting `BAT_PAGER` to an empty string.

### Cygwin

`bat` on Windows does not natively support Cygwin's unix-style paths (`/cygdrive/*`). When passed an absolute cygwin path as an argument, `bat` will encounter the following error: `The system cannot find the path specified. (os error 3)`

This can be solved by creating a wrapper or adding the following function to your `.bash_profile` file:

```bash
bat() {
    local index
    local args=("$@")
    for index in $(seq 0 ${#args[@]}) ; do
        case "${args[index]}" in
        -*) continue;;
        *)  [ -e "${args[index]}" ] && args[index]="$(cygpath --windows "${args[index]}")";;
        esac
    done
    command bat "${args[@]}"
}
```

## Troubleshooting

### Garbled output

If an input file contains color codes or other ANSI escape sequences or control characters, `bat` will have problems
performing syntax highlighting and text wrapping, and thus the output can become garbled.

If your version of `bat` supports the `--strip-ansi=auto` option, it can be used to remove such sequences
before syntax highlighting. Alternatively, you may disable both syntax highlighting and wrapping by
passing the `--color=never --wrap=never` options to `bat`.

For untrusted input, the `--sanitize=auto|always|never` option additionally replaces terminal-active
control bytes and Unicode bidi / zero-width formatting characters with the Unicode replacement
character. It implies `--strip-ansi` at the same value.

> [!NOTE]
> The `auto` option of `--strip-ansi` avoids removing escape sequences when the syntax is plain text.

### Terminals & colors

`bat` handles terminals *with* and *without* truecolor support. However, the colors in most syntax
highlighting themes are not optimized for 8-bit colors. It is therefore strongly recommended
that you use a terminal with 24-bit truecolor support (`terminator`, `konsole`, `iTerm2`, ...),
or use one of the basic [8-bit themes](#8-bit-themes) designed for a restricted set of colors.
See [this article](https://gist.github.com/XVilka/8346728) for more details and a full list of
terminals with truecolor support.

Make sure that your truecolor terminal sets the `COLORTERM` variable to either `truecolor` or
`24bit`. Otherwise, `bat` will not be able to determine whether or not 24-bit escape sequences
are supported (and fall back to 8-bit colors).

### Line numbers and grid are hardly visible

Please try a different theme (see `bat --list-themes` for a list). The `OneHalfDark` and
`OneHalfLight` themes provide grid and line colors that are brighter.

### File encodings

`bat` natively supports UTF-8 as well as UTF-16. For every other file encoding, you may need to
convert to UTF-8 first because the encodings can typically not be auto-d
