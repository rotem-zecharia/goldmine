# RapidAI/RapidOCR

📄 Awesome OCR multiple programing languages toolkits based on ONNX Runtime, OpenVINO, MNN, PaddlePaddle, TensorRT and PyTorch.

## installation

```bash
pip install rapidocr onnxruntime
```

## tools

```python
from rapidocr import RapidOCR

engine = RapidOCR()

img_url = "https://www.modelscope.cn/models/RapidAI/RapidOCR/resolve/master/resources/test_files/ch_en_num.jpg"
result = engine(img_url)
print(result)

result.vis("vis_result.jpg")
```

### 🐳 Docker

Docker development environments are available for all supported inference engines:

```bash
# Build and test with ONNX Runtime (CPU)
make build-onnxruntime-cpu
make test-onnxruntime-cpu

# Or use any engine: onnxruntime-gpu, tensorrt, paddle, openvino, pytorch, mnn
make build-tensorrt
make shell-tensorrt
```

See [docker/README.md](./docker/README.md) for full setup instructions, GPU configuration, and troubleshooting.

### 📚 Documentation

Full documentation can be found on [docs](https://rapidai.github.io/RapidOCRDocs/), in Chinese.

### 👥 Who use? ([more](https://github.com/RapidAI/RapidOCR/network/dependents))

- [Docling](https://github.com/DS4SD/docling)
- [CnOCR](https://github.com/breezedeus/CnOCR)
- [api-for-open-llm](https://github.com/xusenlinzy/api-for-open-llm)
- [arknights-mower](https://github.com/ArkMowers/arknights-mower)
- [pensieve](https://github.com/arkohut/pensieve)
- [genshin_artifact_auxiliary](https://github.com/SkeathyTomas/genshin_artifact_auxiliary)
- [ChatLLM](https://github.com/yuanjie-ai/ChatLLM)
- [langchain](https://github.com/langchain-ai/langchain)
- [Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)
- [JamAIBase](https://github.com/EmbeddedLLM/JamAIBase)
- [PAI-RAG](https://github.com/aigc-apps/PAI-RAG)
- [ChatAgent_RAG](https://github.com/junyuyang7/ChatAgent_RAG)
- [OpenAdapt](https://github.com/OpenAdaptAI/OpenAdapt)
- [Umi-OCR](https://github.com/hiroi-sora/Umi-OCR)

> For more projects that use RapidOCR, you are welcome to [register](https://github.com/RapidAI/RapidOCR/discussions/286) at the registration address. Registration is solely for product promotion.

### 🙏 Acknowledgements

- Many thanks to [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) for everything.
- Many thanks to [PaddleOCR2Pytorch](https://github.com/frotms/PaddleOCR2Pytorch) for providing the converted PyTorch format models.
- Many thanks to [PaddleX](https://github.com/PaddlePaddle/PaddleX) for providing the document models.
- Many thanks to [DeliciaLaniD](https://github.com/DeliciaLaniD) for fixing the misplaced start position of scan animation in ocrweb.
- Many thanks to [zhsunlight](https://github.com/zhsunlight) for the suggestion about parameterized call GPU reasoning and the careful and thoughtful testing.
- Many thanks to [lzh111222334](https://github.com/lzh111222334) for fixing some bugs of rec preprocessing under python version.
- Many thanks to [AutumnSun1996](https://github.com/AutumnSun1996) for the suggestion in the [#42](https://github.com/RapidAI/RapidOCR/issues/42).
- Many thanks to [DeadWood8](https://github.com/DeadWood8) for providing the [document](https://rapidai.github.io/RapidOCRDocs/main/install_usage/rapidocr_web/nuitka_package/) which packages rapidocr_web to exe by Nuitka.
- Many thanks to [Loovelj](https://github.com/Loovelj) for fixing the bug of sorting the text boxes. For details see [issue 75](https://github.com/RapidAI/RapidOCR/issues/75).

### 🤝 Contribution Guide

This repository contains the **Python** component of RapidOCR. Components for other languages have been migrated to separate repositories.

For the complete workflow on contributing to Python development, please refer to: [**Python CONTRIBUTING**](docs/CONTRIBUTING.md).

### 🎖 Code Contributors

<p align="left">
  <a href="https://github.com/RapidAI/RapidOCR/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=RapidAI/RapidOCR&max=400&columns=10" width="60%"/>
  </a>
</p>

### 🌟 Sponsors & Backers

RapidOCR is an Apache2.0-licensed open source project with its ongoing development made possible entirely by the support of these awesome backers. If you'd like to join them, please consider [sponsoring RapidOCR's developmen
