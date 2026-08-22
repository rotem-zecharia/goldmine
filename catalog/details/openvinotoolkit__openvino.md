# openvinotoolkit/openvino

OpenVINO™ is an open source toolkit for optimizing and deploying AI inference

## installation

[Get your preferred distribution of OpenVINO](https://docs.openvino.ai/2026/get-started/install-openvino.html) or use this command for quick installation:

```sh
pip install -U openvino
```

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
