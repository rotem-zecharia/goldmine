# pranshuparmar/witr

Why is this running? Trace any process, port, container, or file back to what started it - CLI + TUI.

## features

Trace any process, port, container, or file back to the exact chain that started it —<br>
one command, machine-readable JSON, or an [interactive TUI](#3-interactive-mode-tui).

[![Latest Release](https://img.shields.io/github/v/release/pranshuparmar/witr?label=Latest%20Release&style=flat-square)](https://github.com/pranshuparmar/witr/releases/latest) [![Platforms](https://img.shields.io/badge/platforms-linux%20%7C%20macos%20%7C%20windows%20%7C%20freebsd-blue?style=flat-square)](#8-platform-support) <br> [![Package Managers](https://img.shields.io/badge/Package%20Managers-brew%20|%20conda%20|%20aur%20|%20winget%20|%20npm%20|%20ports%20|%20...%20-blue?style=flat-square)](https://repology.org/project/witr/versions)

<a href="https://trendshift.io/repositories/18714" target="_blank"><img src="https://trendshift.io/api/badge/repositories/18714" alt="pranshuparmar/witr on Trendshift" width="250" height="55" /></a>
<a href="https://www.producthunt.com/products/witr?embed=true&amp;utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=badge-witr" target="_blank" rel="noopener noreferrer"><img alt="witr - Why is this running? Trace process, port, container or file. | Product Hunt" width="250" height="54" src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1211309&amp;theme=light&amp;t=1785480480150"></a>

### 🎮 [**Try witr in your browser →**](https://pranshuparmar.github.io/witr/)
*Investigate a simulated Linux box — a guided tutorial and free-play sandbox, no install required.*

<a href="https://pranshuparmar.github.io/witr/"><img width="1232" alt="witr's interactive TUI and CLI answering why a node process is running — the same systemd → PM2 → node chain in both" src="https://github.com/user-attachments/assets/dbe271ad-25e5-425b-b414-392d0c4eee37" /></a>

</div>

---

<div align="center">

[**Purpose**](#1-purpose) • [**Installation**](#2-installation) • [**TUI**](#3-interactive-mode-tui) • [**Flags**](#4-flags--options) • [**Core Concept**](#5-core-concept) • [**Examples**](#6-example-outputs)
<br>
[**Output Behavior**](#7-output-behavior) • [**Platforms**](#8-platform-support) • [**Success Criteria**](#9-success-criteria) • [**Sponsors**](#10-sponsors)

</div>

---

## 1. Purpose

**witr** exists to answer a single question:

> **Why is this running?**

When something is running on a system, whether it is a process, a service, or something bound to a port, there is always a cause. That cause is often indirect, non-obvious, or spread across multiple layers such as supervisors, containers, services, or shells.

Existing tools (`ps`, `top`, `lsof`, `ss`, `systemctl`, `docker ps`) expose state and metadata. They show _what_ is running, but leave the user to infer _why_ by manually correlating outputs across tools.

**witr** makes that causality explicit.

It explains **where a running thing came from**, **how it was started**, and **what chain of systems is responsible for it existing right now**, in a single, human-readable output or an **interactive TUI dashboard**.

> 📖 Curious how witr came to be? [Read the story](https://medium.com/@pranshu.parmar/witr-why-is-this-running-a9a97cbedd18) or browse the [Hacker News discussion](https://news.ycombinator.com/item?id=46392910).

---

## installation

witr is distributed as a single static binary for Linux, macOS, FreeBSD, and Windows.

witr is also independently packaged and maintained across multiple operating systems and ecosystems. An up-to-date overview of packaging status is available on [Repology](https://repology.org/project/witr/versions). Please note that community packages may lag GitHub releases due to independent review and validation.

> [!TIP]
> If you use a package manager (Homebrew, Conda, Winget, etc.), we recommend installing via that for easier updates. Otherwise, the install script is the quickest way to get started.

---

### 2.1 Quick Install

#### Unix (Linux, macOS & FreeBSD)

```bash
curl -fsSL https://raw.githubusercontent.com/pranshuparmar/witr/main/install.sh | bash
```

<details>
<summary>Script Details</summary>

The script will:
- Detect your operating system (`linux`, `darwin` or `freebsd`)
- Detect your CPU architecture (`amd64` or `arm64`)
- Download the latest released binary and man page
- Install it to `/usr/local/bin/witr`
- Install the man page to `/usr/local/share/man/man1/witr.1`
- Pass INSTALL_PREFIX to override default install path

</details>

#### Windows (PowerShell)

```powershell
irm https://raw.githubusercontent.com/pranshuparmar/witr/main/install.ps1 | iex
```

<details>
<summary>Script Details</summary>

The script will:
- Download the latest release (zip) and verify checksum.
- Extract `witr.exe` to `%LocalAppData%\witr\bin`.
- Add the bin directory to your User `PATH`.

</details>

---

### 2.2 Package Managers

<details>
<summary><strong>APT (Debian, Ubuntu & Derivatives)</strong> <a href="https://packages.debian.org/sid/witr"><img src="https://repology.org/badge/version-for-repo/debian_unstable/witr.svg?style=flat-square" alt="Debian"></a></summary>
<br>


You can install **witr** from the official Debian and Ubuntu repositories (Ubuntu 26.04+, Debian sid and later), as well as derivative distributions like Kali Linux, Devuan, and Raspbian:

```bash
sudo apt install witr
```

> Note: The apt-shipped version may lag the latest GitHub release. For the newest features, use the install script or another installation method.
</details>

<details>
<summary><strong>Homebrew (macOS & Linux)</strong> <a href="https://formulae.brew.sh/formula/witr"><img src="https://img.shields.io/homebrew/v/witr?style=flat-square" alt="Homebrew"></a></summary>
<br>


You can install **witr** using [Homebrew](https://brew.sh/) on macOS or Linux:

```bash
brew install witr
```
</details>

<details>
<summary><strong>MacPorts (macOS)</strong> <a href="https://ports.macports.org/port/witr/"><img src="https://repology.org/badge/version-for-repo/macports/witr.svg?style=flat-square" alt="MacPorts"></a></summary>
<br>


You can install **witr** using [MacPorts](https://www.macports.org/) on macOS:

```bash
sudo port install witr
```
</details>

<details>
<summary><strong>Conda (macOS, Linux & Windows)</strong> <a href="https://anaconda.org/conda-forge/witr"><img src="https://img.shields.io/conda/vn/conda-forge/witr?style=flat-square" alt="Conda"></a></summary>
<br>


You can install **witr** using [conda](https://docs.conda.io/en/latest/), [mamba](https://mamba.readthedocs.io/en/latest/), or [pixi](https://pixi.prefix.dev/latest/) on macOS, Linux, and Windows:

```bash
conda install -c conda-forge witr
# alternatively using mamba
mamba install -c conda-forge witr
# alternatively using pixi
pixi global install witr
```
</details>

<details>
<summary><strong>Arch Linux (AUR)</strong> <a href="https://aur.archlinux.org/packages/witr-bin"><img src="https://img.shields.io/aur/version/witr-bin?style=flat-square" alt="AUR"></a></summary>
<br>


On Arch Linux and derivatives, install from the [AUR package](https://aur.archlinux.org/packages/witr-bin):

```bash
yay -S witr-bin
# alternatively using paru
paru -S witr-bin
# or use your preferred AUR helper
```
</details>

<details>
<summary><strong>Winget (Windows)</strong> <a href="https://winstall.app/apps/Prans

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

## 5. Core Concept

witr treats **everything as a process question**.

Ports, services, containers, and commands all eventually map to **PIDs**. Once a PID is identified, witr builds a causal chain explaining _why that PID exists_.

At its core, witr answers:

1. What is running?
2. How did it start?
3. What is keeping it running?
4. What context does it belong to?

---

## 6. Example Outputs

> 💡 Prefer learning by doing? The [interactive browser tutorial](https://pranshuparmar.github.io/witr/) walks you through outputs like these live on a simulated box — for a better feel of witr, no install required.

### 6.1 Name Based Query

```bash
witr node
```

```
Target      : node

Process     : node (pid 14233)
User        : pm2
Command     : node index.js
Started     : 2 days ago (Mon 2025-02-02 11:42:10 +05:30)

Why It Exists :
  systemd (pid 1) → pm2 (pid 5034) → node (pid 14233)

Source      : pm2

Working Dir : /opt/apps/expense-manager
Git Repo    : expense-manager (main)
Sockets     : 127.0.0.1:5001 (TCP | LISTENING)
```

---

### 6.2 Short Output

```bash
witr --port 5000 --short
```

```
systemd (pid 1) → PM2 v5.3.1: God (pid 1481580) → python (pid 1482060)
```

---

### 6.3 Tree Output

```bash
witr --pid 143895 --tree
```

```
systemd (pid 1)
  └─ init-systemd(Ub (pid 2)
    └─ SessionLeader (pid 143858)
      └─ Relay(143860) (pid 143859)
        └─ bash (pid 143860)
          └─ sh (pid 143886)
            └─ node (pid 143895)
              ├─ node (pid 143930)
              ├─ node (pid 144189)
              └─ node (pid 144234)
```

Note: _Tree view includes child processes (up to 10) and highlights the target process._

---

### 6.4 Multiple Matches

```bash
witr ng
```

```
Multiple matching processes found:

[1] nginx (pid 2311)
    nginx -g daemon off;
[2] nginx (pid 24891)
    nginx -g daemon off;
[3] ngrok (pid 14233)
    ngrok http 5000

Re-run with:
  witr --pid <pid>
```

To avoid substring matching and only find processes with an exact name, use the `--exact` flag:

```bash
witr nginx -x
```

---

### 6.5 File Based Query

```bash
witr --file /var/lib/dpkg/lock
```

Explains the process holding a file open.

---

### 6.6 Container Based Query

```bash
witr --container redis
```

Loo
