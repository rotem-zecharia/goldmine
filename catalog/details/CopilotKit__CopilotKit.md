# CopilotKit/CopilotKit

The Frontend Stack for Agents & Generative UI. React, Angular, Mobile, Slack, and more. Makers of the AG-UI Protocol

## installation

Up and running in under five minutes. All you need is an LLM key (OpenAI, Anthropic, Gemini, etc.).

```bash
npx copilotkit@latest create
```

## Agent Skills

CopilotKit ships [agent skills](https://docs.copilotkit.ai) that teach your coding agent (Claude Code, Codex, Cursor, Gemini, and others) how to set up, build with, integrate, debug, and upgrade CopilotKit.

Install them into any project directory:

```bash
npx copilotkit@latest skills install
```

Run it again any time to refresh to the latest skills.

## Bring Your App to Life

https://github.com/user-attachments/assets/72b7b4f3-b6e7-460c-a932-5746fe3c8db3

<div align="center"> Add AI to your app in 1 minute</div>

**Features:**

- **Chat UI** – A fully customizable chat interface that supports message streaming, tool calls, and agent responses.
- **Backend Tool Rendering** – Enables agents to call backend tools that return UI components rendered directly in the client.
- **Generative UI** – Allows agents to generate and update UI components dynamically at runtime based on user intent and agent state.
- **Shared State** – A synchronized state layer that both agents and UI components can read from and write to in real time.
- **Human-in-the-Loop** – Lets agents pause execution to request user input, confirmation, or edits before continuing.
- **Self-Learning** _(early access)_ – Agents that continuously improve from user feedback via in-context reinforcement learning (CLHF).

## 🧩 Works With Your Stack

One agent backend. Every frontend.

| Platform                                                        | Status         | Get Started                                                                                             |
| --------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------- |
| ⚛️ React / Next.js                                              | ✅ GA          | [Quickstart](https://docs.copilotkit.ai/built-in-agent/quickstart)                                      |
| 🅰️ Angular                                                      | ✅ Supported   | [Source Code & Quickstart](https://github.com/CopilotKit/CopilotKit/tree/main/packages/angular)         |
| 💚 Vue                                                          | ✅ Supported   | [Source Code - Quickstart coming soon](https://github.com/CopilotKit/CopilotKit/tree/main/packages/vue) |
| 📱 React Native                                                 | ✅ Supported   | [Quickstart](https://docs.copilotkit.ai/react-native)                                                   |
| 💬 Slack / Microsoft Teams                                      | ✅ Supported   | [Channels](https://www.copilotkit.ai/channels) · [Quickstart](https://docs.copilotkit.ai/slack)         |
| 🔜 Discord / WhatsApp / Telegram / Google Chat / iMessage / SMS | 🟡 Coming soon | [Channels](https://www.copilotkit.ai/channels)                                                          |

Your agent logic stays the same — AG-UI handles the wire protocol, CopilotKit handles the UI layer for each framework and channel.

## 💬 Channels: One Agent, Every Chat App

<img width="1920" height="1080" alt="Write it once, run every channel" src="https://github.com/user-attachments/assets/883e5ede-0387-4ae8-a361-48da3adf8f22" />

The **Channels SDK** takes the agent you already built and drops it into the chat apps your users live in — same tools, same shared state, same human-in-the-loop, no rewrite (**[Learn more](https://www.copilotkit.ai/channels)**).

- **Slack** – Agents as first-class Slack apps: threads, tool calls, and human-in-the-loop approvals right in the channel.
- **Microsoft Teams** – Bring agentic workflows to the enterprise, where your org already lives.

👉 **[Explore Channels →](https://www.copilotkit.ai/channels)**

## 🧠 Self-Learning Agents

Improve your product by learning over time.

With **Continuous Learning from Huma
