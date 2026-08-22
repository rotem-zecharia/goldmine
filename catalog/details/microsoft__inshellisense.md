# microsoft/inshellisense

IDE style command line auto complete

## installation

**npm (recommended)**

```shell
npm install -g @microsoft/inshellisense
is init
```

**homebrew (macOS/linux)**

```shell
brew tap microsoft/inshellisense https://github.com/microsoft/inshellisense
brew install inshellisense
is init
```

## tools

| Action                                | Command | Description                                      |
| ------------------------------------- | ------- | ------------------------------------------------ |
| Start                                 | `is`    | Start inshellisense session on the current shell |
| Stop                                  | `exit`  | Stop inshellisense session on the current shell  |
| Check If Inside Inshellisense Session | `is -c` | Check if shell inside inshellisense session      |

#### Keybindings

All other keys are passed through to the shell. The keybindings below are only captured when the inshellisense suggestions are visible, otherwise they are passed through to the shell as well. These can be customized in the [config](#configuration).

| Action                    | Keybinding     |
| ------------------------- | -------------- |
| Accept Current Suggestion | <kbd>tab</kbd> |
| View Next Suggestion      | <kbd>↓</kbd>   |
| View Previous Suggestion  | <kbd>↑</kbd>   |
| Dismiss Suggestions       | <kbd>esc</kbd> |

## configuration

All configuration is done through a [toml](https://toml.io/) file. You can create this file at `~/.inshellisenserc` or `$XDG_CONFIG_HOME/inshellisense/rc.toml`. When `XDG_CONFIG_HOME` is unset, empty, or not an absolute path, the XDG configuration path defaults to `~/.config/inshellisense/rc.toml`. The [JSON schema](https://json-schema.org/) for the configuration file can be found [here](https://github.com/microsoft/inshellisense/blob/main/src/utils/config.ts).

On new Unix-like installations, generated resources are stored under `$XDG_DATA_HOME/inshellisense`. When `XDG_DATA_HOME` is unset, empty, or non-absolute, it defaults to `~/.local/share` as defined by the XDG specification. Existing installations continue using `~/.inshellisense` when that directory is present so current shell plugins keep working; Windows also keeps using that location. Running `is reinit` migrates legacy resources to the XDG data directory.
