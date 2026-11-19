# blader/humanizer

Agent skill that removes signs of AI-generated writing from text

## installation

Once installed, run it with `/humanizer`.

### Claude Code

```text
/plugin marketplace add blader/humanizer
/plugin install humanizer@humanizer
```

The plugin requires Claude Code 2.1.142 or newer; on older versions, run `npx skills add blader/humanizer --global --agent claude-code`.

### Codex

```bash
npx skills add blader/humanizer --global --agent codex
```

### pi

```bash
pi install git:github.com/blader/humanizer
```

Add `-l` to install it only in the current project. `pi update --extensions` pulls new versions.

### Claude.ai and Claude Desktop

Download this repository as a ZIP (**Code → Download ZIP**) and upload it as a skill in Settings.

### Other agents

```bash
npx skills add blader/humanizer --global --agent '*'
```

This installs Humanizer for every agent the Skills CLI supports, including Gemini CLI, GitHub Copilot, and Windsurf. Omit `--global` in any command above to install it only in the current project. For an agent the Skills CLI does not cover, copy `SKILL.md` into its skill folder.

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

To rewrite a file, pass its path:

```
Humanize the prose in docs/launch-post.md
```

Humanizer reads the current file in full before editing, including files it wrote earlier in the session. Its summary states how many sections it reviewed and names any it could not cover.

### Match your voice

To make the rewrite sound like you, include a writing sample:

```
/humanizer

Here's a sample of my writing for voice matching:
[paste 2-3 paragraphs of your own writing]

Now humanize this text:
[paste AI text to humanize]
```

Humanizer follows the sample's rhythm, word choice, punctuation, and deliberate quirks, including dashes if you use them.

## How it works

A language model writes whatever is most likely to come next, so by default it makes the choice that fits the widest range of readers and subjects. A person chooses for one reader and one subject. Every tell Humanizer looks for is a form of that default choice: a sentence that signals importance instead of adding a fact, rhythm or formatting applied by rule, an ordinary fact dressed as a pivotal one, text left over from the chat, or a reply that re-explains what the reader already knows.

> "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."
> Wikipedia, ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)

Humanizer marks every tell it finds, strongest first. It drafts a rewrite, merging, splitting, or reordering sentences and paragraphs as needed, then checks the draft against the patterns and the original claims before writing the final version. Where the text is generic, it adds a specific detail it knows to be true, and it keeps every claim the original made.

When you paste text, Humanizer shows its work: the first rewrite, a short list of tells that survived it, and the final version. Point it at a file and it edits only the prose, leaving code, data, frontmatter, and link targets alone. Personal writing keeps the writer's opinions and quirks; technical and reference prose stays neutral and plain. Informal human text, such as chat messages, rants, and angry reviews, is left alone unless two unrelated tells appear together, and Humanizer keeps the writer's anger at full strength.

## The 26 patterns

Humanizer numbers the patterns from strongest and most common to weakest. It edits any of the first five on one sighting, and acts on a pattern marked *weak alone* only when other tells appear in the same passage, because a careful writer may use any one of them on purpose.

### A. Staging instead of stating

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 1 | **Not X but Y** | "It's not just X, it's Y", "This doesn't mean X. It means Y." | State the point directly |
| 2 | **One-line closers and dramatic fragments** | "That is the real win." after every section; "This shows the importance of..." after an example; "No prior. No nostalgia." | Cut the closer that repeats or explains the example; merge fragments into a specific claim |
| 3 | **Sayings that sound deep** | "At its core, what matters is...", "Symmetry is the language of trust" | Replace the saying with the specific claim |
| 4 | **Staged run-up before the point** | "Let's dive in", "Honestly? It depends...", "The hard part is...", "the part that doesn't" | Remove the run-up and state the point; name what "the part" stands for |
| 5 | **Arguing with no one** | "This isn't mainly about...", "A tempting approach would be..." | Remove the unraised objection or fake option; keep any real claim |

### B. Rhythm by rule

| # | Pattern | Before | After |
|---|---------|--------|-------|
| 6 | **Forced triads** | "innovation, inspiration, and insights"; three examples plus a lesson | Use the number of items 
