# opendatalab/MinerU

Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows.

## features

### MinerU 4.1

- **Automatic acceleration across major platforms and GPUs:** Windows and Linux gain automatic ONNX acceleration for compatible Intel, AMD, and NVIDIA GPUs, alongside existing MPS/Metal support on macOS. MinerU detects devices, prioritizes discrete GPUs, and selects GPU or CPU execution for integrated graphics based on performance and compatibility. Representative core inference workloads run at approximately **2–3× CPU speed**.
- **A unified asynchronous Tasks API:** `/v1/tasks` replaces the previous `/v1/uploads` and `/v1/parse/jobs` workflow, with file manifests, URL inputs, cached-upload reuse, per-file execution and downloads, status queries, and cancellation. This is a breaking API update; review the [Tasks API reference](https://opendatalab.github.io/MinerU/usage/tasks/) before upgrading.
- **Recoverable synchronous file parsing:** The standalone `file-parse-server` provides `/v1/file_parse` for single-file uploads and attachment responses. Requests remain queryable after a wait timeout, and request IDs support recovery of known tasks. See the [file-parse API reference](https://opendatalab.github.io/MinerU/usage/file_parse/).
- **Hardware diagnostics and tier recommendations:** New `mineru-kit hardware detect` and `hardware info` commands help select a suitable service tier and inspect devices, runtime versions, and calibration information.

**Upgrade note:** Supported Python versions are now **3.11–3.14**. Deployments using the previous HTTP APIs should upgrade servers, Routers, SDKs, and clients together. See the [4.1 migration guide](https://opendatalab.github.io/MinerU/reference/migration_4_1/) for upgrade steps.

### MinerU 4.0

MinerU 4.0 brings document parsing, a local document library, and service tools into one workflow for document conversion, application integration, and agent reading.

- **Four parsing tiers**: Flash for fast previews and indexing, Basic for OCR and model-based parsing, and Standard / Advanced for more demanding layouts and quality requirements.
- **Multiple input formats**: PDF, images, DOC/DOCX, PPT/PPTX, XLS/XLSX, RTF, ODT/ODS/ODP, EPUB, OFD, HTML/MHTML, and CSV/TSV. [DocVortex](https://github.com/myhloli/docvortex) provides native document parsing.
- **Document library and agent reading**: discover files, cache results, search content, continue by page or block, and preserve stable citation locators.
- **Independent model configuration**: ONNX or Torch for small models; llama.cpp, vLLM, or LMDeploy for the VLM.
- **Unified tools**: Python SDK, V1 API, stateless batch conversion, multi-service Router, and a Gradio-based WebUI.
- **Structured results and rendering**: one document model supports nine rendering targets: Markdown, HTML, LaTeX, DOCX, EPUB, PDF, Structured Content, and Content List V1/V2. Each CLI/API exposes its own subset of exports; see [Output Formats and Result Contract](https://opendatalab.github.io/MinerU/reference/output_files/).

PDF and images support all four tiers. Office, OpenDocument, EPUB, OFD, HTML/MHTML, and CSV/TSV use local Flash native parsing. Plain text is read directly rather than parsed. Documents are not automatically uploaded to the official service; remote parsing requires explicit configuration.

## installation

> [!TIP]
> To choose between `flash`, `basic`, `standard`, and `advanced`, see the [MinerU 4.x Parsing Tiers Guide](https://github.com/opendatalab/MinerU/discussions/5709) for guidance on quality, speed, and resource trade-offs.

### Try Online

Try MinerU in your browser without installing it locally:

- [![HuggingFace](https://img.shields.io/badge/Demo_on_HuggingFace-yellow.svg?logo=data:image/png;base64,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&labelColor=white)](https://huggingface.co/spaces/opendatalab/MinerU) — Due to ZeroGPU limitations, only the `flash` and `basic` tiers are available.
- [![ModelScope](https://img.shields.io/badge/Demo_on_ModelScope-purple?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIzIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCiA8Zz4KICA8dGl0bGU+TGF5ZXIgMTwvdGl0bGU+CiAgPHBhdGggaWQ9InN2Z18xNCIgZmlsbD0iIzYyNGFmZiIgZD0ibTAsODkuODRsMjUuNjUsMGwwLDI1LjY0OTk5bC0yNS42NSwwbDAsLTI1LjY0OTk5eiIvPgogIDxwYXRoIGlkPSJzdmdfMTUiIGZpbGw9IiM2MjRhZmYiIGQ9Im05OS4xNCwxMTUuNDlsMjUuNjUsMGwwLDI1LjY1bC0yNS42NSwwbDAsLTI1LjY1eiIvPgogIDxwYXRoIGlkPSJzdmdfMTYiIGZpbGw9IiM2MjRhZmYiIGQ9Im0xNzYuMDksMTQxLjE0bC0yNS42NDk5OSwwbDAsMjIuMTlsNDcuODQsMGwwLC00Ny44NGwtMjIuMTksMGwwLDI1LjY1eiIvPgogIDxwYXRoIGlkPSJzdmdfMTciIGZpbGw9IiMzNmNmZDEiIGQ9Im0xMjQuNzksODkuODRsMjUuNjUsMGwwLDI1LjY0OTk5bC0yNS42NSwwbDAsLTI1LjY0OTk5eiIvPgogIDxwYXRoIGlkPSJzdmdfMTgiIGZpbGw9IiMzNmNmZDEiIGQ9Im0wLDY0LjE5bDI1LjY1LDBsMCwyNS42NWwtMjUuNjUsMGwwLC0yNS42NXoiLz4KICA8cGF0aCBpZD0ic3ZnXzE5IiBmaWxsPSIjNjI0YWZmIiBkPSJtMTk4LjI4LDg5Ljg0bDI1LjY0OTk5LDBsMCwyNS42NDk5OWwtMjUuNjQ5OTksMGwwLC0yNS42NDk5OXoiLz4KI

## configuration

First, download the models for the target startup tier (`basic`, or `standard`).
Replace `<tier>` with `basic` or `standard`.

```bash
mineru-kit models download --tier <tier>
mineru-kit models verify --tier <tier>
```

Then, enable managed local parse server for the startup tier.

```bash
mineru config set parse_server.local.managed_tier <tier>
mineru config set parse_server.local.mode managed
mineru server status --json
```

Rules:

- Change local parse-server config or restart the server only when the user asks for or approves.
- Download and verify models for the startup tier (`basic` or `standard`) before enabling managed mode.
- Set `parse_server.local.managed_tier` before `parse_server.local.mode=managed`.
- Poll `mineru server status --json` and use managed parsing only after the target tier is healthy.
- If local quality parsing cannot start, do not add `--remote` automatically; ask the user first.

## First Read From A File

Use `mineru parse` for the first active read from a local file path.

```bash
mineru parse "report.pdf"
```

By default, readable content is printed to stdout. Use `--output` only when the user wants the result saved to a file.

Use JSON when you need structured status, tier, content, and continuation:

```bash
mineru parse "report.pdf" --json
```

PDF page selection is shared across CLI, Doclib, API, Gradio and Python. See the [page-range syntax and historical result compatibility](docs/next/page-ranges.md). New requests use the current syntax; stored positive page ranges using ASCII `~` remain readable without rebuilding Doclib caches. Fullwidth `～` and negative page-number notation are not supported.

For a specific page range (1-based, inclusive; `r1` is the last page, `all` selects every page):

```bash
mineru parse "report.pdf" --pages 1-10
mineru parse "report.pdf" --pages all
```

For bounded context:

```bash
mineru parse "report.pdf" --limit 12000
```

For no synchronous wait:

```bash
mineru parse "report.pdf" --no-wait --json
```

For longer wait:

```bash
mineru parse "report.pdf" --wait 180 --json
```

For output to a file:

```bash
mineru parse "report.pdf" --output ./report.md
```

Rules:

- Quote paths with spaces.
- For paged documents, the default active read range is the first page window, usually `1-10`; continue with the returned marker or `next_request` instead of reading the whole document by default.
- Use the default tier unless the user has a quality/speed/privacy preference.
- Use `--pages all` only when the user asks for the whole document or the document is known to be small enough.
- Prefer `--limit` and continuation for long documents.
- Once you have a locator, switch to `mineru read`.

## Continue Reading

MinerU output may include a command to continue reading:

```text
<!-- Next: mineru read doc:ab12cd3/tier:standard/page:11 -->
```

or:

```text
<!-- Next: mineru parse report.pdf --pages 11-20 -->
```

Run the suggested command exactly unless the user asks for a different page, block, format, or limit.

Agent rules:

- Do not guess the next page or block if MinerU provides a next command.
- Do not restart parsing from page 1 when continuing.
- For non-paged long documents, continuation may use an `--after` cursor from `next_request.after`; use that exact cursor.
- Prefer `mineru read` when the next command or JSON output gives a locator.
- Use `--limit` to keep output within the conversation budget.
- Preserve locators for citations and follow-up reads.

## Read By Locator

Use `mineru read` when a document has already been parsed or when the user gives a locator.

Locator forms:

```text
doc:{short_id}
doc:{short_id}/tier:{tier}
doc:{short_id}/tier:{tier}/page:{page_no}
doc:{short_id}/tier:{tier}/page:{page_no}/block:{block_no}
doc:{short_id}/tier:{tier}/page:{page_no}/block:{block_no}/char:{offset}
```

Examples:

```bash
mineru read "doc:ab12cd3/tier:standard/page:4"
mineru read "doc:ab12cd3/tier:standard/page:4/block:7"
mineru read "doc:ab12cd3/tier:standa

## tools

Query usage and limits for the configured Remote API:

```bash
mineru usage
mineru usage --json
```

## JSON Output

Use `--json` when an agent needs stable machine-readable fields.

`mineru parse --json` returns:

```json
{
  "parse": { "...": "parse summary" },
  "content": { "...": "readable content and continuation data" }
}
```

If parsing is still pending, timed out, or `--no-wait` is used, `content` may be `null`.

Errors use:

```json
{
  "error": {
    "type": "engine_error",
    "code": "quality_tier_unavailable",
    "message": "...",
    "param": "tier",
    "retryable": false,
    "user_action": "...",
    "docs_url": null
  }
}
```

Agent rules:

- Branch on `error.code`, not on prose in `message`.
- Respect `retryable`.
- Use `user_action` to decide the next command or user-facing suggestion.
- Do not strip locator fields from parsed content; they are needed for continuation and citation.

## Error Recovery

### Normal-Quality Recovery Gate

When `quality_tier_unavailable` or `no_engine` is returned for an active document-reading request:

1. Run `mineru server status --json` to inspect locally available tiers and parse-server state.
2. If no local quality tier is available, follow [Assess Local Hardware](#assess-local-hardware). Do not treat an unconfigured or disabled local parse server as proof that the hardware is unsupported.
3. Present the currently available tiers. If hardware was assessed, also present the detected hardware and each applicable local tier's hardware status. Then follow the tier-choice guidance in the Quality Tiers section.
4. Stop and wait for the user to choose a recovery path.
5. Run only the selected path. If that path fails, report the failure and return to this decision gate with the remaining applicable choices.

Do not use another document parser before this gate unless the user already requested or authorized that fallback. A recoverable MinerU setup or tier error does not by itself mean that MinerU is unavailable.

Use this table for common error codes:

| Code | Meaning | Agent action |
|---|---|---|
| `server_not_running` | MinerU background service is unavailable | Run `mineru server start`, then retry once |
| `quality_tier_unavailable` | Normal reading quality is unavailable | Follow the Normal-Quality Recovery Gate; do not fall back automatically |
| `no_engine` | Requested tier is unavailable locally | Follow the Normal-Quality Recovery Gate; do not fall back automatically |
| `engine_unavailable` | Engine process unavailable | Retry if `retryable`; otherwise check `mineru server status` |
| `parse_server_unavailable` | Parsing service cannot be reached | Check `mineru server status`; do not switch privacy boundary |
| `tier_mismatch` | Requested tier unsupported | Ask user to choose a supported tier |
| `parse_failed` | MinerU could not parse the file | Report failure; suggest a different tier only if privacy rules allow |
| `parse_timeout` | Parse exceeded timeout | Retry with longer `--wait`, inspect status, or use lower tier if user accepts |
| `parse_oom` | Memory or VRAM exhausted | Suggest lower quality, smaller `--pages`, or remote only with permission |
| `remote_not_allowed` | Remote might be needed but was not authorized | Ask user whether uploading is acceptable; do not add `--remote` yourself |
| `invalid_api_key` | API key invalid | Ask user to set a valid key |
| `quota_exceeded` | Remote quota exhausted | Suggest waiting or using local |
| `rate_limit_exceeded` | Remote rate limit | Retry later if appropriate |
| `file_not_found` | Path or file id missing | Ask for correct path or run `mineru find` |
| `file_permission_denied` | Local file unreadable | Ask user to fix permissions |
| `file_type_unsupported` | Format unsupported | Report unsupported type |
| `file_encrypted` | Password-protected file | Ask user for an unlocked copy |
| `file_corrupted` | File cannot be read | Ask for a valid copy |
| `page_range_invalid` | Bad PDF `--pages` value, or `--page
