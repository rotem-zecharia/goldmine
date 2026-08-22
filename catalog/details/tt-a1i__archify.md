# tt-a1i/archify

Agent skill for beautiful, verifiable architecture, workflow, sequence, data-flow, and lifecycle diagrams—self-contained HTML with motion and crisp export.

## installation

```bash
npx skills add tt-a1i/archify -g
```

For an explicit, non-interactive Cursor install:

```bash
npx -y skills add tt-a1i/archify --skill archify --agent cursor --global --copy --yes
```

To try without installing:

```bash
npx skills use tt-a1i/archify@archify --agent codex
```

[DSH community opt-in](integrations/deepseek-harness/README.md): `dsh plugin --profile web add @tt-a1i/archify-dsh@0.1.0`

The [agent switcher](https://tt-a1i.github.io/archify/start.html?agent=cursor&type=architecture) covers `cursor`, `codex`, `claude-code`, and `opencode`. For Raven's manual ZIP install, extract [`archify.zip`](archify.zip) into `~/.raven/workspace/skills`; it yields `~/.raven/workspace/skills/archify`. Raven is not a switcher target.

## features

- **Layout judgment over generic auto-layout** — the agent chooses hierarchy, spacing, routes, and emphasis; shared automatic endpoints spread deterministically instead of piling arrows on one midpoint.
- **Typed JSON IR** — every renderer-backed mode has a schema and reproducible source.
- **Atomic validation before delivery** — schema, layout, HTML/SVG, route, and label-to-route clearance checks must all pass before a showcase artifact replaces the last known good output.
- **Failures come with a repair receipt** — `validate --json` and `deliver --json` return stable rule codes, the exact subject, measured evidence, and only supported repair controls instead of a Node stack or an unstructured retry guess.
- **Last-good live preview** — an optional desktop loop watches one JSON file, refreshes only after the latest candidate passes every gate, and keeps the previous verified diagram visible when a save is incomplete or invalid.
- **Truthful interaction** — focus, upstream/downstream reach, exact routes, role comparison, and stories reuse authored nodes and relationships instead of inventing topology or claiming runtime impact.
- **Source evidence, only when requested** — Evidence-backed Architecture nodes mark themselves `SRC n` and open Git-verified files and line ranges pinned to one public commit; ordinary artifacts stay source-free.
- **Portable by default** — the result is one HTML file; exports remain full-diagram and free of temporary viewer state.

Archify is not a general-purpose drawing editor or a Mermaid theme. It turns technical intent into a communication artifact.
