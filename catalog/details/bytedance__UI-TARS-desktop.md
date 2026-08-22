# bytedance/UI-TARS-desktop

The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra

## features

- 🖱️ **One-Click Out-of-the-box CLI** - Supports both **headful** [Web UI](https://agent-tars.com/guide/basic/web-ui.html) and **headless** [server](https://agent-tars.com/guide/advanced/server.html) [execution](https://agent-tars.com/guide/basic/cli.html).
- 🌐 **Hybrid Browser Agent** - Control browsers using [GUI Agent](https://agent-tars.com/guide/basic/browser.html#visual-grounding), [DOM](https://agent-tars.com/guide/basic/browser.html#dom), or a hybrid strategy.
- 🔄 **Event Stream** - Protocol-driven Event Stream drives [Context Engineering](https://agent-tars.com/beta#context-engineering) and [Agent UI](https://agent-tars.com/blog/2025-06-25-introducing-agent-tars-beta.html#easy-to-build-applications).
- 🧰 **MCP Integration** - The kernel is built on MCP and also supports mounting [MCP Servers](https://agent-tars.com/guide/basic/mcp.html) to connect to real-world tools.

## installation

<img alt="Agent TARS CLI" src="https://agent-tars.com/agent-tars-cli.png">

```bash
# Launch with `npx`.
npx @agent-tars/cli@latest

# Install globally, required Node.js >= 22
npm install @agent-tars/cli@latest -g

# Run with your preferred model provider
agent-tars --provider volcengine --model doubao-1-5-thinking-vision-pro-250428 --apiKey your-api-key
agent-tars --provider anthropic --model claude-3-7-sonnet-latest --apiKey your-api-key
```

Visit the comprehensive [Quick Start](https://agent-tars.com/guide/get-started/quick-start.html) guide for detailed setup instructions.

### Documentation

> 🌟 **Explore Agent TARS Universe** 🌟

<table>
  <thead>
    <tr>
      <th width="20%" align="center">Category</th>
      <th width="30%" align="center">Resource Link</th>
      <th width="50%" align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">🏠 <strong>Central Hub</strong></td>
      <td align="center">
        <a href="https://agent-tars.com">
          <img src="https://img.shields.io/badge/Visit-Website-4F46E5?style=for-the-badge&logo=globe&logoColor=white" alt="Website" />
        </a>
      </td>
      <td align="left">Your gateway to Agent TARS ecosystem</td>
    </tr>
      <tr>
      <td align="center">📚 <strong>Quick Start</strong></td>
      <td align="center">
        <a href="https://agent-tars.com/guide/get-started/quick-start.html">
          <img src="https://img.shields.io/badge/Get-Started-06B6D4?style=for-the-badge&logo=rocket&logoColor=white" alt="Quick Start" />
        </a>
      </td>
      <td align="left">Zero to hero in 5 minutes</td>
    </tr>
    <tr>
      <td align="center">🚀 <strong>What's New</strong></td>
      <td align="center">
        <a href="https://agent-tars.com/beta">
          <img src="https://img.shields.io/badge/Read-Blog-F59E0B?style=for-the-badge&logo=rss&logoColor=white" alt="Blog" />
        </a>
      </td>
      <td align="left">Discover cutting-edge features & vision</td>
    </tr>
    <tr>
      <td align="center">🛠️ <strong>Developer Zone</strong></td>
      <td align="center">
        <a href="https://agent-tars.com/guide/get-started/introduction.html">
          <img src="https://img.shields.io/badge/View-Docs-10B981?style=for-the-badge&logo=gitbook&logoColor=white" alt="Docs" />
        </a>
      </td>
      <td align="left">Master every command & features</td>
    </tr>
    <tr>
      <td align="center">🎯 <strong>Showcase</strong></td>
      <td align="center">
        <a href="https://github.com/bytedance/UI-TARS-desktop/issues/842">
          <img src="https://img.shields.io/badge/View-Examples-8B5CF6?style=for-the-badge&logo=github&logoColor=white" alt="Examples" />
        </a>
      </td>
      <td align="left">View use cases built by the official and community</td>
    </tr>
    <tr>
      <td align="center">🔧 <strong>Reference</strong></td>
      <td align="center">
        <a href="https://agent-tars.com/api/">
          <img src="https://img.shields.io/badge/API-Reference-EF4444?style=for-the-badge&logo=book&logoColor=white" alt="API" />
        </a>
      </td>
      <td align="left">Complete technical reference</td>
    </tr>
  </tbody>
</table>

<br/>
<br/>
<br/>

## UI-TARS Desktop

<p align="center">
  <img alt="UI-TARS" width="260" src="./apps/ui-tars/resources/icon.png">
</p>

UI-TARS Desktop is a native GUI agent for your local computer, driven by [UI-TARS](https://github.com/bytedance/UI-TARS) and Seed-1.5-VL/1.6 series models.

<div align="center">
<p>
        &nbsp&nbsp 📑 <a href="https://arxiv.org/abs/2501.12326">Paper</a> &nbsp&nbsp
        | 🤗 <a href="https://huggingface.co/ByteDance-Seed/UI-TARS-1.5-7B">Hugging Face Models</a>&nbsp&nbsp
        | &nbsp&nbsp🫨 <a href="https://discord.gg/pTXwYVjfcs">Discord</a>&nbsp&nbsp
        | &nbsp&nbsp🤖 <a href="https://www.modelscope.cn/collections/UI-TARS-bccb56fa1ef640">ModelScope</a>&nbsp&nbsp
<br>
🖥️ Desktop Application &nbsp&nbsp
| &nbsp&nbsp 👓 <a href="https://
