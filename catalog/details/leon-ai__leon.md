# leon-ai/leon

🧠 Leon is your open-source personal assistant.

## requirements

- [Node.js](https://nodejs.org/) >= 24.0.0
- Supported OSes: Linux, macOS, and Windows

Recommended: manage Node.js with [Volta](https://volta.sh/).

## installation

```sh
# Clone the repository
git clone https://github.com/leon-ai/leon.git

# Go to the project root
cd leon

# Install pnpm
npm install --global pnpm@latest

# Install dependencies
pnpm install
```

### Run Leon

```sh
# Run Leon
pnpm start
```

### Check Your Setup

```sh
# Check the setup went well
pnpm run check
```

By default, Leon runs locally and the app is available on `http://localhost:5366`.

## 🏗️ Architecture Snapshot

At a high level, Leon currently consists of:

- `server/`: the main runtime, routing, memory, context management, HTTP API, and agent/controlled execution
- `app/`: the web application
- `aurora/`: UI components and preview environment
- `skills/`: built-in capabilities, split between `native/` skills and `agent/` skills
- `bridges/`: Node.js and Python bridges plus toolkit definitions and tool runtimes
- `tcp_server/`: Python services used by parts of the runtime stack
- `core/context/`: generated identity and architecture context documents that describe Leon's current behavior

This repository already includes skills and toolkits for areas such as search, productivity, system utilities, media workflows, coding assistance, memory-backed interactions, and voice/audio features.

## 📚 Documentation Status

The new docs for Leon 2.0 are not ready yet.

For now:

- treat this repository as the source of truth for the **2.0 Developer Preview**
- use [`core/context/LEON.md`](./core/context/LEON.md) for Leon's current identity and behavior
- use [`core/context/ARCHITECTURE.md`](./core/context/ARCHITECTURE.md) for the current architecture overview
- expect the public docs site to lag behind the new core until the updated documentation is published

## ❤️ Contributing

We are starting to progressively onboard contributors for the **2.0 Developer Preview**.

If you want to follow the project or express interest in joining that onboarding:

- [2.0 Developer Preview contributor form](https://forms.gle/6PCG2D5rYo1q8tKMA)
- [Roadmap](http://roadmap.getleon.ai)
- [Discord](https://discord.gg/MNQqqKg)
- [GitHub issues](https://github.com/leon-ai/leon/issues)

## features

Leon has been evolving for a long time, but the current 2.0 work is a major transition period.

For a long time, Leon was a smaller assistant project with a simpler architecture. Today, the core is being rebuilt into a much more capable system around tools, memory, context, and agent-style execution. That means a lot of things are still moving, and it makes contribution harder than it will be once the new docs and architecture settle down.

Another important reason is simply time: Leon is still developed largely during spare time. So progress can be uneven, and opening the project more broadly has to be balanced with keeping the direction coherent while the 2.0 Developer Preview is still taking shape.

## 📖 The Story Behind Leon

Leon started in 2017 and has been active since 2019. If you want the longer backstory, read [the story behind Leon](https://blog.getleon.ai/the-story-behind-leon/).

## 🔔 Stay Tuned

- [X / Twitter](https://x.com/grenlouis) is the main place where I share Leon progress updates
- [Newsletter](https://leonai.substack.com/subscribe)
- [Blog](https://blog.getleon.ai)
- [YouTube](https://www.youtube.com/channel/UCW6mk6j6nQUzFYY97r47emQ)

## 👨 Author

**Louis Grenard** ([@grenlouis](https://x.com/grenlouis))

## 👍 Sponsors

You can also contribute by [sponsoring Leon](http://sponsor.getleon.ai).

## Thanks

| ![OpenAI logo.](./.github/assets/thanks/openai-logo-light-mode.svg?v=2#gh-light-mode-only)![OpenAI logo.](./.github/assets/thanks/openai-logo-dark-mode.svg?v=2#gh-dark-mode-only) | ![JetBrains logo.](./.github/assets/thanks/jetbrains-mono-black.svg?v=2#gh-light-mode-only)![JetBrains logo.](./.github/assets/thanks/jetbrains-mono-white.svg?v=2#gh-dark-mode-only) | ![MacStadium logo.](./.github/assets/thanks/macstadium-logo-light-mode.svg?v=2#gh-light-mode-only)![MacStadium logo.](./.github/assets/thanks/macstadium-logo-dark-mode.svg?v=2#gh-dark-mode-only) |
| --- | --- | --- |
| [openai.com/form/codex-for-oss](https://openai.com/form/codex-for-oss/) | [jb.gg/OpenSource](https://jb.gg/OpenSource) | [macstadium.com/company/opensource](https://macstadium.com/company/opensource) |
