# winstonkoh87/Athena-Public

Athena is a local-first agentic PKM that helps you make better decisions with your own context — persistent memory, structured reasoning, and governed AI agents that work across any LLM. Own the state

## features

Athena moves the memory layer to **your machine**. Plain Markdown files that you own, version-control, and point at any model.

- **🧠 Your Memory, Your Machine** — Files on your disk, not in OpenAI's cloud. Read them, edit them, git-version them.
- **🔌 Switch Models Freely** — Claude today, Gemini tomorrow, GPT next week. The memory stays. The model is just whoever's on shift.
- **📈 It Compounds** — Session 500 recalls patterns from session 5. The durable asset isn't the code — it's your data: anyone can fork Athena; nobody can fork your sessions. That's a personal continuity advantage, not vendor lock-in — the files move with you. Honest caveat: compounding needs curation. Keep the `/end` loop running; unpruned memory decays like any archive. [→ The Compounding Effect](Athena-Public.wiki/The-Compounding-Effect.md)
- **⚡ 2K–20K Token Boot** — Scales to the task. Lightweight chat (~2K) → `/start` (~10K) → `/ultrastart` (~20K). 80–98% of your context window stays free, even after 10,000 sessions.
- **🔬 Meta-Game Reasoning** — Generic LLMs optimise *within* the game you're playing. Athena asks whether you should be playing that game at all. [→ Meta-Game Thesis](docs/concepts/Meta_Game_Thesis.md)
- **🛡️ Governed Autonomy** — 6 constitutional laws, 4 capability levels, bounded agency.

> *A generic LLM is a brilliant amnesiac. Athena is the hippocampus — the memory that makes intelligence useful.*
>
> *Or in engineering terms: The LLM is the engine. Athena is the chassis, the memory, and the rules of the road. Swap the engine anytime — the car remembers every road you've driven.*
>
> *The design philosophy: [augment the human, not replace them](docs/concepts/Grace_Protocol.md). After 1,900+ sessions, the bottleneck shifted — [optimising the operator is now higher-leverage than optimising the AI](docs/USER_DRIVEN_RSI.md#phase-2-optimising-the-operator).*

### The Human Augmentation Thesis

Athena's centralised design principle: **augment human cognition, not replace it.** The more context you give Athena, the sharper its answers become — not by remembering your preferences, but by **reasoning differently because of what it knows about you.**

But personalization is only half the design — and on its own, it's the dangerous half. An AI tuned purely to *fit you* is a mirror: it hands your own blind spots back to you, faster and more fluently than you'd rationalise them yourself. The moat was never that Athena agrees with you more precisely. It's that Athena knows you well enough to tell you when **you** are the problem — and has the standing (Law #1, the Committee of Seats) to refuse a premise a generic assistant would obligingly help you execute.

So the USP has two legs, not one:

- **It knows you** — owned, portable, compounding context. The substrate nobody else has.
- **It will disagree with you** — grounded in *your* documented patterns, not generic hedging. The leg that makes the first one safe to stand on.

Personalization is what makes the disagreement credible (it's aimed at your actual situation, not a textbook). The disagreement is what keeps the personalization from becoming a well-decorated echo chamber. Neither leg is the USP alone; the product is the pair.

A generic LLM gives the internet's statistically average answer — correct *on average, across all humans*. Athena gives answers calibrated to *your specific situation* — including the situations where the honest answer is the one you were hoping it wouldn't say:

<table>
<tr>
<th width="25%">Question</th>
<th width="37%">Generic LLM</th>
<th width="38%">Athena (with your context)</th>
</tr>
<tr>
<td><strong>The Trolley Problem</strong></td>
<td>
“Pull the lever — utilitarian calculus says save five lives.”
</td>
<td>
Challenges the false binary. Generates third options. Asks why you’re on the tracks in the first place. Identifies the systemic failures that created the dilemma. Refuses to solve the wrong problem.
</td>
</tr>
<tr>
<td><strong>“Should I double down on 1

## installation

**Works on macOS, Windows, and Linux.**

### 1. Clone the repo

```bash
git clone https://github.com/winstonkoh87/Athena-Public.git
cd Athena-Public
```

Clone it anywhere you keep projects (e.g. `~/Projects/`). This folder **is** your Athena workspace — your memory, protocols, and config all live here.

## configuration

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows
```

> [!IMPORTANT]
> On macOS (Homebrew) and Ubuntu 23.04+, installing packages without a virtual environment will fail with `externally-managed-environment`. The step above prevents this.
