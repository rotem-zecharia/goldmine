# iOfficeAI/AionUi

Open-source 24/7 Cowork app for OpenClaw, Hermes, Claude Code, Codex, OpenCode and 20+ more CLI Agent / Customize your assistants / Team them up｜Star if you like it!

## installation

AionUi ships with a complete AI agent engine. Unlike tools that require you to install CLI agents separately, **AionUi works the moment you install it**.

- **No CLI tools to install** — the agent engine is built in
- **No complex setup** — paste any API key to get started
- **Full agent capabilities** — file read/write, web search, image generation, MCP (Model Context Protocol) tools
- **Ready-to-use assistants** — 21 built-in professional assistants (Cowork, PPT Creator, Word Creator, Word Form Creator, Excel Creator, Morph PPT, Morph PPT 3D, Pitch Deck Creator, Dashboard Creator, Academic Paper Writer, Financial Model Creator, and more) ready to use immediately

<p align="center">
  <img src="./resources/homepage.png" alt="Built-in Agents" width="800">
</p>

### **Office assistants — PPT, Word & Excel**

These tracks match what the app actually ships: **Morph PPT** presets and the **`pptx` / `docx` / `xlsx` skills**. The canonical [assistant catalog](https://github.com/iOfficeAI/AionCore/blob/main/crates/aionui-app/assets/builtin-assistants/assistants.json) and [built-in skills](https://github.com/iOfficeAI/AionCore/tree/main/crates/aionui-app/assets/builtin-skills) are maintained with AionCore. Want document/table output? AionUi’s built-in **[OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)** helps PPT (Morph), Word (`.docx`), and Excel (`.xlsx/.xlsm/.csv`) go from request to deliverable faster and more reliably.
The three assistant types map to file workflows, and the final outputs are directly editable and reusable.

#### **PPT assistant**

> **Output:** editable Morph PPT (`.pptx`)
> Morph-animated slide-to-slide transitions with coherent story pacing; powered by [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI).

<table>
  <tr>
    <td align="center" width="50%">
      <img src="./resources/morph-ppt-balanced.gif" alt="Morph PPT — slide-to-slide transitions (OfficeCLI)" width="390">
    </td>
    <td align="center" width="50%">
      <img src="./resources/readme-demo-assistant-ppt.gif" alt="PPT assistant — screen recording" width="390">
    </td>
  </tr>
</table>

#### **Word assistant**

> **Output:** editable Word (`.docx`)
> Paper/thesis writing and production-ready document editing via the `docx` skill; powered by [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI).

<table>
  <tr>
    <td align="center" width="50%">
      <img src="./resources/readme-demo-generate-academic-paper.gif" alt="Generate academic paper demo" width="390">
    </td>
    <td align="center" width="50%">
      <img src="./resources/readme-demo-assistant-write-paper.gif" alt="Paper writing assistant demo" width="390">
    </td>
  </tr>
</table>

#### **Excel assistant**

> **Output:** usable Excel (`.xlsx/.xlsm/.csv`)
> Generate/refresh spreadsheets with `xlsx` for analysis, auto-formatting, and charts; powered by [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI).

<table>
  <tr>
    <td align="center" width="50%">
      <img src="./resources/readme-demo-generate-excel.gif" alt="Excel generation demo" width="390">
    </td>
    <td align="center" width="50%">
      <img src="./resources/readme-demo-assistant-excel.gif" alt="Excel assistant demo" width="390">
    </td>
  </tr>
</table>

---

## Multi-Agent Mode — Already Have CLI Agents? Bring Them In

If you already use Claude Code, Codex, Hermes Agent, or OpenClaw, AionUi auto-detects them and lets you Cowork with all of them — alongside the built-in agent.

**Supported Agents:** Built-in Agent (powered by the embedded [aionrs](https://github.com/iOfficeAI/aionrs) agent engine) • Claude Code • Codex • Qwen Code • Gemini CLI • Goose • OpenClaw • Augment Code • CodeBuddy • Kimi CLI • OpenCode • Factory Droid • GitHub Copilot • Qoder • Mistral Vibe • Nanobot • Snow • Hermes • Cursor Agent • Pi • MiMo Code • omp • Antigravity • and more

<p align="center">
  <img src="./resources/multi-agent支持openclaw.gif" alt="Multi-Agent Cowork" width="800">
</p>

- **Auto Detection** — automatically reco

## tools

Other AI apps give you a chatbox with your API key. **AionUi gives you a full Cowork agent.**

| Your API Key               | What You Get                                |
| :------------------------- | :------------------------------------------ |
| Gemini API Key             | Gemini-powered Cowork Agent                 |
| OpenAI API Key             | GPT-powered Cowork Agent                    |
| Anthropic API Key          | Claude-powered Cowork Agent                 |
| AWS Bedrock credentials    | Bedrock-powered Agent via Aion CLI (aionrs) |
| Ollama / LM Studio (local) | Local model Cowork Agent                    |
| NewAPI Gateway             | Unified access to 20+ models                |

Same agent capabilities — file read/write, web search, image generation, tool use — regardless of which model powers it. AionUi supports **30+ AI platforms** including cloud services and local deployments.

<p align="center">
  <img src="./resources/llm_newapi.png" alt="Multi-Model Support" width="800">
</p>

<details>
<summary><strong>🔍 View All 30+ Supported Platforms ▶️</strong></summary>

<br>

**Comprehensive Platform Support:**

- **Official Platforms** — Gemini, Gemini (Vertex AI), Anthropic (Claude), OpenAI
- **Cloud Providers** — AWS Bedrock, New API (unified AI model gateway)
- **Chinese Platforms** — Dashscope (Qwen), Dashscope Coding Plan, Zhipu, Moonshot (Kimi), Qianfan (Baidu), Hunyuan (Tencent), Lingyi, ModelScope, InfiniAI, Ctyun, StepFun, SiliconFlow-CN, PPIO
- **International Platforms** — DeepSeek, MiniMax, Novita, OpenRouter, SiliconFlow, xAI, Ark (Volcengine), Poe
- **Local Models** — Ollama, LM Studio (via Custom platform with local API endpoint)

AionUi also supports [NewAPI](https://github.com/QuantumNous/new-api) gateway service — a unified AI model hub that aggregates and distributes various LLMs. Flexibly switch between different models in the same interface to meet various task requirements.

</details>

---

## Extensible Assistants & Skills

_Extensible assistant system with 21 built-in professional assistants and a three-tier skill system. Create and manage your own assistants and skills._

- **Create Custom Assistants** — Define your own assistants with custom rules and capabilities
- **Three-tier Skills** — Builtin skills (shipped with AionUi), custom skills (your own), and Extension skills (contributed by third-party extensions); enable/disable per conversation with the skill indicator
- **Per-conversation Control** — A skill indicator in the chat header shows active skills for the current conversation; search and exclude skills as needed

<p align="center">
  <img src="./resources/assitants.png" alt="AI Assistants & Skills Ecosystem" width="800">
</p>

AionUi supports three skill layers: **built-in** skills (shipped with the app), **custom** skills (user-defined), and **extension** skills (loaded from the Extension SDK).

<details>
<summary><strong>🔍 View Assistant Details and Custom Skills ▶️</strong></summary>

<br>

AionUi includes **21 professional assistants** with predefined capabilities, extendable through custom skills:

- **🤝 Cowork** — Autonomous task execution (file operations, document processing, workflow planning)
- **📊 PPT Creator / Morph PPT / Morph PPT 3D** — Generate and animate PPTX presentations with Morph transitions
- **📐 Pitch Deck Creator** — Investor-ready pitch deck generation
- **📊 Dashboard Creator** — Data dashboard generation
- **📝 Word Creator** — Production-ready Word (`.docx`) document generation
- **📋 Word Form Creator** — Structured Word form / contract template generation
- **📗 Excel Creator** — Spreadsheet generation with analysis, charts, and auto-formatting
- **🎓 Academic Paper Writer** — Structured academic paper writing
- **💰 Financial Model Creator** — Financial models and projections
- **🎮 3D Game** — Single-file 3D game generation
- **🎨 UI/UX Pro Max** — Professional UI/UX design (57 styles, 95 color palettes)
- **📋 Planning with Files** — File-based 

## features

<details>
<summary><strong>Click to see detailed comparison</strong></summary>

<br>

AionUi is a **free and open-source Multi-AI Agent Desktop**. Compared to Claude Cowork which only runs on macOS and is locked to Claude, AionUi is its full-model, cross-platform enhanced version.

| Dimension     | Claude Cowork | AionUi                                                    |
| :------------ | :------------ | :-------------------------------------------------------- |
| OS            | macOS Only    | macOS / Windows / Linux                                   |
| Model Support | Claude Only   | Gemini, Claude, DeepSeek, OpenAI, Ollama, ...             |
| Interaction   | Desktop GUI   | Desktop GUI + WebUI + Telegram / Lark / DingTalk / WeChat |
| Automation    | Manual only   | Cron scheduled tasks — 24/7 unattended                    |
| Cost          | $100/month    | Free & Open Source                                        |

Deep AI Office Scenario Support:

- **File Management**: Intelligently organize local folders and batch rename with one click.
- **Data Processing**: Deeply analyze and automatically beautify Excel reports.
- **Document Generation**: Automatically write and format PPT, Word, and Markdown documents.
- **Instant Preview**: Built-in 10+ format preview panels, AI collaboration results instantly visible.

</details>

---

## Quick Q&A

<details>
<summary><strong>Q: Do I need to install Gemini CLI or Claude Code first?</strong></summary>
A: <strong>No.</strong> AionUi has a built-in AI agent that works immediately after installation. Just enter any API key to get started. If you also have CLI tools like Claude Code or Gemini CLI installed, AionUi will auto-detect and integrate them for even more capabilities.
</details>

<details>
<summary><strong>Q: What can I do with AionUi?</strong></summary>
A: AionUi is your <strong>private Cowork workspace</strong>. The built-in agent can batch organize folders, process Excel data, generate documents, search the web, and generate images. With Multi-Agent Mode, you can also leverage Claude Code, Codex, and other powerful CLI agents through the same interface.
</details>

<details>
<summary><strong>Q: Is it free?</strong></summary>
A: AionUi is completely free and open source. You only pay for the API usage of whichever provider you choose, and you can use API keys from any provider you prefer.
</details>

<details>
<summary><strong>Q: Can I run AionUi on a server (headless)?</strong></summary>
A: Yes — AionUi WebUI mode runs as a standalone HTTP server. See the WebUI section above for setup instructions.
</details>

<details>
<summary><strong>Q: Is my data secure?</strong></summary>
A: All data is stored locally in a SQLite database. Nothing is uploaded to any server.
</details>

---

## See How People Use AionUi

<p align="center">
  <a href="https://www.youtube.com/watch?v=vWxE6VO9TKo" target="_blank">
    <img src="https://img.youtube.com/vi/vWxE6VO9TKo/maxresdefault.jpg" alt="Hermes + Aion UI is Insane (FREE)!" width="400">
  </a>
  &nbsp;&nbsp;
  <a href="https://www.youtube.com/watch?v=RgSLdOhICZw" target="_blank">
    <img src="https://img.youtube.com/vi/RgSLdOhICZw/maxresdefault.jpg" alt="OpenClaw + Aion UI is Insane (FREE!)" width="400">
  </a>
</p>
<p align="center">
  <em>Julian Goldie SEO — Hermes + Aion UI is Insane (FREE!) · 27K views</em> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <em>Julian Goldie SEO — OpenClaw + Aion UI is Insane (FREE!) · 11K views</em>
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=yUU5E-U5B3M" target="_blank">
    <img src="https://img.youtube.com/vi/yUU5E-U5B3M/maxresdefault.jpg" alt="WorldofAI Review" width="400">
  </a>
  &nbsp;&nbsp;
  <a href="https://www.youtube.com/watch?v=enQnkKfth10" target="_blank">
    <img src="https://img.youtube.com/vi/enQnkKfth10/maxresdefault.jpg" alt="Julian Goldie SEO Review" width="400">
  </a>
</p>
<p align="center">
  <em>WorldofAI (200K subscribers)</em> &nbsp;&nbsp;&nbsp;&nbsp;&n

## requirements

- **macOS**: 10.15 or higher
- **Windows**: Windows 10 or higher
- **Linux**: Ubuntu 18.04+ / Debian 10+ / Fedora 32+
- **Memory**: 4GB+ recommended
- **Storage**: 500MB+ available space
