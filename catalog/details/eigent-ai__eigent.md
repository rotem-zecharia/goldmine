# eigent-ai/eigent

Eigent: The Open Source Cowork Desktop - Local and Free Alternative to Claude Cowork and Codex

## installation

> **🔓 Build in Public** — Eigent is **100% open source** from day one. Every feature, every commit, every decision is transparent. We believe the best AI tools should be built openly with the community, not behind closed doors.

### 🏠 Local Deployment (Recommended)

The recommended way to run Eigent — fully standalone with complete control over your data, no cloud account required.

👉 **[Full Local Deployment Guide](./server/README_EN.md)**

This setup includes:

- Local backend server with full API
- Local model integration (vLLM, Ollama, LM Studio, etc.)
- Complete isolation from cloud services
- Zero external dependencies

### ⚡ Quick Start (Cloud-Connected)

For a quick preview using our cloud backend — get started in seconds:

#### Prerequisites

- Node.js (version 18-22) and npm

#### Steps

```bash
git clone https://github.com/eigent-ai/eigent.git
cd eigent
npm install
npm run dev
```

> Note: This mode connects to Eigent cloud services and requires account registration. For a fully standalone experience, use [Local Deployment](#-local-deployment-recommended) instead.

#### Updating Dependencies

After pulling new code (`git pull`), update both frontend and backend dependencies:

```bash

## requirements

npm install

# 2. Update backend/Python dependencies (in backend directory)
cd backend
uv sync
```

### 🏢 Enterprise

For organizations requiring maximum security, customization, and control:

- **Exclusive Features** (like SSO & custom development)
- **Scalable Enterprise Deployment**
- **Negotiated SLAs** & implementation services

📧 For further details, [contact our sales team](https://www.eigent.ai/contact-sales).

### ☁️ Cloud Version

For teams who prefer managed infrastructure, we also offer a cloud platform. The fastest way to experience Eigent's multi-agent AI capabilities without setup complexity. We'll host the models, APIs, and cloud storage, ensuring Eigent runs flawlessly.

- **Instant Access** - Start building multi-agent workflows in minutes.
- **Managed Infrastructure** - We handle scaling, updates, and maintenance.
- **Premium Support** - Subscribe and get priority assistance from our engineering team.

<br/>

[![image-public-beta]][eigent-download]

<div align="right">
<a href="https://www.eigent.ai/download">Get started at Eigent.ai →</a>
</div>

## features

### 🧑‍💻 Cowork with Single Agent

Start with one focused agent for direct tasks. Research, write, debug, and operate alongside it in your desktop workspace.

### 🏭 Cowork with Workforce

Scale to multiple specialized agents that divide work, collaborate in parallel, and execute complex multi-step workflows together.

### ⏰ Automation

Schedule recurring workflows and let agents run tasks at the right time—so work continues even when you step away.

### 🔒 Local & Secure

Run agents on your machine with local-first execution. Your files, credentials, and context stay under your control.

### 🧠 Model Agnostic

Connect the models you already use—cloud APIs, enterprise gateways, or local inference—without locking into one vendor.

### 👐 100% Open Source

Eigent is completely open-sourced. You can download, inspect, and modify the code, ensuring transparency and fostering a community-driven ecosystem for multi-agent innovation.

## 🧩 Use Cases - Open Source Cowork

Explore how Eigent turns complex desktop work into repeatable agent workflows.

### For Developers

#### [Build 10 Chinese New Year HTML5 Games with Eigent](https://www.eigent.ai/use-cases/build-10-cny-horse-themed-html5-games)

Coordinate parallel agents to build ten polished, mobile-friendly browser games across genres, complete with scoring, increasing difficulty, and restart flows.

[View demo →](https://www.eigent.ai/use-cases/build-10-cny-horse-themed-html5-games/video)

[View guide →](https://www.eigent.ai/use-cases/build-10-cny-horse-themed-html5-games)

#### [Build a 3D Snow Bros Platformer with Gemini 3.1 Pro](https://www.eigent.ai/use-cases/build-3d-snow-bros-platformer-gemini)

Create a complete browser-based 3D platformer with snowball combat, enemy chains, scoring, lives, scaling difficulty, and layered environments.

[View demo →](https://www.eigent.ai/use-cases/build-3d-snow-bros-platformer-gemini/video)

[View guide →](https://www.eigent.ai/use-cases/build-3d-snow-bros-platformer-gemini)

#### [Automate Monthly Dev Reports with DeepSeek via Ollama](https://www.eigent.ai/use-cases/monthly-dev-reports-automated-eigent-with-deepseek-v4-pro-via-ollama)

Review a month of GitHub pull requests with a locally hosted model, generate a Word summary, and prepare the corresponding Slack release update.

[View demo →](https://www.eigent.ai/use-cases/monthly-dev-reports-automated-eigent-with-deepseek-v4-pro-via-ollama/video)

[View guide →](https://www.eigent.ai/use-cases/monthly-dev-reports-automated-eigent-with-deepseek-v4-pro-via-ollama)

### Featured

#### [Organize Desktop Files](https://www.eigent.ai/use-cases/organize-desktop-files)

Ask Eigent to inspect a cluttered desktop and organize files into a cleaner, more useful structure directly on your machine.

[View demo →](https://www.eigent.ai/use-cases/organize-desktop-files/video)

[View guide →](https://www.eigent.ai/use-cases/organize-desktop-files)

#### [Audit ML CI Failures with Gemini 3.5 Flash on Eigent](https://www.eigent.ai/use-cases/eigent-gemini-managed-agents)

Orchestrate a multi-agent CI investigation that fetches logs, compares golden values, traces evidence, delegates deep reasoning, and produces structured audit reports.

[View demo →](https://www.eigent.ai/use-cases/eigent-gemini-managed-agents/video)

[View guide →](https://www.eigent.ai/use-cases/eigent-gemini-managed-agents)

#### [Ticket Management System Integration and Reporting](https://www.eigent.ai/use-cases/ticket-management-system-integration-and-reporting)

Import local ticket data into a browser-based management system, then generate a statistical report with charts and visual summaries.

[View demo →](https://www.eigent.ai/use-cases/ticket-management-system-integration-and-reporting/video)

[View guide →](https://www.eigent.ai/use-cases/ticket-management-system-integration-and-reporting)

[Explore more use cases →](https://www.eigent.ai/use-cases)

## 🛠️ Tech Stack

Eigent open-source Cowork desktop is built on modern, reliable 

## limitations

Our open-source Cowork continues to evolve with input from the community. Here's what's coming next:

| Topics                      | Issues                                                                                                                         | Discord Channel                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| **Context Engineering**     | - Prompt caching<br> - System prompt optimize<br> - Toolkit docstring optimize<br> - Context compression                       | [**Join Discord →**](https://discord.com/invite/CNcNpquyDc) |
| **Multi-modal Enhancement** | - More accurate image understanding when using browser<br> - Advanced video generation                                         | [**Join Discord →**](https://discord.com/invite/CNcNpquyDc) |
| **Multi-agent system**      | - Workforce support fixed workflow<br> - Workforce support multi-round conversion                                              | [**Join Discord →**](https://discord.com/invite/CNcNpquyDc) |
| **Browser Toolkit**         | - BrowseComp integration<br> - Benchmark improvement<br> - Forbid repeated page visiting<br> - Automatic cache button clicking | [**Join Discord →**](https://discord.com/invite/CNcNpquyDc) |
| **Document Toolkit**        | - Support dynamic file editing                                                                                                 | [**Join Discord →**](https://discord.com/invite/CNcNpquyDc) |
| **Terminal Toolkit**        | - Benchmark improvement<br> - Terminal-Bench integration                                                                       | [**Join Discord →**](https://discord.com/invite/CNcNpquyDc) |
| **Environment & RL**        | - Environment design<br> - Data-generation<br> - RL framework integration (VERL, TRL, OpenRLHF)                                | [**Join Discord →**](https://discord.com/invite/CNcNpquyDc) |

## [🤝 Contributing][contribution-link]

We believe in building trust and embracing all forms of open-source collaborations. Your creative contributions help drive the innovation of `Eigent`. Explore our GitHub issues and projects to dive in and show us what you’ve got 🤝❤️ [Contribution Guideline][contribution-link]

## Contributors

<a href="https://github.com/eigent-ai/eigent/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=eigent-ai/eigent" />
</a>

Made with [contrib.rocks](https://contrib.rocks).

<br>

## [❤️ Sponsor][sponsor-link]

Eigent is built on top of [CAMEL-AI.org][camel-ai-org-github]'s research and infrastructures. [Sponsoring CAMEL-AI.org][sponsor-link] will make `Eigent` better.

## **📄 Open Source License**

This repository is licensed under the [Apache License 2.0](LICENSE).

## 🌐 Community & Contact

For more information please contact info@eigent.ai

- **GitHub Issues:** Report bugs, request features, and track development. [Submit an issue][github-issue-link]

- **Discord:** Get real-time support, chat with the community, and stay updated. [Join us](https://discord.com/invite/CNcNpquyDc)

- **X (Twitter):** Follow for updates, AI insights, and key announcements. [Follow us][social-x-link]

- **WeChat Community:** Scan the QR code below to add our WeChat assistant, and join our WeChat community group.

<div align="center">
  <img src="./src/assets/wechat_qr.jpg" width="200" style="display: inline-block; margin: 10px;">
</div>

<!-- LINK GROUP -->

<!-- Social -->

<!-- camel & eigent -->

<!-- marketing -->

<!-- feature -->

[built-with-camel]: https://img.shields.io/badge/-Built--with--CAMEL-4C19E8.svg?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQ4IiBoZWlnaHQ9IjI3MiIgdmlld0JveD0iMCAwIDI0OCAyNzIiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik04LjgzMTE3IDE4LjU4NjVMMCAzMC44MjY3QzUuNDY2
