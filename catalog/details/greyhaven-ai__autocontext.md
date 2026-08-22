# greyhaven-ai/autocontext

a recursive self-improving harness designed to help your agents (and future iterations of those agents) succeed on any task

## installation

| Surface             | Command                               |
| ------------------- | ------------------------------------- |
| Python CLI          | `uv tool install autocontext==0.16.1` |
| Python library/dev  | `uv pip install autocontext==0.16.1`  |
| TypeScript/Node CLI | `bun add -g autoctx@0.16.1`           |
| Pi extension        | `pi install npm:pi-autocontext@0.10.0` |

The PyPI package is `autocontext`; the CLI is `autoctx`. The npm package is `autoctx` (not the unrelated `autocontext` npm package). Provider variables live in [`.env.example`](.env.example).
The npm CLI and TUI require Node.js 22.19.0 or newer; contributors should use
the version pinned in [`ts/.nvmrc`](ts/.nvmrc).
