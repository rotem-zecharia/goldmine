# langbot-app/LangBot

Production-grade platform for building agentic IM bots - 生产级多平台智能机器人开发平台/ Agent、知识库编排、插件系统 / Bots for Discord / Slack / LINE / Telegram / WeChat(企业微信, 企微智能机器人, 公众号) / 飞书 / 钉钉 / QQ / Matrix e.g. Integr

## features

- **AI Conversations & Agents** — Multi-turn dialogues, tool calling, multi-modal support, streaming output. Built-in RAG (knowledge base) with deep integration to [Dify](https://dify.ai), [Coze](https://coze.com), [n8n](https://n8n.io), [Langflow](https://langflow.org), [Deerflow](https://deerflow.tech), [Weknora](https://weknora.weixin.qq.com).
- **Universal IM Platform Support** — One codebase for Discord, Telegram, Slack, LINE, QQ, WeChat, WeCom, Lark, DingTalk, KOOK.
- **Production-Ready** — Access control, rate limiting, sensitive word filtering, comprehensive monitoring, and exception handling. Trusted by enterprises.
- **Plugin Ecosystem** — Hundreds of plugins, event-driven architecture, component extensions, and [MCP protocol](https://modelcontextprotocol.io/) support.
- **Web Management Panel** — Configure, manage, and monitor your bots through an intuitive browser interface. No YAML editing required.
- **Multi-Pipeline Architecture** — Different bots for different scenarios, with comprehensive monitoring and exception handling.

[→ Learn more about all features](https://langbot.app/docs/en/insight/features)

📍 Practical guides: [deploy a multi-platform AI bot in 5 minutes](https://langbot.app/en/blog/deploy-ai-bot-in-5-minutes/), [connect DeepSeek to WeChat, Discord, and Telegram](https://langbot.app/en/blog/connect-deepseek-to-wechat/), [run a Dify Agent in Discord, Telegram, and Slack](https://langbot.app/en/blog/dify-agent-discord-telegram-slack/), and [build an n8n-powered chatbot](https://langbot.app/en/blog/n8n-multi-platform-ai-chatbot/).

---

## 😎 Stay Updated

Click the Star and Watch buttons in the top-right corner of the repository to get the latest updates.

![star gif](https://langbot.app/star.gif)

## installation

### ☁️ LangBot Cloud (Recommended)

**[LangBot Cloud](https://space.langbot.app/cloud)** — Zero deployment, ready to use.

### One-Line Launch

```bash
uvx langbot
```

> Requires [uv](https://docs.astral.sh/uv/getting-started/installation/). Visit http://localhost:5300 — done.

### Docker Compose

```bash
git clone https://github.com/langbot-app/LangBot
cd LangBot/docker
docker compose --profile all up -d
```


### One-Click Cloud Deploy

[![Deploy on Zeabur](https://zeabur.com/button.svg)](https://zeabur.com/en-US/templates/ZKTBDH)
[![Deploy on Railway](https://railway.com/button.svg)](https://railway.app/template/yRrAyL?referralCode=vogKPF)

**More options:** [Docker](https://langbot.app/docs/en/deploy/langbot/docker) · [Manual](https://langbot.app/docs/en/deploy/langbot/manual) · [BTPanel](https://langbot.app/docs/en/deploy/langbot/one-click/bt) · [Kubernetes](https://langbot.app/docs/en/deploy/langbot/kubernetes)

---

## Live Demo

**Try it now:** https://demo.langbot.dev/

- Email: `demo@langbot.app`
- Password: `langbot123456`

_Note: Public demo environment. Do not enter sensitive information._

---

## Supported Platforms

| Platform | Status | Notes |
|----------|--------|-------|
| Discord | ✅ | Official |
| Telegram | ✅ | Official |
| Slack | ✅ | Official |
| LINE | ✅ | Official |
| QQ | ✅ | Personal & Official API (Channel, DM, Group) |
| WeCom | ✅ | Enterprise WeChat, External CS, AI Bot |
| WeChat | ✅ | Personal & Official Account |
| Lark | ✅ | Official |
| DingTalk | ✅ | Official |
| KOOK | ✅ | Official |
| Satori | ✅ |  |
| Email | ✅ | Matrix, Satori |
| Matrix | ✅ | Supports multiple bridged platforms such as Signal, WhatsApp, Messenger, iMessage, Mattermost, Google Chat, IRC, XMPP, Zulip, and more |

---

## Supported LLMs & Integrations

| Provider                                                                                                          | Type         | Status |
| ----------------------------------------------------------------------------------------------------------------- | ------------ | ------ |
| [OpenAI](https://platform.openai.com/)                                                                            | LLM          | ✅     |
| [Anthropic](https://www.anthropic.com/)                                                                           | LLM          | ✅     |
| [DeepSeek](https://www.deepseek.com/)                                                                             | LLM          | ✅     |
| [Google Gemini](https://aistudio.google.com/prompts/new_chat)                                                     | LLM          | ✅     |
| [xAI](https://x.ai/)                                                                                              | LLM          | ✅     |
| [Moonshot](https://www.moonshot.cn/)                                                                              | LLM          | ✅     |
| [Zhipu AI](https://open.bigmodel.cn/)                                                                             | LLM          | ✅     |
| [Ollama](https://ollama.com/)                                                                                     | Local LLM    | ✅     |
| [LM Studio](https://lmstudio.ai/)                                                                                 | Local LLM    | ✅     |
| [Dify](https://dify.ai)                                                                                           | LLMOps       | ✅     |
| [MCP](https://modelcontextprotocol.io/)                                                                           | Protocol     | ✅     |
| [SiliconFlow](https://siliconflow.cn/)                                                                            | Gateway      | ✅     |
| [Aliyun Bailian](https://bailian.console.aliyun.com/)                                                             | Gateway      | ✅     |
| [Volc Engine Ark](https://console.volcengine.com/ark/region:ark+cn-beijing/model?vendor=Byt
