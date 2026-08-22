# agentscope-ai/QwenPaw

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

## installation

### Option 1: Pip Install

If you prefer managing Python yourself (requires Python >= 3.11, < 3.14):

```bash
pip install qwenpaw
qwenpaw init --defaults
qwenpaw app
```

Then open the Console in your browser at **http://127.0.0.1:8088/** to configure your model. To chat in DingTalk, Lark, WeChat, etc., see the [Channel setup](https://qwenpaw.agentscope.io/docs/channels) documentation.

![Console](https://img.alicdn.com/imgextra/i2/O1CN01EP1ra01iOAcBvF0TC_!!6000000004402-2-tps-3822-2070.png)

---

### Option 2: Script Install

No Python setup required, one command installs everything. The script will automatically download uv (Python package manager), create a virtual environment, and install QwenPaw with all dependencies (including Node.js and frontend assets). Note: May not work in restricted network environments or corporate firewalls.

**macOS / Linux:**

```bash
curl -fsSL https://qwenpaw.agentscope.io/install.sh | bash
```

**Windows (CMD):**

```CMD
curl -fsSL https://qwenpaw.agentscope.io/install.bat -o install.bat && install.bat
```

**Windows (PowerShell):**

```powershell
irm https://qwenpaw.agentscope.io/install.ps1 | iex
```

> **Note**: The installer will automatically check the status of uv. If it is not installed, it will attempt to download and configure it automatically. If the automatic installation fails, please follow the on-screen prompts or execute `python -m pip install -U uv`, then rerun the installer.

> **⚠️ Special Notice for Windows Enterprise LTSC Users**
>
> If you are using Windows LTSC or an enterprise environment governed by strict security policies, PowerShell may run in **Constrained Language Mode**, potentially causing the following issue:
> 1. **If using CMD (.bat): Script executes successfully but fails to write to `Path`**
>
>    The script completes file installation. Due to **Constrained Language Mode**, it cannot automatically update environment variables. Manually configure as follows:
>    - **Locate the installation directory**:
>      - Check if `uv` is available: Enter `uv --version` in CMD. If a version number appears, **only configure the QwenPaw path**. If you receive the prompt `'uv' is not recognized as an internal or external command, operable program or batch file,` configure both paths.
>      - uv path (choose one based on installation location; use if `uv` fails): Typically `%USERPROFILE%\.local\bin`, `%USERPROFILE%\AppData\Local\uv`, or the `Scripts` folder within your Python installation directory
>      - QwenPaw path: Typically located at `%USERPROFILE%\.qwenpaw\bin`.
>    - **Manually add to the system's Path environment variable**:
>      - Press `Win + R`, type `sysdm.cpl` and press Enter to open System Properties.
>      - Click “Advanced” -> “Environment Variables”.
>      - Under “System variables”, locate and select `Path`, then click “Edit”.
>      - Click “New”, enter both directory paths sequentially, then click OK to save.
> 2. **If using PowerShell (.ps1): Script execution interrupted**
>
>   Due to **Constrained Language Mode**, the script may fail to automatically download `uv`.
>   - **Manually install uv**: Refer to the [GitHub Release](https://github.com/astral-sh/uv/releases) to download `uv.exe` and place it in `%USERPROFILE%\.local\bin` or `%USERPROFILE%\AppData\Local\uv`; or ensure Python is installed and run `python -m pip install -U uv`.
>   - **Configure `uv` environment variables**: Add the `uv` directory and `%USERPROFILE%\.qwenpaw\bin` to your system's `Path` variable.
>   - **Re-run the installation**: Open a new terminal and execute the installation script again to complete the `QwenPaw` installation.
>   - **Configure the `QwenPaw` environment variable**: Add `%USERPROFILE%\.qwenpaw\bin` to your system's `Path` variable.

Once installed, open a new terminal and run:

```bash
qwenpaw init --defaults   # or: qwenpaw init (interactive)
qwenpaw app
```

<details>
<summary><b>Install options</b></summary>

**macOS / Linux:**

```bash
# Insta

## tools

If you use a **cloud LLM API** (e.g., DashScope / Qwen, OpenAI, Anthropic, Google Gemini, DeepSeek, Kimi, OpenRouter, and more), you must configure an API key before chatting. QwenPaw will not work until a valid key is set. See the [official docs](https://qwenpaw.agentscope.io/docs/models) for details.

**How to configure:**

1. **Console (recommended)** — After running `qwenpaw app`, open **http://127.0.0.1:8088/** → **Settings** → **Models**. Choose a provider, enter the **API Key**, and enable that provider and model.
2. **`qwenpaw init`** — When you run `qwenpaw init`, it will guide you through configuring the LLM provider and API key. Follow the prompts to choose a provider and enter your key.
3. **Environment variable** — For DashScope you can set `DASHSCOPE_API_KEY` in your shell or in a `.env` file in the working directory.

Tools that need extra keys (e.g. `TAVILY_API_KEY` for web search) can be set in Console **Settings → Environment variables**, see [Config](https://qwenpaw.agentscope.io/docs/config) for details.

> **Using local models only?** If you use [Local Models](#local-models) (QwenPaw Local / Ollama / LM Studio), you do **not** need any API key.

## Local Models

QwenPaw can run LLMs entirely on your machine — no API keys or cloud services required. See the [official docs](https://qwenpaw.agentscope.io/docs/models) for details.

QwenPaw also provides the **QwenPaw-Flash** series — purpose-trained 2B / 4B / 9B models for agent scenarios, with Q4 and Q8 quantizations. Available on [ModelScope](https://www.modelscope.cn/organization/AgentScope?tab=model) and [Hugging Face](https://huggingface.co/agentscope-ai/models).

| Backend              | Best for                                 | Install                                                              |
| -------------------- | ---------------------------------------- | -------------------------------------------------------------------- |
| **QwenPaw Local** (llama.cpp) | Cross-platform (macOS / Linux / Windows) | Built-in; click "Download" in the web UI. Supports QwenPaw-Flash with hardware-aware recommendations. |
| **Ollama**           | Cross-platform (requires Ollama service) | Install and start Ollama; set context length ≥ 32k. |
| **LM Studio**        | Cross-platform (requires LM Studio)      | Install and start LM Studio; enable Local Server. |

---

## features

QwenPaw includes four core security layers:

- **Sandbox** — Kernel-level execution isolation using Seatbelt (macOS), Bubblewrap / Landlock (Linux), and AppContainer (Windows). Shell commands run inside a restricted filesystem view.
- **Tool Guard** — YAML rule engine with `ShellEvasionGuardian` inspects every tool call before execution, detecting command injection, path traversal, reverse shells, and obfuscated attacks. Configurable approval levels: STRICT / SMART / AUTO / OFF.
- **File Guard** — Independent of Tool Guard; blocks agent access to sensitive files and directories (default-protects `~/.qwenpaw.secret/`, `~/.ssh`, etc.).
- **Skill Scanner** — Pre-activation scanning with block / warn / off modes and whitelist support. Detects prompt injection, hardcoded secrets, data exfiltration, and more.

See [Security](https://qwenpaw.agentscope.io/docs/security) for details.

---

## Documentation

| Topic                                                                 | Description                                      |
| --------------------------------------------------------------------- | ------------------------------------------------ |
| [Introduction](https://qwenpaw.agentscope.io/docs/intro)                | What QwenPaw is and how to use it                  |
| [Quick start](https://qwenpaw.agentscope.io/docs/quickstart)            | Install and run (local or ModelScope Studio)    |
| [Console](https://qwenpaw.agentscope.io/docs/console)                   | Web UI: chat and agent configuration            |
| [Terminal UI (TUI)](https://qwenpaw.agentscope.io/docs/tui)             | Full-screen terminal chat, same agent as Console |
| [Desktop App](https://qwenpaw.agentscope.io/docs/desktop)               | Desktop application installation and usage       |
| [Models](https://qwenpaw.agentscope.io/docs/models)                     | Configure cloud, local, and custom providers    |
| [Channels](https://qwenpaw.agentscope.io/docs/channels)                  | DingTalk, Lark, QQ, Discord, iMessage, and more |
| [Skills](https://qwenpaw.agentscope.io/docs/skills)                      | Extend and customize capabilities               |
| [Plugins](https://qwenpaw.agentscope.io/docs/plugins)                    | Plugin system and Plugin Market                  |
| [MCP](https://qwenpaw.agentscope.io/docs/mcp)                            | Manage MCP clients                               |
| [Persona](https://qwenpaw.agentscope.io/docs/persona)                   | Agent personality customization (SOUL / PROFILE)  |
| [Memory](https://qwenpaw.agentscope.io/docs/memory)                     | Self-evolving personal knowledge base built on local, editable, searchable, and linked Markdown memory, powered by [ReMe](https://github.com/agentscope-ai/ReMe) |
| [ReMe Documentation](https://docs.agentscope.io/reme/latest/en/overview) | Official ReMe overview and documentation          |
| [Memory-Evolving & Proactive](https://qwenpaw.agentscope.io/docs/memory-evolving-and-proactive) | Agent memory evolution and proactive interaction |
| [Context](https://qwenpaw.agentscope.io/docs/context)                   | Scroll-based context management                  |
| [Magic commands](https://qwenpaw.agentscope.io/docs/commands)           | Control conversation state without waiting for the AI |
| [Heartbeat](https://qwenpaw.agentscope.io/docs/heartbeat)                | Scheduled check-in and digest                    |
| [Cron / Scheduled Tasks](https://qwenpaw.agentscope.io/docs/cron)       | Scheduled tasks and automation                   |
| [Multi-Agent](https://qwenpaw.agentscope.io/docs/multi-agent)           | Create multiple agents and enable collaboration  |
| [Security](https://qwenpaw.agentscope.io/docs/security)                 | Sandbox, tool guard, file guard, skill scanner, access policy |
| [Backup & Restore](https://qwenpaw.agentscope.io/docs/backup)           | Data backup and recovery                         |
| [Config &

## limitations

| Area                            | Item                                                                   | Status               |
| ------------------------------- | ---------------------------------------------------------------------- | -------------------- |
| **Horizontal Expansion**        | More channels, models, skills, and MCPs                                | Seeking Contributors |
| **Existing Feature Extension**  | Display, download, and Windows improvements                            | Seeking Contributors |
| **Models**                      | Multi-model switching                                                  | In Progress          |
| **Safety & Approval**           | Batch preview and approval                                              | In Progress          |
| **Automation**                  | Automated tasks                                                         | In Progress          |
| **Agent Interaction**           | Agent task handoff                                                      | In Progress          |
|                                 | Running task steering                                                   | In Progress          |
| **Workspaces**                  | Multiple workspaces                                                    | In Progress          |
| **Context**                     | System prompt compression                                               | In Progress          |
| **Tooling**                     | Multi-location file changes                                             | In Progress          |
|                                 | Persistent terminals and background tasks                              | In Progress          |
| **Computer-use**                | On-screen target detection and actions                                  | In Progress          |
| **Voice Interaction**           | Real-time voice tasks                                                   | In Progress          |
| **Context Management & Memory** | Hot-swappable vector models and storage                                 | In Progress          |
|                                 | Personal knowledge base                                                 | In Progress          |
| **QwenPaw Applications**        | QwenPaw Insight                                                        | In Progress          |
|                                 | QwenPaw Mail                                                           | In Progress          |

_Status:_ **In Progress** — actively being worked on; **Seeking Contributors** — we strongly encourage community contributions.

---

## Contributing

QwenPaw evolves through open collaboration, and we welcome all forms of contribution! Check the [Roadmap](#roadmap) above (especially items marked **Seeking Contributors**) to find areas that interest you, and read [CONTRIBUTING](https://github.com/agentscope-ai/QwenPaw/blob/main/CONTRIBUTING.md) to get started. We particularly welcome:

- **Horizontal expansion** — new channels, model providers, skills, MCPs.
- **Existing feature extension & refinement** — display and interaction improvements, download hints, Windows path compatibility, etc.

Join [GitHub Discussions](https://github.com/agentscope-ai/QwenPaw/discussions) to discuss ideas or pick up tasks.

---
