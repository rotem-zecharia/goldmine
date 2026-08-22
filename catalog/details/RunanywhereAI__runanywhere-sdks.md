# RunanywhereAI/runanywhere-sdks

Production ready toolkit to run AI locally

## installation

The fastest way to feel it. Install, load, generate, all local:

```bash
pip install runanywhere
```

```python
import runanywhere as ra
from runanywhere import LlmOptions

ra.initialize()
# downloads on first use
print(ra.llm.generate("Explain on-device AI in one sentence.",
                      LlmOptions(model="qwen2.5-0.5b")).text)
```

Prefer a terminal? The same core ships as a CLI:

```bash
brew install runanywhereai/tap/rcli
rcli run qwen3 "Explain on-device AI in one sentence."
```

Building for mobile, web, or desktop? Every platform below speaks the same API.

<details>
<summary><b>Swift</b> (iOS / macOS)</summary>

<br/>

```swift
import RunAnywhere
import LlamaCPPRuntime

// 1. Initialize
LlamaCPP.register()
try RunAnywhere.initialize()

// 2. Load a model
var load = RAModelLoadRequest()
load.modelID = "smollm2-360m"
load.category = .language
load.framework = .llamaCpp
_ = await RunAnywhere.loadModel(load)

// 3. Generate
var req = RALLMGenerateRequest()
req.prompt = "What is the capital of France?"
let result = try await RunAnywhere.generate(req)
print(result.text) // "Paris is the capital of France."
```

Add the MLX backend (`import RunAnywhereMLX; MLX.register()`) for Apple-native LLM, VLM, STT, TTS, and embeddings on Apple silicon.

Install via Swift Package Manager:

```
https://github.com/RunanywhereAI/runanywhere-sdks
```

