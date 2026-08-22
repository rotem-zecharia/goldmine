# keon/browser-control

A tiny, fast Rust CLI that drives a real browser over the Chrome DevTools Protocol — built for coding agents.

## features

- **Shell-native.** Every capability is a subcommand that prints compact text or JSON. No SDK, no long-running server to babysit, no language lock-in — if your agent can run a shell command, it can drive a browser.
- **Refs built for LLMs.** `snapshot` hands back stable `@e1` / `@e2` handles you act on directly (`click @e3`), instead of brittle, hand-written selectors. CSS selectors and `x,y` coordinates still work when you want them.
- **Raw CDP escape hatch.** Anything the helper surface can't express, `eval` and `cdp` can. You never hit a wall and have to switch tools.
- **Self-observing.** A hidden daemon keeps in-memory event / network / console rings, and every command failure drops a compact trace under `.browser-control/traces/` so an agent can diagnose itself.
- **Provider-agnostic cloud.** Drive a local Chrome or a remote session on Browser Use, Steel, Hyperbrowser, Browserbase — or any CDP provider — with the same commands.
- **Reproducible.** One static Rust binary, built from a pinned toolchain and a committed `Cargo.lock`.

## requirements

- **Rust** — the toolchain pinned in `rust-toolchain.toml` (installed automatically by `rustup toolchain install`).
- **Chrome / Chromium** — any recent build reachable over CDP. `browser-control launch` will start one for you; `doctor` reports what it found.

## installation

```bash
browser-control init                       # create the .browser-control/ workspace
browser-control launch https://example.com # start Chrome + connect
export BROWSER_CONTROL_CDP_URL=http://127.0.0.1:9222

browser-control doctor                      # endpoint, browser, pid, daemon, workspace
browser-control snapshot                    # numbered refs for every actionable element
browser-control click @e1
browser-control eval 'document.title'
browser-control cdp Browser.getVersion
```

Already have a browser listening on CDP? Skip `launch` and point at it:

```bash
export BROWSER_CONTROL_CDP_WS='ws://127.0.0.1:9222/devtools/browser/<id>'
