# MODSetter/SurfSense

Air-gapped, privacy-focused, open-source NotebookLM alternative. AI agent that researches, transforms, and edits your documents. Join our Discord: https://discord.gg/ejRNvftDp9

## installation

1. Install SurfSense and do the initial onboarding setup.
2. Drop your files or folders in your sources.
3. Ask the agent to search or extract or edit your files.

## features

| Format | Research (cited answers) | Create | Edit (as a copy) | Transform |
|---|---|---|---|---|
| **PDF** | ✓ scanned pages too³ | ✓ | Fill and flatten forms; stamp watermarks, page numbers, headers, footers | Merge, split, extract, rotate, reorder pages |
| **Word** `.docx` | ✓ | ✓ or from your own `.docx` as a template | ✓ body text, as tracked changes and comments | To PDF¹ |
| **Excel** `.xlsx` | ✓ the agent also reads formulas | ✓ with formulas and native charts | ✓ cell values and formulas | Analyse with pandas, chart the results |
| **PowerPoint** `.pptx` | ✓ | ✓ or from your own `.pptx` as a template | Replace text on slides and notes; delete or duplicate slides | To PDF¹ |
| **CSV** | ✓ | — | — | Analyse with pandas, chart the results |
| **Images** PNG, JPEG, TIFF, BMP, WebP | ✓ text read by OCR³ | Images and infographics, edited by instruction² | — | Place in new documents |
| **Markdown**, plain text | ✓ | ✓ Markdown | — | — |
| **HTML** | ✓ | ✓ web page | — | — |
| **Books** EPUB, MOBI, AZW3 | ✓ without DRM | — | — | — |
| **Recordings** WAV, MP3, FLAC, Ogg Vorbis | ✓ transcribed on your machine | — | — | — |
| **Podcast** (audio) | — | ✓ with a transcript, voiced on your machine by default | — | — |
| **Mind maps, flashcards, quizzes** | — | ✓ in the app | — | — |

<sub>¹ With Office support (LibreOffice), turned on in Settings; it is never in the installer. ² Needs an image model, local or remote; none is chosen by default. ³ OCR reads Latin, Chinese and Japanese script.</sub>

Edits, conversions and PDF tools always make a new file; your original is never changed. PDF, Word and Excel do the most today, and support for the other formats keeps improving.

## Plugins

Connect them in **Settings › Plugins**.

**By SurfSense.** They read public pages without your own accounts and need a SurfSense license: [download the app](https://www.surfsense.com/downloads) and enter your email there for a free 14-day one.

| Plugin | What it does |
|---|---|
| **Google Search** | Search Google and read its results, ads and related questions |
| **Web Crawl** | Read a web page, or crawl a whole site into clean text |
| **YouTube** | Read YouTube videos, channels and their comments |
| **TikTok** | Read TikTok videos and their comments, search users, and see what is trending |
| **Reddit** | Read public Reddit posts with their comment threads, or a whole community |
| **Instagram** | Read public Instagram profiles, posts and reels, and find profiles by search |
| **Google Maps** | Find places on Google Maps and read their reviews |
| **Amazon** | Read Amazon products and search results |
| **Walmart** | Read Walmart products, search results and reviews |
| **Indeed** | Read job listings on Indeed |

**Third-party.** MCP servers from the [plugin registry](backend/plugins/registry), such as DeepWiki and Notion, or any you add by URL. No license needed; they stay off until you allow them.

## How it compares

| | NotebookLM (now Gemini Notebook) | SurfSense |
|---|---|---|
| Runs offline / air-gapped | No | **Yes** |
| Your documents leave your machine | Yes | **No**, unless you pick a remote model |
| Can edit your files | No | **Yes** |
| Open source | No | **Apache-2.0** |
| Models | Gemini only | Any OpenAI-compatible API, or a local one |

## Community

- [Discord](https://discord.gg/ejRNvftDp9) for help, [Issues](https://github.com/MODSetter/SurfSense/issues) for bugs, [Discussions](https://github.com/MODSetter/SurfSense/discussions) for ideas.
- **Contributing:** PRs go against `dev`; see [CONTRIBUTING.md](CONTRIBUTING.md) and [`surfsense_local/`](./surfsense_local) for the dev loop. How it works is in [`docs/`](docs/README.md).

<a href="https://github.com/MODSetter/SurfSense/graphs/contributors"><img src="https://contrib.rocks/image?repo=MODSetter/SurfSense" alt="SurfSense contributors" /></a>

## License

Apache-2.0. See [LICENSE](LICENSE).
