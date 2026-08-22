# virgiliojr94/book-to-skill

Turn any technical book PDF into a Claude Code skill — ready to study, reference, and use while you work.

## tools

`/book-to-skill <path|folder|glob> [skill-name]` — plus analyze-only, generate-from-analysis, and update/fold-in modes. After a conversion, the converter can publish the skill to GitHub (private by default) so any host installs it with `npx skills add`.

▶️ **All modes and examples → [docs/usage.md](docs/usage.md)**

💬 **In practice → [use cases](https://github.com/virgiliojr94/book-to-skill-use-cases)** — a DevEx book became a survey of 300+ engineers; a scanned PDF that stalled became [#130](https://github.com/virgiliojr94/book-to-skill/pull/130). Add yours: the account lives in your own Gist, the index takes a one-line PR.

---

## installation

```bash
# One command, any host — via the cross-agent skills CLI:
npx skills add virgiliojr94/book-to-skill

# Or manually — clone into your skills folder (registers /book-to-skill):
git clone https://github.com/virgiliojr94/book-to-skill.git ~/.claude/skills/book-to-skill
# (Copilot CLI: ~/.copilot/skills/ · Amp/cross-agent: ~/.agents/skills/)
```

📥 **All hosts, optional extractors, and the standalone CLI → [docs/install.md](docs/install.md)**

---

## ❓ FAQ

Common questions — "why not just dump the PDF?", cost, privacy, non-book inputs, multi-file books.

❓ **Answers → [docs/faq.md](docs/faq.md)**

---

<details>
<summary>🔧 <strong>Requirements</strong></summary>


The extractor tries tools in order per format and uses the first available. If nothing is installed, it tells you which command to run. Plain text, Markdown, reStructuredText and AsciiDoc need no extra deps.

> **Check your setup in one command:** `python3 scripts/extract.py --check` prints which extractors are installed for every format and the exact command to install anything missing — no file needed.

**PDF — choose by book type:**

| Book type | Tool | Install | Speed |
|-----------|------|---------|-------|
| Text-heavy (prose, few tables) | `pdftotext` (poppler) | `sudo apt install poppler-utils` | ⚡ instant |
| Text-heavy fallback | `pypdf` | `pip3 install pypdf` | ⚡ instant |
| Text-heavy fallback | `pdfminer.six` | `pip3 install pdfminer.six` | ⚡ instant |
| **Technical (code, tables, formulas)** | **`docling`** | `pip3 install docling` | ~1.5s/page |

> Before extraction begins, the skill asks you whether the book is **technical** or **text-heavy** and picks the right tool automatically. Docling preserves markdown tables and code blocks; pdftotext is faster for prose-only books.

> **Scanned PDFs need OCR first.** A PDF that is page images with no text layer — a photographed or scanned book — has nothing for these tools to extract. The extractor checks the first pages and stops immediately with an explanation, rather than working through the whole book to produce an empty skill. Run OCR yourself, then convert the result:
>
> ```bash
> ocrmypdf input.pdf output.pdf
> ```

**EPUB:**

| Tool | Install | Quality |
|------|---------|---------|
| `ebooklib` + `beautifulsoup4` | `pip3 install ebooklib beautifulsoup4` | ⭐⭐⭐ Best |
| stdlib `zipfile` | built-in — no install needed | ⭐⭐ Always available |

**Other formats:**

| Format | Tool | Install |
|--------|------|---------|
| DOCX | `python-docx` (fallback: stdlib ZIP/XML) | `pip3 install python-docx` |
| HTML | `beautifulsoup4` (fallback: stdlib `html.parser`) | `pip3 install beautifulsoup4` |
| RTF | `striprtf` (fallback: regex) | `pip3 install striprtf` |
| MOBI / AZW / AZW3 | Calibre `ebook-convert` (external app, not pip) | https://calibre-ebook.com/download |
| TXT / Markdown / reStructuredText / AsciiDoc | built-in | — |

---


</details>

<details>
<summary>📁 <strong>Repository structure</strong></summary>


```
book-to-skill/
├── SKILL.md              # Skill definition + step-by-step instructions (the generator spec)
├── scripts/
│   ├── extract.py        # Thin entrypoint wrapper
│   └── extractor/        # Modular extraction package
│       ├── config.py     # Extensions, paths, dependency constants
│       ├── dependencies.py  # optional-dep probing + --check
│       ├── exceptions.py # ExtractionError (per-source failures, batch-safe)
│       ├── utils.py      # CLI parsing, multi-source resolution, chapter detection, runner
│       └── parsers/      # Format-specific parsers (pdf, epub, docx, html, rtf, calibre, text)
├── tools/
│   ├── discovery_tax.py  # measures token cost vs context-dump / discovery loop
│   └── validate_skill.py # checks a generated SKILL.md against host rules (--lens claude|copilot|amp)
├── tests/                # pytest suite (extraction, detection, discovery tax)
├── docs/
│   ├── performance.md    # measured benchmarks, discovery tax, cost
│   └── architecture.md 
