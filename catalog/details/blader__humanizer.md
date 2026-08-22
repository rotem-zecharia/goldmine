# blader/humanizer

Agent skill that removes signs of AI-generated writing from text

## tools

Call the skill directly:

```
/humanizer

[paste your text here]
```

Or ask in plain language:

```
Please humanize this text: [your text]
```

To rewrite a file, give Humanizer its path:

```
Humanize the prose in docs/launch-post.md
```

### Match your voice

If you want the rewrite to sound more like you, include a sample:

```
/humanizer

Here's a sample of my writing for voice matching:
[paste 2-3 paragraphs of your own writing]

Now humanize this text:
[paste AI text to humanize]
```

Humanizer follows the sample's rhythm, word choice, punctuation, and deliberate quirks.

## The 35 patterns

### Content patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 1 | **Inflated importance and legacy** | "marking a pivotal moment in the evolution of..." | "was established in 1989 as part of a wider decentralization" |
| 2 | **Name-dropping to prove importance** | "cited in NYT, BBC, FT, and The Hindu" | Keep only useful, sourced context |
| 3 | **Shallow -ing analysis** | "symbolizing... reflecting... showcasing..." | Keep only what the source supports |
| 4 | **Sales language** | "nestled within the breathtaking region" | "is a town in the Gonder region" |
| 5 | **Vague sources** | "Experts believe it plays a crucial role" | Name a real source or remove the claim |
| 6 | **Formulaic challenges and outlook** | "Despite challenges... continues to thrive" | Keep the facts and remove the sales pitch |

### Language and grammar patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 7 | **Overused AI words** | "Actually... additionally... gated on... quietly... testament... landscape... showcasing" | "also... needs... remain common" |
| 8 | **Avoiding is and are** | "serves as... features... boasts" | "is... has" |
| 9 | **Not X but Y and clipped endings** | "It's not just X, it's Y", "..., no guessing" | State the point directly |
| 10 | **Forced groups of three** | "innovation, inspiration, and insights" | Use the number of items the meaning needs |
| 11 | **Changing names and repeated openings** | "protagonist... main character... hero" or "She noted... She noted... She filed..." | Use one name or merge the repeated sentences |
| 12 | **False from X to Y ranges** | "from the Big Bang to dark matter" | List the topics directly |
| 13 | **Passive voice and missing subjects** | "No configuration file needed" | Name the actor when that helps |

### Style patterns

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 14 | **Em/en dashes** | "institutions—not the people—yet this continues—" | Cut them: periods, commas, colons, or parentheses |
| 15 | **Too much bold text** | "**OKRs**, **KPIs**, **BMC**" | "OKRs, KPIs, BMC" |
| 16 | **Lists with bold mini-headings** | "**Performance:** Performance improved" | Use prose when a list adds no value |
| 17 | **Title case in headings** | "Strategic Negotiations And Partnerships" | "Strategic negotiations and partnerships" |
| 18 | **Emojis** | "🚀 Launch Phase: 💡 Key Insight:" | Remove emojis |
| 19 | **Curly quotes** | `said “the project”` | `said "the project"` |
| 26 | **Too many hyphenated word pairs** | “cross-functional, data-driven, client-facing” | Keep only the hyphens grammar needs |
| 27 | **A fake deeper truth** | "At its core, what matters is..." | State the point directly |
| 28 | **Announcing the next point** | "Let's dive in", or "one thing that bit me" | Start with the content |
| 29 | **A heading repeated below itself** | "## Performance" + "Speed matters." | Let the heading do the work |
| 30 | **Writing about the old version** | "This function was added to replace..." | Describe what it does now |
| 31 | **Forced punchlines and fragments** | "It had no preference. No prior. No nostalgia." | Use natural sentence lengths and specific claims |
| 32 | **Formulaic sayings** | "Symmetry is the language of trust" | State the specific claim |
| 33 | **Fake-candid openings** | "Honestly? It depends..." | State the answer

## installation

Install Humanizer with the Skills CLI:

```bash
npx skills add blader/humanizer --global
```

Leave off `--global` to install Humanizer only in the current project. Add `--agent <name>` or `--agent '*'` to choose which agents receive it, then reload their skills.

Claude Code 2.1.142 or newer can install the plugin instead:

```text
/plugin marketplace add blader/humanizer
/plugin install humanizer@humanizer
```

The plugin command is `/humanizer:humanizer`.

In Claude Desktop, download this repository as a ZIP and upload it as a skill.

For a manual install, copy `SKILL.md` into the agent's skill folder.
