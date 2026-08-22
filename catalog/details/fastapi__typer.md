# fastapi/typer

Typer, build great CLIs. Easy to code. Based on Python type hints.

## tools

**Typer** is [FastAPI](https://fastapi.tiangolo.com)'s little sibling, it's the FastAPI of CLIs.

## installation

First, [install `uv`](https://docs.astral.sh/uv/getting-started/installation/), and then add **Typer** to your project:

<div class="termy">

```console
$ uv add typer
---> 100%
```

</div>

This installs both the Typer library and the `typer` command in the project's virtual environment. To use `typer` directly with shell completion, [activate the project environment and install completion](tutorial/install.md#activate-the-virtual-environment).

If you prefer to use `pip`, install `typer` inside a virtual environment. See the [installation guide](tutorial/install.md) for the alternative steps.

## Example

### The absolute minimum

* Create a file `main.py` with:

```Python
def main(name: str):
    print(f"Hello {name}")
```

This script doesn't even use Typer internally. But you can use the `typer` command to run it as a CLI application.

### Run it

Run your application with the `typer` command:

<div class="termy">

```console
// Run your application
$ typer main.py run

// You get a nice error, you are missing 'name'
Usage: typer [PATH_OR_MODULE] run [OPTIONS] {name}
Try 'typer [PATH_OR_MODULE] run --help' for help.
╭─ Error ───────────────────────────────────────────╮
│ Missing argument 'name'.                          │
╰───────────────────────────────────────────────────╯


// You get a --help for free
$ typer main.py run --help

Usage: typer [PATH_OR_MODULE] run [OPTIONS] {name}

Run the provided Typer app.

╭─ Arguments ───────────────────────────────────────╮
│ *    name      <str>  [required]                  │
╰───────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────╮
│ --help          Show this message and exit.       │
╰───────────────────────────────────────────────────╯

// Now pass the 'name' argument
$ typer main.py run Camila

Hello Camila

// It works! 🎉
```

</div>

This is the simplest use case, not even using Typer internally, but it can already be quite useful for simple scripts.

**Note**: auto-completion works when you create a Python package and run it with `--install-completion` or when you use the `typer` command.

## Use Typer in your code

Now let's start using Typer in your own code, update `main.py` with:

```Python
import typer


def main(name: str):
    print(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
```

Now you could run it with Python directly:

<div class="termy">

```console
// Run your application
$ uv run python main.py

// You get a nice error, you are missing 'name'
Usage: main.py [OPTIONS] {name}
Try 'main.py --help' for help.
╭─ Error ───────────────────────────────────────────╮
│ Missing argument 'name'.                          │
╰───────────────────────────────────────────────────╯


// You get a --help for free
$ uv run python main.py --help

Usage: main.py [OPTIONS] {name}

╭─ Arguments ───────────────────────────────────────╮
│ *    name      <str>  [required]                  │
╰───────────────────────────────────────────────────╯
╭─ Options ─────────────────────────────────────────╮
│ --help          Show this message and exit.       │
╰───────────────────────────────────────────────────╯

// Now pass the 'name' argument
$ uv run python main.py Camila

Hello Camila

// It works! 🎉
```

</div>

**Note**: you can also call this same script with the `typer` command, but you don't need to.

## Example upgrade

This was the simplest example possible.

Now let's see one a bit more complex.

## requirements

**Typer** requires only a few dependencies (most are tiny):

* [`rich`](https://rich.readthedocs.io/en/stable/index.html): to show nicely formatted errors automatically.
* [`shellingham`](https://github.com/sarugaku/shellingham): to automatically detect the current shell when installing completion.
* [`annotated-doc`](https://github.com/fastapi/annotated-doc): to generate documentation from Python type annotations.
* [`colorama`](https://github.com/tartley/colorama) (only on Windows): for producing colored terminal text on Windows.

### Click code

Typer used to depend on [Click](https://click.palletsprojects.com/) as well, a popular tool for building CLIs in Python.

Since version 0.26.0, Typer has vendored Click (included Click's source code internally, instead of installing it as a third party package) and has unified the code interactions between Typer and the embedded Click source code for easier maintainability in the future.

Note that some Click functionality will not be available anymore in the future, as we continue to improve and extend Typer's codebase.

### `typer-slim`

There used to be a slimmed-down version of Typer called `typer-slim`, which didn't include the dependencies `rich` and `shellingham`, nor the `typer` command.

However, since version 0.22.0, we have stopped supporting this, and `typer-slim` now simply installs (all of) Typer.

If you want to disable Rich globally, you can set an environmental variable `TYPER_USE_RICH` to `False` or `0`.

## License

This project is licensed under the terms of the MIT license.
