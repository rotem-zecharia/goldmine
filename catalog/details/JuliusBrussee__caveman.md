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
<td align="center" width="33%"><h3>33.2% fewer</h3>input tokens through <a href="#the-proxy-332-fewer-input-tokens">the proxy</a><br><sub>54 Claude Code runs, 18 of 18 answers right</sub></td>
<td align="center" width="33%"><h3>129.8× smaller</h3>web pages for the agent<br><sub><a href="./browse/BENCHMARK.md"><code>caveman browse</code></a> vs a Playwright snapshot</sub></td>
<td align="center" width="33%"><h3>1.4 to 2.4× cheaper</h3>with caveman-style output<br><sub><a href="https://arxiv.org/abs/2606.24083">Adobe Research</a>, eight models</sub></td>
</tr>
</table>

Cited by **[Adobe Research](https://arxiv.org/abs/2606.24083)** · A/B tested by **[JetBrains](https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/)** · Remade for Elasticsearch on **[Elasticsearch Labs](https://www.elastic.co/search-labs/blog/elastic-caveman-ai-token-reduction)**<br>
**#1** on [Hacker News](https://news.ycombinator.com/item?id=47647455) · **#1** on GitHub Trending · *"No way this actually works."* [ThePrimeagen](https://www.youtube.com/watch?v=L29q2LRiMRc)

**[How it talks](#how-caveman-talks) · [Install](#install) · [The numbers](#the-numbers) · [The proxy](#big-rock-the-proxy) · [The skill](#small-rock-the-skill) · [What you get](#what-you-get) · [In the wild](#in-the-wild)**

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

## How caveman talks

Caveman is a voice, not broken grammar. Every reply follows the same structure:

| Rule | What it means |
|---|---|
| **Answer first** | `[thing] [action] [reason]. [next step].` No greeting, no "let me", no recap, no "hope this helps" |
| **One idea per sentence** | Built on [ASD-STE100](https://www.asd-ste100.org/), the controlled English written for aircraft maintenance manuals: 20 words max, active voice, one term per thing |
| **Meaning never dropped** | Articles can go. *not*, *never*, *no*, *only* never go. Numbers and units stay exact |
| **Payload verbatim** | Code, commands, paths, error messages, and your existing code comments untouched, character for character. Small fix shows the changed lines, not the whole file again |
| **Quiet tool runs** | No chatter between tool calls. One line per phase, one line with the result |
| **Knows when to stop**

## installation

```bash
npm install -g @caveman-ai/cli && caveman setup --install
caveman claude        # or codex · gemini · aider · kilo · qwen · opencode · hermes · openclaw · pi
```

**This is the proxy, the big rock.** Your agent reads 33.2% fewer input tokens across whole sessions, same answers. It runs on your machine, with your keys and your Claude Pro/Max login. Needs Node.js 22.13+. After the first run, plain `claude` stays caveman'd. One rock. That it.

[What the proxy does](#big-rock-the-proxy) · Only want shorter answers? [Get just the skill](#small-rock-the-skill)

## The numbers

Outside labs first, then ours. Nothing rounded up. Red rows stay red.

| Who | Setup | Result |
|---|---|---|
| **[Adobe Research](https://arxiv.org/abs/2606.24083)**, CAVEWOMAN paper (cites this repo) | Caveman-style output, eight models, five datasets | **Cost cut 1.4 to 2.4× per model, up to 3×** |
| **[Elastic](https://www.elastic.co/search-labs/blog/elastic-caveman-ai-token-reduction)**, Elasticsearch Labs | Caveman mode remade for Elasticsearch, eight live MCP scenarios | **63.6% fewer response tokens.** *"Zero information loss."* |
| **[JetBrains](https://blog.jetbrains.com/ai/2026/07/speak-to-ai-agents-like-cavemen-tosave-tokens/)** | 86 real coding tasks, paired A/B | **No measurable quality loss** (p = 0.82). 8.5% fewer output tokens |

Two findings shaped caveman. Adobe found that cavemanning *your* prompt makes answers longer and worse, so caveman never touches your prompt. JetBrains found that agent sessions are mostly code and tool calls, which the skill leaves alone. So caveman grew a second rock that shrinks what the agent *reads*: [the proxy](#big-rock-the-proxy).

### The proxy: 33.2% fewer input tokens

| File type | The file, through caveman | File saved | Whole Claude Code session, 3 runs | Session saved |
|---|---:|---:|---:|---:|
| CSV | 28,041 → **314** | **98.9%** | 165,823 → 74,484 | **55.1%** |
| Logs | 22,810 → **348** | **98.5%** | 148,807 → 74,068 | **50.2%** |
| YAML | 20,447 → **178** | **99.1%** | 132,124 → 71,027 | **46.2%** |
| Test output | 18,806 → **203** | **98.9%** | 150,377 → 108,514 | **27.8%** |
| JSON | 18,837 → **281** | **98.5%** | 147,975 → 108,939 | **26.4%** |
| HTML | 21,670 → 21,670 | none yet | 140,687 → 154,641 | 9.9% worse |
| **All six** | 130,611 → 22,994 | 82.4% | **885,793 → 591,673** | **33.2%** |

**18 of 18 answers right.** *The file* is each benchmark file run through today's compressor on its own. *The session* is the whole agent run, which also carries the system prompt, tool definitions, conversation, and caveman's own rules, so it moves less than the file. The session run is from August 2026, on an engine that only got the JSON file down to 8,106 tokens. HTML has no compressor yet, so caveman paid its overhead and won nothing back. Each file hides one record in 61 to 72 KB of noise; your files will vary. Headroom on the same suite got 15 of 18 right and used 6.7% fewer tokens on those 15. [Method](./docs/WRAP-BENCHMARK.md#per-file-compression)

### The skill: ten dev questions on claude-opus-5-5

| Instruction | Output tokens |
|---|---:|
| None | 6,983 |
| `Answer concisely.` | 4,334 |
| `/caveman` | 4,119 |
| `/ultracave` | **2,693** |

New models already know "be concise", so that line is the real baseline. On top of it, `/caveman` cuts 3% more at the median and `/ultracave` cuts 35% more. Measured on the 3.1.0 skill text, not yet re-run on this release's. [Harness](./evals/README.md)

<!-- BENCHMARK-TABLE-START -->
<!-- BENCHMARK-TABLE-END -->

### Everything else

| What | Result |
|---|---|
| A web page the agent reads (`caveman browse`, 200-row table) | **121 tokens instead of 15,704** for a Playwright snapshot, 129.8× smaller. Tiny forms lose 2.3×. [Bench](./browse/BENCHMARK.md) |
| Memory files like `CLAUDE.md` (`/caveman-compress`) | **4,138 tokens instead of 6,198** across five fixtures, 22.8% to 49.1% smaller per file, with every heading, code block, and path intact. [Bench](
