# rollingSirius/equity-research-skill

Possibly the deepest AI equity-research skill: nine-chapter single-stock deep dives and earnings deep-dives, with scripted DCF/EPV/EVA and reproducible valuation. Covers US, HK and A-shares. Docs in E

## features

### 1. Full deep-dive research

For studying a company systematically for the first time, or rebuilding an investment framework from scratch. Default output is a nine-chapter report:

1. One-page summary (verdict box + tearsheet + expectations-gap table)
2. Company and business detail
3. Competitive landscape and moat
4. Management, governance, and capital-allocation scorecard
5. Financial analysis and earnings-quality review
6. Multi-method valuation (with a football-field chart)
7. Analyst views and divergence attribution
8. News, risks, and catalysts
9. Investment verdict, counter-case, and position-sizing reference

### 2. Deep earnings mode

For the moment right after a company reports a quarter, a full year, guidance, or a call transcript, when the question is "what did this print actually change?" Earnings mode splits into two cases:

| Coverage status | How the skill handles it |
|---|---|
| A prior report or model exists | Continuing-coverage update, focused on what the print changes relative to the old thesis, old forecasts, and old valuation. |
| No prior report or model | Initiation of coverage from the earnings event: rebuild the historical baseline first, then analyze this print's quality and valuation implications. |

Earnings mode outputs nine chapters by default:

1. Verdict and snapshot
2. Surprise and its quality
3. Revenue, segments, and KPIs
4. Margins, costs, and earnings quality
5. Cash flow, balance sheet, and capital allocation
6. Guidance, the call, and management signals
7. Competition, industry, and market reaction
8. Model, valuation, and the fair-value bridge
9. Thesis update and action list

Every earnings run also executes a minimum check set: accrual ratio, cash conversion, DSO/deferred-revenue divergence, and whether Non-GAAP adjustments are recurring.

### 3. Valuation and calibration

This skill does not allow a target price that merely "looks reasonable." It requires at least three valuation methods cross-checked against each other, with assumptions, calculations, and the label mapping all filed:

- Reverse DCF + PVGO decomposition: what revenue growth, margin, or return on capital the current price implies, and how much of the price is paying for future growth.
- Three-scenario DCF: bull, base, and bear scenarios with a probability-weighted fair value, plus a robustness test that pushes the probabilities toward the extremes.
- EPV / three-factor method: the asset-reproduction floor · EPV · growth entry ladder; the multi-year EPV-to-adjusted-book trend as financial verification of the moat.
- EVA / residual income: incumbent ROIC vs. incremental ROIIC, with the "growth = reinvestment rate × ROIIC" consistency check.
- Relative valuation: warranted-multiple discipline — derive the multiple the company deserves from growth, returns, and risk rather than copying the peer median.
- SOTP: for multi-business or multi-asset companies, or where segments differ sharply.
- Monte Carlo (optional): the P10–P90 fair-value distribution and P(intrinsic value < current price).

The verdict label (undervalued / fairly valued / overvalued + action) maps through pre-registered calibration rules (a ±15% buffer band), overlaid with an action matrix and veto conditions; each action ships with expected value, upside/downside asymmetry, and a Kelly-lite (¼ Kelly) sizing-magnitude reference.

### 4. Earnings-quality review

Before valuing anything, answer whether the profit is real:

- Accrual quality (Sloan): total accruals ratio and the cash-conversion trend.
- The eight-variable Beneish M-Score (computed automatically by the checker).
- Revenue-recognition red flags: DSO divergence, deferred-revenue divergence, channel-stuffing signals.
- Expense capitalization and earnings smoothing; governance and audit signals.
- Output: an A–D earnings-credibility grade. Grade C caps the action at "wait and see," grade D is always "avoid" — "it's cheap" may never be used to offset a credibility problem.

### 5. Industry-spec

## installation

### Easiest method

Copy this repo link and send it to any AI tool that supports skills or agent instructions:

```text
https://github.com/rollingSirius/equity-research-skill
```

For example:

```text
Please install and use this skill:
https://github.com/rollingSirius/equity-research-skill
```

### Claude Code

```bash
# Personal scope: available across all projects
git clone https://github.com/rollingSirius/equity-research-skill.git ~/.claude/skills/equity-research

# Project scope: shared with the repo
git clone https://github.com/rollingSirius/equity-research-skill.git .claude/skills/equity-research
```

### Claude Desktop / Cowork

Zip this repo, or download a Release, and upload it under **Settings -> Capabilities -> Skills**.

## tools

The skill itself is Markdown instructions, accompanied by reproducible scripts. Any agent that can read files can use it, and local Python is **not a prerequisite for installation**:

1. Put this repo in your project directory, e.g. `skills/equity-research/`.
2. Add one line to your agent config: when the user asks to research or analyze a stock, first read and follow the full workflow in `skills/equity-research/SKILL.md`.
3. When the valuation or checker scripts need to run, prefer the agent's own code environment; with no local Python, run them in a hosted AI code environment or an online notebook — no local Python setup required first.

## requirements

| Dependency | Required? | Notes |
|---|---|---|
| Web search / page fetching | Recommended | For live quotes, regulatory filings, industry data, analyst ratings, and news; offline use requires the user to supply the materials. |
| An executable Python environment | Needed to run the scripts | The agent's own environment, a hosted AI environment, an online notebook, or local Python all work; no local install required. The scripts use the standard library only. |
| PDF generation | Needed for the default output | A PDF skill or an md→PDF toolchain; if unavailable, delivery downgrades to `.md` with an explanation. |
| IBKR or other market-data connectors | Optional | One quote path among several; without it, use exchanges, professional data APIs, or public quote sources. |
| Morningstar or other professional data connectors | Optional | Used for an external valuation anchor, moat ratings, consensus, and standardized data; none are required. |
| docx / xlsx skills | Optional | Only when the user asks for a Word report or an Excel valuation workbook. |

## Design stance

This skill is designed **depth first**: it would rather be slow than give up clear sources, transparent assumptions, reproducible valuation, accountable conclusions, and falsifiable disagreements. It suits serious investment research, long-term coverage, and investment memos, and is not for anyone who just wants a one-line quote or general market commentary.

## Disclaimer

Everything this skill produces is research reference only and **does not constitute investment advice**. Neither the author nor this skill is a licensed investment advisor; investment decisions and their consequences are the user's own.

## License

[MIT](LICENSE)
