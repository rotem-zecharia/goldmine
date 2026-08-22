# NVIDIA/SkillSpector

Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, security risks, prompt injection, data exfiltration, and supply-chain risks in Claude Code, Codex, and MCP skills befo

## features

AI agent skills (used by Claude Code, Codex CLI, Gemini CLI, etc.) execute with implicit trust and minimal vetting. Research shows that **26.1% of skills contain vulnerabilities** and **5.2% show likely malicious intent**.

SkillSpector helps you answer: **"Is this skill safe to install?"**

SkillSpector is part of the [NVIDIA Verified Skills pipeline](https://docs.nvidia.com/skills/), which scans, evaluates, and signs agent skills before publication. Skills that pass are published to the [NVIDIA skills catalog](https://github.com/NVIDIA/skills).

## Documentation

- **[Scan agent skills before installation](https://docs.nvidia.com/skills/scanning-agent-skills)** — Hosted guide: when to scan, how to read a report, and how to gate installs.
- **[Development guide](docs/DEVELOPMENT.md)** — Architecture, package layout, and how to extend the analyzer pipeline.
- **[Analysis resource bounds](docs/ANALYSIS_RESOURCE_BOUNDS.md)** — Fail-closed bundle, parser, nested-artifact, ledger, and finding ceilings.
- **[Pi extension](docs/PI_EXTENSION.md)** — Install SkillSpector as a Pi tool for scanning skills from inside agent sessions.

## Features

- **Multi-format input**: Scan Git repos, URLs, zip files, directories, or single files
- **70 vulnerability patterns** across 17 categories: prompt injection, data exfiltration, privilege escalation, supply chain, excessive agency, output handling, system prompt leakage, memory poisoning, tool misuse, rogue agent, anti-refusal, trigger abuse, dangerous code (AST), taint tracking, YARA signatures, MCP least privilege, and MCP tool poisoning
- **Two-stage analysis**: Fast static analysis + optional LLM semantic evaluation
- **Live vulnerability lookups**: SC4 queries [OSV.dev](https://osv.dev) for real-time CVE data with automatic offline fallback
- **Multiple output formats**: Terminal, JSON, Markdown, and SARIF reports
- **Risk scoring**: 0-100 score with severity labels and clear recommendations
- **Baseline / false-positive suppression**: Accept known findings via a glob-rule or fingerprint baseline so re-scans surface only *new* issues ([docs](docs/SUPPRESSION.md))

## installation

### Installation

> **Open-source software notice:** This project will download and install additional third-party open source software projects. Review the license terms of these open source projects before use.

Create and activate a virtual environment first (all `make` targets assume the venv is active). Use **uv** or **pip**; the Makefile uses `uv` if available, otherwise `pip`.

**Quick install with uv (CLI-only):**

```bash
uv tool install git+https://github.com/NVIDIA/skillspector.git
# Update later: uv tool update skillspector
```

If you plan to run `skillspector mcp`, install the MCP extra at install time:

```bash
uv tool install 'skillspector[mcp] @ git+https://github.com/NVIDIA/skillspector.git'
```

**From source:**

```bash
# Clone the repository
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

## configuration

uv venv .venv && source .venv/bin/activate
# or: python3 -m venv .venv && source .venv/bin/activate

## tools

```bash
# Scan a local skill directory
skillspector scan ./my-skill/

# Scan a single SKILL.md file
skillspector scan ./SKILL.md

# Scan a Git repository
skillspector scan https://github.com/user/my-skill

# Scan a zip file
skillspector scan ./my-skill.zip
```

#### Size limits

SkillSpector enforces two independent caps on remote and archive inputs to bound the impact of oversized downloads and zip bombs:

- **Per-ingest cap**: `INGEST_MAX_BYTES` (100 MiB) — applied to streamed URL downloads, total uncompressed size of zip archives, and post-clone disk usage of Git repos.
- **Zip member cap**: `INGEST_MAX_ZIP_MEMBERS` (10,000) — caps the number of entries in a single zip.

Note that the per-file 1 MB analysis cap (`MAX_FILE_BYTES`) is a separate, downstream limit: it bounds what individual analyzers will read out of an already-ingested directory. The ingest caps above bound how much content can land on disk in the first place. A breach of either ingest cap fails closed with an `IngestLimitExceededError`.

### Output Formats

```bash
# Terminal output (default) - pretty formatted
skillspector scan ./my-skill/

# JSON output - machine readable
skillspector scan ./my-skill/ --format json --output report.json

# Markdown output - for documentation
skillspector scan ./my-skill/ --format markdown --output report.md

# SARIF output - for CI/CD integration and IDE tooling
skillspector scan ./my-skill/ --format sarif --output report.sarif
```

### Batch Scanning

Scan entire directories of skills in parallel from `contrib/batch_scan/`:

```bash
python -m contrib.batch_scan.batch_scan ./my-skills/ --no-llm
python -m contrib.batch_scan.batch_scan ./my-skills/ --workers 20 -f json -o report.json
python -m contrib.batch_scan.batch_scan ./tests/fixtures/ -f terminal --workers 20
```

Supports multilingual detection (zh/ja/ko) and terminal/JSON/Markdown output.

For LLM scans with higher concurrency, configure multiple API keys following
[`.env.example`](contrib/batch_scan/.env.example) — the pool improves throughput
and resilience, provided the keys don't share an account-level rate limit.

See the [contrib guide](contrib/batch_scan/docs/) for details.

> **Note on LLM support:** The default configuration targets DeepSeek as the
> cheapest public option. DeepSeek-Chat is
> [expected to sunset](https://api-docs.deepseek.com/), and the contributor
> does not have hardware to test against local models. The batch scanner was
> originally tested with OpenAI-compatible endpoints — DeepSeek's lack of
> structured-output support required manual JSON-parsing patches. If you can
> contribute a more universal backend (Ollama, vLLM, or a different provider),
> PRs are very welcome.

### Suppressing False Positives (baseline)

Suppress known/accepted findings so the risk score reflects only un-triaged
issues and re-scans surface only *new* findings. See the
[suppression guide](docs/SUPPRESSION.md) for the full reference.

```bash
# Accept all current findings into a baseline (run once), then commit it.
skillspector baseline ./my-skill/ -o .skillspector-baseline.yaml

# Scan against the baseline — only NEW findings are reported and scored.
skillspector scan ./my-skill/ --baseline .skillspector-baseline.yaml

# Review what was suppressed (still excluded from the score).
skillspector scan ./my-skill/ --baseline .skillspector-baseline.yaml --show-suppressed
```

A baseline can also use drift-tolerant glob rules (by rule id, file path, or
message) — see [`.skillspector-baseline.example.yaml`](.skillspector-baseline.example.yaml).
Exact fingerprint baselines are evidence-bound: changing the scanned source or
SkillSpector version keeps the finding active until it is reviewed again.
When a selected baseline or baseline output is stored inside the skill
directory, SkillSpector excludes that exact file from content analysis so its
suppression text cannot create findings or enter regenerated fingerprints;
sibling files remain in normal scan scope.

### LLM Analys

## limitations

- **Non-English content**: May miss patterns in other languages
- **Image-based attacks**: Cannot analyze text in images
- **Encrypted/binary code**: Cannot analyze compiled or encrypted content
- **Runtime behavior**: Static analysis only, no dynamic execution
- **Offline SC4**: Without network access to `api.osv.dev`, SC4 uses a small static fallback list

## Research Background

Based on research from "Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale" (Liu et al., 2026):

- **Dataset**: 42,447 skills from major marketplaces
- **Vulnerable**: 26.1% contain at least one vulnerability
- **High-severity**: 5.2% show likely malicious intent
- **Key finding**: Skills with executable scripts are 2.12x more likely to be vulnerable
