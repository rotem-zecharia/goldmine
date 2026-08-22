# mlc-ai/web-llm

High-performance In-browser LLM Inference Engine

## features

WebLLM is a high-performance in-browser LLM inference engine that brings language model inference directly onto web browsers with hardware acceleration.
Everything runs inside the browser with no server support and is accelerated with WebGPU.

WebLLM is **fully compatible with [OpenAI API](https://platform.openai.com/docs/api-reference/chat).**
That is, you can use the same OpenAI API on **any open source models** locally, with functionalities
including streaming, JSON-mode, function-calling (WIP), etc.

We can bring a lot of fun opportunities to build AI assistants for everyone and enable privacy while enjoying GPU acceleration.

You can use WebLLM as a base [npm package](https://www.npmjs.com/package/@mlc-ai/web-llm) and build your own web application on top of it by following the examples below. This project is a companion project of [MLC LLM](https://github.com/mlc-ai/mlc-llm), which enables universal deployment of LLM across hardware environments.

<div align="center">

**[Check out WebLLM Chat to try it out!](https://chat.webllm.ai/)**

</div>

## Key Features

- **In-Browser Inference**: WebLLM is a high-performance, in-browser language model inference engine that leverages WebGPU for hardware acceleration, enabling powerful LLM operations directly within web browsers without server-side processing.

- [**Full OpenAI API Compatibility**](#full-openai-compatibility): Seamlessly integrate your app with WebLLM using OpenAI API with functionalities such as streaming, JSON-mode, logit-level control, seeding, and more.

- **Structured JSON Generation**: WebLLM supports state-of-the-art JSON mode structured generation, implemented in the WebAssembly portion of the model library for optimal performance. Check [WebLLM JSON Playground](https://huggingface.co/spaces/mlc-ai/WebLLM-JSON-Playground) on HuggingFace to try generating JSON output with custom JSON schema.

- [**Extensive Model Support**](#built-in-models): WebLLM natively supports a range of models including Llama 3, Phi 3, Gemma, Mistral, Qwen(通义千问), and many others, making it versatile for various AI tasks. For the complete supported model list, check [MLC Models](https://mlc.ai/models).

- [**Custom Model Integration**](#custom-models): Easily integrate and deploy custom models in MLC format, allowing you to adapt WebLLM to specific needs and scenarios, enhancing flexibility in model deployment.

- **Plug-and-Play Integration**: Easily integrate WebLLM into your projects using package managers like NPM and Yarn, or directly via CDN, complete with comprehensive [examples](./examples/) and a modular design for connecting with UI components.

- **Streaming & Real-Time Interactions**: Supports streaming chat completions, allowing real-time output generation which enhances interactive applications like chatbots and virtual assistants.

- **Web Worker & Service Worker Support**: Optimize UI performance and manage the lifecycle of models efficiently by offloading computations to separate worker threads or service workers.

- **Chrome Extension Support**: Extend the functionality of web browsers through custom Chrome extensions using WebLLM, with examples available for building both basic and advanced extensions.

## Built-in Models

Check the complete list of available models on [MLC Models](https://mlc.ai/models). WebLLM supports a subset of these available models and the list can be accessed at [`prebuiltAppConfig.model_list`](https://github.com/mlc-ai/web-llm/blob/main/src/config.ts#L293).

Here are the primary families of models currently supported:

- **Llama**: Llama 3, Llama 2, Hermes-2-Pro-Llama-3
- **Phi**: Phi 3, Phi 2, Phi 1.5
- **Gemma**: Gemma-2B
- **Mistral**: Mistral-7B-v0.3, Hermes-2-Pro-Mistral-7B, NeuralHermes-2.5-Mistral-7B, OpenHermes-2.5-Mistral-7B
- **Qwen (通义千问)**: Qwen2 0.5B, 1.5B, 7B

If you need more models, [request a new model via opening an issue](https://github.com/mlc-ai/web-llm/issues/new/choose) or check [Custom Models](#custom-models) for ho

## tools

Learn how to use WebLLM to integrate large language models into your application and generate chat completions through this simple Chatbot example:

[![Example Chatbot on JSFiddle](https://img.shields.io/badge/Example-JSFiddle-blue?logo=jsfiddle&logoColor=white)](https://jsfiddle.net/neetnestor/4nmgvsa2/)
[![Example Chatbot on Codepen](https://img.shields.io/badge/Example-Codepen-gainsboro?logo=codepen)](https://codepen.io/neetnestor/pen/vYwgZaG)

For an advanced example of a larger, more complicated project, check [WebLLM Chat](https://github.com/mlc-ai/web-llm-chat/blob/main/app/client/webllm.ts).

More examples for different use cases are available in the [examples](./examples/) folder.

## Get Started

WebLLM offers a minimalist and modular interface to access the chatbot in the browser.
The package is designed in a modular way to hook to any of the UI components.

## installation

#### Package Manager

```sh
# npm
npm install @mlc-ai/web-llm
# yarn
yarn add @mlc-ai/web-llm
# or pnpm
pnpm install @mlc-ai/web-llm
```

Then import the module in your code.

```typescript
// Import everything
import * as webllm from "@mlc-ai/web-llm";
// Or only import what you need
import { CreateMLCEngine } from "@mlc-ai/web-llm";
```

#### CDN Delivery

Thanks to [jsdelivr.com](https://www.jsdelivr.com/package/npm/@mlc-ai/web-llm), WebLLM can be imported directly through URL and work out-of-the-box on cloud development platforms like [jsfiddle.net](https://jsfiddle.net/), [Codepen.io](https://codepen.io/), and [Scribbler](https://scribbler.live):

```javascript
import * as webllm from "https://esm.run/@mlc-ai/web-llm";
```

It can also be dynamically imported as:

```javascript
const webllm = await import("https://esm.run/@mlc-ai/web-llm");
```

### Create MLCEngine

Most operations in WebLLM are invoked through the `MLCEngine` interface. You can create an `MLCEngine` instance and loading the model by calling the `CreateMLCEngine()` factory function.

(Note that loading models requires downloading and it can take a significant amount of time for the very first run without caching previously. You should properly handle this asynchronous call.)

```typescript
import { CreateMLCEngine } from "@mlc-ai/web-llm";

// Callback function to update model loading progress
const initProgressCallback = (initProgress) => {
  console.log(initProgress);
};
const selectedModel = "Llama-3.1-8B-Instruct-q4f32_1-MLC";

const engine = await CreateMLCEngine(
  selectedModel,
  { initProgressCallback: initProgressCallback }, // engineConfig
);
```

Under the hood, this factory function does the following steps for first creating an engine instance (synchronous) and then loading the model (asynchronous). You can also do them separately in your application.

```typescript
import { MLCEngine } from "@mlc-ai/web-llm";

// This is a synchronous call that returns immediately
const engine = new MLCEngine({
  initProgressCallback: initProgressCallback,
});

// This is an asynchronous call and can take a long time to finish
await engine.reload(selectedModel);
```

### Cache Backend Policy

WebLLM supports four cache backends through `AppConfig.cacheBackend`:

- `"cache"`: browser [Cache API](https://developer.mozilla.org/en-US/docs/Web/API/Cache) (default).
- `"indexeddb"`: browser [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API).
- `"opfs"`: browser [Origin Private File System (OPFS)](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API/Origin_private_file_system).
- `"cross-origin"`: experimental Chrome [Cross-Origin Storage API](https://github.com/WICG/cross-origin-storage) extension backend. Install the [Cross-Origin Storage extension](https://chromewebstore.google.com/detail/cross-origin-storage/denpnpcgjgikjpoglpjefakmdcbmlgih) to use it. (If the extension isn't installed, WebLLM falls back to the default cache automatically.)

Example:

```typescript
import { CreateMLCEngine, prebuiltAppConfig } from "@mlc-ai/web-llm";

const appConfig = { ...prebuiltAppConfig, cacheBackend: "cross-origin" };
const engine = await CreateMLCEngine("Llama-3.1-8B-Instruct-q4f32_1-MLC", {
  appConfig,
});
```

Notes:
- If `"opfs"` is selected in an environment without OPFS support, cache operations fail with an OPFS availability error.
- When using `"opfs"`, `appConfig.opfsAccessMode` can be set to `"auto"` to use OPFS sync access handles where supported, or `"sync"` to require sync access handles. The default is `"async"`.
- The `"cross-origin"` backend requires installing and enabling a compatible browser extension.
- Cross-origin backend currently does not support programmatic tensor-cache deletion; clearing is extension-managed.

### Chat Completion

After successfully initializing the engine, you can now invoke chat completions using OpenAI style chat APIs through the `engine.chat.completions` interface. For the full list of
