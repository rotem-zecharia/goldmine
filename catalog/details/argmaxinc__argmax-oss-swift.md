# argmaxinc/argmax-oss-swift

On-device Speech AI for Apple Silicon

## installation

### Swift Package Manager

WhisperKit, TTSKit, and SpeakerKit are separate library products in the same Swift package. Add the package once and pick the products you need. You can also use the `ArgmaxOSS` umbrella product to import everything at once.

## requirements

- macOS 14.0 or later.
- Xcode 16.0 or later.

### Xcode Steps

1. Open your Swift project in Xcode.
2. Navigate to `File` > `Add Package Dependencies...`.
3. Enter the package repository URL: `https://github.com/argmaxinc/argmax-oss-swift`.
4. Choose the version range or specific version.
5. When prompted to choose library products, select **ArgmaxOSS** (all kits), or individual kits: **WhisperKit**, **TTSKit**, **SpeakerKit**.

### Package.swift

Add the package dependency:

```swift
dependencies: [
    .package(url: "https://github.com/argmaxinc/argmax-oss-swift.git", from: "0.9.0"),
],
```

Then add the products you need as target dependencies:

```swift
.target(
    name: "YourApp",
    dependencies: [
        // Import everything at once:
        .product(name: "ArgmaxOSS", package: "argmax-oss-swift"),

        // Or pick individual kits:
        // .product(name: "WhisperKit", package: "argmax-oss-swift"),   // speech-to-text
        // .product(name: "TTSKit", package: "argmax-oss-swift"),       // text-to-speech
        // .product(name: "SpeakerKit", package: "argmax-oss-swift"),   // speaker diarization
    ]
),
```

### Homebrew

