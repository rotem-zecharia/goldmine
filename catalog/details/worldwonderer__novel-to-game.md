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
