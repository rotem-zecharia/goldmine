# huggingface/speech-to-speech

Build voice agents with open-source models

## installation

```bash
pip install speech-to-speech
export OPENAI_API_KEY=...
speech-to-speech serve
```

This starts an OpenAI Realtime-compatible server at `ws://localhost:8765/v1/realtime` using Parakeet TDT for local STT, an OpenAI-compatible LLM, and Qwen3-TTS for local speech output.

Talk to it from a second terminal:

```bash
speech-to-speech talk --url ws://127.0.0.1:8765/v1/realtime
```

To start the server and packaged microphone/speaker client in one command:

```bash
speech-to-speech local
```

Prefer to keep the LLM on your own machine? Serve Gemma 4 with llama.cpp:

```bash
llama-server -hf ggml-org/gemma-4-E4B-it-GGUF -np 2 -c 65536 -fa on --swa-full
```

Then point the OpenAI-compatible LLM backend at it:

```bash
speech-to-speech serve \
    --model_name "ggml-org/gemma-4-E4B-it-GGUF" \
    --responses_api_base_url "http://127.0.0.1:8080/v1" \
    --responses_api_api_key ""
```

Clients using the implemented core Realtime event set can connect. The official OpenAI Agents SDK is tested over both stock transports; see [Realtime API](#realtime-api) for the tested surface and [LLM backends](#llm-backends) for provider and local-server options.

## tools

| Command | Behavior | Use it when |
|---|---|---|
| `serve` | Runs the pipeline server over OpenAI Realtime WebSocket and WebRTC. | You are building an app or device against the API. |
| `talk --url <full-realtime-url>` | Runs the packaged microphone/speaker client. | You want to talk to an existing Realtime server. |
| `local` | Composes `serve` and `talk` in-process over loopback. | You want to run the server and talk to it from one command. |

`serve` binds to `127.0.0.1` by default; pass `--host 0.0.0.0` explicitly for network exposure. `local` always binds to loopback and connects the same packaged client at `ws://127.0.0.1:<port>/v1/realtime`.

The packaged client can opt in to local Python tools with `talk --tool-module <module>` or `local --tool-module <module>`. The module contract, programmatic API, and a Serper web-search example are documented in [Tool calling design](./src/speech_to_speech/api/openai_realtime/README.md#packaged-python-client-tools).
