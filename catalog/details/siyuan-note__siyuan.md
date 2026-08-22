# siyuan-note/siyuan

An open-source, privacy-first, self-hosted knowledge workspace where humans and AI agents work together 开源、隐私优先、自托管的知识工作空间，让人与智能体在此协作

## features

Most features are free, even for commercial use.

- Content block
  - Block-level reference and two-way links
  - Custom attributes
  - SQL query embed
  - Protocol `siyuan://`
- Editor
  - Block-style
  - Markdown WYSIWYG
  - List outline
  - Block zoom-in
  - Million-word large document editing
  - Mathematical formulas, charts, flowcharts, Gantt charts, timing charts, staves, etc.
  - Web clipping
  - PDF Annotation link
- Export
  - Block ref and embed
  - Standard Markdown with assets
  - PDF, Word and HTML
  - Copy to WeChat MP, Zhihu and Yuque
- Database
  - Table view
- Flashcard spaced repetition
- AI writing and Q/A chat via OpenAI API
- Tesseract OCR 
- Multi-tab, drag and drop to split screen
- Template snippet
- JavaScript/CSS snippet
- Android/iOS/HarmonyOS App
- Docker deployment
- [API](https://github.com/siyuan-note/siyuan/blob/master/docs/API.md)
- Community marketplace

Some features are only available to paid members, for more details please refer to [Pricing](https://b3log.org/siyuan/en/pricing.html).

## limitations

- [SiYuan development plan and progress](https://github.com/orgs/siyuan-note/projects/1)
- [SiYuan changelog](CHANGELOG.md)

## installation

It is recommended to give priority to installing through the application market on desktop and mobile, so that you can upgrade the version with one click in the future.

## tools

| Category | Commands |
|----------|----------|
| Notebooks & Documents | `notebook`, `document`, `dailynote` — CRUD and daily notes |
| Content | `block`, `attr`, `outline` — block read/write, attributes, outline |
| Metadata | `tag`, `bookmark`, `template` — tags, bookmarks, template snippets |
| Queries | `search`, `sql` — full-text, semantic, asset-content, and SQL queries |
| References | `ref` — backlinks and mentions |
| Import/Export | `export`, `import`, `inbox` — Markdown, HTML, preview, Word, .sy.zip, Data, cloud inbox |
| Data Management | `repo`, `history`, `sync` — snapshots, versions, cloud sync |
| Utilities | `asset`, `file` — resources and file system |
| Database | `database` — attribute view management |
| Server | `serve` — start the kernel HTTP server |
| Workspace & System | `workspace`, `system` — list, inspect, system info |

Run `siyuan --help` for the full command tree. Use `-f json` (default is `-f table`) for script-friendly output. Most mutating commands also support `--dry-run` to preview changes without applying them.
