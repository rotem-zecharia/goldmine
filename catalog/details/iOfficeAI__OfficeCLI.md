# iOfficeAI/OfficeCLI

OfficeCLI is the first and best Office suite purpose-built for AI agents to read, edit, and automate Word, Excel, and PowerPoint files. Free, open-source, single binary, no Office installation require

## installation

curl -fsSL https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.sh | bash
# Windows (PowerShell): irm https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/main/install.ps1 | iex

# 2. Create a blank PowerPoint
officecli create deck.pptx

# 3. Start live preview — opens http://localhost:26315 in your browser
officecli watch deck.pptx

# 4. Open another terminal, add a slide — watch the browser update instantly
officecli add deck.pptx / --type slide --prop title="Hello, World!"
```

That's it. Every `add`, `set`, or `remove` command you run will refresh the preview in real time. Keep experimenting — the browser is your live feedback loop.

## Quick Start

```bash
# Create a presentation and add content
officecli create deck.pptx
officecli add deck.pptx / --type slide --prop title="Q4 Report" --prop background=1A1A2E
officecli add deck.pptx '/slide[1]' --type shape \
  --prop text="Revenue grew 25%" --prop x=2cm --prop y=5cm \
  --prop font=Arial --prop size=24 --prop color=FFFFFF

# View as outline
officecli view deck.pptx outline
# → Slide 1: Q4 Report
# →   Shape 1 [TextBox]: Revenue grew 25%

# View as HTML — opens a rendered preview in your browser, no server needed
officecli view deck.pptx html

# Get structured JSON for any element
officecli get deck.pptx '/slide[1]/shape[1]' --json

# Save and close — flushes the resident session to disk
officecli close deck.pptx
```

```json
{
  "tag": "shape",
  "path": "/slide[1]/shape[1]",
  "attributes": {
    "name": "TextBox 1",
    "text": "Revenue grew 25%",
    "x": "720000",
    "y": "1800000"
  }
}
```

## features

What used to take 50 lines of Python and 3 separate libraries:

```python
from pptx import Presentation
from pptx.util import Inches, Pt
prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[0])
title = slide.shapes.title
title.text = "Q4 Report"
# ... 45 more lines ...
prs.save('deck.pptx')
```

Now takes one command:

```bash
officecli add deck.pptx / --type slide --prop title="Q4 Report"
```

**What OfficeCLI can do:**

- **Create** documents from scratch -- blank or with content
- **Read** text, structure, styles, formulas -- in plain text or structured JSON
- **Analyze** formatting issues, style inconsistencies, and structural problems
- **Modify** any element -- text, fonts, colors, layout, formulas, charts, images
- **Reorganize** content -- add, remove, move, copy elements across documents

| Format | Read | Modify | Create |
|--------|------|--------|--------|
| Word (.docx) | ✅ | ✅ | ✅ |
| Excel (.xlsx) | ✅ | ✅ | ✅ |
| PowerPoint (.pptx) | ✅ | ✅ | ✅ |

**Word** — full [i18n & RTL support](https://github.com/iOfficeAI/OfficeCLI/wiki/i18n) (per-script font slots, per-script BCP-47 lang tags `lang.latin/ea/cs`, complex-script bold/italic/size, `direction=rtl` cascading through paragraph/run/section/table/style/header/footer/docDefaults, `rtlGutter` + `pgBorders` shorthand, locale-aware page numbering for Hindi/Arabic/Thai/CJK; `create --locale ar-SA` auto-enables RTL), [paragraphs](https://github.com/iOfficeAI/OfficeCLI/wiki/word-paragraph) (framePr, tabs shorthand, char-based indents), [runs](https://github.com/iOfficeAI/OfficeCLI/wiki/word-run) (underline.color, position half-pts), [tables](https://github.com/iOfficeAI/OfficeCLI/wiki/word-table) (virtual column ops add/remove/move/copyfrom, hMerge), [styles](https://github.com/iOfficeAI/OfficeCLI/wiki/word-style), [textbox](https://github.com/iOfficeAI/OfficeCLI/wiki/word-textbox) / [shape](https://github.com/iOfficeAI/OfficeCLI/wiki/word-shape) (textbox: rotation, `textDirection` `eaVert`/`vert270`, gradient, shadow, opacity), [headers/footers](https://github.com/iOfficeAI/OfficeCLI/wiki/word-header-footer), [images](https://github.com/iOfficeAI/OfficeCLI/wiki/word-picture) (PNG/JPG/GIF/SVG), [equations](https://github.com/iOfficeAI/OfficeCLI/wiki/word-equation) (LaTeX input), [diagrams](https://github.com/iOfficeAI/OfficeCLI/wiki/diagram) (mermaid → native editable shapes, or any mermaid type as a full-fidelity PNG), [comments](https://github.com/iOfficeAI/OfficeCLI/wiki/word-comment), [footnotes](https://github.com/iOfficeAI/OfficeCLI/wiki/word-footnote), [watermarks](https://github.com/iOfficeAI/OfficeCLI/wiki/word-watermark), [bookmarks](https://github.com/iOfficeAI/OfficeCLI/wiki/word-bookmark), [TOC](https://github.com/iOfficeAI/OfficeCLI/wiki/word-toc), [charts](https://github.com/iOfficeAI/OfficeCLI/wiki/word-chart), [hyperlinks](https://github.com/iOfficeAI/OfficeCLI/wiki/word-hyperlink), [sections](https://github.com/iOfficeAI/OfficeCLI/wiki/word-section), [form fields](https://github.com/iOfficeAI/OfficeCLI/wiki/word-formfield), [content controls (SDT)](https://github.com/iOfficeAI/OfficeCLI/wiki/word-sdt), [fields](https://github.com/iOfficeAI/OfficeCLI/wiki/word-field) (22 zero-param types + MERGEFIELD / REF / PAGEREF / SEQ / STYLEREF / DOCPROPERTY / IF), [OLE objects](https://github.com/iOfficeAI/OfficeCLI/wiki/word-ole), [revisions / tracked changes](https://github.com/iOfficeAI/OfficeCLI/wiki/word-revision) (`revision.type=ins\|del\|format\|moveFrom\|moveTo` + `revision.action=accept\|reject`, per-target `/revision[@author=Alice]` selector, tracked Find&Replace), page background color, [document properties](https://github.com/iOfficeAI/OfficeCLI/wiki/word-document)

**Excel** — [cells](https://github.com/iOfficeAI/OfficeCLI/wiki/excel-cell) (phonetic guide / furigana on add, Excel-UI `--shift left\|up` on remove / `shift=right\|down` on add), formulas (350+ built-in functions with auto-evaluation, spilling dynamic arrays with `_xlfn.` au

## tools

officecli batch deck.pptx --commands '[{"op":"set","path":"/slide[1]/shape[1]","props":{"text":"Hi"}}]'

# Keep whatever succeeds even if some items fail (pre-1.0.137 behavior)
officecli batch deck.pptx --input updates.json --best-effort --json

# Stop at the first failing command instead of running the rest (still rolls back everything unless combined with --best-effort)
officecli batch deck.pptx --input updates.json --stop-on-error --json
```

