# skalesapp/skales

Personal AI desktop agent for Windows, macOS, Linux, Android & iOS. Set a goal, it works on its own. Teams (pair two desktops, agents + humans), Agent2Agent, Workflows, Codework, multi-agent orgs, des

## features

Skales is an AI agent that lives on your desktop. Not in a browser tab, not behind a restrictive API, not in a complex Docker container. It sits on your machine, has access to your files, your browser, your calendar, your email, and it does real work.

| | Typical AI Agents | Skales 🦎 |
|---|---|---|
| **Setup** | Docker, Terminal, Python CLI | Download EXE/DMG/AppImage, double-click |
| **RAM Usage** | 1.5GB - 3GB+ | ~300MB |
| **OS Support** | Linux / Docker required | Windows + macOS + Linux native |
| **Time to first task** | Hours to days | 30 seconds |
| **Privacy** | Cloud only | Local-first, BYOK, offline capable |
| **Updates** | Manual Git pull and rebuild | One-click auto-updater |
| **Security** | Unsigned scripts | Apple Developer ID signed (Windows signing coming) |
| **Emoji** | Platform-dependent | Consistent Noto emojis + animated brand emojis |
| **Migration** | Start from scratch | Import from ChatGPT, Claude, OpenClaw, Hermes |

*A 6-year-old built a game with it. A grandmother approved the setup.*

---

## 🚪 The ten places Skales lives

One sidebar, one list, and every entry is somewhere you actually work. Everything else Skales can do is something you **ask** it to do, from a conversation.

### 💬 Chat

The front door. Ask a question, or hand over a task and let it run.

