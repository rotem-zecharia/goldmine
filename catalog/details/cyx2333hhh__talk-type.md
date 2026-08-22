# cyx2333hhh/talk-type

macOS AI 语音输入工具，支持中文与中英混合识别、AI 文本整理、上下文格式匹配和本地优先。

## features

- **Live recognition and cleanup**: Shows the live transcript while recording. With AI cleanup enabled, the text updates during recording and the app shows recognition, cleanup, and insertion status after recording ends.
- **Chinese, English, and mixed input**: Choose Chinese or English as the primary recognition language. Mixed Chinese-English recognition is on by default and uses the other language as a second pass.
- **Local Whisper fallback**: Uses local Whisper Small when Apple Speech returns no result.
- **Multiple AI providers**: Supports DeepSeek, Anthropic (Claude), OpenAI, xAI (Grok), Qwen, and Kimi (Moonshot).
- **Context-aware cleanup**: Uses nearby cursor text to handle punctuation, sentence breaks, spacing, and inline insertion.
- **Cross-app input**: Writes into the focused field through macOS Accessibility, or keeps the text on the clipboard when unavailable.
- **Global shortcuts and local history**: Supports `fn` and custom shortcuts; recent input stays on the Mac.

## installation

On first use, grant Microphone, Speech Recognition, and Accessibility permissions in **Settings → Permissions**. In **Settings → Recognition & Cleanup**, choose Chinese or English as the input language; mixed Chinese-English recognition is enabled by default. AI cleanup is optional. On the same page, choose a provider and enter its API key and model ID; settings are stored separately for each provider.
