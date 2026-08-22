# HKUDS/nanobot

Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps

## features

- **Persistent workflows**: goals, memory, tools, and chat context survive long-running work.
- **Chat-native reach**: WebUI, API, Telegram, Feishu, Slack, Discord, Teams, email, and Mattermost.
- **Model freedom**: OpenAI-compatible APIs, local LLMs, image generation, search, and fallbacks.
- **Small core**: readable internals with MCP, memory, deployment, and automation built in.
- **Own your stack**: inspect, customize, self-host, and extend without a giant platform.

## installation

> [!IMPORTANT]
> If you want the newest features and experiments, install from source.
>
> If you want the most stable day-to-day experience, install from PyPI or with `uv`.

Pick **one** install method:

| Track | Install with | Update with | What runs |
|---|---|---|---|
| Stable | installer, `uv`, or pip | the same package tool | one released Python/WebUI/TUI version |
| Current source | editable Git checkout | `git pull --ff-only` + editable dependency sync | Python, WebUI, and TUI from that checkout |

Prerequisites: Python 3.11 or newer. Git and [Bun](https://bun.sh/) are only needed for a source install. Published packages include the WebUI and fetch a checksummed, version-matched TUI archive—with its licenses, notices, corresponding application source, source offer, and relinking instructions—on first use.

If terminals, API keys, or config files are new to you, use the guided zero-background walkthrough in [Start Without Technical Background](./docs/start-without-technical-background.md) instead of this compact README path.

**One-command setup**

macOS / Linux:

```bash
curl -fsSL https://raw.githubusercontent.com/HKUDS/nanobot/main/scripts/install.sh | sh
```

Windows PowerShell:

```powershell
irm https://raw.githubusercontent.com/HKUDS/nanobot/main/scripts/install.ps1 | iex
```

The default command installs or upgrades `nanobot-ai` from PyPI. On a fresh local desktop, it then starts `nanobot webui` so you can configure the first provider and model in **Settings → Models**. SSH, headless, existing-config, and older-release paths keep the terminal setup wizard. The installer avoids system-wide pip installs by using an active virtual environment, `uv`, `pipx`, or a managed venv under `~/.nanobot/venv`. It also prints the exact command it used to run nanobot; reuse that full command below if `nanobot` is not on `PATH`.

To preview the plan without changing your environment, pass `--dry-run`.

```bash
curl -fsSL https://raw.githubusercontent.com/HKUDS/nanobot/main/scripts/install.sh | sh -s -- --dry-run
```

```powershell
& ([scriptblock]::Create((irm https://raw.githubusercontent.com/HKUDS/nanobot/main/scripts/install.ps1))) --dry-run
```

If you prefer to inspect the script first, open [`scripts/install.sh`](./scripts/install.sh) or [`scripts/install.ps1`](./scripts/install.ps1).

**Install with `uv`**

```bash
uv tool install nanobot-ai
```

**Install from PyPI with pip**

```bash
python -m pip install nanobot-ai
```

If pip reports `externally-managed-environment` on macOS or Linux, use the one-command installer, `uv tool install nanobot-ai`, `pipx install nanobot-ai`, or install inside a virtual environment.

**Install from source**

Clone the repository and install it in editable mode. Bun is required because the source
checkout runs the matching TUI directly instead of downloading an older release binary.

```bash
git clone https://github.com/HKUDS/nanobot.git
cd nanobot
python -m venv .venv
```

Activate it with `source .venv/bin/activate` on macOS/Linux or
`.venv\Scripts\Activate.ps1` in Windows PowerShell, then run:

```bash
python -m pip install -e .
```

After that, the normal commands are identical to a stable install. `nanobot agent` runs the TUI
from this checkout, and `nanobot webui` rebuilds stale frontend assets automatically. A later
`git pull --ff-only` updates the Python, TUI, and WebUI source together; rerun
`python -m pip install -e .` when Python dependencies change. Contributors should also read
[`CONTRIBUTING.md`](./CONTRIBUTING.md).

Verify the install:

```bash
nanobot --version
```

If `nanobot` is not on `PATH`, invoke it through the method that installed it: reuse the recommended installer's command, use `uv tool run --from nanobot-ai nanobot ...` or `pipx run --spec nanobot-ai nanobot ...`, or use the Python executable from the environment where pip installed the package.

## 🚀 Quick Start

**Open nanobot in your browser**

```bash
nanobot webui
```

This is the recommended first run. Th
