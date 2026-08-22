# Floe-Labs/floe-guard

The spend meter and budget gate for AI voice agents. Meters STT + TTS + LLM + telephony per call, out of the box (Pipecat, LiveKit — Python & TypeScript). Hard-stops the next turn before it crosses yo

## tools

Straight from the install — no repository checkout needed:

```bash
pip install floe-guard
floe-guard demo
```

This rigs a loop against a **stub LLM** — no real API key, no account, no network.
It prices each fake `gpt-4o` call offline and the guard halts the loop after a few
iterations, before it can cross the $0.10 ceiling. This is the reproducible "stop
the loop" demo. Cloned the repo? The same demo is
[`examples/runaway_loop.py`](examples/runaway_loop.py) (a thin wrapper around
`floe_guard.demo.run_demo`).

## What did that call cost?

The other demo — one voice call, every leg priced from the bundled map, no
manual rates, no API key, no network:

```bash
pip install "floe-guard[livekit]"     # the demo imports livekit-agents
python examples/voice_call_cost_livekit.py
```

```text
Per-leg call cost (all priced from the bundled cost map, no manual rates):
  livekit-stt          $0.001027   # 8s  × ($0.0077/min ÷ 60)   Deepgram Nova-3
  gpt-4o               $0.003700   # 600 in / 220 out tokens    LLM
  livekit-tts          $0.009000   # 180 chars / 1k × $0.05     ElevenLabs Flash
  livekit-telephony    $0.012750   # 1.5 min × $0.0085/min      Twilio US inbound
  TOTAL                $0.026477
```

That's the answer a token-level tool can't give: it meters the LLM leg and
misses the rest of the bill. Rates are a snapshot of public US list prices and
drift — details, caveats, and the Pipecat version in
[Voice adapters](#voice-adapters-stt--llm--tts).

## features

You can already *see* what your agent spends — the problem is seeing it too late.
floe-guard is the part that **stops the call**, not the part that reports the damage.

- **`max_tokens` / `max_rpm`** cap size and rate, not **dollars** — a cheap model
  stuck in a loop still drains the budget.
- **Usage logs and provider dashboards** tell you what you spent *after* it's gone.
  floe-guard refuses the call *before* it crosses your ceiling.
- **A cost callback that just logs** is notified after the fact and can't halt the
  run — enforcement has to stand in front of the next call. That's where it lives.
- **A hand-rolled `spent += cost` counter races under parallel agents** (CrewAI
  fan-out, `asyncio`, `Promise.all`): N calls read the same under-limit total and
  all fire. floe-guard reserves atomically (`reserve()`/`settle()`), so the ceiling
  holds under concurrency.

The whole job: a hard stop **before** the next call, that **holds under fan-out** —
no account, no network, no crypto.

## How it works

The guard sits **in the call path**, not on an event bus. A passive listener is
told about spend *after the fact* and can't halt anything — so enforcement has to
be the thing standing in front of the next call:

- **`check()`** runs before each LLM call. It predicts the next call's cost from
  the last one and raises `BudgetExceeded` if that would cross your ceiling — the
  call never runs. (A running-total check also catches an overshoot if an estimate
  came in low.)
- **`record(model, prompt_tokens, completion_tokens)`** runs after each response.
  It prices the tokens **offline** from a bundled
  [LiteLLM cost map](src/floe_guard/cost_map.json) and adds the USD to a running
  total.

### Persist one UTC-day budget across processes (Python)

Cron and serverless jobs can share one ceiling only when every process opens the
same database file on storage with reliable SQLite file locking. Isolated
serverless instances with separate local files do not coordinate; use hosted
enforcement when no shared file is available:

```python
from floe_guard import BudgetGuard, SqliteStore

guard = BudgetGuard(
    limit_usd=5.00,
    window="utc-day",
    store=SqliteStore("agent-budget.sqlite3"),
)
reservation = guard.reserve_tool(0.02)  # atomic across sharing processes
guard.settle_tool("search", 0.02, reserved=reservation)
```

One database file represents one logical budget. Settled spend and in-flight
reservations persist until a new UTC date selects a fresh window; per-call logs,
tool attribution, and next-call estimates remain process-local. A process that
dies with a reservation leaves a fail-closed hold that must be recovered
manually. This feature is Python-only and supports `window="utc-day"` only;
arbitrary rolling durations are not yet supported. As elsewhere, enforcement is
estimate-based, so size reservations to the real request when possible.

### Unpriceable models fail closed

If a model isn't in the cost map and you didn't supply a price, the guard **warns
loudly and refuses** (`UnpriceableModelError`) rather than silently treat it as
free — *you can't cap spend you can't measure.* Give it a price to enforce it:

```python
from floe_guard import BudgetGuard, ManualPrice

guard = BudgetGuard(
    limit_usd=5.00,
    price_overrides={"my-self-hosted-model": ManualPrice(1e-6, 2e-6)},  # USD/token
)
# or, set fail_closed=False to warn-and-skip for models you accept un-metered.
```

### What the bundled map prices

The bundled prices are a **dated snapshot** of public list rates — vendors change
them, so treat freshness as a signal, not a guarantee. The snapshot date is
exposed: `floe_guard.cost_map_generated_at()` (Python) / `costMapGeneratedAt()`
(TypeScript) returns the `YYYY-MM-DD` it was last generated/verified, so you can
display it or gate on it.

The vendored map deliberately covers **OpenAI, Anthropic, Google Gemini (AI
Studio), and a curated set of Groq models** (the rules live in
[`scripts/update-cost-map.mjs`](scri
