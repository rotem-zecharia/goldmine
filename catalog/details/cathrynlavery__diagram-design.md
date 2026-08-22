# cathrynlavery/diagram-design

38 editorial diagram types for Claude Code, Codex, and Pi. Self-contained HTML + SVG. No shadows. No Mermaid slop.

## features

I write at [littlemight.com](https://littlemight.com?utm_source=diagram-design&utm_medium=readme&utm_campaign=github&utm_content=intro) (and run [BestSelf.co](https://bestself.co?utm_source=diagram-design&utm_medium=readme&utm_campaign=github&utm_content=intro) on the side). Every time I needed a diagram — an architecture sketch, a flowchart, a pyramid of what matters most — I'd ask Claude and get back a generic rounded-box thing that looked nothing like the rest of the site. I'd either fight with Figma for 30 minutes or just skip the diagram.

So I built a Claude Code skill for it. Thirty-nine visual types, editorial quality, matches your brand in 60 seconds by reading your website.

> *The highest-quality move is usually deletion.* Every node earns its place. The accent color is reserved for the 1–2 things the reader should look at first. Target density: 4/10.

---

## What it makes

All 39 visual types ship in three static variants: minimal light, minimal dark, and full-editorial. Open any of them directly in a browser. There is no build step, JavaScript, or external image dependency.

<table>
<tr>
  <td align="center" width="33%"><img src="docs/screenshots/architecture.png" alt="Architecture"><br><b>Architecture</b><br><sub>Components + connections</sub></td>
  <td align="center" width="33%"><img src="docs/screenshots/it-state.png" alt="IT current-state"><br><b>IT current-state</b><br><sub>Legacy landscape + modernization</sub></td>
  <td align="center" width="33%"><img src="docs/screenshots/flowchart.png" alt="Flowchart"><br><b>Flowchart</b><br><sub>Decision logic</sub></td>
</tr>
<tr>
  <td align="center"><img src="docs/screenshots/sequence.png" alt="Sequence"><br><b>Sequence</b><br><sub>Messages over time</sub></td>
  <td align="center"><img src="docs/screenshots/state.png" alt="State machine"><br><b>State machine</b><br><sub>States + transitions</sub></td>
  <td align="center"><img src="docs/screenshots/er.png" alt="ER"><br><b>ER / data model</b><br><sub>Entities + fields</sub></td>
</tr>
<tr>
  <td align="center"><img src="docs/screenshots/timeline.png" alt="Timeline"><br><b>Timeline</b><br><sub>Events on an axis</sub></td>
  <td align="center"><img src="docs/screenshots/swimlane.png" alt="Swimlane"><br><b>Swimlane</b><br><sub>Cross-functional flow</sub></td>
  <td align="center"><img src="docs/screenshots/quadrant.png" alt="Quadrant"><br><b>Quadrant</b><br><sub>Two-axis positioning</sub></td>
</tr>
<tr>
  <td align="center"><img src="docs/screenshots/radar.png" alt="Radar chart"><br><b>Radar / spider</b><br><sub>Multi-axis comparison</sub></td>
  <td align="center"><img src="docs/screenshots/loop.png" alt="Loop"><br><b>Loop / flywheel</b><br><sub>Reinforcing cycle + shared hub</sub></td>
  <td align="center"><img src="docs/screenshots/nested.png" alt="Nested"><br><b>Nested</b><br><sub>Hierarchy by containment</sub></td>
</tr>
<tr>
  <td align="center"><img src="docs/screenshots/tree.png" alt="Tree"><br><b>Tree</b><br><sub>Parent → children</sub></td>
  <td align="center"><img src="docs/screenshots/org-chart.png" alt="Org chart"><br><b>Org chart</b><br><sub>Ownership + routing</sub></td>
  <td align="center"><img src="docs/screenshots/layers.png" alt="Layer stack"><br><b>Layer stack</b><br><sub>Stacked abstractions</sub></td>
</tr>
<tr>
  <td align="center"><img src="docs/screenshots/venn.png" alt="Venn"><br><b>Venn</b><br><sub>Set overlap</sub></td>
  <td align="center"><img src="docs/screenshots/pyramid.png" alt="Pyramid"><br><b>Pyramid / funnel</b><br><sub>Ranked hierarchy or drop-off</sub></td>
  <td align="center"><img src="docs/screenshots/bar.png" alt="Bar chart"><br><b>Bar chart</b><br><sub>Categorical comparison</sub></td>
</tr>
<tr>
  <td align="center"><img src="docs/screenshots/treemap.png" alt="Treemap"><br><b>Treemap</b><br><sub>Part-of-whole by area</sub></td>
  <td align="center"><img src="docs/screenshots/line.png" alt="Line chart"><br><b>Line chart</b><br><sub>Trends over time</sub></td>
  <td align=

## installation

**Claude Code:**

```text
/plugin marketplace add cathrynlavery/diagram-design
/plugin install diagram-design@diagram-design
```

Then enable updates once: run `/plugin`, open **Marketplaces**, select **diagram-design**, and choose **Enable auto-update**. Claude Code disables auto-update by default for third-party marketplaces; after this toggle, it refreshes the marketplace and installed plugin in the background after startup. Run `/reload-plugins` when prompted, or let the next session load the update.

**Codex:**

```bash
codex plugin marketplace add cathrynlavery/diagram-design
codex plugin add diagram-design@diagram-design
```

Codex refreshes configured Git marketplaces at startup. To fetch immediately, run `codex plugin marketplace upgrade diagram-design` and start a new session.

**Factory Droid:**

```bash
droid plugin marketplace add https://github.com/cathrynlavery/diagram-design
droid plugin install diagram-design@diagram-design --scope user
```

Droid tracks Git plugins by commit rather than the manifest's display version. To fetch a merged update, run `droid plugin marketplace update diagram-design`, then `droid plugin update diagram-design@diagram-design --scope user`, and start a new session.

**Claude Cowork (organization marketplace):** Organization GitHub marketplaces currently require a private or internal repository, so first mirror this public repository into one owned by your organization. In **Organization settings → Plugins**, choose **Add plugin → GitHub**, connect that mirror, and enable **Sync automatically** from the marketplace menu. Automatic sync runs when a pull request containing a plugin version bump is merged to the mirror's default branch; direct pushes do not trigger the webhook. Install Diagram Design from the resulting organization marketplace.

**Pi:**

```bash
pi install https://github.com/cathrynlavery/diagram-design
```

Run `/reload` in an open Pi session. Pi makes the skill available for matching diagram requests; use `/skill:diagram-design` to invoke it explicitly. Pi also loads the `/export-diagram`, `/import-mermaid`, `/profile`, and `/doctor` prompt templates. The unpinned Git install is intentional: Pi has no automatic package refresh, so run `pi update --extensions` to pull merged updates.

> **One-time migration:** an existing standalone `npx skills add` copy will not start following the Codex marketplace automatically. Remove that standalone copy, then use the Codex marketplace commands above. Likewise, uninstall a personal Cowork copy and reinstall Diagram Design from your organization's marketplace. Future marketplace version bumps then flow through each client's native update path.

### Editable install

Managed installs are convenient, but changes to `references/style-guide.md` may be replaced by package updates. Saved profiles in `~/.diagram-design/profiles/` survive updates, and projects with a `.diagram-design` marker are unaffected. Clone the repo and install the local path if you plan to customize the working style guide directly:

```bash
git clone git@github.com:cathrynlavery/diagram-design.git ~/code/diagram-design

# Pi: register the checkout as a local package
pi install ~/code/diagram-design

# Claude Code: symlink the inner skill
ln -s ~/code/diagram-design/skills/diagram-design ~/.claude/skills/diagram-design
```

The shared skill lives at `skills/diagram-design/`. Pi discovers it through the repo's standard `skills/` package directory; Claude Code, Codex, Factory Droid, and other Agent Skills-compatible tools use the same files.

---

## Onboarding — make it look like *your* brand

The whole point: ship editorial-quality diagrams in **your** colors and typography, not a generic template.

Out of the box, diagrams render in a clean **jet-black + atomic-tangerine** palette (white-smoke paper, jet-black ink, atomic-tangerine accent, blue-slate muted, silver hairlines). Good enough to screenshot straight away. But 60 seconds of onboarding is better — the skill
