# worldwonderer/novel-to-game

Agent Skills that turn novels into source-grounded, fully playable games for Claude Code, Codex, and Kimi Code(K3).

## features

A one-line “turn this book into a game” prompt often produces a generic reskin or a clickable plot summary. NovelToGame keeps the adaptation traceable and gives each major decision a clear owner:

- **Source-grounded adaptation:** extract rules, spaces, character agency, conflicts, and visual anchors with citations;
- **Real game design:** turn source evidence into player verbs, systems, levels, feedback, failure, and outcomes;
- **Target-runtime delivery:** build for the approved platform or engine without implementation silently redesigning the game;
- **Optional, restrained voice:** synthesize only selected high-value lines at build time, keep subtitles and mute fallbacks, and never send the whole novel to a TTS provider by default;
- **Evidence-based QA:** verify startup, rendering, input, the core loop, an outcome, restart, and explicit limitations in the tested runtime.

## installation

### 1. Install the seven skills

| Agent CLI | Install | Invoke |
|---|---|---|
| Claude Code | `npx skills add worldwonderer/novel-to-game -g -y -a claude-code -s '*'` | `/novel-to-game` |
| Codex | `npx skills add worldwonderer/novel-to-game -g -y -a codex -s '*'` | `$novel-to-game` |
| Kimi Code | `npx skills add worldwonderer/novel-to-game -g -y -a kimi-code-cli -s '*'` | `/skill:novel-to-game` |

Install adapters for all three CLIs on the same machine:

```bash
npx skills add worldwonderer/novel-to-game -g -y -s '*' \
  -a claude-code -a codex -a kimi-code-cli
```

Cloning the repository also enables project-local skill discovery in all three CLIs.

### 2. Start an adaptation

Give the agent a novel file, directory, or link:

```text
Use novel-to-game quick to adapt this novel into a fully playable game.
Recommend the target platform, genre, and engine from the source, and keep the first build to about 15 minutes.
Let the player enter the world as an original character with a new playable route through its conflict.
```

When you want an **interactive story** rather than a systems game, say so. That locks the `narrative-led` experience profile, so concept, design, and QA judge continuous scenes, character dialogue, testimony, and key choices instead of applying rounds, cards, and resource bars:

```text
Use novel-to-game quick to adapt this novel into an interactive story.
Carry the experience with continuous scenes, character dialogue, testimony, and key choices.
Keep variables as hidden causal tags rather than a visible stat panel.
Key choices must change later scenes, character attitudes, and the ending, and be named back in later text.
```

The narrative track **lowers no standard**: it still needs a recognizable gameplay precedent, the same
three-phase arc, and the same hard vetoes. Only the expression changes -- new people to question, new ways to
press a contradiction, and attitudes that shifted because of what you did earlier.

`quick` is the low-friction option: the agent drafts sensible defaults, asks only about materially branching or safety-sensitive choices, compares three concepts, and continues through design, build, and QA. Every project runs one minimum QA path covering real startup, rendering, input, a complete loop, an outcome, restart, and explicit limitations. It does not require a human playtest or a separate approval report. Choose `director` when you want to pick the concept yourself.

<details>
<summary><strong>Native plugin installation</strong></summary>

#### Claude Code

```text
/plugin marketplace add worldwonderer/novel-to-game
/plugin install novel-to-game@novel-to-game-skills
/novel-to-game:novel-to-game quick
```

#### Codex

```bash
codex plugin marketplace add worldwonderer/novel-to-game
codex plugin add novel-to-game@novel-to-game-skills
```

#### Kimi Code 0.27 or newer

```text
/plugins install https://github.com/worldwonderer/novel-to-game
/reload
/skill:novel-to-game quick
```

</details>

## Workflow

The orchestrator locks `PRODUCT_BRIEF.md`, then hands the adaptation through six stages with separate ownership. Concept, experience/level design, and art direction remain distinct, while acceptance checks only scope consistency and the six-effect minimum playable contract.

```text
Novel → Source analysis → Concept → World design → Art direction → Build → QA → Playable game
```

Build targets the chosen runtime and prepares one verification entry point; QA runs it once and records the six minimum player-visible effects with real execution evidence. Capability-specific regression checks run only when that capability is actually adopted. No human-playtest gate or duplicate QA report is required. Source identity, public hosting, marketing, rights, subjective fun, and publication quality are not machine-proven by this QA record.

## Skills

| Skill | Responsibility |
|---|---|
| [`novel-to-game`](skills/novel-to-game/) | Confirm requirements, choose a mode, orchestrate stage handoffs, a
