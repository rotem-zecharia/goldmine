# sirmalloc/ccstatusline

🚀 Beautiful highly customizable statusline for Claude Code CLI with powerline support, themes, and more.

## configuration

- **📦 Config import/export** - Export the current TUI configuration to JSON, validate and preview imports, then replace all settings or merge only supplied fields while preserving local installation metadata and leaving the result unsaved for review.

## tools

- **🪄 Weekly Fable usage** - Added a `Weekly Fable Usage` widget with percentage, progress-bar, remaining-mode, and time-cursor controls.
- **📊 Reshaped usage API support** - Session and all-model weekly usage can fall back to the newer `limits[]` response, while Sonnet, Opus, and Fable weekly widgets read authoritative `weekly_scoped` entries so migrated accounts do not show stale or frozen values.
- **🧠 Correct post-compaction context** - Context length and percentage widgets reset immediately from `compact_boundary.postTokens` after `/compact`, then switch to the first new turn instead of retaining the pre-compaction size.
- **🧹 Reliable hidden-widget separators** - Manual separators now look past widgets that render empty, preserve the intended visible boundary, and inherit colors from the actual preceding visible widget.
- **⚡ Non-blocking Git PR/CI refreshes** - Git PR and CI widgets render from a versioned disk cache while stale data refreshes in the background, preventing slow `gh` calls from blocking the status line.

## features

- **📊 Real-time Metrics** - Display model name, git branch, token usage, Sonnet/Opus/Fable weekly usage, extra usage limits, voice input state, session duration, compaction count, block timer, and more
- **🎨 Fully Customizable** - Choose what to display and customize colors for each element
- **⚡ Powerline Support** - Beautiful Powerline-style rendering with arrow separators, caps, and custom fonts
- **📐 Multi-line Support** - Configure multiple independent status lines
- **🖥️ Interactive TUI** - Built-in configuration interface using React/Ink
- **🔎 Fast Widget Picker** - Add/change widgets by category with search and ranked matching
- **⚙️ Global Options** - Apply consistent formatting across all widgets (padding, separators, bold, minimalist mode, and color overrides)
- **📦 Portable Configurations** - Export settings to JSON and preview replace-or-merge imports for backups and sharing
- **🚀 Cross-platform** - Works seamlessly with both Bun and Node.js
- **🔧 Flexible Configuration** - Supports custom Claude Code config directory via `CLAUDE_CONFIG_DIR` environment variable
- **📏 Smart Width Detection** - Automatically adapts to terminal width with flex separators
- **⚡ Zero Config** - Sensible defaults that work out of the box

<br />

## 🌐 Localizations

The localizations in this section are third-party forks maintained outside this repository. They are not maintained, reviewed, or endorsed by this repository, so review their code and releases before using them.

- 🌏 **中文版 (Chinese):** [ccstatusline-zh](https://github.com/huangguang1999/ccstatusline-zh)

<br />

## installation

### No installation needed! Use directly with npx or bunx:

```bash
