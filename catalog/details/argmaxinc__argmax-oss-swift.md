# argmaxinc/argmax-oss-swift

On-device Speech AI for Apple Silicon

## requirements

- macOS 14.0 or later.
- Xcode 16.0 or later.

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

## limitations

Our goal is to make this SDK better and better over time and we'd love your help! Just search the code for "TODO" for a variety of features that are yet to be built. Please refer to our [contribution guidelines](CONTRIBUTING.md) for submitting issues, pull requests, and coding standards, where we also have a public roadmap of features we are looking forward to building in the future.

**External dependencies:** `Sources/ArgmaxCore/External/` contains a copy of [swift-transformers](https://github.com/huggingface/swift-transformers) (Hub and Tokenizers modules, v1.1.6) with Jinja-dependent code removed. When updating to a newer version, copy the fresh sources over that directory and re-apply the patches marked with `// Argmax-modification:` (`grep -r "Argmax-modification:" Sources/ArgmaxCore/External/`). The matching upstream tests are vendored under `Tests/ArgmaxCoreTests/External/` using the same convention.
