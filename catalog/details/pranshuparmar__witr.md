# pranshuparmar/witr

Why is this running? Trace any process, port, container, or file back to what started it - CLI + TUI.

## features

Trace any process, port, container, or file back to the exact chain that started it —<br>
one command, machine-readable JSON, or an [interactive TUI](#3-interactive-mode-tui).

[![Latest Release](https://img.shields.io/github/v/release/pranshuparmar/witr?label=Latest%20Release&style=flat-square)](https://github.com/pranshuparmar/witr/releases/latest) [![Platforms](https://img.shields.io/badge/platforms-linux%20%7C%20macos%20%7C%20windows%20%7C%20freebsd-blue?style=flat-square)](#8-platform-support) <br> [![Package Managers](https://img.shields.io/badge/Package%20Managers-brew%20|%20conda%20|%20aur%20|%20winget%20|%20npm%20|%20ports%20|%20...%20-blue?style=flat-square)](https://repology.org/project/witr/versions)

<a href="https://trendshift.io/repositories/18714" target="_blank"><img src="https://trendshift.io/api/badge/repositories/18714" alt="pranshuparmar/witr on Trendshift" width="250" height="55" /></a>
<a href="https://www.producthunt.com/products/witr?embed=true&amp;utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=badge-witr" target="_blank" rel="noopener noreferrer"><img alt="witr - Why is this running? Trace process, port, container or file. | Product Hunt" width="250" height="54" src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1211309&amp;theme=light&amp;t=1785480480150"></a>

## installation

witr is distributed as a single static binary for Linux, macOS, FreeBSD, and Windows.

witr is also independently packaged and maintained across multiple operating systems and ecosystems. An up-to-date overview of packaging status is available on [Repology](https://repology.org/project/witr/versions). Please note that community packages may lag GitHub releases due to independent review and validation.

> [!TIP]
> If you use a package manager (Homebrew, Conda, Winget, etc.), we recommend installing via that for easier updates. Otherwise, the install script is the quickest way to get started.

---

## configuration

```
  -c, --container strings container(s) to look up (repeatable)
      --env              show environment variables for the process
  -x, --exact            use exact name matching (no substring search)
  -f, --file strings     file(s) held open by a process (repeatable)
  -h, --help             help for witr
  -i, --interactive      interactive mode (TUI)
      --json             show result as JSON
      --no-color         disable colorized output
  -p, --pid strings      pid(s) to look up (repeatable)
  -o, --port strings     port(s) to look up (repeatable)
  -s, --short            show only ancestry
  -t, --tree             show only ancestry as a tree
      --verbose          show extended process information
  -v, --version          version for witr
      --warnings         show only warnings
```

Positional arguments (without flags) are treated as process or service names. Multiple names can be passed. By default, name matching uses substring matching (fuzzy search). Use `--exact` to match only processes with the exact name.

All target flags (`--pid`, `--port`, `--file`, `--container`) are repeatable and can be mixed with each other and with positional name arguments. When multiple targets are provided, results are shown sequentially with labeled dividers. All output modes (standard, short, tree, JSON, env, warnings, verbose) work with multiple inputs.

The `--container` flag searches across Docker, Podman, nerdctl, K8s/crictl, Incus, LXC, LXD, and FreeBSD jails, and matches against container name, image, command, and compose project/service labels.

The TUI is launched if no arguments or relevant flags (`--pid`, `--port`, `--file`, `--container`) are provided, or if the `--interactive` flag is explicitly used.

---
