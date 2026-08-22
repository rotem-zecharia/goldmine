# mahimairaja/voiceai

Set of 📝 with 🔗 to help those building Voice AI agents 🎙️🤖

## tools

- 🟡 [OpenAI Realtime API: Guide](https://developers.openai.com/api/docs/guides/realtime): Official guide to `gpt-realtime-2` (GA; GPT-5-class with configurable reasoning) over WebRTC, WebSockets, or SIP.
- 🟡 [Google Gemini Live API: Overview](https://ai.google.dev/gemini-api/docs/live-api): Low-latency, bidirectional voice + vision agents with barge-in and tool use, on Gemini native audio.
- 🟡 [Twilio ConversationRelay](https://www.twilio.com/docs/voice/conversationrelay): WebSocket bridge that handles STT/TTS so you focus on LLM logic; works with any LLM.
### Vendor-neutral comparisons

- 🟡 [Vapi vs Pipecat vs LiveKit (AssemblyAI)](https://www.assemblyai.com/blog/vapi-vs-pipecat-vs-livekit): Architecture-focused comparison of pipeline control and transport choices.
- 🟢 [11 Voice Agent Platforms Compared (Softcery)](https://softcery.com/lab/choosing-the-right-voice-agent-platform-in-2025): Broad market map with use-case recommendations.
- 🟡 [Best Voice Agent Stack (Hamming AI)](https://hamming.ai/resources/best-voice-agent-stack): Buy-vs-build framework with concrete cost, latency, and time-to-launch numbers.

</details>

## 🎧 3. Speech-to-text (STT / ASR)

Pick **one streaming STT** and learn it deeply before shopping around. Deepgram, AssemblyAI, and Whisper-derivatives cover most use cases. (All-in-one ASR + end-of-turn models like Deepgram Flux are covered under [turn-taking](#-6-voice-activity-detection-and-turn-taking).)

| Pick | Type | Best for |
|------|------|----------|
| **Deepgram Nova-3** | Commercial | General-purpose, 36+ languages |
| **AssemblyAI Universal-3 Pro** | Commercial | Accuracy, diarization |
| **Soniox** | Commercial | Multilingual + built-in translation |
| **faster-whisper** | Open source | Self-hosted Whisper |
| **NVIDIA Parakeet (NeMo)** | Open source | Top-of-leaderboard accuracy |

<details>
<summary><b>20 resources</b></summary>

### Commercial APIs

- 🟢 [Deepgram Nova-3: STT benchmarks](https://deepgram.com/learn/speech-to-text-benchmarks): Primer on WER, latency, and cost alongside Deepgram's product reference; Nova-3 spans 36+ languages with multilingual code-switching.
- 🟡 [AssemblyAI Universal-3 Pro Streaming](https://www.assemblyai.com/blog/build-voice-agent-function-calling): Streaming STT walkthrough that doubles as a function-calling tutorial; Universal-3 Pro Streaming is the current real-time flagship, adding real-time diarization and keyterm prompting.
- 🟢 [OpenAI Whisper / gpt-4o-transcribe API docs](https://developers.openai.com/api/docs/guides/speech-to-text): Easiest cloud STT if you already use OpenAI.
- 🟢 [Cartesia Ink 2](https://docs.cartesia.ai/build-with-cartesia/stt/latest): GA streaming STT with built-in eager turn detection and noise robustness, paired with Sonic TTS for a single-vendor low-latency stack.
- 🟢 [Soniox Speech-to-Text](https://soniox.com/docs/stt/get-started): One model spanning 60+ languages with real-time WebSocket streaming and async APIs, speaker diarization, language identification, endpoint detection, and built-in real-time speech translation (one-way or two-way).
- 🟡 [Speechmatics Melia](https://www.speechmatics.com/company/articles-and-news/introducing-melia-multilingual-speech-to-text-model): Single-pass multilingual STT with native code-switching across 56+ languages.
- 🟡 [Gladia Solaria-3](https://www.gladia.io/blog/solaria-3-speech-to-text-model-for-european-languages): STT tuned for noisy, multi-speaker European business audio (9.6% WER on English production calls).
- 🟢 [Gradium STT](https://docs.gradium.ai/guides/speech-to-text): Streaming STT with built-in semantic VAD; step messages every 80 ms carry end-of-turn probabilities so agents can decide when a speaker has finished.
### Open source

- 🟢 [openai/whisper](https://github.com/openai/whisper): The original repo and the de facto starting point for any DIY ASR project.
- 🟡 [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper): CTranslate2 reimplementation up to 4× faster w
