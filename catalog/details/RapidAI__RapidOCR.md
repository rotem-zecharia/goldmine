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
