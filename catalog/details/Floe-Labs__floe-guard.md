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
