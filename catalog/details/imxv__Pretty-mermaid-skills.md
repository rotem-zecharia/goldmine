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

## tools

Check the 6 template files in `assets/example_diagrams/`:
- `flowchart.mmd` - Flowchart
- `sequence.mmd` - Sequence Diagram
- `state.mmd` - State Diagram
- `class.mmd` - Class Diagram
- `er.mmd` - ER Diagram
- `xychart.mmd` - XY Chart (bar and line)

The renderer also supports CJK state names, multiline labels, `linkStyle`, configurable ELK layout spacing, interactive XY chart tooltips, and ANSI-colored terminal output.

## requirements

- Node.js 16+
