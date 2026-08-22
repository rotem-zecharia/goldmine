# openvinotoolkit/openvino

OpenVINO™ is an open source toolkit for optimizing and deploying AI inference

## installation

[Get your preferred distribution of OpenVINO](https://docs.openvino.ai/2026/get-started/install-openvino.html) or use this command for quick installation:

```sh
pip install -U openvino
```

### Verify Installation

After installation, you can verify OpenVINO is installed correctly by running:

```python
import openvino as ov
print(ov.__version__)
```

Check [system requirements](https://docs.openvino.ai/2026/about-openvino/release-notes-openvino/system-requirements.html) and [supported devices](https://docs.openvino.ai/2026/documentation/compatibility-and-support/supported-devices.html) for detailed information.

## tools

[OpenVINO Quickstart example](https://docs.openvino.ai/2026/get-started.html) will walk you through the basics of deploying your first model.

Learn how to optimize and deploy popular models with the [OpenVINO Notebooks](https://github.com/openvinotoolkit/openvino_notebooks) 📚:
- [Create an LLM-powered Chatbot using OpenVINO](https://github.com/openvinotoolkit/openvino_notebooks/blob/latest/notebooks/llm-chatbot/llm-chatbot-generate-api.ipynb)
- [YOLOv11 Optimization](https://github.com/openvinotoolkit/openvino_notebooks/blob/latest/notebooks/yolov11-optimization/yolov11-object-detection.ipynb)
- [Text-to-Image Generation](https://github.com/openvinotoolkit/openvino_notebooks/blob/latest/notebooks/text-to-image-genai/text-to-image-genai.ipynb)
- [Multimodal assistant with LLaVa and OpenVINO](https://github.com/openvinotoolkit/openvino_notebooks/blob/latest/notebooks/llava-multimodal-chatbot/llava-multimodal-chatbot-genai.ipynb)
- [Automatic speech recognition using Whisper and OpenVINO](https://github.com/openvinotoolkit/openvino_notebooks/blob/latest/notebooks/whisper-asr-genai/whisper-asr-genai.ipynb)

Discover more examples in the [OpenVINO Samples (Python & C++)](https://docs.openvino.ai/2026/get-started/learn-openvino/openvino-samples.html) and [Notebooks (Python)](https://docs.openvino.ai/2026/get-started/learn-openvino/interactive-tutorials-python.html).

Here are easy-to-follow code examples demonstrating how to run PyTorch and TensorFlow model inference using OpenVINO:

**PyTorch Model**

```python
import openvino as ov
import torch
import torchvision

# load PyTorch model into memory
model = torch.hub.load("pytorch/vision", "shufflenet_v2_x1_0", weights="DEFAULT")

# convert the model into OpenVINO model
example = torch.randn(1, 3, 224, 224)
ov_model = ov.convert_model(model, example_input=(example,))

# compile the model for CPU device
core = ov.Core()
compiled_model = core.compile_model(ov_model, 'CPU')

# infer the model on random data
output = compiled_model({0: example.numpy()})
```

**TensorFlow Model**

```python
import numpy as np
import openvino as ov
import tensorflow as tf

# load TensorFlow model into memory
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# convert the model into OpenVINO model
ov_model = ov.convert_model(model)

# compile the model for CPU device
core = ov.Core()
compiled_model = core.compile_model(ov_model, 'CPU')

# infer the model on random data
data = np.random.rand(1, 224, 224, 3)
output = compiled_model({0: data})
```

OpenVINO supports the CPU, GPU, and NPU [devices](https://docs.openvino.ai/2026/openvino-workflow/running-inference/inference-devices-and-modes.html) and works with models from PyTorch, TensorFlow, ONNX, TensorFlow Lite, PaddlePaddle, and JAX/Flax [frameworks](https://docs.openvino.ai/2026/openvino-workflow/model-preparation.html). It includes [APIs](https://docs.openvino.ai/2026/api/api_reference.html) in C++, Python, C, NodeJS, and offers the GenAI API for optimized model pipelines and performance.

## Generative AI with OpenVINO

Get started with the OpenVINO GenAI [installation](https://docs.openvino.ai/2026/get-started/install-openvino/install-openvino-genai.html) and refer to the [detailed guide](https://docs.openvino.ai/2026/openvino-workflow-generative/inference-with-genai.html) to explore the capabilities of Generative AI using OpenVINO.

Learn how to run LLMs and GenAI with [Samples](https://github.com/openvinotoolkit/openvino.genai/tree/master/samples) in the [OpenVINO™ GenAI repo](https://github.com/openvinotoolkit/openvino.genai). See GenAI in action with Jupyter notebooks: [LLM-powered Chatbot](https://github.com/openvinotoolkit/openvino_notebooks/tree/latest/notebooks/llm-chatbot) and [LLM Instruction-following pipeline](https://github.com/openvinotoolkit/openvino_notebooks/tree/latest/notebooks/llm-question-answering).

## Documentation

[User documentation](https://docs.openvino.ai/) contains detailed information about OpenVINO and gui
