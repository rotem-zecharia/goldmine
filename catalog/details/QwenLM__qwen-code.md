# QwenLM/qwen-code

An open-source AI coding agent that lives in your terminal.

## features

- **Agentic out of the box** — Auto-Memory, Auto-Skills, SubAgents, Agent Teams, and MCP. Dynamic workflows, zero setup.
- **Open-source, inside and out** — The framework and the Qwen models are open-source. They evolve together. No vendor lock-in.
- **Multi-protocol** — Supports OpenAI, Anthropic, Gemini, and Qwen APIs. Any third-party provider or local model (Ollama / vLLM). Switch at runtime.
- **Beyond the terminal** — IDE plugins, Desktop app, daemon mode, SDKs, and IM bots (Telegram / DingTalk / WeChat / Feishu).

> [!TIP]
> Qwen Code is actively iterating on itself — using its own agent and models to file issues, submit PRs, review code, and run tests. Powered by the community, driven by AI.

## installation

**Linux / macOS:**

```bash
curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.sh | bash
```

**Windows:**

```powershell
irm https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.ps1 | iex
```

> Restart your terminal after installation to ensure environment variables take effect.

<details>
<summary>NPM / Homebrew</summary>

**NPM** (requires [Node.js 22+](https://nodejs.org/)):

```bash
npm install -g @qwen-code/qwen-code@latest
```

**Homebrew** (macOS / Linux):

```bash
brew install qwen-code
```

</details>

## Quick Start

```bash
qwen          # Launch interactive terminal UI
# Inside the session:
/auth         # Configure your provider and API key
```

See the [Authentication Guide](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/auth/) and [Settings Reference](https://qwenlm.github.io/qwen-code-docs/en/users/configuration/settings/) for detailed setup.

![Qwen Code](https://img.alicdn.com/imgextra/i2/O1CN01K0nwj41RM1Il8kB0t_!!6000000002096-2-tps-1544-1060.png)

## How to Use Qwen Code

| Mode            | Command         | Use Case                                                                                                                                                                                                                                        |
| --------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Interactive** | `qwen`          | Terminal UI with rich rendering, `@file` references, slash commands                                                                                                                                                                             |
| **Headless**    | `qwen -p "..."` | Scripts, CI/CD, batch processing — no UI                                                                                                                                                                                                        |
| **IDE**         | —               | [VS Code](https://qwenlm.github.io/qwen-code-docs/en/users/integration-vscode/), [Zed](https://qwenlm.github.io/qwen-code-docs/en/users/integration-zed/), [JetBrains](https://qwenlm.github.io/qwen-code-docs/en/users/integration-jetbrains/) |
| **Desktop**     | —               | [Qwen Code Desktop](https://github.com/QwenLM/qwen-code/releases/tag/desktop-latest) — GUI for macOS, Windows, Linux                                                                                                                            |
| **Daemon**      | `qwen serve`    | Shared agent session over HTTP+SSE (ACP). Multiple clients, one agent. _(experimental)_ [Docs](https://qwenlm.github.io/qwen-code-docs/en/users/qwen-serve)                                                                                     |
| **SDK**         | —               | [TypeScript](./packages/sdk-typescript/README.md), [Python](./packages/sdk-python/README.md), [Java](./packages/sdk-java/qwencode/README.md)                                                                                                    |
| **IM Bot**      | `qwen channel`  | Connect to Telegram, DingTalk, WeChat, or Feishu                                                                                                                                                                                                |

<details>
<summary>SDK example (Python)</summary>

```python
import asyncio

from qwen_code_sdk import is_sdk_result_message, query


async def main() -> None:
    result = query(
        "Summarize the repository layout.",
        {
            "cwd": "/path/to/project",
            "path_to_qwen_executable": "qwen",
        },
    )

    async for message in re
