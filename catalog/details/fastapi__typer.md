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

## requirements

**Typer** requires only a few dependencies (most are tiny):

* [`rich`](https://rich.readthedocs.io/en/stable/index.html): to show nicely formatted errors automatically.
* [`shellingham`](https://github.com/sarugaku/shellingham): to automatically detect the current shell when installing completion.
* [`annotated-doc`](https://github.com/fastapi/annotated-doc): to generate documentation from Python type annotations.
* [`colorama`](https://github.com/tartley/colorama) (only on Windows): for producing colored terminal text on Windows.
