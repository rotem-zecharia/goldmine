# Manavarya09/design-extract

Extract any website's complete design system with one command. DTCG tokens, semantic+primitive+composite, MCP server for Claude Code/Cursor/Windsurf, multi-platform emitters (iOS SwiftUI, Android Comp

## installation

```bash
npx designlang https://stripe.com                      # extract everything
npx designlang site stripe.com                         # whole-site: one canonical system + consistency grade ← v12.23
npx designlang fidelity stripe.com --clone localhost:3000  # score a clone vs the original (visual + motion) ← v12.24
npx designlang gallery                                 # static shareable gallery of measured clones      ← v12.24
npx designlang studio                                  # live token editor: edit, preview, export, share ← v12.19
npx designlang verify stripe.com                       # fidelity score: rebuild from tokens vs live ← v12.18
npx designlang pair stripe.com linear.app              # fuse two designs (visuals A × voice B)    ← v12.8
npx designlang brand stripe.com                        # full brand-guidelines book (13 chapters)  ← v12.7
npx designlang theme-swap stripe.com --primary "#ff4800"  # recolour around your brand        ← v12.6
npx designlang pack stripe.com                         # one polished design-system directory ← v12.4
npx designlang remix stripe.com --as cyberpunk         # restyle in another vocabulary       ← v12.3
npx designlang remix stripe.com --all                  # emit all 6 vocabs at once           ← v12.3
npx designlang grade https://stripe.com --badge        # report card + SVG badge             ← v12.2
npx designlang battle stripe.com vercel.com            # head-to-head graded fight           ← v12.2
npx designlang clone https://stripe.com                # working Next.js starter
npx designlang --full https://stripe.com               # screenshots + responsive + interactions
```

Drop a live design-score badge in any README:

```markdown
![Design Score](https://designlang.app/badge/stripe.com.svg)
```

## features

Other tools give you the paint. designlang reads the architecture:

- **Layout system** — grids, flex containers, container widths, gaps — not just tokens.
- **Responsive** — crawls 4 breakpoints and reports what changes (`--responsive`).
- **Interaction states** — programmatically hovers and focuses, captures the deltas (`--interactions`, `--deep-interact`).
- **Motion language** — durations, easing families, spring detection, scroll-linked flag, `feel` fingerprint (springy / smooth / mechanical / mixed).
- **Runtime motion (`--motion-runtime`)** — drives the page (load / scroll / hover / focus) and reads `document.getAnimations()` to capture what *actually* animates: real durations, **choreography/stagger** sequences, and **scroll recipes** (parallax / reveal / pin). Folded into `*-motion-tokens.json` and previewable live in the studio's Motion tab.
- **Component anatomy** — slot trees with variant × size × state matrices, emitted as typed `.tsx`.
- **Brand voice** — tone, pronoun posture, heading style, CTA verb inventory.
- **Page intent + section roles** — `landing` / `pricing` / `docs` etc., with semantic regions (`hero`, `feature-grid`, `pricing-table`, `cta`…).
- **Multi-page consistency** — auto-discovers canonical pages, reconciles shared vs per-route tokens.
- **WCAG** — every fg/bg pair scored, with a remediation palette suggesting nearest passing colors.
- **Drift + lint + visual-diff** — `designlang drift`, `lint`, `visual-diff` all CI-ready, exit non-zero on failure.
- **Live-site sync** — treat the deployed site as source of truth (`designlang sync`).
- **MCP server** — `designlang mcp` exposes tokens, regions, components, and contrast pairs to any MCP-aware agent.

```bash
designlang grade https://stripe.com         # ← v12.1: shareable report card
designlang clone https://stripe.com         # → working Next.js app
designlang apply https://stripe.com -d ./app   # auto-detect framework, write tokens
designlang brands stripe.com vercel.com linear.app   # N-brand matrix
designlang drift https://yourapp.com --tokens ./src/tokens.json
designlang lint ./src/tokens/design-tokens.json     # CI-ready linter
designlang visual-diff https://staging.app https://app   # single-file HTML diff
designlang mcp                              # stdio MCP server for Cursor / Claude Code
designlang doctor                           # sanity-check the local install
```
