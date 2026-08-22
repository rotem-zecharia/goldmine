# ajeetdsouza/zoxide

A smarter cd command. Supports all major shells.

## installation

![Tutorial][tutorial]

```sh
z foo              # cd into highest ranked directory matching foo
z foo bar          # cd into highest ranked directory matching foo and bar
z foo /            # cd into a subdirectory starting with foo

z ~/foo            # z also works like a regular cd command
z foo/             # cd into relative path
z ..               # cd one level up
z -                # cd into previous directory

zi foo             # cd with interactive selection (using fzf)

z foo<SPACE><TAB>  # show interactive completions (bash 4.4+/fish/zsh only)
```

Read more about the matching algorithm [here][algorithm-matching].

## Installation

zoxide can be installed in 4 easy steps:

1. **Install binary**

   zoxide runs on most major platforms. If your platform isn't listed below,
   please [open an issue][issues].

   <details>
   <summary>Linux / WSL</summary>

   > The recommended way to install zoxide is via the install script:
   >
   > ```sh
   > curl -sSfL https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | sh
   > ```
   >
   > Or, you can use a package manager:
   >
   > | Distribution        | Repository              | Instructions                                                      |
   > | ------------------- | ----------------------- | ----------------------------------------------------------------- |
   > | **_Any_**           | **[crates.io]**         | `cargo install zoxide --locked`                                   |
   > | _Any_               | [conda-forge]           | `conda install -c conda-forge zoxide`                             |
   > | _Any_               | [guix]                  | `guix install zoxide`                                             |
   > | _Any_               | [Linuxbrew]             | `brew install zoxide`                                             |
   > | _Any_               | [nixpkgs]               | `nix-env -iA nixpkgs.zoxide`                                      |
   > | Alpine Linux 3.13+  | [Alpine Linux Packages] | `apk add zoxide`                                                  |
   > | Arch Linux          | [Arch Linux Extra]      | `pacman -S zoxide`                                                |
   > | ~~Debian~~[^1]      | ~~[Debian Packages]~~   | ~~`apt install zoxide`~~                                          |
   > | Devuan 4.0+         | [Devuan Packages]       | `apt install zoxide`                                              |
   > | Exherbo Linux       | [Exherbo packages]      | `cave resolve -x repository/rust` <br /> `cave resolve -x zoxide` |
   > | Fedora 32+          | [Fedora Packages]       | `dnf install zoxide`                                              |
   > | Gentoo              | [Gentoo Packages]       | `emerge app-shells/zoxide`                                        |
   > | Manjaro             |                         | `pacman -S zoxide`                                                |
   > | openSUSE Tumbleweed | [openSUSE Factory]      | `zypper install zoxide`                                           |
   > | ~~Parrot OS~~[^1]   |                         | ~~`apt install zoxide`~~                                          |
   > | ~~Raspbian~~[^1]    | ~~[Raspbian Packages]~~ | ~~`apt install zoxide`~~                                          |
   > | Rhino Linux         | [Pacstall Packages]     | `pacstall -I zoxide-deb`                                          |
   > | Slackware 15.0+     | [SlackBuilds]           | [Instructions][slackbuilds-howto]                                 |
   > | Solus               | [Solus Packages]        | `eopkg install zoxide`                                            |
   > | ~~Ubuntu~~[^1]      | ~~[Ubuntu Packages]~~   | ~~`apt install zoxide`~~                                          |
   > | Void Linux          | [Void Linux Packages]   | `xbps-install -S zoxide`                                          |

   </details>

   <details>
   <summary>macOS</summary>


## configuration

### Flags

When calling `zoxide init`, the following flags are available:

- `--cmd`
  - Changes the prefix of the `z` and `zi` commands.
  - `--cmd j` would change the commands to (`j`, `ji`).
  - `--cmd cd` would replace the `cd` command.
- `--hook <HOOK>`
  - Changes how often zoxide increments a directory's score:

    | Hook            | Description                       |
    | --------------- | --------------------------------- |
    | `none`          | Never                             |
    | `prompt`        | At every shell prompt             |
    | `pwd` (default) | Whenever the directory is changed |

- `--no-cmd`
  - Prevents zoxide from defining the `z` and `zi` commands.
  - These functions will still be available in your shell as `__zoxide_z` and
    `__zoxide_zi`, should you choose to redefine them.

### Environment variables

Environment variables[^2] can be used for configuration. They must be set before
`zoxide init` is called.

- `_ZO_DATA_DIR`
  - Specifies the directory in which the database is stored.
  - The default value varies across OSes:

    | OS          | Path                                     | Example                                    |
    | ----------- | ---------------------------------------- | ------------------------------------------ |
    | Linux / BSD | `$XDG_DATA_HOME` or `$HOME/.local/share` | `/home/alice/.local/share`                 |
    | macOS       | `$HOME/Library/Application Support`      | `/Users/Alice/Library/Application Support` |
    | Windows     | `%LOCALAPPDATA%`                         | `C:\Users\Alice\AppData\Local`             |

- `_ZO_ECHO`
  - When set to 1, `z` will print the matched directory before navigating to
    it.
- `_ZO_EXCLUDE_DIRS`
  - Excludes the specified directories from the database.
  - This is provided as a list of [globs][glob], separated by OS-specific
    characters:

    | OS                  | Separator | Example                 |
    | ------------------- | --------- | ----------------------- |
    | Linux / macOS / BSD | `:`       | `$HOME:$HOME/private/*` |
    | Windows             | `;`       | `$HOME;$HOME/private/*` |

  - By default, this is set to `"$HOME"`.
- `_ZO_FZF_OPTS`
  - Custom options to pass to [fzf] during interactive selection. See
    [`man fzf`][fzf-man] for the list of options.
- `_ZO_MAXAGE`
  - Configures the [aging algorithm][algorithm-aging], which limits the maximum
    number of entries in the database.
  - By default, this is set to 10000.
- `_ZO_RESOLVE_SYMLINKS`
  - When set to 1, `z` will resolve symlinks before adding directories to the
    database.

## Third-party integrations

| Application           | Description                                  | Plugin                     |
| --------------------- | -------------------------------------------- | -------------------------- |
| [aerc]                | Email client                                 | Natively supported         |
| [alfred]              | macOS launcher                               | [alfred-zoxide]            |
| [clink]               | Improved cmd.exe for Windows                 | [clink-zoxide]             |
| [emacs]               | Text editor                                  | [zoxide.el]                |
| [felix]               | File manager                                 | Natively supported         |
| [joshuto]             | File manager                                 | Natively supported         |
| [lf]                  | File manager                                 | See the [wiki][lf-wiki]    |
| [nnn]                 | File manager                                 | [nnn-autojump]             |
| [ranger]              | File manager                                 | [ranger-zoxide]            |
| [raycast]             | macOS launcher                               | [raycast-zoxide]           |
| [rfm]                 | File manager                                 | Natively supported         |
| [sesh]         
