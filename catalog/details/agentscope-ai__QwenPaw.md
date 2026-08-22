# agentscope-ai/QwenPaw

Your Personal AI Assistant; easy to install, deploy on your own machine or on the cloud; supports multiple chat apps with easily extensible capabilities.

## installation

If you prefer managing Python yourself (requires Python >= 3.11, < 3.14):

```bash
pip install qwenpaw
qwenpaw init --defaults
qwenpaw app
```

Then open the Console in your browser at **http://127.0.0.1:8088/** to configure your model. To chat in DingTalk, Lark, WeChat, etc., see the [Channel setup](https://qwenpaw.agentscope.io/docs/channels) documentation.

![Console](https://img.alicdn.com/imgextra/i2/O1CN01EP1ra01iOAcBvF0TC_!!6000000004402-2-tps-3822-2070.png)

---

## tools

If you use a **cloud LLM API** (e.g., DashScope / Qwen, OpenAI, Anthropic, Google Gemini, DeepSeek, Kimi, OpenRouter, and more), you must configure an API key before chatting. QwenPaw will not work until a valid key is set. See the [official docs](https://qwenpaw.agentscope.io/docs/models) for details.

**How to configure:**

1. **Console (recommended)** — After running `qwenpaw app`, open **http://127.0.0.1:8088/** → **Settings** → **Models**. Choose a provider, enter the **API Key**, and enable that provider and model.
2. **`qwenpaw init`** — When you run `qwenpaw init`, it will guide you through configuring the LLM provider and API key. Follow the prompts to choose a provider and enter your key.
3. **Environment variable** — For DashScope you can set `DASHSCOPE_API_KEY` in your shell or in a `.env` file in the working directory.

Tools that need extra keys (e.g. `TAVILY_API_KEY` for web search) can be set in Console **Settings → Environment variables**, see [Config](https://qwenpaw.agentscope.io/docs/config) for details.

> **Using local models only?** If you use [Local Models](#local-models) (QwenPaw Local / Ollama / LM Studio), you do **not** need any API key.

## features

QwenPaw includes four core security layers:

- **Sandbox** — Kernel-level execution isolation using Seatbelt (macOS), Bubblewrap / Landlock (Linux), and AppContainer (Windows). Shell commands run inside a restricted filesystem view.
- **Tool Guard** — YAML rule engine with `ShellEvasionGuardian` inspects every tool call before execution, detecting command injection, path traversal, reverse shells, and obfuscated attacks. Configurable approval levels: STRICT / SMART / AUTO / OFF.
- **File Guard** — Independent of Tool Guard; blocks agent access to sensitive files and directories (default-protects `~/.qwenpaw.secret/`, `~/.ssh`, etc.).
- **Skill Scanner** — Pre-activation scanning with block / warn / off modes and whitelist support. Detects prompt injection, hardcoded secrets, data exfiltration, and more.

See [Security](https://qwenpaw.agentscope.io/docs/security) for details.

---

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
