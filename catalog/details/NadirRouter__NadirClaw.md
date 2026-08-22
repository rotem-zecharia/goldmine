# NadirRouter/NadirClaw

Open-source LLM router & AI cost optimizer. Routes simple prompts to cheap/local models, complex ones to premium — automatically. Drop-in OpenAI-compatible proxy for Claude Code, Codex, Cursor, OpenCl

## features

Most LLM requests don't need a premium model. In typical coding sessions, **60-70% of prompts are simple** — reading files, short questions, formatting. They can be handled by models that cost 10-20x less.

```
$ nadirclaw serve
✓ Classifier ready — Listening on localhost:8856

SIMPLE  "What is 2+2?"              → gemini-flash    $0.0002
SIMPLE  "Format this JSON"          → haiku-4.5       $0.0004
COMPLEX "Refactor auth module..."   → claude-sonnet    $0.098
COMPLEX "Debug race condition..."   → gpt-5.2          $0.450
SIMPLE  "Write a docstring"         → gemini-flash    $0.0002

3 of 5 routed cheaper · $0.549 vs $1.37 all-premium · 60% saved
```

- **Cut AI API costs 40-70%** — real savings from day one
- **~10ms classification overhead** — you won't notice it
- **Drop-in proxy** — works with any OpenAI-compatible tool
- **Runs locally** — your API keys never leave your machine
- **Fallback chains** — automatic failover when models are down
- **Built-in cost tracking** — dashboard, reports, budget alerts

> **Your keys. Your models. No middleman.** NadirClaw runs locally and routes directly to providers. No third-party proxy, no subsidized tokens, no platform that can pull the plug on you. [Why this matters.](docs/vs-clawrouter.md)

## How NadirClaw works

<p align="center">
  <img src="docs/images/how-it-works.svg" alt="How NadirClaw works — Route, Verify, Escalate" width="100%" />
</p>

Three moves, on every request:

1. **Route** — a ~10ms embedding classifier predicts the *smallest* model likely to answer and sends the prompt there first. Routing modifiers (agentic tool loops, reasoning markers, vision content, long context) can override the score and force a stronger tier.
2. **Verify** — the cheap answer is scored against quality heuristics (refusals, truncation, JSON-format failures) before it ships. Pro swaps the heuristic for a trained DeBERTa cross-encoder.
3. **Escalate** — if the answer falls below the acceptance threshold (τ = 0.80), NadirClaw steps up to the next-best model automatically. You only pay for the big model when the small one wasn't enough.

## Benchmarks — proof, not promises

<p align="center">
  <img src="docs/images/proof.svg" alt="NadirClaw benchmarks — −60% cost, 98.3% quality preserved, 0.961 verifier AUROC, ~10ms overhead" width="100%" />
</p>

NadirClaw and Nadir Pro share the same routing architecture. The numbers
below are from the trained classifier + DeBERTa verifier in Nadir Pro;
the NadirClaw OSS classifier uses a simpler binary centroid that trades
some accuracy for zero training cost. Both run the same cascade rule
engine (`nadirclaw/cascade_rules/`).

### RouterBench (held-out, n=11,420)

The composed system (pre-generation classifier + post-generation
cascade verifier, τ=0.80):

| Metric | Value |
| --- | ---: |
| AUROC | **0.961** |
| Expected Calibration Error (ECE) | **0.016** |
| Quality preserved vs always-Opus | **98.3%** |
| Catastrophic-downgrade rate | 1.7% |
| Composed cost vs always-Opus | -60% |

Full τ-sweep and per-domain breakdown is in [`MODEL_CARD.md`](MODEL_CARD.md).

### RouterArena (sub_10, n=809, public leaderboard)

| Metric | Value |
| --- | ---: |
| Composite score | **0.7118** |
| Projected leaderboard rank | **#5** |
| Routers below (selected) | NotDiamond-0001, Auto Router, Martian |

