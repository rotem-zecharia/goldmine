# imxv/Pretty-mermaid-skills

AI Agent Skill to generate and render beautiful Mermaid diagrams as SVG or terminal ASCII — 15 themes, 6 diagram types, batch CLI, no browser.

## installation

```bash
npx skills add imxv/pretty-mermaid-skills@pretty-mermaid -g -y
```

[View the skill, install count, and security audits on skills.sh →](https://www.skills.sh/imxv/pretty-mermaid-skills/pretty-mermaid)

## features

- **Made for AI agents**: works with Claude Code, Cursor, Codex, Gemini CLI, and more
- **One source, two outputs**: polished SVG for docs and ASCII/Unicode for terminals
- **No browser required**: renders locally without Chromium, Puppeteer, or a DOM
- **Flexible by default**: 15 themes, custom colors, six diagram types, and batch rendering

## ✨ Features

- 📊 **Multi-format Support**: SVG and ASCII rendering export
- 🎨 **Rich Themes**: 15 built-in themes for different scenarios
- 📈 **Six Diagram Types**: Flowchart, Sequence, State, Class, ER, and XY charts
- ⚡ **High Performance**: Batch parallel rendering
- 📚 **Ready to Use**: Complete templates and detailed documentation

### Supported Themes
| Light Themes | Dark Themes | Other |
| :--- | :--- | :--- |
| zinc-light | zinc-dark | nord |
| tokyo-night-light | tokyo-night | nord-light |
| catppuccin-latte | tokyo-night-storm | dracula |
| github-light | catppuccin-mocha | one-dark |
| solarized-light | github-dark | |
| | solarized-dark | |

## 🎨 Theme Gallery

Compare the same flowchart across every built-in theme in the [complete 15-theme gallery](docs/THEME_GALLERY.md).

<p align="center">
  <img src="assets/theme_gallery/tokyo-night.svg" alt="Tokyo Night theme preview" width="49%">
  <img src="assets/theme_gallery/github-light.svg" alt="GitHub Light theme preview" width="49%">
</p>

## 🤖 AI Assistant Integration

Seamlessly integrates with the following AI coding environments:

- **Claude Code**
- **Cursor**
- **Gemini CLI**
- **Antigravity**
- **OpenCode**
- **Codex**
- **qoder**

## tools

Check the 6 template files in `assets/example_diagrams/`:
- `flowchart.mmd` - Flowchart
- `sequence.mmd` - Sequence Diagram
- `state.mmd` - State Diagram
- `class.mmd` - Class Diagram
- `er.mmd` - ER Diagram
- `xychart.mmd` - XY Chart (bar and line)

The renderer also supports CJK state names, multiline labels, `linkStyle`, configurable ELK layout spacing, interactive XY chart tooltips, and ANSI-colored terminal output.

## 📚 Documentation

- [Skill usage guide](SKILL.md)
- [Theme gallery](docs/THEME_GALLERY.md)
- [Diagram syntax reference](references/DIAGRAM_TYPES.md)
- [Theme and custom color reference](references/THEMES.md)
- [beautiful-mermaid API reference](references/api_reference.md)
- [Release process](RELEASING.md)

## 🤝 Community

Read the [contribution guide](CONTRIBUTING.md), report problems with the issue templates, and review the [security policy](SECURITY.md) before sharing sensitive findings. Release history is tracked in the [changelog](CHANGELOG.md).

## requirements

- Node.js 16+

## 📄 License
MIT License

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=imxv/Pretty-mermaid-skills&type=timeline&legend=top-left)](https://www.star-history.com/?repos=imxv%2FPretty-mermaid-skills&type=timeline&legend=bottom-right)

## 🙏 Acknowledgments
Based on [beautiful-mermaid](https://github.com/lukilabs/beautiful-mermaid)
