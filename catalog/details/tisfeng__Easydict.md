# tisfeng/Easydict

一个简洁优雅的词典翻译 macOS App。开箱即用，支持离线 OCR 识别，支持有道词典，🍎 苹果系统词典，🍎 苹果系统翻译，OpenAI，Gemini，DeepL，Google，Bing，腾讯，百度，阿里，小牛，彩云和火山翻译。A concise and elegant Dictionary and Translator macOS App for looking up words and t

## features

- 🚀 Out of the box, automatic language recognition
- 🖱️ Auto select with mouse and shortcut key
- 📸 OCR screenshot translation and slient screenshot OCR
- 🔊 Multiple TTS voice services
- 📚 Support 🍎 [Apple System Dictionary](./docs/user-docs/en/How-to-use-macOS-system-dictionary-in-Easydict.md) and [System Translation](./docs/user-docs/en/How-to-use-macOS-system-translation-in-Easydict.md)
- 🌐 Support 20+ translation services (OpenAI, Gemini, DeepL, Google, Ollama, Groq, etc.)
- 🗣️ Support for 48 languages

**If you like this app, please consider giving it a [Star](https://github.com/tisfeng/Easydict) ⭐️, thanks! (^-^)**

## Contributing

Contributions through issues and pull requests are welcome. Read the Chinese
[contribution guide](./CONTRIBUTING.md) for the development workflow and pull
request requirements.

### AI Coding

We welcome contributions assisted by programming agents such as `Codex` and
`Claude`. Prefer the latest available GPT or Claude model suitable for complex
coding tasks, and carefully review and test the final changes. See the Chinese
[contribution guide](./CONTRIBUTING.md) for the Agent workflow and
review requirements.

## Issue/PR Triage Notes

The maintainer has been quite busy recently and usually only has time to triage issues on weekends. PRs (especially bugfix PRs) are prioritized. Also, due to an overloaded inbox and notifications, some messages may not be seen or replied to promptly. Thanks for your understanding.

## installation

### Homebrew Installation (Recommended)

```bash
brew install --cask easydict
```

### Manual Installation

[Download](https://github.com/tisfeng/Easydict/releases) the latest release.

> [!NOTE]
> Latest version supports macOS 13.0+, for older systems please use [2.7.2](https://github.com/tisfeng/Easydict/releases/tag/2.7.2)

---

## tools

| Ways                      | Description                                                                                                                                  | Preview                                                                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Input Translate           | Press the input translate shortcut key (default `⌥ + A`), enter the text to be translated, and `Enter` key to translate          | ![iShot_2023-01-20_11.28.46-1674185354](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/iShot_2023-01-20_11.28.46-1674185354.gif) |
| Mouse Select Translate    | The query icon is automatically displayed after the word is selected, and the mouse hovers over it to query                                  | ![iShot_2023-01-20_11.01.35-1674183779](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/iShot_2023-01-20_11.01.35-1674183779.gif) |
| Shortcut Select Translate | After selecting the text to be translated, press the shortcut key (default `⌥ + D`)                                                          | ![iShot_2023-01-20_11.24.37-1674185125](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/iShot_2023-01-20_11.24.37-1674185125.gif) |
| Screenshot Translate      | Press the screenshot translate shortcut key (default `⌥ + S`) to capture the area to be translated                                           | ![iShot_2023-01-20_11.26.25-1674185209](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/iShot_2023-01-20_11.26.25-1674185209.gif) |
| Silent Screenshot OCR     | Press the Silent Screenshot shortcut key（default `⌥ + ⇧ + S`）to capture the area, the OCR results will be copied directly to the clipboard | ![屏幕录制 2023-05-20 22 39 11](https://github.com/Jerry23011/Easydict/assets/89069957/c16f3c20-1748-411e-be04-11d8fe0e61af)                     |

---

## Documentation

- 📚 [Public Documentation Index](./docs/user-docs/README.md) - English and Chinese guides
- 📖 [Complete Usage Guide](./docs/user-docs/en/GUIDE.md) - Detailed features, configuration and tips
- 🔧 [Developer Build Guide](./docs/user-docs/en/GUIDE.md#developer-build) - Build and run from source code
- 🍎 [How to use macOS System Dictionary](./docs/user-docs/en/How-to-use-macOS-system-dictionary-in-Easydict.md)
- 🍎 [How to use macOS System Translation](./docs/user-docs/en/How-to-use-macOS-system-translation-in-Easydict.md)
- 🌍 [How to translate Easydict](./docs/user-docs/en/How-to-translate-Easydict.md)

---

## Acknowledgements

- This project was inspired by [saladict](https://github.com/crimx/ext-saladict) and [Bob](https://github.com/ripperhe/Bob), and the initial version was made based on [Bob (GPL-3.0)](https://github.com/1xiaocainiao/Bob). Easydict has made many improvements and optimizations on the original project, and many features and UI are referenced from Bob.
- Screenshot feature is based on [isee15](https://github.com/isee15)'s [Capture-Screen-For-Multi-Screens-On-Mac](https://github.com/isee15/Capture-Screen-For-Multi-Screens-On-Mac), and optimized on this project.
- Select text feature is referenced from [PopClip](https://pilotmoon.com/popclip/).

## Statement

Easydict is licensed under the [GPL-3.0](https://github.com/tisfeng/Easydict/blob/main/LICENSE) open source license, which is for learning and communication only. Anyone can get this product and source code for free. If you believe that your legal rights have been violated, please contact the [author](https://github.com/tisfeng) immediately. You can use the source code freely, but you must attach the corresponding license and copyright.

## Sponsor

Easydict is a free
