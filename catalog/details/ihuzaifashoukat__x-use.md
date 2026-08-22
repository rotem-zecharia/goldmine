# ihuzaifashoukat/x-use

Browser-native AI agents for X (Twitter): multi-account, MCP-ready, no X API key required.

## installation

From PyPI (CLI and MCP server):

```bash
pip install x-use-mcp
```

For the full repo setup (presets, example configs, docs), the one-line installer clones the repo, installs x-use into its own virtual environment, and finishes with `x-use doctor` so you can see what is left to configure.

Windows (PowerShell):

```powershell
iex "& { $(irm https://raw.githubusercontent.com/ihuzaifashoukat/x-use/main/install.ps1) }"
```

macOS / Linux / Git Bash:

```bash
curl -fsSL https://raw.githubusercontent.com/ihuzaifashoukat/x-use/main/install.sh | bash
```

Or the manual way:

```bash
git clone https://github.com/ihuzaifashoukat/x-use.git
cd x-use
pip install -e .
```

Requires Python 3.10+ and Chrome. Any of these gives you the `x-use` command.

## tools

33 tools in six groups, full reference with signatures and examples: [docs/MCP_GUIDE.md](docs/MCP_GUIDE.md). Two safety gates: write tools run in draft mode by default (review, then `approve_draft`), and the queue only stores work until an explicit `process_queue` call.

| Group | Tools |
|---|---|
| Read-only & status | `list_accounts`, `get_account`, `get_metrics`, `search_tweets`, `search_profile`, `get_tweet`, `prepare_reply`, `list_queue`, `list_drafts`, `get_draft`, `reject_draft`, `get_run_status`, `get_account_health`, `list_proxies` |
| Write (draft-gated) | `post_tweet`, `generate_and_post`, `reply_to_tweet`, `engage`, `run_cycle`, `approve_draft` |
| Scheduled queue | `queue_post`, `queue_engagement`, `cancel_queued_action`, `process_queue` |
| Composite (server LLM) | `research_and_stage`, `draft_post_variations` |
| Account management | `add_account`, `update_account`, `set_account_active`, `remove_account` |
| Proxy management | `add_proxy`, `remove_proxy`, `test_proxy` |

Interactive use needs no LLM key: your MCP client (Claude, Codex, ...) does the thinking, sees tweet images via `get_tweet`/`prepare_reply`, and passes explicit text to the write tools. The optional server-side LLM (`llm` block) only powers the composite tools, `"auto"` text, and background automation.

Drafts persist in `data/drafts.jsonl`; the queue persists in `data/engagement_queue.jsonl`. Both survive restarts.

## features

| Area | What you get |
|---|---|
| MCP server | 33 tools over stdio on the official MCP Python SDK (`FastMCP`, pinned `mcp>=1.6,<2`): draft-gated writes, a persistent scheduled-action queue with daily caps, account management, and a lazy per-account browser session pool. |
| Draft mode | On by default. Write tools build the full payload (including LLM-generated text), store a draft, and touch nothing until `approve_draft` runs. |
| Multi-account engine | Post (including communities and media), reply, repost/quote, like, keyword search, and relevance-gated engagement. Per-account overrides for keywords, LLM settings, and action behavior. |
| LLM generation | One OpenAI-compatible client (`llm`: api_key, base_url, model) covers OpenAI, OpenRouter, Azure, Gemini, and local servers. Only needed for `"auto"` text and background automation; interactive MCP use runs keyless. Keys resolve from env/`.env` first, then `config/settings.json`. |
| Stealth | undetected-chromedriver, selenium-stealth, randomized user agents, headless support. |
| Proxies | Per-account proxy, named pools, hash or round-robin rotation, `${VAR}` env interpolation in proxy strings. |
| Metrics | Per-account counters in `data/metrics/<account_id>.json` plus JSONL event logs in `logs/accounts/<account_id>.jsonl`. |

## configuration

- `config/accounts.json`: your accounts (gitignored). Start from [`config/accounts.example.json`](config/accounts.example.json) or let `x-use init` write it.
- `config/settings.json`: global defaults for browser, pacing, action caps, LLM, proxies, and the `mcp` section.
- `.env`: LLM API keys; overrides `settings.json` (env wins). See [`.env.example`](.env.example).

Full schema: [docs/CONFIG_REFERENCE.md](docs/CONFIG_REFERENCE.md). Starter templates: [`presets/`](presets/) (offered as wizard choices by `x-use init`).
