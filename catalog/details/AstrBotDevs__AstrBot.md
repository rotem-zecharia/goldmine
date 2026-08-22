# AstrBotDevs/AstrBot

AI Agent Assistant & development framework that integrates lots of IM platforms, LLMs, plugins and AI feature, and can be your openclaw alternative. ✨

## features

1. 💯 Free & Open Source.
2. ✨ AI LLM Conversations, Multimodal, Agent, MCP, Skills, Knowledge Base, Persona Settings, Auto Context Compression.
3. 🤖 Supports integration with Dify, Alibaba Cloud Bailian, Coze, and other agent platforms.
4. 🌐 Multi-Platform: QQ, WeChat Work, Feishu, DingTalk, WeChat Official Accounts, Telegram, Slack, and [more](#supported-messaging-platforms).
5. 📦 Plugin Extensions with 1000+ plugins available for one-click installation.
6. 🛡️ [Agent Sandbox](https://docs.astrbot.app/use/astrbot-agent-sandbox.html) for isolated, safe execution of code, shell calls, and session-level resource reuse.
7. 💻 WebUI Support.
8. 🌈 Web ChatUI Support with built-in agent sandbox and web search.
9. 🌐 Internationalization (i18n) Support.

## installation

### One-Click Cloud Deployment (RainYun)

For users who want one-click 24-hour-online deployment and do not want to manage servers themselves, we recommend RainYun's one-click cloud deployment service ☁️:

[![Deploy on RainYun](https://rainyun-apps.cn-nb1.rains3.com/materials/deploy-on-rainyun-en.svg)](https://app.rainyun.com/apps/rca/store/5994?ref=NjU1ODg0)

### One-Click Deployment

> [!NOTE]
> Requires [uv](https://docs.astral.sh/uv/) to be installed.
> For macOS users: due to macOS security checks, the first run of the `astrbot` command may take longer (about 10-20s).

For users who want to quickly experience AstrBot, are familiar with command-line usage, and can install a `uv` environment on their own, we recommend the `uv` one-click deployment method ⚡️:

```bash
uv tool install astrbot --python 3.12
astrbot init # Only execute this command for the first time to initialize the environment
astrbot run
```

Update `astrbot`:

```bash
uv tool upgrade astrbot --python 3.12
```

### Docker Deployment

For users familiar with containers and looking for a more stable, production-ready deployment method, we recommend deploying AstrBot with Docker / Docker Compose.

Please refer to the official documentation: [Deploy AstrBot with Docker](https://docs.astrbot.app/deploy/astrbot/docker.html#%E4%BD%BF%E7%94%A8-docker-%E9%83%A8%E7%BD%B2-astrbot).

### Desktop Application Deployment

For users who want to use AstrBot on desktop and mainly use ChatUI, we recommend AstrBot App.

Visit [AstrBot-desktop](https://github.com/AstrBotDevs/AstrBot-desktop) to download and install; this method is designed for desktop usage and is not recommended for server scenarios.

### Launcher Deployment

For desktop users who also want fast deployment and isolated multi-instance usage, we recommend AstrBot Launcher.

Visit [AstrBot Launcher](https://github.com/Raven95676/astrbot-launcher) to download and install.

**More deployment methods**

If you need panel-based management or deeper customization, see [BT-Panel Deployment](https://docs.astrbot.app/deploy/astrbot/btpanel.html) for BT Panel app-store setup, [1Panel Deployment](https://docs.astrbot.app/deploy/astrbot/1panel.html) for 1Panel app-market deployment, [CasaOS Deployment](https://docs.astrbot.app/deploy/astrbot/casaos.html) for NAS/home-server visual deployment, and [Manual Deployment](https://docs.astrbot.app/deploy/astrbot/cli.html) for fully custom source-based installation with `uv`.


## ❤️ Sponsors

Welcome to sponsor us via [Afdian](https://afdian.com/a/astrbot_team) or [contact us](mailto:community@astrbot.app).

<p align="center">
  <a target="_blank" href="https://astrbot.app/#/sponsors">
    <img alt="sponsors" src="https://sponsors.astrbot.app/?v=1">
  </a>
</p>


## Supported Messaging Platforms

Connect AstrBot to your favorite chat platform.

| Platform | Maintainer |
|---------|---------------|
| QQ | Official |
| OneBot v11 protocol implementation | Official |
| Telegram | Official |
| Wecom & Wecom AI Bot | Official |
| WeChat Official Accounts | Official |
| Feishu (Lark) | Official |
| DingTalk | Official |
| Slack | Official |
| Discord | Official |
| LINE | Official |
| Satori | Official |
| KOOK | Official |
| Misskey | Official |
| Mattermost | Official |
| WhatsApp (Coming Soon) | Official |
| [Matrix](https://github.com/stevessr/astrbot_plugin_matrix_adapter) | Community |
| [Rocket.Chat](https://github.com/NET-Homeless/astrbot_plugin_rocket_chat_adapter) | Community |
| [VoceChat](https://github.com/HikariFroya/astrbot_plugin_vocechat) | Community |

## Supported Model Services

| Service | Type |
|---------|---------------|
| OpenAI and Compatible Services | LLM Services |
| Anthropic | LLM Services |
| Google Gemini | LLM Services |
| Moonshot AI | LLM Services |
| Zhipu AI | LLM Services |
| DeepSeek | LLM Services |
| Ollama (Self-hosted) | LLM Services |
| LM Studio (Self-hosted) | LLM Services |
| [AIHubMix](https://aihubmix.com/?aff=4bfH) | LLM Services (API G

## configuration

AstrBot uses `ruff` for code formatting and linting.

```bash
git clone https://github.com/AstrBotDevs/AstrBot
pip install pre-commit
pre-commit install
```


## 🌍 Community

### QQ Groups

We have 15+ chat groups, please see: [Community](https://docs.astrbot.app/community.html) for details.

### Discord Server

<a href="https://discord.gg/hAVk6tgV36"><img alt="Discord_community" src="https://img.shields.io/badge/Discord-AstrBot-purple?style=for-the-badge&color=76bad9"></a>

## ❤️ Special Thanks

Special thanks to all Contributors and plugin developers for their contributions to AstrBot ❤️

<a href="https://github.com/AstrBotDevs/AstrBot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AstrBotDevs/AstrBot&max=300&columns=15" />
</a>

Open Source Friends ❤️

- [NapNeko/NapCatQQ](https://github.com/NapNeko/NapCatQQ) - The amazing cat framework
- [Mai-with-u/MaiBot](https://github.com/Mai-with-u/MaiBot) - The powerful "digital life" in your QQ! 

## ⭐ Star History

> [!TIP]
> If this project has helped you in your life or work, or if you're interested in its future development, please give the project a Star. It's the driving force behind maintaining this open-source project <3

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=astrbotdevs/astrbot&type=Date)](https://star-history.com/#astrbotdevs/astrbot&Date)

</div>

<div align="center">

_Companionship and capability should never be at odds. What we aim to create is a robot that can understand emotions, provide genuine companionship, and reliably accomplish tasks._

_私は、高性能ですから!_

<img src="https://files.astrbot.app/watashiwa-koseino-desukara.gif" width="100"/>
</div>
