# pypa/pipx

Install and Run Python Applications in Isolated Environments

## installation

<p align="center">
<a href="https://github.com/pypa/pipx/raw/main/pipx_demo.gif">
<img src="https://github.com/pypa/pipx/raw/main/pipx_demo.gif"/>
</a>
</p>

<p align="center">
<a href="https://github.com/pypa/pipx/actions/workflows/tests.yml">
<img src="https://github.com/pypa/pipx/actions/workflows/tests.yml/badge.svg?event=push&branch=main" alt="image" /></a> <a href="https://badge.fury.io/py/pipx"><img src="https://badge.fury.io/py/pipx.svg" alt="PyPI version"></a> <a href="https://badge.fury.io/py/pipx"><img src="https://static.pepy.tech/badge/pipx"></a>

</p>

**Documentation**: <https://pipx.pypa.io>

**Source Code**: <https://github.com/pypa/pipx>

_For comparison to other tools including pipsi, see
[Comparison to Other Tools](https://pipx.pypa.io/stable/explanation/comparisons.html)._

## features

pipx is a tool to help you install and run end-user applications written in Python. It's roughly similar to macOS's
`brew`, JavaScript's [npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b), and
Linux's `apt`.

It's closely related to pip. In fact, it uses pip, but is focused on installing and managing Python packages that can be
run from the command line directly as applications.

### Features

`pipx` enables you to

- expose CLI entrypoints of packages ("apps") installed to isolated environments with the `install` command,
    guaranteeing no dependency conflicts and clean uninstalls;
- easily list, upgrade, and uninstall packages that were installed with pipx; and
- run the latest version of a Python application in a temporary environment with the `run` command.

Best of all, pipx runs with regular user permissions, never calling `sudo pip install`.