[Documentation](https://docs.runanywhere.ai/swift/introduction) · [Source](bindings/swift/)

</details>

<details>
<summary><b>Kotlin</b> (Android)</summary>

<br/>

```kotlin
import ai.runanywhere.proto.v1.ModelCategory
import ai.runanywhere.proto.v1.SDKEnvironment
import com.runanywhere.sdk.llm.llamacpp.LlamaCPP
import com.runanywhere.sdk.public.RunAnywhere
import com.runanywhere.sdk.public.extensions.*
import com.runanywhere.sdk.public.types.RAModelInfo
import com.runanywhere.sdk.public.types.RAModelLoadRequest

// 1. Initialize (in a coroutine scope)
LlamaCPP.register()
RunAnywhere.initialize(
    context = this,
    environment = SDKEnvironment.SDK_ENVIRONMENT_DEVELOPMENT,
)

// 2. Download and load a model
val modelId = "smollm2-360m-instruct-q8_0"
RunAnywhere.downloadModelStream(RAModelInfo(id = modelId)).collect { /* progress */ }
RunAnywhere.loadModel(
    RAModelLoadRequest(model_id = modelId, category = ModelCategory.MODEL_CATEGORY_LANGUAGE),
)

// 3. Generate
val result = RunAnywhere.generate("What is the capital of France?")
println(result.text) // "Paris is the capital of France."
```

Install via Gradle (Maven Central):

```kotlin
dependencies {
    implementation("io.github.sanchitmonga22:runanywhere-sdk:0.20.11")
    implementation("io.github.sanchitmonga22:runanywhere-llamacpp:0.20.11")
    // Optional: STT / TTS / VAD
    // implementation("io.github.sanchitmonga22:runanywhere-onnx:0.20.11")
}
```

[Documentation](https://docs.runanywhere.ai/kotlin/introduction) · [Source](bindings/kotlin/)

</details>

<details>
<summary><b>Flutter</b></summary>

<br/>

```dart
import 'package:runanywhere/runanywhere.dart';
import 'package:runanywhere_llamacpp/runanywhere_llamacpp.dart';

// 1. Initialize
LlamaCpp.register();
await RunAnywhere.initialize();

// 2. Download and load a model
await RunAnywhere.downloadModel('smollm2-360m');
await RunAnywhere.llm.load('smollm2-360m');

// 3. Generate
final response = await RunAnywhere.llm.chat('What is the capital of France?');
print(response); // "Paris is the capital of France."
```

Install via pub.dev:

```yaml
dependencies:
  runanywhere: ^0.20.11
  runanywhere_llamacpp: ^0.20.11  # LLM/VLM text generation
  # runanywhere_onnx: ^0.20.11    # STT, TTS, VAD, voice agent
  # runanywhere_mlx: ^0.20.11     # Apple-native LLM/VLM/STT/TTS/embeddings
  # runanywhere_qhexrt: ^0.20.11  # Snapdragon Hexagon NPU
```

[Documentation](https://docs.runanywhere.ai/flutter/introduction) · [Source](bindings/flutter/)

</details>

<details>
<summary><b>React Native</b></summary>

<br/>

```typescript
import { RunAnywhere, SDKEnvironment } from '@runan

## features

| Feature | Swift | Kotlin | Flutter | RN | Web | Electron | Python | rcli |
|---------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| LLM generation + streaming | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Vision language models (VLM) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Computer-use agent (CUA) | Yes | Yes | Yes | Yes | API only | n/a | n/a | n/a |
| Speech-to-Text | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Text-to-Speech | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice activity detection | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Voice agent pipeline | Yes | Yes | Yes | Yes | Yes | Yes | Stub | Yes |
| Wake word | No | No | No | No | No | No | No | No |
| Embeddings | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| RAG (with streaming) | Yes | Yes | Yes | Yes | Yes* | Yes | Yes | n/a |
| Structured output (JSON) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | n/a |
| Tool calling | Yes | Yes | Yes | Yes | Yes | Yes | Yes | n/a |
| Image generation (diffusion) | Yes | Yes | Yes | Yes | n/a | n/a | Stub | Yes |
| LoRA adapters | Yes | Yes | Yes | Yes | Yes | Partial | Stub | Yes |
| Diarization (standalone) | Yes | Yes | Gated | Yes | Yes | n/a | Stub | n/a |
| Segmentation | Yes | Yes | Gated | Yes | Yes | n/a | Stub | n/a |
| `capabilities()` discovery | Yes | Yes | Yes | Yes | Yes | Partial | Yes | n/a |

\* Web RAG may be limited to one session per process — check `capabilities().rag.multiSession`.
`Stub` / `Gated` / `Partial` mean the verb is absent, preflight-fails, or only partially wired; call `capabilities()` for the installed build.
| Hexagon NPU (QHexRT) | n/a | Yes | Yes | Yes | n/a | n/a | n/a | n/a |
| MLX (Apple silicon) | Yes | n/a | Yes | Yes | n/a | n/a | n/a | Yes |
| OpenAI-compatible server | n/a | n/a | n/a | n/a | n/a | n/a | Yes | Yes |
| Model download + progress | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **Connect (LAN host/client)** | Host (macOS) / Client (iOS, iPadOS) | Client | — | — | — | — | — | — |

### Connect (trusted LAN)

Connect lets a **macOS Swift app** host a loaded language model on the local network so **iOS, iPadOS, and Android** clients can discover it and stream generation without downloading that model. It is **app-scoped** (lives with the host app process), not an OS daemon.

| Role | Supported today | Not in this release |
|------|-----------------|---------------------|
| **Host** | macOS (Swift example / SDK) | Windows, Electron, Web, RN, Flutter |
| **Client** | iOS, iPadOS (Swift), Android (Kotlin) | React Native, Flutter, Web, Electron |

- **Discovery:** Bonjour / NSD service type `_runanywhere-connect._tcp`
- **Transport:** framed TCP on the LAN; commons owns protocol version, role policy, session accounting, and generation validation (`idl/connect.proto`, `rac_connect_*`)
- **Lifecycle:** the host app selects and loads the model, starts hosting, and supplies generation; stopping the host disconnects clients
- **Threat model:** **trusted LAN only** — no TLS, pairing PIN, or mutual auth in this release. Do not expose Connect across untrusted networks. Future work may add TLS/pairing, Windows hosting, or a daemon; those change lifecycle and security and are out of scope here
- **Electron note:** `RunAnywhereMain.connect()` is **local MessagePort / utility-process IPC** inside one Electron app. It is unrelated to LAN Connect

CUA on Web is "API only": the prompt/parse scaffold ships, but the catalogued
Fara1.5-4B does not fit the 4 GB WASM32 heap, so no CUA model is seeded there.

---

## Inference engines

Every SDK is a thin binding over `runanywhere-commons`, a single C++ core behind a pure C ABI. Engines plug into a capability registry and declare, per modality, what they can run. At inference time the highest-priority engine that serves the modality on the current device wins. Same code, different silicon, no branching in your app.

| Engine | Modalities | Runs on | Notes |
|---|---|---|---|
| **QHexRT** | LLM, VLM, STT, TTS,

## requirements

| Platform | Minimum |
|----------|---------|
| iOS | 17.5+ |
| macOS | 14.5+ |
| Android | API 24 (7.0), arm64 recommended |
| Web | Chrome 96+ / Edge 96+, Chrome 120+ for WebGPU |
| React Native | 0.83.1+, 0.85+ recommended (Node.js 22.12+) |
| Flutter | 3.44+ (Dart 3.12+) |
| Electron | Windows x64 (preview) |
| Python | 3.9+ on Windows, macOS, Linux (3.12+ recommended) |
| rcli | macOS arm64, Linux x86_64 / aarch64, Windows x86_64 |

Hexagon NPU: Snapdragon with Hexagon v75 / v79 / v81, Android arm64.
MLX: Apple silicon, physical devices.
Memory: 2 GB minimum, 4 GB+ recommended for larger models.

---

## Contributing

We welcome contributions. See the [Contributing Guide](CONTRIBUTING.md) for setup and conventions.

```bash
git clone https://github.com/RunanywhereAI/runanywhere-sdks.git
cd runanywhere-sdks
