# junegunn/fzf

:cherry_blossom: A command-line fuzzy finder

## tools

fzf will launch interactive finder, read the list from STDIN, and write the
selected item to STDOUT.

```sh
find * -type f | fzf > selected
```

Without STDIN pipe, fzf will traverse the file system under the current
directory to get the list of files.

```sh
vim $(fzf)
```

> [!NOTE]
> You can override the default behavior
> * Either by setting `$FZF_DEFAULT_COMMAND` to a command that generates the desired list
> * Or by setting `--walker`, `--walker-root`, and `--walker-skip` options in `$FZF_DEFAULT_OPTS`

> [!WARNING]
> A more robust solution would be to use `xargs` but we've presented
> the above as it's easier to grasp
> ```sh
> fzf --print0 | xargs -0 -o vim
> ```

> [!TIP]
> fzf also has the ability to turn itself into a different process.
>
> ```sh
> fzf --bind 'enter:become(vim {})'
> ```
>
> *See [Turning into a different process](#turning-into-a-different-process)
> for more information.*

## configuration

- `FZF_DEFAULT_COMMAND`
    - Default command to use when input is tty
    - e.g. `export FZF_DEFAULT_COMMAND='fd --type f'`
- `FZF_DEFAULT_OPTS`
    - Default options
    - e.g. `export FZF_DEFAULT_OPTS="--layout=reverse --inline-info"`
- `FZF_DEFAULT_OPTS_FILE`
    - If you prefer to manage default options in a file, set this variable to
      point to the location of the file
    - e.g. `export FZF_DEFAULT_OPTS_FILE=~/.fzfrc`

> [!WARNING]
> `FZF_DEFAULT_COMMAND` is not used by shell integration due to the
> slight difference in requirements.
>
> * `CTRL-T` runs `$FZF_CTRL_T_COMMAND` to get a list of files and directories
> * `ALT-C` runs `$FZF_ALT_C_COMMAND` to get a list of directories
> * `vim ~/**<tab>` runs `fzf_compgen_path()` with the prefix (`~/`) as the first argument
> * `cd foo**<tab>` runs `fzf_compgen_dir()` with the prefix (`foo`) as the first argument
>
> The available options are described later in this document.

## installation

_fzf_setup_completion path ag git kubectl
_fzf_setup_completion dir tree
```

#### Custom fuzzy completion

_**(Custom completion API is experimental and subject to change)**_

For a command named _"COMMAND"_, define `_fzf_complete_COMMAND` function using
`_fzf_complete` helper.

```sh
