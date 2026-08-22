# Osmantic/ODS

Turn your PC, Mac, or Linux box into an AI server. LLM inference, chat UI, voice, agents, workflows, RAG, and image generation.

## features

A handful of companies control the vast majority of global AI traffic — and with it, your data, your costs, and your uptime. Every query you send to a centralized provider is business intelligence you don’t own, running on infrastructure you don’t control, priced on terms you can’t negotiate.

If AI is becoming critical infrastructure, it shouldn’t be rented. Self-hosting local AI should be a sovereign human right, not a career choice.

Because running your own AI shouldn't require a CS degree and a weekend of debugging CUDA drivers. Right now, setting up local AI means stitching together a dozen projects, writing Docker configs from scratch, and praying everything talks to each other. Most people give up and go back to paying OpenAI.

We built ODS so you don't have to.

- **One command** — detects your GPU, picks the right model, generates credentials, launches everything
- **Chatting in under 2 minutes** — bootstrap mode gives you a working model instantly while your full model downloads in the background
- **Full service stack, pre-wired** — chat, agents, voice, workflows, search, RAG, image generation, privacy tools, observability, and developer tools. All talking to each other out of the box
- **Fully moddable** — every service is an extension. Drop in a folder, run `ods enable`, done

<details>
<summary><b>Manual install (Linux)</b></summary>

```bash
git clone https://github.com/Osmantic/ODS.git
cd ODS/ods
./install.sh
```

</details>

<details>
<summary><b>Windows (PowerShell)</b></summary>

Requires [Docker Desktop](https://www.docker.com/products/docker-desktop/) with WSL2 backend enabled.
**Install Docker Desktop first and make sure it is running before you start.**

Open a normal **PowerShell** session and run:

```powershell
$ProgressPreference = "SilentlyContinue"
$odsSrc = Join-Path $env:TEMP ("ods-install-" + [guid]::NewGuid().ToString("N"))
$odsZip = Join-Path $odsSrc "ods-main.zip"
New-Item -ItemType Directory -Path $odsSrc | Out-Null
Invoke-WebRequest "https://github.com/Osmantic/ODS/archive/refs/heads/main.zip" -OutFile $odsZip
Expand-Archive -LiteralPath $odsZip -DestinationPath $odsSrc -Force
cd (Get-ChildItem -LiteralPath $odsSrc -Directory | Select-Object -First 1).FullName
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\install.ps1
```

> The `Set-ExecutionPolicy` command allows the installer script to run in the current session. It does not change your system-wide policy.
> Running as Administrator is not recommended for the installer because user-level paths such as `.opencode`, `data/`, and `.env` can be created with admin-owned permissions.

The installer detects your GPU, picks the right model, generates credentials, starts all services, and creates a Desktop shortcut to the Dashboard. Manage from the runtime directory with `.\ods.ps1 status`; uninstall with `.\ods.ps1 uninstall --force`.

</details>

<details>
<summary><b>macOS (Apple Silicon)</b></summary>

Requires Apple Silicon (M1+) and [Docker Desktop](https://www.docker.com/products/docker-desktop/).
**Install Docker Desktop first and make sure it is running before you start.**

```bash
git clone https://github.com/Osmantic/ODS.git
cd ODS/ods
./install.sh
```

The installer detects your chip, picks the right model for your unified memory, launches llama-server natively with Metal acceleration, and starts all other services in Docker. Manage with `./ods-macos.sh status`.

See the [macOS Quickstart](ods/docs/MACOS-QUICKSTART.md) for details.

</details>

---
