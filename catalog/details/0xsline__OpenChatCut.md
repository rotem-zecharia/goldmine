# 0xsline/OpenChatCut

Open-source, local-first conversational AI video editor with a professional multi-track timeline, Agent Skills, MCP integration, and Remotion rendering.

## features

Traditional editors excel at precise control. One-shot AI video generators excel at producing results quickly. OpenChatCut connects both approaches through one continuously editable project:

| Capability | Traditional timeline editor | One-shot AI video generation | **OpenChatCut** |
|---|:---:|:---:|:---:|
| Track- and clip-level precision | ✅ | ❌ | **✅** |
| Modify a project with natural language | ❌ | ✅ | **✅** |
| Inspectable and undoable changes | ✅ | Usually unavailable | **✅** |
| Linked transcript and visuals | Partial | ❌ | **✅** |
| Direct control from Codex / Claude Code | ❌ | ❌ | **✅ MCP** |
| Built-in and external agent collaboration | ❌ | ❌ | **✅ Shared tools** |
| Local projects and BYOK | Product-dependent | Usually cloud-based | **✅** |

The core editing loop:

```text
Describe the goal → Agent reads the project → Produces verifiable edits → Writes to the timeline
                  → Preview / adjust / undo → Captions and mixing → Export
```

---

## Core Capabilities

| Area | Implemented capabilities |
|---|---|
| Timeline | Multitrack editing, move, trim, split, ripple edits, snapping, keyframes, markers, undo, and redo |
| Visuals | WebGL effects, LUTs, chroma key, zoom, transitions, and custom shaders |
| Audio | Multiple audio tracks, sound effects, background music, voice-over recording, loudness, auto-ducking, and vocal isolation |
| Transcript | Transcription jobs, word-level editing, pause compression, search, speakers, and clip views |
| Captions | Automatic captions, named styles, translation, timeline overlays, and SRT export |
| Motion Graphics | Built-in templates, a secure sandbox, custom templates, and video rendering |
| AI generation | Image, video, speech, music, and sound-effect jobs with progress tracking |
| Media | Uploads, folders, online image/video/audio search, and Firecrawl visual-media fallback |
| Export | MP4, audio, captions, FCPXML, project import/export, export history, hardware-aware H.264 acceleration, and resource-aware export queueing |
| Agent | Built-in conversational agent, skills, proposal-based edits, and external Streamable HTTP MCP |

---

## Community Resources

The [OpenChatCut resource library](https://openchatcut.com/resources) is a shared catalog for reusable MG animations, sound effects, transitions, visual effects, zooms, and LUTs.

<p align="center">
  <a href="https://openchatcut.com/resources">
    <img src="assets/readme-pic/08-community-resources.en.png" alt="OpenChatCut community resource library" />
  </a>
</p>

## installation

- Hover visual cards to watch the complete result, or play audio resources before downloading.
- Copy a resource's install URL into OpenChatCut's Extension Center, or download its original package.
- Browse the website catalog inside the editor and manage installed extensions locally.

### Contribute a resource

1. Open [Contribute a resource](https://openchatcut.com/resources/submit) and choose its category.
2. Upload the resource and the category-specific preview inputs; the site renders the published preview.
3. Add the creator and license information, then submit it for review and publication.

Installable visual resources use the editor's `openchatcut-plugin@1` format and runtime validation. Official OpenChatCut resources use the MIT license; community contributors select a license during submission, and each published card identifies its creator and license.

---

## Use Cases

- **Talking-head and interview editing**: transcribe audio or video, remove mistakes, pauses, and repetition through text, then generate captions automatically.
- **Fast multiformat assembly**: import video, images, and audio, then let an agent create the rough cut, transitions, soundtrack, and pacing.
- **Short-form and social content**: reframe the canvas and generate titles, captions, voice-over, music, and visual packaging.
- **Motion Graphics**: use built-in templates or ask an agent to create editable motion-graphics clips.
- **Developer automation**: use MCP to let Codex, Claude Code, or another compatible client inspect and modify a real project.

## Workflow

1. Create a project and import local media.
2. Edit manually on the timeline or describe the result you want.
3. The agent reads project context and invokes editing tools.
4. Review the proposal and preview the result, then apply, adjust, or undo it.
5. Finish captions, audio, effects, and color.
6. Export video, audio, captions, FCPXML, or the complete project.

---

## Quick Start

### Desktop installers

Download the latest macOS, Windows, and Linux builds from [GitHub Releases](https://github.com/0xsline/OpenChatCut/releases/latest). The release currently includes DMG installers for Apple Silicon and Intel Macs, an x64 Windows installer, and an x64 Linux AppImage.

These are early builds. The macOS packages are not yet signed or notarized, so the operating system may require manual approval on first launch.

### Run from source

Requires Node.js 24.x and npm. The supported Node.js range is enforced by `package.json`, and `.nvmrc` selects the matching major version for Node version managers.

```bash
git clone https://github.com/0xsline/OpenChatCut.git
cd OpenChatCut
npm install
cp .env.example .env.local
npm run dev
```

Open:

```text
http://localhost:5199
```

Only add the model or media-service credentials you actually use to `.env.local`. Features without configured third-party credentials report the missing key explicitly; local timeline editing, built-in media, and other configured capabilities continue to work.

Development launches are isolated per Git checkout/worktree by default. `npm run dev` and
`npm run desktop:dev` keep that checkout's projects, imported media, generation jobs,
credentials, settings, and local authorization state under its own profile in
`~/.openchatcut/dev-profiles/`. Use `npm run dev:shared` only when you intentionally need
the legacy shared development store.

### Built-in Agent authentication

- **API keys:** open **Settings → Agent model**, choose a provider, and save its API key and model. Keys remain server-side.
- **ChatGPT subscription:** install the official Codex CLI 0.146.0 or newer, then open **Settings → Agent model → OpenAI · Codex**. Sign in through the browser or device-code flow, load the account's models, choose a model-specific reasoning effort (or keep its default), and select Codex from the chat model picker. OpenChatCut uses a dedicated Codex profile; the official CLI owns credential storage, token renewal, and logout, while O