You can install the command line app using [Homebrew](https://brew.sh) by running the following command:

```bash
brew install whisperkit-cli
```  

## WhisperKit

To get started with WhisperKit, you need to initialize it in your project.

### Quick Example

This example demonstrates how to transcribe a local audio file:

```swift
import WhisperKit

// Initialize WhisperKit with default settings
Task {
    let pipe = try? await WhisperKit()
    let results = try? await pipe?.transcribe(audioPath: "path/to/your/audio.{wav,mp3,m4a,flac}")
    let transcription = results?.map(\.text).joined(separator: " ")
    print(transcription ?? "")
}
```

### Memory-Efficient Loading for Large Files

By default WhisperKit loads the whole audio file into memory before transcribing. For long recordings, `.incremental` streams it from disk in bounded-memory chunks instead:

```swift
import WhisperKit

let pipe = try await WhisperKit()

let options = AudioInputOptions(audioLoadingMode: .incremental)
let results = try await pipe.transcribe(
    audioPath: "path/to/large-audio.wav",
    audioInputOptions: options
)
print(results.map(\.text).joined(separator: " "))
```

It splits the audio at silence (VAD) boundaries, so the result matches a full-file transcription run with `chunkingStrategy: .vad` — only peak memory differs. Tune the chunking with `.incremental(chunkDuration:chunkBufferSize:)`, or pick channels with `AudioInputOptions(channelMode:)`.

From the CLI, add `--incremental-loading` (optionally `--incremental-chunk-duration` / `--incremental-chunk-buffer-size`):

```bash
swift run argmax-cli transcribe --model large-v3-v20240930_626MB --audio-path "path/to/large-audio.wav" --incremental-loading
```

### Model Selection

> [!NOTE]
> Argmax recommends `large-v3-v20240930_626MB` for maximum multilingual accuracy and `tiny` for the fastest debugging workflow.

| Whisper Version                  | WhisperKit Variant                                                                                                 | Description                                                                      |
|----------------------------------|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Large v3 Turbo (compressed)      | [large-v3-v20240930_626MB](https://huggingface.co/argmaxinc/whisperkit-coreml/tree/main/openai_whisper-large-v3-v20240930_626MB) | Recommended across iOS and macOS for maximum accuracy                            |
| Large v3 Turbo                   | [large-v3-v20240930_turbo](https://huggingface.co/argmaxinc/whisperkit-coreml/tree/main/openai_whisper-large-v3-v20240930_turbo) | Recommended on macOS for maximum speed and accuracy                   

## configuration

BUILD_ALL=1 swift run argmax-cli serve --help
```

#### API Endpoints

- **POST** `/v1/audio/transcriptions` - Transcribe audio to text
- **POST** `/v1/audio/translations` - Translate audio to English

#### Supported Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `file` | Audio file (wav, mp3, m4a, flac) | Required |
| `model` | Model identifier | Server default |
| `language` | Source language code | Auto-detect |
| `prompt` | Text to guide transcription | None |
| `response_format` | Output format (json, verbose_json) | verbose_json |
| `temperature` | Sampling temperature (0.0-1.0) | 0.0 |
| `timestamp_granularities[]` | Timing detail (word, segment) | segment |
| `stream` | Enable streaming | false |

#### Client Examples

**Python Client (OpenAI SDK)**
```bash
cd Examples/ServeCLIClient/Python
uv sync
python whisperkit_client.py transcribe --file audio.wav --language en
python whisperkit_client.py translate --file audio.wav
```

Quick Python example:
```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:50060/v1")
result = client.audio.transcriptions.create(
    file=open("audio.wav", "rb"),
    model="tiny"  # Model parameter is required
)
print(result.text)
```

**Swift Client (Generated from OpenAPI Spec, see ServeCLIClient/Swift/updateClient.sh)**
```bash
cd Examples/ServeCLIClient/Swift
swift run whisperkit-client transcribe audio.wav --language en
swift run whisperkit-client translate audio.wav
```

**CurlClient (Shell Scripts)**
```bash
cd Examples/ServeCLIClient/Curl
chmod +x *.sh
./transcribe.sh audio.wav --language en
./translate.sh audio.wav --language es
./test.sh  # Run comprehensive test suite
```

#### Generating the API Specification

The server's OpenAPI specification and code are generated from the official OpenAI API:

```bash
# Generate latest spec and server code
make generate-server
```

#### Client Generation

You can generate clients for any language using the OpenAPI specification, for example:

```bash
# Generate Python client
swift run swift-openapi-generator generate scripts/specs/localserver_openapi.yaml \
  --output-directory python-client \
  --mode client \
  --mode types

# Generate TypeScript client
npx @openapitools/openapi-generator-cli generate \
  -i scripts/specs/localserver_openapi.yaml \
  -g typescript-fetch \
  -o typescript-client
```

#### API Limitations

Compared to the official OpenAI API, the local server has these limitations:

- **Response formats**: Only `json` and `verbose_json` supported (no plain text, SRT, VTT formats)
- **Model selection**: Client must launch server with desired model via `--model` flag

#### Fully Supported Features

The local server fully supports these OpenAI API features:

- **Include parameters**: `logprobs` parameter for detailed token-level log probabilities
- **Streaming responses**: Server-Sent Events (SSE) for real-time transcription
- **Timestamp granularities**: Both `word` and `segment` level timing
- **Language detection**: Automatic language detection or manual specification
- **Temperature control**: Sampling temperature for transcription randomness
- **Prompt text**: Text guidance for transcription style and context

## TTSKit

TTSKit is an on-device text-to-speech framework built on Core ML. It runs [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) models entirely on Apple silicon with real-time streaming playback, no server required.

- macOS 15.0 or later.
- iOS 18.0 or later.

### Quick Example

This example demonstrates how to generate speech from text:

```swift
import TTSKit

Task {
    let tts = try await TTSKit()
    let result = try await tts.generate(text: "Hello from TTSKit!")
    print("Generated \(result.audioDuration)s of audio at \(result.sampleRate)Hz")
}
```

`TTSKit()` automatically downloads the default 0.6B model on first run. The tokenizer and CoreML models are loaded lazily on the first `generate()` call.

### Model Selection

TTSKit ships two 

## limitations

Our goal is to make this SDK better and better over time and we'd love your help! Just search the code for "TODO" for a variety of features that are yet to be built. Please refer to our [contribution guidelines](CONTRIBUTING.md) for submitting issues, pull requests, and coding standards, where we also have a public roadmap of features we are looking forward to building in the future.

**External dependencies:** `Sources/ArgmaxCore/External/` contains a copy of [swift-transformers](https://github.com/huggingface/swift-transformers) (Hub and Tokenizers modules, v1.1.6) with Jinja-dependent code removed. When updating to a newer version, copy the fresh sources over that directory and re-apply the patches marked with `// Argmax-modification:` (`grep -r "Argmax-modification:" Sources/ArgmaxCore/External/`). The matching upstream tests are vendored under `Tests/ArgmaxCoreTests/External/` using the same convention.

## License

Argmax OSS is released under the MIT License. See [LICENSE](LICENSE) for more details.

This project incorporates third-party software under their own license terms. See [NOTICES](NOTICES) for attributions.

## Citation

If you use this SDK for something cool or just find it useful, please drop us a note at [info@argmaxinc.com](mailto:info@argmaxinc.com)!

If you use WhisperKit, SpeakerKit or TTSKit for academic work, please cite the project using the following BibTeX:

```bibtex
@misc{whisperkit-argmax,
   title = {Argmax OSS: On-device Speech AI with WhisperKit, SpeakerKit and TTSKit},
   author = {Argmax, Inc.},
   year = {2024},
   URL = {https://github.com/argmaxinc/argmax-oss-swift}
}
```
