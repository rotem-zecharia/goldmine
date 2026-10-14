# JuliusBrussee/caveman

🪨 why use many token when few token do trick. Viral skill + proxy for coding agents that cuts 65% of tokens by talking like a caveman.

## features

**Caveman make your AI agent say less and read less. Code stay exact. Brain still big.**

<a href="https://github.com/JuliusBrussee/caveman/stargazers"><img src="https://img.shields.io/github/stars/JuliusBrussee/caveman?style=flat-square&color=F0A63C&label=stars" alt="GitHub stars"></a>
<a href="https://www.npmjs.com/package/@caveman-ai/cli"><img src="https://img.shields.io/npm/dm/@caveman-ai/cli?style=flat-square&color=F0A63C&label=cli%20downloads" alt="npm downloads"></a>
<a href="./INSTALL.md"><img src="https://img.shields.io/badge/works_with-30%2B_agents-orange?style=flat-square" alt="30+ agents"></a>
<a href="#license"><img src="https://img.shields.io/badge/license-Apache--2.0-green?style=flat-square" alt="License"></a>

<table>
<tr>
<td align="center" width="25%"><h3>33.2% fewer</h3>input tokens, whole sessions<br><sub><a href="#read-less-332-fewer-input-tokens">54 Claude Code runs</a>, 18 of 18 answers right</sub></td>
<td align="center" width="25%"><h3>54% cheaper</h3>with Auto, same score<br><sub><a href="#auto-54-cheaper-same-score">85 coding tasks</a> vs Opus 5.5 at xhigh, interim</sub></td>
<td align="center" width="25%"><h3>397 → 76</h3>tokens for one test run<br><sub><a href="#blocks-code-mode-script-written-once">Blocks</a> vs <code>| tail -20</code></sub></td>
<td align="center" width="25%"><h3>1.4 to 2.4× cheaper</h3>with caveman-style output<br><sub><a href="https://arxiv.org/abs/2606.24083">Adobe Research</a>, eight models</sub></td>
</tr>
</table>

