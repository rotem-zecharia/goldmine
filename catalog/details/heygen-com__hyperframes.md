# heygen-com/hyperframes

AI video you can actually edit. HyperFrames is a free, open-source AI video editor. Describe any video and get a real project you can change down to the frame.

## installation

Using Claude Code, Codex, Cursor, or another coding agent? Install the skills once, then ask your agent to make a video.

### Give your coding agent the skills (recommended)

```bash
npx skills add heygen-com/hyperframes     # pick "Core Skills" in the picker
# or, with no picker (scripts, CI):
npx hyperframes skills update
```

Then try: _Using `/hyperframes`, create a 10-second product intro with a fade-in title, a background video, and subtle background music._

### Claude Code plugin

```bash
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
```

### Codex, Cursor, Gemini CLI, Copilot

See the [plugin guide](https://hyperframes.heygen.com/guides/plugins?utm_source=github&utm_medium=readme).

### By hand, with the CLI

```bash
npx hyperframes init my-video
cd my-video
npx hyperframes preview      # live preview in the browser
npx hyperframes render       # render to MP4
```

Requirements: Node.js 22+ and FFmpeg. Render in the cloud with `hyperframes cloud render`, or on your own [AWS Lambda](https://hyperframes.heygen.com/deploy/aws-lambda?utm_source=github&utm_medium=readme).

<details>
<summary>Skill install options, updates and the core set (full details)</summary>

### Claude Code plugin updates

To enable auto-update for the **hyperframes** marketplace, run `claude` in a
terminal in your project. In Claude Code's terminal UI, run `/plugin`, then select
**Marketplaces** → **hyperframes** → **Enable auto-update**. Afterward, use
`/hyperframes:hyperframes`. See the [plugin guide](docs/guides/plugins.mdx)
for Copilot, VS Code, Cursor, Gemini CLI, updates, and migration.

### Standalone skills (including OpenCode)

> The picker opens with nothing pre-selected — the **Core Skills** group is all you need; `/slideshow`, `/remotion-to-hyperframes` and `/figma` install on demand. Without the picker (a script or a CI job), `npx hyperframes skills update` installs exactly the core set, whereas `skills add --all` installs all 9 published skills. The six repo-internal skills under `.claude/skills` / `.agents/skills` are excluded by default. For the full published set use `npx hyperframes skills`.
>
> `skills add` resolves the skills.sh registry blob, which can lag `main` by hours. `npx hyperframes skills update` installs the skills from the release tag that matches your CLI version, so they match the CLI that runs them.

Run project-local installs from your video project's directory. From a HyperFrames
checkout, use `npx hyperframes skills update` for a global install instead: a
project-local installer target can overlap the tracked `skills/` source and
overwrite uncommitted edits. See [contributor setup](CONTRIBUTING.md#getting-started).

</details>

The skills teach agents the HyperFrames production loop: plan the video, write valid HTML, wire seekable animations, add media, lint, preview, and render. They work with Claude Code, Codex, Cursor, Gemini CLI, IBM Bob, and other coding agents that support skills.

### Share a video for review

Sign in with `npx hyperframes auth login`, then run `npx hyperframes share` to
choose who can open the rendered review. Use `share --update` when edits should
become a new version and `share --manage` for web settings. CLI and Desktop use
the same sharing system and five free projects per workspace. Existing legacy
published links remain reachable.

## Skills

HyperFrames ships 9 skills. Make any video by asking for it; the `/hyperframes` skill carries the contract and the references (film, captions, overlays, motion, look). Read it first.

The **core set** below is what `npx hyperframes skills update` installs and what the picker lists as "Core Skills". Install one skill with `npx skills add heygen-com/hyperframes --skill <name>`, or all 9 with `--all`. A non-interactive or agent run of `npx skills add` without `--skill` installs all 9. `npx hyperframes init` adds the core set only when it is missing and never touches a skill you already have; on-

## features

- **HTML-native:** make videos programmatically with HTML, CSS and JavaScript; compositions are HTML files with data attributes. No React requirement, no proprietary timeline format.
- **Agent-friendly:** agents already write HTML, and the CLI is non-interactive by default.
- **Deterministic:** same input, same frames, same output. Built for CI, regression tests, and automated rendering.
- **No build step:** an `index.html` composition plays as-is and can be previewed directly in the browser.
- **Adapter-based animation:** bring GSAP, CSS animations, Lottie, Three.js, Anime.js, WAAPI, or a custom runtime.
- **Open source:** Apache 2.0 license, with no per-render fees or commercial-use thresholds.

## HyperFrames vs Remotion

HyperFrames is inspired by [Remotion](https://www.remotion.dev). Both tools render video with headless Chrome and FFmpeg. The main difference is the authoring model: Remotion's bet is React components; HyperFrames' bet is plain HTML that humans and agents can both write easily.

|                          | **HyperFrames**                       | **Remotion**                            |
| ------------------------ | ------------------------------------- | --------------------------------------- |
| Authoring                | HTML + CSS + seekable animation       | React components                        |
| Build step               | None; `index.html` plays as-is        | Bundler required                        |
| Agent handoff            | Plain HTML files                      | JSX / React project                     |
| Library-clock animations | Seekable, frame-accurate via adapters | Wall-clock animation patterns need care |
| Distributed rendering    | Local and AWS Lambda render paths     | Remotion Lambda, mature cloud renderer  |
| License                  | Apache 2.0                            | Source-available Remotion License       |

Read the full comparison in the [HyperFrames vs Remotion guide](https://hyperframes.heygen.com/guides/hyperframes-vs-remotion?utm_source=github&utm_medium=readme), or the [side-by-side comparison page](https://hyperframes.heygen.com/vs/remotion?utm_source=github&utm_medium=readme).

## Catalog

Install ready-to-use blocks and components:

```bash
npx hyperframes add flash-through-white   # shader transition
npx hyperframes add instagram-follow      # social overlay
npx hyperframes add data-chart            # animated chart
```

Browse the catalog at [hyperframes.heygen.com/catalog](https://hyperframes.heygen.com/catalog/blocks/data-chart?utm_source=github&utm_medium=readme).

## HyperFrames Stack

HyperFrames is the open-source rendering engine, plus a growing set of tools around HTML-native video creation.

| Piece                                                                                 | Status              | What it does                                                                                    |
| ------------------------------------------------------------------------------------- | ------------------- | ----------------------------------------------------------------------------------------------- |
| CLI                                                                                   | Available           | Scaffold, preview, lint, inspect, and render local video projects                               |
| Core / Engine / Producer                                                              | Available           | Parse compositions, drive headless Chrome, encode video, and mix audio                          |
| Catalog                                                                               | Available           | Reusable blocks and components for transitions, overlays, captions, charts, maps, and effects   |
| Agent skills                                                                          | Available           | Teach coding agents the video-production patterns that generic web docs miss                    |
| Browser editor
