# o2sh/onefetch

Command-line Git information tool

## installation

Onefetch is available on Linux, macOS, and Windows platforms. Binaries for Linux, Windows, and macOS are available on the [release page](https://github.com/o2sh/onefetch/releases).

### Linux

- Ubuntu

  ```
  wget https://github.com/o2sh/onefetch/releases/latest/download/onefetch_amd64.deb && sudo dpkg -i ./onefetch_amd64.deb && rm onefetch_amd64.deb
  ```

- Arch Linux

  ```
  pacman -S onefetch
  ```

- openSUSE

  ```
  zypper install onefetch
  ```

### macOS

```
brew install onefetch
```

### Windows

```
winget install onefetch
```

## tools

```
onefetch /path/of/your/repo
```

Or

```
cd /path/of/your/repo
onefetch
```

## Customization

Onefetch can be customized via [command-line arguments](https://github.com/o2sh/onefetch/wiki/command-line-options) to display exactly what you want, the way you want it: adjust the text styling, disable info lines, ignore files and directories, output in multiple formats (JSON, YAML), etc.

## Frequently Asked Questions

## features

By default, onefetch only displays `programming` and `markup` languages. Languages classified as `prose` (like Org mode, Markdown, or Text) or `data` (like JSON, YAML, or TOML) are hidden unless you include them with `--type`.

```
onefetch --type programming markup prose data
```

### Why do duplicate authors appear?

Onefetch reads authors from the Git history. If the same person committed with different names or emails, they may appear more than once.

To merge those entries, add a [`.mailmap`](https://git-scm.com/docs/gitmailmap) file to the repository.

## Contributing

Currently, onefetch supports more than [100 different programming languages](https://onefetch.dev); if your language of choice isn't supported, open an issue and support will be added.

Contributions are very welcome! See [CONTRIBUTING](CONTRIBUTING.md) for more info.
