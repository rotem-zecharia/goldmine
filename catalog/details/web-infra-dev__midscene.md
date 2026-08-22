# web-infra-dev/midscene

GUI Agent for E2E Testing

## features

Most UI automation — including AI tools that read the DOM or the accessibility tree — depends on page structure. That structure is fragile and incomplete: selectors break on every refactor, elements without semantic markup (icon-only buttons, custom controls, `<canvas>`) are invisible to it, native apps and cross-origin iframes are out of reach, and it cannot tell whether something actually looks right. Midscene works from the screenshot alone, and you describe each step in natural language:

- **Less maintenance** — no selectors to chase when the UI changes.
- **Reach every element and surface** — if a human can see it, Midscene can target it, even with no semantic annotations, on `<canvas>`, native apps, and cross-origin iframes.
- **Assert what users actually see** — verify colors, highlights, layout, and rendered state, not just whether a DOM node exists.
- **Two ways to test** — add Midscene to your [Playwright](https://midscenejs.com/integrate-with-playwright) / Vitest suite, or let an AI agent test autonomously via [Skills](https://midscenejs.com/skills).

Midscene is built for UI testing first, but the same vision-driven engine handles any UI automation task.

## 💡 What you can automate

Midscene works anywhere you can take a screenshot — web browsers, Android, iOS, HarmonyOS, desktop apps, and [any custom interface](https://midscenejs.com/integrate-with-any-interface) — all through one API. Write automation with the JavaScript SDK or in YAML, hand it to AI agents via [Skills](https://midscenejs.com/skills), and look up every method (`aiAct`, `aiQuery`, `aiAssert`, and more) in the [API reference](https://midscenejs.com/reference/#common).

## 🚀 Get started

- **Try Midscene in Chrome** — use the [Quick start](https://midscenejs.com/quick-start) to configure a model, install the Chrome extension, and run your first natural-language instruction.
- **Write your first script** — create an Agent and run a complete browser script with [Playwright](https://midscenejs.com/integrate-with-playwright) or [Puppeteer](https://midscenejs.com/integrate-with-puppeteer).
- **Other platforms** — getting-started guides for [Android](https://midscenejs.com/platforms/android), [iOS](https://midscenejs.com/platforms/ios), [HarmonyOS](https://midscenejs.com/platforms/harmonyos), and [desktop](https://midscenejs.com/platforms/desktop).

## ✨ Driven by Multimodal Models

Midscene is all-in on pure vision for UI actions: element localization is based on screenshots only. It runs on multimodal models with strong UI localization, such as `Qwen3.x`, `Doubao-Seed-2.1`, `GLM-4.6V`, `gemini-3.5-flash`, and `UI-TARS`, including open-source options you can self-host. For data extraction and page understanding, you can still opt in to include DOM when needed.

Read more about [Model Strategy](https://midscenejs.com/model-strategy).



## 📄 Resources

* Documentation: [https://midscenejs.com](https://midscenejs.com/)
* Sample projects: [midscene-example](https://github.com/web-infra-dev/midscene-example)
* API reference: [https://midscenejs.com/reference/#common](https://midscenejs.com/reference/#common)

## 🤝 Community

* [Discord](https://discord.gg/2JyBHxszE4)
* [Follow us on X](https://x.com/midscene_ai)
* [Lark Group (飞书交流群)](https://applink.larkoffice.com/client/chat/chatter/add_by_link?link_token=693v0991-a6bb-4b44-b2e1-365ca0d199ba)

## 🌟 Awesome Midscene

Community projects that extend Midscene.js capabilities:

* [midscene-ios](https://github.com/lhuanyu/midscene-ios) - iOS Mirror automation support for Midscene
* [midscene-pc](https://github.com/Mofangbao/midscene-pc) - PC operation device for Windows, macOS, and Linux
* [midscene-pc-docker](https://github.com/Mofangbao/midscene-pc-docker) - Docker image with Midscene-PC server pre-installed
* [Midscene-Python](https://github.com/Python51888/Midscene-Python) - Python SDK for Midscene automation
* [midscene-java](https://github.com/Master-Frank/midscene-java) by @Master-Frank - Java SDK for Mi
