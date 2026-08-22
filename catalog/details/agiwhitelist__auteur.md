# agiwhitelist/auteur

The Claude Code skill that directs a website like a film. Commit-sheet, generated assets, build, and an executable anti-slop linter that gates every ship.

## installation

auteur is an [Agent Skill](https://code.claude.com/docs/en/skills): a `SKILL.md`
plus reference recipes and a few runnable scripts. ~1MB, no dependencies, no
API keys, no build step.

**Any agent — one command.** Detects what you have installed and writes to each
agent's skills folder:

```bash
npx skills add agiwhitelist/auteur
```

<sub>Claude Code · Codex · Cursor · OpenCode · Gemini CLI · Windsurf · Cline ·
Goose · Copilot · Hermes · Kiro · Roo · OpenHands — [75+ agents](https://www.skills.sh/),
project-level or `-g` for global.</sub>

**Claude Code, as a plugin** — installs and updates in place:

```
/plugin marketplace add agiwhitelist/auteur
/plugin install auteur@auteur
```

**OpenClaw:**

```bash
openclaw skills install git:agiwhitelist/auteur --global
```

**Anything else that reads a `SKILL.md`** — clone it into the agent's skills
directory:

```bash
git clone --depth 1 https://github.com/agiwhitelist/auteur ~/.claude/skills/auteur
```

Then just ask:

```
"build me a cinematic landing with auteur"
```

Claude runs the pipeline — commit-sheet → assets → build → gate — and hands you
the site.

## The proof: ten live sites

Don't take the pitch — open them. Each was built by auteur, and each passes the
skill's own linter at **0 fails / 0 warns**. The tenth was not built by Claude:
Kimi K3 was handed `SKILL.md` and a brief, saw none of the other nine, and came
out lit, serif and green in a category whose every reflex is black and gold —
naming in writing, before it built, the four house tells it intended to break.
The skill is the thing that travels, not the model.

<table>
<tr>
<td width="33%" align="center">
  <a href="https://agiwhitelist.github.io/auteur/showcase/flux/"><img src="assets/readme/flux.webp" alt="FLUX — the wordmark drawn in neon outline over a magenta and cyan fluid simulation"></a>
  <br><b>FLUX</b><br><sub>WebGL fluid that tears the wordmark under the cursor</sub>
</td>
<td width="33%" align="center">
  <a href="https://agiwhitelist.github.io/auteur/showcase/swarm/"><img src="assets/readme/swarm.webp" alt="SWARM — the word SWARM glowing orange, formed from a field of particles"></a>
  <br><b>SWARM</b><br><sub>131,072 GPU particles on a curl-noise field</sub>
</td>
<td width="33%" align="center">
  <a href="https://agiwhitelist.github.io/auteur/showcase/static/"><img src="assets/readme/static.webp" alt="STATIC — huge broadcast-style type with chromatic glitch fringing"></a>
  <br><b>STATIC</b><br><sub>Broadcast-glitch type you can shred with a drag</sub>
</td>
</tr>
<tr>
<td align="center">
  <a href="https://agiwhitelist.github.io/auteur/showcase/hale/"><img src="assets/readme/hale.webp" alt="HALE — a brass microscope exploded into labelled parts on a dark stage"></a>
  <br><b>HALE</b><br><sub>A CC0 microscope taken apart on scroll — sourced, not generated</sub>
</td>
<td align="center">
  <a href="https://agiwhitelist.github.io/auteur/showcase/noon/"><img src="assets/readme/noon.webp" alt="TRUE NOON — an analemma curve of the sun's position drawn across a measured grid"></a>
  <br><b>TRUE NOON</b><br><sub>A year of real sun positions, computed live for your latitude</sub>
</td>
<td align="center">
  <a href="https://agiwhitelist.github.io/auteur/showcase/proof/"><img src="assets/readme/proof.webp" alt="PROOF — a bakery production dashboard with deck timers, a late-runs panel and a schedule"></a>
  <br><b>PROOF</b><br><sub>Five screens of a production floor — a product, not a page</sub>
</td>
</tr>
<tr>
<td align="center">
  <a href="https://agiwhitelist.github.io/auteur/showcase/drift/"><img src="assets/readme/drift.webp" alt="DRIFT — flying between pale cyan monoliths in volumetric fog"></a>
  <br><b>DRIFT</b><br><sub>A 3D world of monoliths and volumetric fog you fly through</sub>
</td>
<td align="center">
  <a href="https://agiwhitelist.github.io/auteur/showcase/atlas/"><img src="assets/readme/atlas.webp" alt="ATLAS — sea stacks and breaking surf lit by sunrays through a canyon mouth"></a>
  <br

## requirements

- **Claude Code** (the skill runs inside it).
- **Node 18+** for `slopscan` (zero dependencies).
- **Playwright** for `motionqa` / `shoot` / `refscout` / `moodboard`
  (`npx playwright install chromium`).
- Optional, for asset generation: whichever local media CLIs you have
  (Codex, Gemini/`agy`, Blender). The skill routes to what's present and
  degrades gracefully to hand-authored assets when they aren't.

## Network and permissions

The skill declares a narrow tool surface: `node scripts/*` for its own gates,
`npx playwright *` for the browser passes, and the media CLIs (`agy`, `codex`,
`grok`, `ffmpeg`) only if you have them.

Two phases reach the network, and only those two: **recon** reads live pages
(awwwards, Bing / Pinterest / are.na image search) and **sourcing** fetches
licence-clean assets (Poly Haven, Iconify, Google Fonts, Openverse, Coverr).
No API keys, no logins, no credentials of any kind. Fetched content is treated
as reference material and licence metadata — never executed. Skip phases 0–1
and everything else runs offline.

## Accessibility floor

Every site auteur ships: `prefers-reduced-motion` → a rich still, never blank;
all copy readable with JavaScript off; no full-frame strobe; responsive at
390 / 768 / 1440 with no horizontal overflow. These are enforced, not aspired.

## Credits

The photoreal scroll-scrubbed-video engine (`templates/scroll-flight-engine.js`)
and its technique are adapted from **[scroll-world](https://github.com/cth9191/scroll-world)**
by cyw (MIT) — a sibling Claude Code skill focused on AI-video camera flights.
auteur pairs it with its own asset generation and slopscan / motionqa gates.

## License

MIT © agiwhitelist — see [LICENSE](LICENSE). Vendored components retain their
own MIT notices (see file headers).