Cited by **[Adobe Research](https://arxiv.org/abs/2606.24083)** · A/B tested by **[JetBrains](https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/)** · Remade for Elasticsearch on **[Elasticsearch Labs](https://www.elastic.co/search-labs/blog/elastic-caveman-ai-token-reduction)**<br>
**#1** on [Hacker News](https://news.ycombinator.com/item?id=47647455) · **#1** on GitHub Trending · *"No way this actually works."* [ThePrimeagen](https://www.youtube.com/watch?v=L29q2LRiMRc)

**[Install](#install) · [Six rocks](#six-rocks-one-install) · [Proof](#proof) · [Say less](#say-less-the-caveman-voice) · [Read less](#read-less-332-fewer-input-tokens) · [Auto](#auto-54-cheaper-same-score) · [Blocks](#blocks-code-mode-script-written-once) · [Commands](#commands) · [Caveman Cloud](#caveman-cloud)**

</div>

---

<table>
<tr>
<th width="50%">Normal agent · 63 tokens</th>
<th width="50%"><img src="docs/assets/dancing-rock.svg" width="18" height="18" alt=""> Caveman agent · 20 tokens</th>
</tr>
<tr>
<td valign="top">

> The reason your React component is re-rendering is likely because you're creating a new object reference on each render cycle. When you pass an inline object as a prop, React's shallow comparison sees it as a different object every time, which triggers a re-render. I'd recommend using useMemo to memoize the object.

</td>
<td valign="top">

> New object ref each render, so React re-renders. Wrap the prop in `useMemo`.

</td>
</tr>
</table>

**Same fix. 63 token become 20. Brain still big.**

Pick your club:

| Skill | Same answer | Tokens |
|---|---|---:|
| `/caveman` | New object ref each render, so React re-renders. Wrap the prop in `useMemo`. | 20 |
| `/ultracave` | Inline object prop, new ref, re-render. `useMemo`. | 14 |
| `/megacave` | 新參照致重繪。`useMemo`。 | **13** |

<sub>Token counts: tiktoken o200k.</sub>

## installation

```bash
npx @caveman-ai/cli@latest
```

One command. Mac, Linux, Windows. Caveman find your agents and your logins, show what it change. Press Enter. Done. Needs Node.js 22.13+.

After that, plain `claude` stays caveman'd. So do Codex, Gemini CLI, OpenCode, and [30+ more](./INSTALL.md). It runs on your machine, with your keys and your Claude Pro/Max login. One rock. That it.

<sub>Had caveman before 4.0? Say <code>@latest</code>, or the old copy on your machine wins. Already set up? <code>caveman setup</code> opens the screen again. Only want shorter answers? <a href="#say-less-the-caveman-voice">Get just the skill</a>.</sub>

## Six rocks, one install

New in 4.0: caveman is six parts. All on after install. Each has its own switch.

| Rock | What it does | Measured |
|---|---|---|
| **[Say less](#say-less-the-caveman-voice)** | Agent answers short. Code stays exact | 63 → 20 tokens, same fix |
| **[Read less](#read-less-332-fewer-input-tokens)** | Logs, JSON, CSV, test output shrink before the model reads them | **33.2%** fewer input tokens per session |
| **[Auto](#auto-54-cheaper-same-score)** · new | Picks the model and the effort for each ask | **54%** cheaper than Opus at xhigh, same score |
| **[Blocks](#blocks-code-mode-script-written-once)** · new | Code mode: agent keeps the scripts it writes and runs them again | **397 → 76** tokens for one test run |
| **[Waste fixes](#smaller-rocks)** | Finds where your tokens go and fixes it. New: keeps the prompt cache warm while you pause | Not measured yet |
| **[Browse](#smaller-rocks)** | Web pages come back compressed | **129.8×** smaller page |

`caveman status` shows what is on. `caveman off browse` turns one off. Only Auto needs an account, and it is free. [4.0.0 release notes](https://github.com/JuliusBrussee/caveman/releases/tag/v4.0.0)

## Proof

Outside labs first. Ours come with each rock below. Nothing rounded up. Red rows stay red.

| Who | Setup | Result |
|---|---|---|
| **[Adobe Research](https://arxiv.org/abs/2606.24083)**, CAVEWOMAN paper (cites this repo) | Caveman-style output, eight models, five datasets | **Cost cut 1.4 to 2.4× per model, up to 3×** |
| **[Elastic](https://www.elastic.co/search-labs/blog/elastic-caveman-ai-token-reduction)**, Elasticsearch Labs | Caveman mode remade for Elasticsearch, eight live MCP scenarios | **63.6% fewer response tokens.** *"Zero information loss."* |
| **[JetBrains](https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/)** | 86 real coding tasks, paired A/B | **No measurable quality loss** (p = 0.82). 8.5% fewer output tokens |

Two findings shaped caveman. Adobe: cavemanning *your* prompt makes answers worse, so caveman never touches your prompt. JetBrains: agent sessions are mostly code and tool calls, which the voice leaves alone. So caveman grew rocks that shrink what the agent *reads* and what it *runs on*.

## Say less: the caveman voice

**A voice, not broken grammar. Every reply follows the same structure.**

| Rule | What it means |
|---|---|
| **Answer first** | `[thing] [action] [reason]. [next step].` No greeting, no "let me", no recap |
| **One idea per sentence** | Built on [ASD-STE100](https://www.asd-ste100.org/), the controlled English of aircraft maintenance manuals: 20 words max, active voice, one term per thing |
| **Meaning never dropped** | Articles can go. *not*, *never*, *no*, *only* never go. Numbers and units stay exact |
| **Payload verbatim** | Code, commands, paths, and error messages untouched, character for character |
| **No theater** | No "me think". No chatter between tool calls. If caveman phrasing isn't shorter, plain wins |
| **Knows when to stop** | Security warnings, irreversible actions, and confused users get full sentences. Then grunt resumes |
| **Your prompts stay yours** | Never rewritten. [Research say that backfire](#proof) |

Ten dev questions on claude-opus-5-5:

| Instruction | Output tokens |
|---|---:|
| None | 6,983 |
| `Answer concise

## tools

In your terminal:

```bash
caveman claude                # start an agent on caveman: codex · gemini · opencode · aider · kilo · qwen · hermes · openclaw · pi
caveman status                # what is on, which agents it reaches, one next step
caveman on browse             # switch one rock on or off: output · input · waste-fixes · routing · scripts · browse
caveman login                 # free account, turns on Auto
caveman learn                 # where your tokens go
caveman trial -- claude       # A/B a real session on your own work
caveman shrink -- pnpm test   # compress noisy command output
caveman convert --dry-run     # pixel mode: skills the model reads as images
caveman stats                 # your token history
caveman doctor                # one problem per line, with its fix
```

In your agent:

| Command | What it does |
|---|---|
| `/caveman` · `/ultracave` · `/megacave` | The voice, the grunt, the 文言文. `/caveman status` shows the mode, `/caveman off` stops it |
| `/caveman-commit` | One-line Conventional Commit |
| `/caveman-review` | One finding per line: `L42: 🔴 null deref. Guard it.` |
| `/caveman-compress <file>` | Shrinks memory files and backs up the original |
| `/caveman-stats` | Real token usage for this Claude Code session |
| `/caveman-help` | Every mode and command on one screen |
| `cavecrew` | Subagents that find, edit, and review code, then report back in caveman |
| `investigate-first` · `lean-build` · `surgical-patch` · `safe-refactor` · `migration` · `verify-and-stop` | Work patterns that write less code. Your agent picks them up when a task fits |
| `caveman-setup` · `caveman-discover` · `caveman-learn` · `caveman-manage` · `caveman-optimize` · `caveman-explore` · `caveman-evidence-review` | Drive the proxy from inside your agent |

## Caveman Cloud

**Everything above is for the coding agent you use. Caveman Cloud is for the agents you build.**

You ship an agent. Every run costs money. Is it good? Is it cheap? Which change made it worse? Cloud answers.

| Cloud does | What you get |
|---|---|
| **Observability** | Every run traced to the work and what it cost. Sets itself up from your repo, your keys, and the logs or OpenTelemetry you already have |
| **Evals** | Grades how good the answers are, on your own tasks, from your real traffic |
| **Autopilot** | Proposes a cheaper change, tests it on your recorded work, ships only when the evals say answers are still as good. You approve the pull request |
| **Proof** | Every number says if it is measured, inferred, or verified. A saving counts only after real traffic shows it |

<p align="center">
<a href="https://app.caveman.so/signup"><b>Sign up free</b></a> &nbsp;·&nbsp; <a href="https://caveman.so/demo">Try the demo</a> &nbsp;·&nbsp; <a href="https://cal.com/caveman/chat">Book a call</a> &nbsp;·&nbsp; <a href="https://docs.caveman.so">Docs</a>
</p>

## In the wild

<a href="https://www.youtube.com/watch?v=L29q2LRiMRc"><img src="https://img.youtube.com/vi/L29q2LRiMRc/hqdefault.jpg" alt="ThePrimeagen reacts to Caveman: No way this actually works" width="340" align="right"></a>

**ThePrimeagen**: *"No way this actually works."* [Watch](https://www.youtube.com/watch?v=L29q2LRiMRc)

**Adobe Research**: [CAVEWOMAN](https://arxiv.org/abs/2606.24083), arXiv, June 2026

**JetBrains**: *"It is fun, and it costs you nothing measurable in quality."* [Read](https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/)

**Elastic**: [elastic-caveman](https://www.elastic.co/search-labs/blog/elastic-caveman-ai-token-reduction) on Elasticsearch Labs, April 2026

**Hacker News**: [#1, 904 points](https://news.ycombinator.com/item?id=47647455)

**GitHub Trending** #1 overall, July 2026 · **[Trendshift](https://trendshift.io/repositories/25391)** #1 repo of the day, April 2026 · **[Product Hunt](https://www.producthunt.com/products/caveman)** #8 of the day

Started as a joke in April 2026. Now past 100,000 stars. Joke got serious. Voice di
