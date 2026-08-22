# flytohub/flyto-core

AI said it finished. Flyto2 shows the proof.

## tools

flyto recipe scrape-to-csv --url https://news.ycombinator.com --selector ".titleline a"
```

Every recipe is traced. Every run is replayable. [See all 41 recipes ->](docs/RECIPES.md)

---

## installation

```bash
pip install flyto-core            # Core engine + CLI + MCP server
pip install flyto-core[browser]   # + browser automation (Playwright)
playwright install chromium        # one-time browser setup
```

---

## The 85-line problem

Here's what competitive pricing analysis looks like in Python:

<table>
<tr>
<td width="50%">

**Python** — 85 lines

```python
import asyncio, json, time
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://competitor.com/pricing")

        # Extract pricing
        prices = await page.evaluate("""() => {
            const cards = document.querySelectorAll(
              '[class*="price"]'
            );
            return Array.from(cards).map(
              c => c.textContent.trim()
            );
        }""")

        # Desktop screenshot
        await page.screenshot(
            path="desktop.png", full_page=True
        )

        # Mobile
        await page.set_viewport_size(
            {"width": 390, "height": 844}
        )
        await page.screenshot(
            path="mobile.png", full_page=True
        )

        # Performance
        perf = await page.evaluate("""() => {
            const nav = performance
              .getEntriesByType('navigation')[0];
            return {
              ttfb: nav.responseStart,
              loaded: nav.loadEventEnd
            };
        }""")

        # Save report
        report = {
            "prices": prices,
            "performance": perf,
        }
        with open("report.json", "w") as f:
            json.dump(report, f, indent=2)

        await browser.close()

asyncio.run(main())
```

</td>
<td width="50%">

**flyto-core** — 12 steps

```yaml
name: Competitor Intel
steps:
  - id: launch
    module: browser.launch
  - id: navigate
    module: browser.goto
    params: { url: "{{url}}" }
  - id: prices
    module: browser.evaluate
    params:
      script: |
        JSON.stringify([
          ...document.querySelectorAll(
            '[class*="price"]'
          )
        ].map(e => e.textContent.trim()))
  - id: desktop_shot
    module: browser.screenshot
    params: { path: desktop.png, full_page: true }
  - id: mobile
    module: browser.viewport
    params: { width: 390, height: 844 }
  - id: mobile_shot
    module: browser.screenshot
    params: { path: mobile.png, full_page: true }
  - id: perf
    module: browser.performance
  - id: save
    module: file.write
    params:
      path: report.json
      content: "${prices.result}"
  - id: close
    module: browser.close
```

</td>
</tr>
<tr>
<td>

No trace. No replay. No timing. If step 5 fails, re-run everything.

</td>
<td>

Full trace. Replay from any step. Per-step timing. Every run is debuggable.

</td>
</tr>
</table>

---

## Current Platform Snapshot

- **Open-source AI agent framework boundary**: MCP-compatible clients call reviewed flyto-core modules through schemas, not arbitrary generated production code.
- **AI workflow automation substrate** for browser automation, API workflows, data/file operations, AI calls, notifications, verification, trace, evidence, and replay.
- **468 registry-backed modules** across **85 catalog categories**. `docs/TOOL_CATALOG.md` is generated from `ModuleRegistry`, not hand-counted.
- **41 built-in recipes** for audit, browser automation, data/image work, DevOps, integrations, and deterministic verification.
- **Deterministic verification modules** (`verification.*` with `warroom.*` compatibility aliases) support site graph discovery, replay scenario generation, run evidence, and report packs.
- **Hardened outbound and file access** in the 2.26.x line: guarded HTTP clients prevent SSRF bypasses, and file/data writes are confined through the sandbox path guard.
- **Replayable browser and workflow execution** remains the core contract: every step can produce trace 

## features

- **Execution Trace** — structured record of every step: input, output, timing, status
- **Replay** — re-execute from any step with the original (or modified) context
- **Breakpoints** — pause execution at any step, inspect state, resume
- **Evidence Snapshots** — full state before and after each step boundary
- **Data Lineage** — track data flow across steps, build dependency graphs
- **Timeout Guard** — configurable workflow-level and per-step timeout protection

## Architecture

CLI, MCP, HTTP, Python, and packaged recipes converge on the same workflow
engine, module registry, policy, trace, evidence, and replay boundaries. Start
with the [Technical Whitepaper](docs/WHITEPAPER.md), then use the
[Architecture Map](docs/architecture-map.md) and exhaustive
[source reference](docs/reference/README.md) for implementation detail.

## configuration

Core is configured through package extras, CLI arguments, workflow parameters,
module policy, environment variables, and local run state. Security-sensitive
network, filesystem, auth, callback, and permission switches are documented in
[Configuration](docs/CONFIGURATION.md); all 107 detected environment readers are
linked to source in the generated
[configuration reference](docs/reference/configuration.md).

---

## Extensions

Core manages two — and only two — kinds of installable extension:

| Kind | Name prefix | Entry-point group |
|---|---|---|
| Module packs | `flyto-modules-` | `flyto.modules` |
| Plugins | `flyto-plugin-` | `flyto.plugins` |

Admission is by prefix and entry-point group alone, so a new pack such as
`flyto-modules-robotics` works the day it is published — no Core source names
any extension, and none has to change for one.

```bash
export FLYTO_EXTENSIONS_INSTALL_ENABLED=1   # operator opt-in, off by default

curl -H "Authorization: Bearer $TOKEN" localhost:8333/v1/extensions
curl -X POST -H "Authorization: Bearer $TOKEN" \
     -H 'Content-Type: application/json' \
     -d '{"name": "flyto-modules-robotics"}' \
     localhost:8333/v1/extensions/install
```

An install is only reported successful once the installed distribution is
*proved* to declare an entry point in its kind's group; a first install that
fails that proof is rolled back, an upgrade that fails it is left in place so
the operator is not left with nothing. Upgrades and uninstalls report
`restart_required`, because Python cannot un-import code already loaded.
Failures return a stable error code and never package-manager output. See
[API](docs/API.md#extension-management).

---
