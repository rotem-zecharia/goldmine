# web-infra-dev/midscene

GUI Agent for E2E Testing

## features

Most UI automation — including AI tools that read the DOM or the accessibility tree — depends on page structure. That structure is fragile and incomplete: selectors break on every refactor, elements without semantic markup (icon-only buttons, custom controls, `<canvas>`) are invisible to it, native apps and cross-origin iframes are out of reach, and it cannot tell whether something actually looks right. Midscene works from the screenshot alone, and you describe each step in natural language:

- **Less maintenance** — no selectors to chase when the UI changes.
- **Reach every element and surface** — if a human can see it, Midscene can target it, even with no semantic annotations, on `<canvas>`, native apps, and cross-origin iframes.
- **Assert what users actually see** — verify colors, highlights, layout, and rendered state, not just whether a DOM node exists.
- **Two ways to test** — add Midscene to your [Playwright](https://midscenejs.com/integrate-with-playwright) / Vitest suite, or let an AI agent test autonomously via [Skills](https://midscenejs.com/skills).

Midscene is built for UI testing first, but the same vision-driven engine handles any UI automation task.
