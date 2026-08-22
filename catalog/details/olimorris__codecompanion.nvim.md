# olimorris/codecompanion.nvim

✨ AI Coding, Vim Style

## features

- :speech_balloon: [Copilot Chat](https://github.com/features/copilot) meets [Zed AI](https://zed.dev/blog/zed-ai), in Neovim
- :zap: Integrates Neovim with LLMs and Agents in the CLI
- :electric_plug: Support for LLMs from [Anthropic](https://platform.claude.com/docs/en/about-claude/models/overview),  [DeepSeek](https://www.deepseek.com), [Google Gemini](https://ai.google.dev/gemini-api/docs/models), [GitHub Copilot](https://github.com/features/copilot), [GitHub Models](https://docs.github.com/en/github-models), [Kimi](https://platform.kimi.ai), [Mistral](https://mistral.ai/), [Novita](https://novita.ai/), [Ollama](https://ollama.com/), [OpenAI](https://developers.openai.com/api/docs/models), Azure OpenAI, [OpenRouter](https://openrouter.ai/), [HuggingFace](https://huggingface.co/) and [xAI](https://docs.x.ai/developers/models) out of the box (or [bring your own](https://codecompanion.olimorris.dev/extending/adapters.html))
- :robot: Support for [Agent Client Protocol](https://agentclientprotocol.com/overview/introduction), enabling coding with agents like [Augment Code](https://docs.augmentcode.com/cli/overview), [Cagent](https://github.com/docker/cagent) from Docker, [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview), [Codex](https://openai.com/codex), [Copilot CLI](https://github.com/features/copilot/cli), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Goose](https://block.github.io/goose/), [Cursor CLI](https://cursor.com/docs/cli/overview), [Kimi CLI](https://github.com/MoonshotAI/kimi-cli), [Kiro](https://kiro.dev/docs/cli/), [Mistral Vibe](https://github.com/mistralai/mistral-vibe) and [OpenCode](https://opencode.ai)
- :heart_hands: User contributed and supported [adapters](https://codecompanion.olimorris.dev/configuration/adapters-http#community-adapters)
- :man_technologist: [Code reviews](https://codecompanion.olimorris.dev/usage/code-review) enabling you to comment on and approve/reject agent code
- :battery: Support for [Model Context Protocol (MCP)](https://codecompanion.olimorris.dev/model-context-protocol#model-context-protocol-mcp-support)
- :rocket: [Inline transformations](https://codecompanion.olimorris.dev/usage/inline.html), code creation and refactoring
- :art: [Editor Context](https://codecompanion.olimorris.dev/usage/chat-buffer/editor-context.html), [Slash Commands](https://codecompanion.olimorris.dev/usage/chat-buffer/slash-commands.html), [Agents/Tools](https://codecompanion.olimorris.dev/usage/chat-buffer/agents-tools) and [Workflows](https://codecompanion.olimorris.dev/usage/workflows.html) to improve LLM output
- :brain: Support for [rules](https://codecompanion.olimorris.dev/usage/chat-buffer/rules.html) files like `CLAUDE.md`, `.cursor/rules` and your own custom ones
- :sparkles: Built-in [prompt library](https://codecompanion.olimorris.dev/usage/action-palette.html) for common tasks like advice on LSP errors and code explanations
- :building_construction: Create your own [custom prompts](https://codecompanion.olimorris.dev/configuration/prompt-library.html#creating-prompts), Editor Context and Slash Commands
- :inbox_tray: Have [multiple chats](https://codecompanion.olimorris.dev/usage/introduction.html#quickly-accessing-a-chat-buffer) open at the same time
- :art: Support for [images](https://codecompanion.olimorris.dev/usage/chat-buffer/#images-vision) and PDFs as input
- :muscle: Async execution for fast performance

<!-- panvimdoc-ignore-start -->

## :camera_flash: In Action

<div align="center">
  <p>
    <h3><a href="https://github.com/user-attachments/assets/aa109f1d-0ec9-4f08-bd9a-df99da03b9a4">The Chat Buffer</a></h3>
    <video controls muted src="https://github.com/user-attachments/assets/3cc83544-2690-49b5-8be6-51e671db52ef"></video>
  </p>
  <p>
    <h3><a href="https://github.com/user-attachments/assets/362b7cfd-e794-4d9c-9a74-90d5e2a87a32">Tools + Agentic Workflows</a></h3>
    <video controls muted src="https://github.com/user-attachments/asset

## installation

Everything you need to know about CodeCompanion (installation, configuration and usage) is within the [docs](https://codecompanion.olimorris.dev).

## :toolbox: Troubleshooting

Before raising an [issue](https://github.com/olimorris/codecompanion.nvim/issues), there are a number of steps you can take to troubleshoot a problem:

**Checkhealth**

Run `:checkhealth codecompanion` and check all dependencies are installed correctly. Also take note of the log file path.

**Turn on logging**

Update your config and turn debug logging on:

```lua
-- lazy.nvim
{
  "olimorris/codecompanion.nvim",
  dependencies = {
    "nvim-lua/plenary.nvim",
    "nvim-treesitter/nvim-treesitter",
  },
  opts = {
    -- NOTE: The log_level is in `opts.opts`
    opts = {
      log_level = "DEBUG", -- or "TRACE"
    },
  },
},

-- Other package managers
require("codecompanion").setup({
  opts = {
    log_level = "DEBUG", -- or "TRACE"
  }
})
```

and inspect the log file as per the location from the checkhealth command.

**Try with a `minimal.lua` file**

A large proportion of issues which are raised in Neovim plugins are to do with a user's own config. That's why I always ask users to fill in a `minimal.lua` file when they raise an issue. We can rule out their config being an issue and it allows me to recreate the problem.

For this purpose, I have included a [minimal.lua](https://github.com/olimorris/codecompanion.nvim/blob/main/minimal.lua) file in the repository for you to test out if you're facing issues. Simply copy the file, edit it and run neovim with `nvim --clean -u minimal.lua`.

<!-- panvimdoc-ignore-start -->

## :gift: Contributing

I am open to contributions but they will be implemented at my discretion. Feel free to open up a discussion before embarking on a PR and please read the [CONTRIBUTING.md](CONTRIBUTING.md) guide.

## :clap: Acknowledgements

- [Steven Arcangeli](https://github.com/stevearc) for his genius creation of the chat buffer and his feedback early on
- [Wtf.nvim](https://github.com/piersolenski/wtf.nvim) for the LSP assistant action
- [CopilotChat.nvim](https://github.com/CopilotC-Nvim/CopilotChat.nvim) for the rendering and usability of the chat
buffer
- [Aerial.nvim](https://github.com/stevearc/aerial.nvim) for the Tree-sitter parsing which inspired the symbols Slash
Command
- [Saghen](https://github.com/Saghen) for the fantastic docs inspiration from [blink.cmp](https://github.com/Saghen/blink.cmp) and continued PRs to the project
- [Catwell](https://github.com/catwell) for the [queue](https://github.com/catwell/cw-lua/blob/master/deque/deque.lua) inspiration that I use to stack agents and tools
- [bassamsdata](https://github.com/bassamsdata) for the amazing `insert_edit_into_file` tool (the list is endless) and ongoing contributions to this project
- [ravitemer](https://github.com/ravitemer) for the fantastic extensions API
- [Davidyz](https://github.com/Davidyz) for his continued, excellent contributions that keep CodeCompanion going
- [Conrad Irwin](https://github.com/conradirwin), [Agus Zubiaga](https://github.com/agu-z) and Morgan Krey from [Zed Industries](https://github.com/zed-industries) for their support in implementing [ACP](https://agentclientprotocol.com)
- [Sidekick.nvim](https://github.com/folke/sidekick.nvim) for the diff and terminal input inspiration
<!-- panvimdoc-ignore-end -->