RouterArena submission PR (live):
[RouteWorks/RouterArena#112](https://github.com/RouteWorks/RouterArena/pull/112).

### Contamination audit

Zero overlap between Nadir's training corpus and either held-out set:

| Held-out set | Audit run | Overlap |
| --- | --- | --- |
| RouterBench `0shot` | 2026-05-24 | 0 of 36,481 |
| RouterArena `sub_10` | 2026-05-27 | 0 of 809 |
| RouterArena `full` | 2026-05-27 | 0 of 8,399 |

The audit is reproducible from this repo:
[`verifier/contamination_audit.py`](verifier/contamination_audit.py).
Hash recipe: `sha256(NFC(prompt).strip().casefold().utf8)`.

## installation

```bash
pip install nadirclaw
```

Or install from source:

```bash
curl -fsSL https://raw.githubusercontent.com/doramirdor/NadirClaw/main/install.sh | sh
```

Then run the interactive setup wizard:

```bash
nadirclaw setup
```

This guides you through selecting providers, entering API keys, and choosing models for each routing tier. Then start the router:

```bash
nadirclaw serve --verbose
```

That's it. NadirClaw starts on `http://localhost:8856` with sensible defaults (Gemini 3 Flash for simple, OpenAI Codex for complex). If you skip `nadirclaw setup`, the `serve` command will offer to run it on first launch.

## NadirClaw vs Nadir Pro

NadirClaw is the free, open-source core. If you are routing production traffic or running a team, [**Nadir Pro**](https://getnadir.com) is the hosted version with more accurate routing, team features, and analytics. Same routing philosophy, zero vendor lock-in (Pro lets you BYOK and you can always fall back to NadirClaw self-hosted).

|  | NadirClaw (Free, OSS) | [Nadir Pro](https://getnadir.com) (Hosted) |
|---|---|---|
| **License** | PolyForm Noncommercial 1.0.0 (free for noncommercial use; commercial license via [getnadir.com](https://getnadir.com)) | Proprietary |
| **Deploy** | Self-hosted, localhost | `api.getnadir.com` or self-host via Docker |
| **Pre-generation classifier** | Binary centroid (~10ms), opt-in DistilBERT, or **bundled** `wide_deep_asym_v3` trained checkpoint (~40ms CPU; see [`MODEL_CARD.md`](MODEL_CARD.md)) | Same trained classifier + closed-loop retraining, provider-health-aware ranking |
| **Post-generation verifier** | Rule-based heuristic (refusal / length / JSON checks, ~1ms) | Trained DeBERTa-v3-small cross-encoder, AUROC 0.96 on RouterBench held-out |
| **Verifier-gated cascade** | Yes (heuristic verifier) | Yes (trained verifier) |
| **Storage** | Local JSONL + SQLite | Postgres (Supabase), multi-tenant |
| **Dashboard** | Terminal + local web | Hosted web dashboard, per-team analytics |
| **Cost tracking** | `nadirclaw savings` CLI | Live dashboard, monthly invoices, projected savings |
| **Extras** | Context optimize, fallback chains | Everything in Free, plus semantic cache, response healing, prompt caching passthrough |
| **Team** | None | SSO, audit logs, API key management, priority support |
| **Billing** | N/A | Pay only on savings: 25% of first $2K, 10% above, plus $9/mo base |
| **Best for** | Solo devs, self-hosters, anyone who wants the router running locally | Teams routing real traffic who want a hosted dashboard and want someone else to maintain the classifier |

**Start free at [getnadir.com](https://getnadir.com/auth?mode=signup)** (15 requests/day on our keys, unlimited with BYOK). If Nadir is not saving you money, you do not pay us.

## requirements

- **Python 3.10+**
- **git**
- **At least one LLM provider:**
  - [Google Gemini API key](https://aistudio.google.com/apikey) (free tier: 20 req/day)
  - [Ollama](https://ollama.com) running locally (free, no API key needed)
  - [Anthropic API key](https://console.anthropic.com/) for Claude models
  - [OpenAI API key](https://platform.openai.com/) for GPT models
  - Provider subscriptions via OAuth (`nadirclaw auth openai login`, `nadirclaw auth anthropic login`, `nadirclaw auth antigravity login`, `nadirclaw auth gemini login`)
  - Or any provider supported by [LiteLLM](https://docs.litellm.ai/docs/providers)

## configuration

### Environment File

NadirClaw loads configuration from `~/.nadirclaw/.env`. Create or edit this file to set API keys and model preferences:

```bash
# ~/.nadirclaw/.env

## tools

GEMINI_API_KEY=AIza...
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# Model routing
NADIRCLAW_SIMPLE_MODEL=gemini-3-flash-preview
NADIRCLAW_COMPLEX_MODEL=gemini-2.5-pro

# Server
NADIRCLAW_PORT=8856
```

If `~/.nadirclaw/.env` does not exist, NadirClaw falls back to `.env` in the current directory.

### Authentication

NadirClaw supports multiple ways to provide LLM credentials, checked in this order:

1. **OpenClaw stored token** (`~/.openclaw/agents/main/agent/auth-profiles.json`)
2. **NadirClaw stored credential** (`~/.nadirclaw/credentials.json`)
3. **Environment variable** (`GEMINI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, etc.)

#### Using `nadirclaw auth` (recommended)

```bash
# Add a Gemini API key
nadirclaw auth add --provider google --key AIza...

# Add any provider API key
nadirclaw auth add --provider anthropic --key sk-ant-...
nadirclaw auth add --provider openai --key sk-...

# Login with your OpenAI/ChatGPT subscription (OAuth, no API key needed)
nadirclaw auth openai login

# Login with your Anthropic/Claude subscription (OAuth, no API key needed)
nadirclaw auth anthropic login

# Login with Google Gemini (OAuth, opens browser)
nadirclaw auth gemini login

# Login with Google Antigravity (OAuth, opens browser)
nadirclaw auth antigravity login
