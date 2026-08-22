# jundot/omlx

LLM inference server with continuous batching & SSD caching for Apple Silicon — managed from the macOS menu bar

## installation

omlx start
omlx stop
omlx restart

## features

Supports text LLMs, vision-language models (VLM), OCR models, embeddings, and rerankers on Apple Silicon.

## tools

Drop-in replacement for OpenAI and Anthropic APIs. Supports streaming usage stats (`stream_options.include_usage`), Anthropic adaptive thinking, and vision inputs (base64, URL).

| Endpoint | Description |
|----------|-------------|
| `POST /v1/chat/completions` | Chat completions (streaming) |
| `POST /v1/completions` | Text completions (streaming) |
| `POST /v1/messages` | Anthropic Messages API |
| `POST /v1/embeddings` | Text embeddings |
| `POST /v1/rerank` | Document reranking |
| `GET /v1/models` | List available models |

## configuration

```bash
