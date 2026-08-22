# bentoml/BentoML

The easiest way to serve AI apps and models - Build Model Inference APIs, Job queues, LLM apps, Multi-model pipelines, and more!

## installation

Install BentoML:

```
# Requires Python≥3.9
pip install -U bentoml
```

Define APIs in a `service.py` file.

```python
import bentoml

@bentoml.service(
    image=bentoml.images.Image(python_version="3.11").python_packages("torch", "transformers"),
)
class Summarization:
    def __init__(self) -> None:
        import torch
        from transformers import pipeline

        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipeline = pipeline('summarization', device=device)

    @bentoml.api(batchable=True)
    def summarize(self, texts: list[str]) -> list[str]:
        results = self.pipeline(texts)
        return [item['summary_text'] for item in results]
```

### 💻 Run locally

Install PyTorch and Transformers packages to your Python virtual environment.

```bash
pip install torch transformers  # additional dependencies for local run
```

Run the service code locally (serving at http://localhost:3000 by default):

```bash
bentoml serve
```

You should expect to see the following output.

```
[INFO] [cli] Starting production HTTP BentoServer from "service:Summarization" listening on http://localhost:3000 (Press CTRL+C to quit)
[INFO] [entry_service:Summarization:1] Service Summarization initialized
```

Now you can run inference from your browser at http://localhost:3000 or with a Python script:

```python
import bentoml

with bentoml.SyncHTTPClient('http://localhost:3000') as client:
    summarized_text: str = client.summarize([bentoml.__doc__])[0]
    print(f"Result: {summarized_text}")
```

### 🐳 Deploy using Docker

Run `bentoml build` to package necessary code, models, dependency configs into a Bento - the standardized deployable artifact in BentoML:

```bash
bentoml build
```

Ensure [Docker](https://docs.docker.com/) is running. Generate a Docker container image for deployment:

```bash
bentoml containerize summarization:latest
```

Run the generated image:

```bash
docker run --rm -p 3000:3000 summarization:latest
```

### ☁️ Deploy on BentoCloud

[BentoCloud](https://www.bentoml.com) provides compute infrastructure for rapid and reliable GenAI adoption. It helps speed up your BentoML development process leveraging cloud compute resources, and simplify how you deploy, scale and operate BentoML in production.

[Sign up for BentoCloud](https://cloud.bentoml.com/signup) for personal access; for enterprise use cases, [contact our team](https://www.bentoml.com/contact).

```bash

## tools

bentoml cloud login

# Deploy from current directory:
bentoml deploy
```

![bentocloud-ui](./docs/source/_static/img/get-started/cloud-deployment/first-bento-on-bentocloud.png)

For detailed explanations, read the [Hello World example](https://docs.bentoml.com/en/latest/get-started/hello-world.html).

## Examples

- LLMs: [Llama 3.2](https://github.com/bentoml/BentoVLLM/tree/main/llama3.2-11b-vision-instruct), [Mistral](https://github.com/bentoml/BentoVLLM/tree/main/ministral-8b-instruct-2410), [DeepSeek Distil](https://github.com/bentoml/BentoVLLM/tree/main/deepseek-r1-distill-llama3.1-8b-tool-calling), and more.
- Image Generation: [Stable Diffusion 3 Medium](https://github.com/bentoml/BentoDiffusion/tree/main/sd3-medium), [Stable Video Diffusion](https://github.com/bentoml/BentoDiffusion/tree/main/svd), [Stable Diffusion XL Turbo](https://github.com/bentoml/BentoDiffusion/tree/main/sdxl-turbo), [ControlNet](https://github.com/bentoml/BentoDiffusion/tree/main/controlnet), and [LCM LoRAs](https://github.com/bentoml/BentoDiffusion/tree/main/lcm).
- Embeddings: [SentenceTransformers](https://github.com/bentoml/BentoSentenceTransformers) and [ColPali](https://github.com/bentoml/BentoColPali)
- Audio: [ChatTTS](https://github.com/bentoml/BentoChatTTS), [XTTS](https://github.com/bentoml/BentoXTTS), [WhisperX](https://github.com/bentoml/BentoWhisperX), [Bark](https://github.com/bentoml/BentoBark)
- Computer Vision: [YOLO](https://github.com/bentoml/BentoYolo) and [ResNet](https://github.com/bentoml/BentoResnet)
- Advanced examples: [Function calling](https://github.com/bentoml/BentoFunctionCalling), [LangGraph](https://github.com/bentoml/BentoLangGraph), [CrewAI](https://github.com/bentoml/BentoCrewAI)

Check out the [full list](https://docs.bentoml.com/en/latest/examples/overview.html) for more sample code and usage.

## Advanced topics

- [Model composition](https://docs.bentoml.com/en/latest/get-started/model-composition.html)
- [Workers and model parallelization](https://docs.bentoml.com/en/latest/build-with-bentoml/parallelize-requests.html)
- [Adaptive batching](https://docs.bentoml.com/en/latest/get-started/adaptive-batching.html)
- [GPU inference](https://docs.bentoml.com/en/latest/build-with-bentoml/gpu-inference.html)
- [Distributed serving systems](https://docs.bentoml.com/en/latest/build-with-bentoml/distributed-services.html)
- [Concurrency and autoscaling](https://docs.bentoml.com/en/latest/scale-with-bentocloud/scaling/autoscaling.html)
- [Model loading and Model Store](https://docs.bentoml.com/en/latest/build-with-bentoml/model-loading-and-management.html)
- [Observability](https://docs.bentoml.com/en/latest/build-with-bentoml/observability/index.html)
- [BentoCloud deployment](https://docs.bentoml.com/en/latest/get-started/cloud-deployment.html)

See [Documentation](https://docs.bentoml.com) for more tutorials and guides.

## Community

Get involved and join our [Community Forum 💬](https://forum.modular.com/c/bento/31), where thousands of AI/ML engineers help each other, contribute to the project, and talk about building AI products.

To report a bug or suggest a feature request, use
[GitHub Issues](https://github.com/bentoml/BentoML/issues/new/choose).

### Contributing

There are many ways to contribute to the project:

- Report bugs and "Thumbs up" on [issues](https://github.com/bentoml/BentoML/issues) that are relevant to you.
- Investigate [issues](https://github.com/bentoml/BentoML/issues) and review other developers' [pull requests](https://github.com/bentoml/BentoML/pulls).
- Contribute code or [documentation](https://docs.bentoml.com/en/latest/index.html) to the project by submitting a GitHub pull request.
- Check out the [Contributing Guide](https://github.com/bentoml/BentoML/blob/main/CONTRIBUTING.md) and [Development Guide](https://github.com/bentoml/BentoML/blob/main/DEVELOPMENT.md) to learn more.
- Share your feedback and discuss roadmap plans in our [forum](https://forum.modular.com/c/bento/31).

Tha
