# nocobase/nocobase

NocoBase is an open-source AI + no-code platform for building business systems fast. Instead of generating everything from scratch, AI works on top of production-proven infrastructure and a WYSIWYG no

## installation

```bash
# Install NocoBase CLI
npm install -g @nocobase/cli
nb --version

# Install a NocoBase app
nb init --ui

# Optional: build together with an AI Agent
codex # claude, opencode
```

Detailed steps:

- <a target="_blank" href="https://docs.nocobase.com/ai/install-nocobase-app">Install a NocoBase app</a>
- <a target="_blank" href="https://docs.nocobase.com/ai/quick-start">AI Agent Integration Guide</a>

## Release Notes

Our [release notes](https://www.nocobase.com/en/blog/timeline) are updated regularly on the blog, with weekly summaries of important changes.

## features

### 1. Collaborative: AI and people build together

Coding agents get a full CLI and skills, while people get a WYSIWYG no-code interface, so both can collaborate efficiently.

#### Build with the AI coding agents you already know

Go from deployment to a working system in minutes with mainstream coding agents.

- Works with mainstream agents like Claude Code, Cursor, Codex, OpenCode, and TRAE
- Agents can handle setup, development, migration, and release end to end

![coding-agent](https://static-docs.nocobase.com/coding-agent.png)

#### Build manually in a WYSIWYG no-code interface

People can build and modify visually in a WYSIWYG interface, even without AI.

- Switch between usage mode and configuration mode with one click
- Review and configure data models, pages, workflows, and permissions visually
- Designed for regular users, not just developers

![wysiwyg](https://static-docs.nocobase.com/wysiwyg.gif)

#### Mix AI development and manual building however you need

Split the work as needed: people can refine what AI builds, and AI can continue from human configuration.

- AI can quickly create data models, pages, and workflows
- People can quickly refine the UI and interactions
- Collaborate as needed and keep iterating

![ai-no-coding](https://static-docs.nocobase.com/ai-no-coding.png)

### 2. Intelligent: AI helps run the business, not just build the system

NocoBase includes AI employees, so AI can work directly inside the system.

#### AI employees integrated into business workflows

AI employees get business context automatically and execute tasks directly inside the system.

- Front-end: help with analysis, Q&A, form filling, and more
- Back-end: handle document recognition, risk monitoring, and task routing automatically
- Integrated with workflows, AI employees can join decisions and execution

![AI-employee](https://static-docs.nocobase.com/ai-employee-home.png)

#### Open interfaces for the agent ecosystem

MCP, HTTP APIs, CLI, and rich skills let external agents connect securely.

- Platforms like OpenClaw, Hermes, Dify, Coze, and n8n connect through standard protocols
- Connects with Telegram, WhatsApp, Slack, and Gmail to query data, trigger actions, and execute business workflows
- One interface model keeps internal and external agents within the same boundaries

![agents](https://static-docs.nocobase.com/f-agents-logos.jpeg)

#### Permission controls keep AI behavior under control

Every AI action follows the same fine-grained permissions as human users.

- Each AI employee has its own role, with field-level read and write permissions
- Audit logs make every data change and workflow trigger traceable
- Admins can adjust AI permissions at any time to keep boundaries clear

![permission](https://static-docs.nocobase.com/f-permission.png)

### 3. Reliable: ready infrastructure for real business

Data models, permissions, and workflows are complex and error-sensitive.  
NocoBase provides them as built-in infrastructure, tested and proven in production.

#### Complete infrastructure, without starting from scratch

Dozens of built-in modules cover the most common business needs.

- Data models, permissions, workflows, and audit logs work out of the box
- Proven in production, instead of regenerated as black-box code each time
- Built-in guardrails keep AI output aligned with the system architecture

![core](https://static-docs.nocobase.com/f-core.png)

#### Data-model driven, with data decoupled from UI

Business data stays in standard relational structures, separate from the UI.

- Use the main database, external databases, and third-party APIs as data sources
- AI and people work on the same data model, so results stay transparent
- Your data always stays in your own database, without platform lock-in

![model](https://static-docs.nocobase.com/model.png)

#### Plugin architecture for sustainable growth

With a microkernel design, everything is a plugin and the system can grow without losing control.

- New fe
