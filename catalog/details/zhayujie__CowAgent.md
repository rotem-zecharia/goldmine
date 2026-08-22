# zhayujie/CowAgent

Open-source super AI assistant & Agent Harness. Plans tasks, runs tools and skills, self-evolves with memory and knowledge. Multi-model, multi-channel. Lightweight, extensible, one-line install. (form

## installation

A one-line installer takes care of dependencies, configuration, and startup:

**Linux / macOS:**

```bash
bash <(curl -fsSL https://cdn.link-ai.tech/code/cow/run.sh)
```

**Windows (PowerShell):**

```powershell
irm https://cdn.link-ai.tech/code/cow/run.ps1 | iex
```

**Docker:**

```bash
curl -O https://cdn.link-ai.tech/code/cow/docker-compose.yml
docker compose up -d
```

Once started, open `http://localhost:9899` to access the **Web console** — your one-stop hub to chat with the Agent, configure models, connect channels, and install skills.

> Deploying on a server? Set `web_host` to `0.0.0.0` in `config.json` to make the console reachable from outside, and set `web_password` to protect it. Don't forget to open port `9899` in your firewall or security group.

> 📖 Detailed guides: [Quick Start](https://docs.cowagent.ai/guide/quick-start) · [Install from Source](https://docs.cowagent.ai/guide/manual-install) · [Upgrade](https://docs.cowagent.ai/guide/upgrade)

After installation, manage the service with the [cow CLI](https://docs.cowagent.ai/cli/index):

```bash
cow start | stop | restart        # service control
cow status | logs                  # status and logs
cow update                         # pull latest code and restart
cow skill install <name>           # install a skill
cow install-browser                # install browser automation
```

> 💻 Desktop client: download the **[CowAgent Desktop client](https://cowagent.ai/download/)** (macOS / Windows) — the backend is bundled, ready to use out of the box.

<br/>

## 🤖 Models

CowAgent supports all mainstream LLM providers. **Chat, vision, image generation, ASR/TTS, and embeddings** can each be routed to a different vendor. Providers are configured directly in the Web console — no manual file editing required.

| Provider | Featured Models | Chat | Vision | Image Gen | ASR | TTS | Embedding |
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: |
| [DeepSeek](https://docs.cowagent.ai/models/deepseek) | deepseek-v4-flash / pro | ✅ | | | | | |
| [Claude](https://docs.cowagent.ai/models/claude) | claude-opus-5 / sonnet-5 | ✅ | ✅ | | | | |
| [OpenAI](https://docs.cowagent.ai/models/openai) | gpt-5.6 series | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Gemini](https://docs.cowagent.ai/models/gemini) | gemini-3.7-flash | ✅ | ✅ | ✅ | | | |
| [MiniMax](https://docs.cowagent.ai/models/minimax) | MiniMax-M3 | ✅ | ✅ | ✅ | | ✅ | |
| [GLM](https://docs.cowagent.ai/models/glm) | glm-5.3, glm-5v-turbo | ✅ | ✅ | | ✅ | | ✅ |
| [Qwen](https://docs.cowagent.ai/models/qwen) | qwen3.8-max | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Kimi](https://docs.cowagent.ai/models/kimi) | kimi-k3 | ✅ | ✅ | | | | |
| [Doubao](https://docs.cowagent.ai/models/doubao) | doubao-seed-2.1 series | ✅ | ✅ | ✅ | | | ✅ |
| [ERNIE](https://docs.cowagent.ai/models/qianfan) | ernie-5.1 | ✅ | ✅ | | | | |
| [MiMo](https://docs.cowagent.ai/models/mimo) | mimo-v2.5 / pro | ✅ | ✅ | | | ✅ | |
| [LinkAI](https://docs.cowagent.ai/models/linkai) | One key for 100+ models | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Custom](https://docs.cowagent.ai/models/custom) | Local models / third-party proxy | ✅ | | | | | |

> For details on each provider, see the [Models overview](https://docs.cowagent.ai/models/index).

<br/>

## 💬 Channels

A single Agent instance can serve multiple channels in parallel. Most channels can be onboarded right from the Web console.

| Channel | Text | Image | File | Voice | Group |
| --- | :-: | :-: | :-: | :-: | :-: |
| [Web Console](https://docs.cowagent.ai/channels/web) (default) | ✅ | ✅ | ✅ | ✅ | |
| [Telegram](https://docs.cowagent.ai/channels/telegram) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Slack](https://docs.cowagent.ai/channels/slack) | ✅ | ✅ | ✅ | | ✅ |
| [Discord](https://docs.cowagent.ai/channels/discord) | ✅ | ✅ | ✅ | | ✅ |
| [WeChat](https://docs.cowagent.ai/channels/weixin) | ✅ | ✅ | ✅ | ✅ | |
| [Feishu / Lark](https://docs.cowagent.ai/channels/feishu) | ✅ | ✅ | ✅ | ✅ | ✅ |
| [DingTalk](https://docs.cowagent.ai/channels/dingtalk) | ✅ | ✅ | ✅ | ✅ | ✅ |
|

## tools

**Tools** are atomic capabilities the Agent uses to interact with system resources. **Skills** are higher-level workflows defined by a manifest file that compose multiple tools to accomplish complex tasks.

### Tool System

**Built-in tools** cover file I/O (`read` / `write` / `edit` / `ls`), terminal (`bash`), file sending (`send`), memory retrieval (`memory`), environment variables (`env_config`), web fetching (`web_fetch`), scheduling (`scheduler`), web search (`web_search`), vision (`vision`), and browser automation (`browser`).

**MCP protocol** integrates the open ecosystem of [Model Context Protocol](https://modelcontextprotocol.io) servers. A single `mcp.json` is enough — supports stdio / SSE transports, hot reload, and zero-code integration.

Learn more: [Tools overview](https://docs.cowagent.ai/tools/index) · [MCP integration](https://docs.cowagent.ai/tools/mcp).

### Skills System

- **[Skill Hub](https://skills.cowagent.ai/)** — open skill marketplace: browse, search, install in one click
- **GitHub / ClawHub / URL and more** — install skills from any source
- **Conversational authoring** — generate custom skills through dialogue with `skill-creator`; turn any workflow or third-party API into a reusable skill

```bash
/skill list                   # list installed skills
/skill search <keyword>        # search the marketplace
/skill install <name>          # one-click install
```

Learn more: [Skills overview](https://docs.cowagent.ai/skills/index) · [Creating Skills](https://docs.cowagent.ai/skills/create).

<br/>

## 🏷 Changelog

> **2026.08.20:** [v2.1.7](https://github.com/zhayujie/CowAgent/releases/tag/2.1.7) — Multiple workspaces, session-level permission modes, task notifications, desktop improvements, plus new model support.

> **2026.08.12:** [v2.1.6](https://github.com/zhayujie/CowAgent/releases/tag/2.1.6) — Sub agents for parallel task delegation, reasoning-effort settings, a pluggable memory vector backend, plus experience and security improvements.

> **2026.07.29:** [v2.1.5](https://github.com/zhayujie/CowAgent/releases/tag/2.1.5) — Workspace with file preview, core tool improvements (file search, write-time validation, background commands), context compaction (`/compact`), one-click prompt optimization, security hardening.

> **2026.07.20:** [v2.1.4](https://github.com/zhayujie/CowAgent/releases/tag/2.1.4) — Desktop experience improvements, MCP OAuth authorization, Lark channel enhancements, scheduler improvements and data backup, new models.

> **2026.07.08:** [v2.1.3](https://github.com/zhayujie/CowAgent/releases/tag/2.1.3) — [Desktop client](https://cowagent.ai/download/) for macOS / Windows, knowledge base document management, on-demand MCP tool retrieval, Traditional Chinese support, new models.

> **2026.06.18:** [v2.1.2](https://github.com/zhayujie/CowAgent/releases/tag/2.1.2) — Web console upgrades (scheduled task management, knowledge base categories, multiple custom model providers), Self-Evolution improvements, new models (kimi-k2.7-code, glm-5.2), security hardening and refinements.

> **2026.06.09:** [v2.1.1](https://github.com/zhayujie/CowAgent/releases/tag/2.1.1) — Self-Evolution, Web console upgrades (message management, parallel sessions), cross-platform MCP enhancements with concurrent calls, new models (MiniMax-M3, qwen3.7-plus), Python 3.13 support.

> **2026.06.01:** [v2.1.0](https://github.com/zhayujie/CowAgent/releases/tag/2.1.0) — Internationalization, new channels (Telegram, Discord, Slack, WeChat Customer Service), CLI interaction upgrades, streamlined one-line install, MCP Streamable HTTP support, new models (claude-opus-4-8, MiMo).

Full history: [Release Notes](https://docs.cowagent.ai/releases/overview)

<br/>

## 🤝 Community & Support

Join our [**Discord server**](https://discord.gg/9U8eA8v9TR) to ask questions, share skills, and follow development:

<a href="https://discord.gg/9U8eA8v9TR"><img src="https://img.shields.io/badge/Discord-Join%20the%20community-5865F2?sty