> **Reading the file with another tool? Flush to disk first.**
> officecli's own reads (`get`/`query`/`view`) always see your latest edits, so within officecli you never need to save. But a live resident defers the disk write, so **before a non‑officecli program reads the file** — python‑docx/openpyxl, Microsoft Word, a renderer, delivery/upload — flush it:
> ```bash
> officecli set report.docx /body/p[1] --prop bold=true
> officecli save report.docx           # flush, keep the resident warm (or `close` to flush + release)
> python my_reader.py report.docx      # now sees the edit
> ```
> A live resident also auto‑flushes shortly after going idle (adaptive 2–10s, scaled to the document's measured save cost). For a pipeline where another program reads after every command, set `OFFICECLI_RESIDENT_FLUSH=each` — every mutation is on disk before the command returns, while the resident stays warm. Full flush model (`each`/`auto`/fixed/`off`, save / close, env tuning): [wiki → open / close](https://github.com/iOfficeAI/OfficeCLI/wiki/command-open#when-the-file-on-disk-is-refreshed).

### Three-Layer Architecture

Start simple, go deep only when needed.

| Layer | Purpose | Commands |
|-------|---------|----------|
| **L1: Read** | Semantic views of content | `view` (text, annotated, outline, stats, issues, html, svg, screenshot) |
| **L2: DOM** | Structured element operations | `get`, `query`, `set`, `add`, `remove`, `move`, `swap` |
| **L3: Raw XML** | Direct XPath access — universal fallback | `raw`, `raw-set`, `add-part`, `validate` |

```bash
# L1 — high-level views
officecli view report.docx annotated
officecli view budget.xlsx text --cols A,B,C --max-lines 50

# L2 — element-level operations
officecli query report.docx "run:contains(TODO)"
officecli add budget.xlsx / --type sheet --prop name="Q2 Report"
officecli move report.docx /body/p[5] --to /body --index 1

# L3 — raw XML when L2 isn't enough
officecli raw deck.pptx '/slide[1]'
officecli raw-set report.docx document \
  --xpath "//w:p[1]" --action append \
  --xml '<w:r><w:t>Injected text</w:t></w:r>'
```

## AI Integration

### MCP Server

Built-in [MCP](https://modelcontextprotocol.io) server — register with one command:

```bash
officecli mcp claude       # Claude Code
officecli mcp cursor       # Cursor
officecli mcp vscode       # VS Code / Copilot
officecli mcp lmstudio     # LM Studio
officecli mcp list         # Check registration status
```

Exposes all document operations as tools over JSON-RPC — no shell access needed.

### Direct CLI Integration

Get OfficeCLI working with your AI agent in two steps:

1. **Install the binary** -- one command (see [Installation](#installation))
2. **Done.** OfficeCLI automatically detects your AI tools (Claude Code, GitHub Copilot, Codex) by checking known config directories and installs its skill file. Your agent can immediately create, read, and modify any Office document.

<details>
<summary><strong>Manual setup (optional)</strong></summary>

If auto-install doesn't cover your setup, you can install the skill file manually:

**Feed SKILL.md to your agent directly:**

```bash
curl -fsSL https://officecli.ai/SKILL.md
```

**Install as a local skill for Claude Code:**

```bash
curl -fsSL https://officecli.ai/SKILL.md -o ~/.claude/skills/officecli.md
```

**Other agents:** Include the contents of `SKILL.md` in your agent's system prompt or tool description.

</details>
