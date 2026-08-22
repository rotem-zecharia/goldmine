# nextlevelbuilder/ui-ux-pro-max-skill

An AI skill that provides design intelligence for building professional UI/UX across multiple platforms.

## features

- **79 Searchable UI Styles (50 active)** - Glassmorphism, Claymorphism, Minimalism, Brutalism, Neumorphism, Bento Grid, Dark Mode, AI-Native UI, and more
- **192 Color Palettes** - Industry-specific palettes aligned 1:1 with the 192 product types
- **74 Font Pairings** - Curated typography combinations with Google Fonts imports
- **25 Chart Types** - Recommendations for dashboards and analytics
- **22 Tech Stacks** - React, Next.js, Astro, Vue, Nuxt.js, Nuxt UI, Svelte, SwiftUI, React Native, Flutter, HTML+Tailwind, shadcn/ui, Jetpack Compose, Angular, Laravel, Three.js, JavaFX, WPF, WinUI 3, UWP, Avalonia, Uno Platform
- **119 UX Guidelines** - Best practices, anti-patterns, accessibility rules, resilient text layout, compact labels, and cancellable interactions
- **192 Reasoning Rules** - Industry-specific design system generation (NEW in v2.0)

## installation

npm install -g ui-ux-pro-max-cli

## tools

```bash
uipro versions              # List available versions
uipro update                # Refresh skill files from installed CLI package
uipro update --global       # Refresh global skill files from installed CLI package
uipro init --offline        # Compatibility flag; installs bundled templates
uipro uninstall             # Remove skill (auto-detect platform)
uipro uninstall --ai claude # Remove specific platform
uipro uninstall --global    # Remove from global install
```

## requirements

Python 3.x is required for the search script (standard library only — the scripts install nothing and make no network calls).

Check if Python is installed:

```bash
python3 --version
```

If it is missing, install it yourself from [python.org](https://www.python.org/downloads/) or with your OS package manager (Homebrew, apt, winget). These install steps are for **you, the human user** — AI agents using this skill should never install software on your machine; they are instructed to ask you instead.
