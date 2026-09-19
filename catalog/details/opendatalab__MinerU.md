# opendatalab/MinerU

Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows.

## installation

### In Agent Workflow

You can install the `mineru` skill, and let agent install MinerU for you. Copy the following message and send it to your agent:

```text
Install or update the global `mineru` skill. First, run `npx skills add opendatalab/MinerU --skill mineru --global --yes`. If `npx` is unavailable, fetch https://gcore.jsdelivr.net/gh/opendatalab/MinerU/skills/mineru/SKILL.md, use its content as `mineru/SKILL.md`, and save it under the appropriate global skills directory for the current agent, not in the current project. Also check both global and project-level skills for other installed skills whose names contain `mineru`. Report any matches and ask before removing them. If global memory is available, record this preference there: "Whenever a PDF, image, or Office document needs to be read or parsed, prefer the `mineru` Skill." Do not write this preference to the current project.
```

### Install Manually

Python `>=3.10,<3.15`. Install MinerU 4.0 stable in a virtual environment:

```bash
pip install uv
uv venv .mineru --python 3.12

# Linux/macOS
source .mineru/bin/activate
# Windows (PowerShell)
.\.mineru\Scripts\Activate.ps1
```

```bash
uv pip install -U "mineru>=4.0,<5"
mineru-kit parse document.pdf -o document.md --tier standard
mineru-kit webui
```

### Python SDK

`DoclibClient` drives the local document library from Python. Start the server first (`mineru server start`), then:

```python
import time

from mineru import DoclibClient
from mineru.doclib import ParseRequest

client = DoclibClient()
submit = client.ensure_parse(ParseRequest(path="paper.pdf", tier="standard"))

# ensure_parse returns immediately; poll the parse tasks it created.
for parse_id in submit.wait_parse_ids:
    parse = client.get_parse(parse_id)
    while parse.status in ("pending", "parsing"):
        time.sleep(1)
        parse = client.get_parse(parse_id)
    if parse.status != "done":
        raise RuntimeError(f"parse {parse_id} ended as {parse.status}: {parse.error_code} {parse.error_msg}")

content = client.read_content(f"doc:{submit.short_id}/tier:standard/page:1")
print(content.content)
```

`DoclibClient` also covers search, watched directories, locators for
page/block continuation, and result invalidation — see
`help(DoclibClient)` or the [SDK and API guide](https://opendatalab.github.io/MinerU/usage/sdk_api/).

The default install works out of the box: small models run ONNX CPU inference and the VLM runs llama.cpp in Vulkan mode, which offers good compatibility on the vast majority of devices. If the device has an NVIDIA GPU, install `mineru[full]>=4.0` for the best throughput. Note that on Windows the GPU build of torch must be installed separately, while on macOS the default install is already the best-throughput package and `[full]` is not needed. On other non-NVIDIA devices, you need to install an accelerated build of torch plus vllm/lmdeploy yourself to get the best inference speed and throughput.

For the document library and agent reading, use `mineru parse document.pdf --json`. It defaults to the first 10 PDF pages; continue with returned locators. Stateless `mineru-kit parse` defaults to all pages.

[Installation](https://opendatalab.github.io/MinerU/quick_start/) · [Tiers and runtimes](https://opendatalab.github.io/MinerU/usage/tiers/) · [SDK and API](https://opendatalab.github.io/MinerU/usage/sdk_api/) · [Docker deployment](https://opendatalab.github.io/MinerU/quick_start/docker_deployment/) · [3.x → 4.0 migration](https://opendatalab.github.io/MinerU/reference/migration_4/) · [Release history](https://opendatalab.github.io/MinerU/reference/changelog/)

> Docker deployment for non-NVIDIA devices is pending an update; see the [legacy platform guides](https://opendatalab.github.io/MinerU/usage/compatibility/) in the meantime.

# Agent Guide

<details>
<summary>Expand for the agent-oriented usage guide</summary>

# MinerU

MinerU is a command-line document reader for agents. It parses local documents into readable conte

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
