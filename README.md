# goldmine

Find the tool that already solves your problem, from inside Claude Code.

goldmine is a Claude Code plugin. It keeps a scored catalog of MCP servers, Claude Code skills and
plugins, and general open-source developer tools, and answers "is there a tool for this?" at the
moment the question comes up. When nothing solves the whole problem, it says how much is solved and
what is left to build.

## Install

```bash
/plugin marketplace add rotemzecharia/goldmine
/plugin install goldmine
```

## Use it

```
/goldmine analyze an Instagram reel frame by frame
```

```
claude-video-vision (1.25k★, established, pushed 2026-08-07) — roughly 65% of what you need
  covered: keyframe extraction, per-frame vision, transcription, synthesis
  missing: Instagram fetching, caption and hashtag metadata
  gap:     two small pieces — a yt-dlp or instaloader wrapper, plus a metadata fetch
```

It also speaks up on its own, once and briefly, when you are about to hand-roll something the
catalog already covers. It stays quiet otherwise.

## Why not just search GitHub

Two failures, both measured rather than assumed.

**Your words are not the maintainer's words.** Searching `instagram reel analysis` returns a 26-star
toy. Searching `video analysis mcp` returns the 1,253-star tool that actually does the job. Same
need. goldmine expands your ask into several domain vocabularies before it searches.

**Stars rank fame, not fitness.** Ask for a tool to download an Instagram carousel and star-ordering
hands you a 42k-star video downloader over the 19k-star gallery downloader that is the right answer.
goldmine filters for relevance first and ranks second.

## How ranking works

Every repository gets a 0–100 score from six signals: stars (log-scaled), star velocity, days since
last push, contributor count, issue close ratio, and packaging quality. Archived, unmaintained,
forked, and brand-new-with-no-traction repositories take hard demotions.

The weights live in [`config/scoring.yaml`](config/scoring.yaml) and are meant to be argued with.
Open a pull request.

### Tiers are percentiles, not star thresholds

- **established** — top 5% of its category, pushed within 90 days, 3+ contributors
- **rising** — young, growing fast, actively maintained
- **watch** — everything else

A star floor sounds reasonable and does not survive contact with the data. Of roughly 25,000
repositories tagged `mcp-server`, about 36 clear 10,000 stars, and those are the large frameworks
rather than the specific tool you need on a Tuesday. This ecosystem is around eighteen months old:
10k stars means famous, not proven. Percentile within a category surfaces the leader of a niche as
readily as the leader of a crowded field.

## Freshness

A GitHub Action regenerates the catalog nightly and commits it, so you get current data by updating
the plugin. If the catalog is more than 30 days old, the skill says so instead of pretending.

Categories that break often upstream, social-media scrapers above all, lean harder on last-push
recency. A year-old scraper is usually a dead one no matter how many stars it has.

## Contributing

- **A missing tool?** Add the topic that reaches it to [`config/sources.yaml`](config/sources.yaml).
- **Wrong ranking?** Argue with [`config/scoring.yaml`](config/scoring.yaml).
- **A query that returns the wrong thing?** Add it to `tests/eval/queries.yaml`. That file is the
  regression suite: every case in it is a failure someone actually hit.

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
GITHUB_TOKEN=$(gh auth token) python -m goldmine.crawl --catalog-dir catalog
```

## Licence

MIT
