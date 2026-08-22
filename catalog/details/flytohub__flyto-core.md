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

## features

- **Execution Trace** — structured record of every step: input, output, timing, status
- **Replay** — re-execute from any step with the original (or modified) context
- **Breakpoints** — pause execution at any step, inspect state, resume
- **Evidence Snapshots** — full state before and after each step boundary
- **Data Lineage** — track data flow across steps, build dependency graphs
- **Timeout Guard** — configurable workflow-level and per-step timeout protection

## configuration

Core is configured through package extras, CLI arguments, workflow parameters,
module policy, environment variables, and local run state. Security-sensitive
network, filesystem, auth, callback, and permission switches are documented in
[Configuration](docs/CONFIGURATION.md); all 107 detected environment readers are
linked to source in the generated
[configuration reference](docs/reference/configuration.md).

---
