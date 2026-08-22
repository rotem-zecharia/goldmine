# dembrandt/dembrandt

Extract any website’s design system into tokens in seconds: logo, colors, typography, borders & more. One command.

## installation

```bash
npm install -g dembrandt
dembrandt install-browser        # one-time: fetches the matching Chromium
dembrandt dembrandt.com
```

The browser step is required. dembrandt drives Chromium through `playwright-core`,
which ships no browser binaries, so a fresh install has nothing to launch until you
run it. Skipping it fails with `browser engine not available`.

Or use npx without installing: `npx dembrandt dembrandt.com`. The browser step applies
here too: run `npx dembrandt install-browser` first. Browsers land in a shared
Playwright cache, so either route only needs it once.

Requires Node.js 18+

## limitations

- Dark mode requires `--dark-mode` flag (not automatically detected)
- Hover/focus states extracted from CSS (not fully interactive)
- Canvas/WebGL-rendered sites cannot be analyzed (no DOM to read)
- JavaScript-heavy sites require hydration time (8s initial + 4s stabilization)
- Some dynamically-loaded content may be missed
- Default viewport is 1920x1080 (use `--mobile` for 390x844 mobile viewport)