- **`/goal` turns a request into ongoing work.** It plans the steps and runs them on its own, in the background, with the app closed. It does not ask you to continue: it stops when the task is done, when it genuinely needs a decision, or before a consequential action like sending an email, where it asks once with a one-tap always-allow. Reopen the app and it picks up where it left off. A goal is only finished when its own success criteria are met, and what it learned folds back into Memory. Run several at once, or put one on a repeating schedule.
- **`/code` binds a folder to this conversation,** without leaving it. Four modes under the composer: **Plan** investigates and proposes, **Code** asks before each edit, **Edits** approves file edits as it goes but still asks before a shell command or a push, **Auto** runs the whole task after a one-time consent. Inline git diffs with an added/removed count, a repo map so it heads straight to the right file in a large codebase, `@` to point at a file by name, and one-click Undo per file or for a whole turn. It commits and pushes with **your own git identity**, no added attribution.
- **`/spin` writes a text again in a plainer voice.** `/spin <text>` rewrites what you hand it, `/spin` on its own rewrites the last answer, and the same action sits in the message menu next to Copy. Select part of a reply and right click the selection to rewrite just that passage, with copy, quote, read aloud and save-to-document beside it. It runs on a model you pick for the job, and a local one keeps the text on your machine.
- **`/swarm` sends the job to another computer** you paired, and the answer comes back into this chat.
- **The sidebar becomes the chat's own navigation** while you are in a conversation: New chat, Agents, Cockpit, and a More group with History, Projects, Teams, Group Chat, Organization, and Add-Ons and Skills.
- **HTML the model writes renders live** in a sandboxed frame right in the conversation, with Show Code, Download, Save as Image, and a mute that silences every preview in every chat at once. A block tagged `html`, `htm`, `svg`, `xhtml` or `html5`, or one that simply opens with a document, all count; `text` and `xml` never do, so markup you asked for as source stays source.
- **Diagrams, formulas and coloured code.** A ```` ```mermaid ```` block is drawn as a diagram (flowchart, sequence, state, ER, gantt, pie, xychart) in your accent and your theme, and downloads as SVG. Maths in `$$` is typeset. Every code block is syntax-coloured with a copy button. Skales knows it can do all of this, in every mode, so asking for a diagram gets you one instead of a paragraph describing it.
- **Voice wo

## installation

**[Download here](https://skales.app)**

> 🍏 **macOS:** signed DMG. Drag to Applications.

> 🪟 **Windows:** EXE installer. Signed binaries coming soon.

> 🐧 **Linux:** `.deb` for Debian / Ubuntu / Mint (keeps the Chromium sandbox on under Ubuntu 24.04+), AppImage for everything else. See [INSTALL-LINUX.md](./INSTALL-LINUX.md) for the Ubuntu 24.04+ AppArmor notes.

> 📱 **Android + iOS:** Skales Mobile. Pair to your desktop via QR, or run standalone. Live on [Google Play](https://play.google.com/store/apps/details?id=app.skales.mobile) and the [App Store](https://apps.apple.com/us/app/skales/id6763328966).

> 🔄 **Switching tools?** Import from ChatGPT, Claude, Copilot, Gemini, OpenClaw, Hermes. Settings > Import.

---

## 🏗️ Architecture

| Layer | Technology |
|---|---|
| **Shell** | Electron |
| **Frontend** | Next.js (App Router), Tailwind CSS, TypeScript |
| **Storage** | `~/.skales-data` (JSON + SQLite) |
| **AI** | ReAct agent loop, 180+ tools, multi-agent delegation, per-turn tool budgeting |
| **Relay** | End-to-end encrypted relay for Mobile ↔ Desktop pairing |

---

## 🤝 Community

12 languages: EN, DE, ES, FR, RU, PT, KO, ZH, JA, VI, HR, TR.

**Maintainer:** Mario Simic (solo founder, Vienna, Austria).

**Contributors:**

<p align="left">
  <a href="https://github.com/jazzroutine"><img src="https://github.com/jazzroutine.png" width="56" height="56" alt="jazzroutine" style="border-radius:50%" /></a>
  <a href="https://github.com/xITmasterx"><img src="https://github.com/xITmasterx.png" width="56" height="56" alt="xITmasterx" style="border-radius:50%" /></a>
  <a href="https://github.com/btafoya"><img src="https://github.com/btafoya.png" width="56" height="56" alt="btafoya" style="border-radius:50%" /></a>
  <a href="https://github.com/bmp-jaller"><img src="https://github.com/bmp-jaller.png" width="56" height="56" alt="bmp-jaller" style="border-radius:50%" /></a>
  <a href="https://github.com/henk717"><img src="https://github.com/henk717.png" width="56" height="56" alt="henk717" style="border-radius:50%" /></a>
  <a href="https://github.com/SohaibKhaliq"><img src="https://github.com/SohaibKhaliq.png" width="56" height="56" alt="SohaibKhaliq" style="border-radius:50%" /></a>
  <a href="https://github.com/VladB-evs"><img src="https://github.com/VladB-evs.png" width="56" height="56" alt="VladB-evs" style="border-radius:50%" /></a>
  <a href="https://github.com/v33-kind"><img src="https://github.com/v33-kind.png" width="56" height="56" alt="v33-kind" style="border-radius:50%" /></a>
  <a href="https://github.com/sidharth-vijayan"><img src="https://github.com/sidharth-vijayan.png" width="56" height="56" alt="sidharth-vijayan" style="border-radius:50%" /></a>
  <a href="https://github.com/saagnik23"><img src="https://github.com/saagnik23.png" width="56" height="56" alt="saagnik23" style="border-radius:50%" /></a>
  <a href="https://github.com/Drizzt-IT"><img src="https://github.com/Drizzt-IT.png" width="56" height="56" alt="Drizzt-IT" style="border-radius:50%" /></a>
  <a href="https://github.com/Kombowz"><img src="https://github.com/Kombowz.png" width="56" height="56" alt="Kombowz" style="border-radius:50%" /></a>
  <a href="https://github.com/anthonytrance"><img src="https://github.com/anthonytrance.png" width="56" height="56" alt="anthonytrance" style="border-radius:50%" /></a>
  <a href="https://github.com/karelrokk-droid"><img src="https://github.com/karelrokk-droid.png" width="56" height="56" alt="karelrokk-droid" style="border-radius:50%" /></a>
  <a href="https://github.com/mclaudiopt"><img src="https://github.com/mclaudiopt.png" width="56" height="56" alt="mclaudiopt" style="border-radius:50%" /></a>
  <a href="https://github.com/1Hackoon"><img src="https://github.com/1Hackoon.png" width="56" height="56" alt="1Hackoon" style="border-radius:50%" /></a>
  <a href="https://github.com/tbaumann"><img src="https://github.com/tbaumann.png" width="56" height="56" alt="tbaumann" style="border-radius:50%" /></a>
  <a href="http
