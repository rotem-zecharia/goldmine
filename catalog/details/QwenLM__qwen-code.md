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
