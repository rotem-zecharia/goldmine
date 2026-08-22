# OpenWhispr/openwhispr

Voice-to-text dictation app with local (Nvidia Parakeet/Whisper) and cloud models (BYOK). Privacy-first and available cross-platform.

## features

- **Voice dictation** — global hotkey to dictate into any app with automatic pasting
- **Dictation translation** — dedicated hotkey to dictate in one language and paste the text in another
- **AI agent** — talk to GPT-5, Claude, Gemini, Groq, Tinfoil, OpenRouter, or local models with a named voice assistant
- **Voice Assistant hotkey** — dedicated hotkey that sends what you say straight to your AI assistant as a command, no wake word needed and no cleanup pass; the answer streams into a floating assistant panel, highlighted text is edited in place, and you can opt in to sending a screenshot of your current screen as context
- **Meeting transcription** — auto-detect Zoom, Teams, and FaceTime calls with live speaker diarization, voice fingerprinting, and Google, Microsoft, or Apple Calendar integration
- **Local speaker diarization** — on-device speaker labelling with voice fingerprint recognition across meetings, no cloud required
- **Notes** — create, organize, and search notes with folders, semantic search, cloud sync, and AI actions
- **Team spaces & sharing** — free for signed-in users; share notes on the web with link, domain, or invite-only visibility, and collaborate in team spaces with roles, invitations, and server-enforced membership
- **Audio import** — transcribe existing audio and video: drag in files, batch-upload, or paste a YouTube/audio URL, with optional speaker detection
- **Local or cloud — your choice** — all core features (transcription, AI reasoning, speaker diarization, semantic search) work with local models or cloud providers — including GPU-accelerated local Whisper on Metal, CUDA, and Vulkan (AMD/Intel)
- **Enterprise controls** — enforce organization policy, company SSO and SCIM, and centrally managed Amazon Bedrock or Azure OpenAI access without distributing cloud keys
- **Public API & MCP** — manage notes and transcriptions programmatically or connect your AI assistant via the [MCP server](https://docs.openwhispr.com/integrations/mcp)

## installation

```bash
git clone https://github.com/OpenWhispr/openwhispr.git
cd openwhispr
npm install
npm run dev
```

Requires Node.js 24+. See the [full documentation](https://docs.openwhispr.com/quickstart) for setup guides, platform-specific instructions, and build details.
