# qubvel-org/segmentation_models.pytorch

Semantic segmentation models with 500+ pretrained convolutional and transformer-based backbones.

## installation

#### 1. Create your first Segmentation model with SMP

The segmentation model is just a PyTorch `torch.nn.Module`, which can be created as easy as:

```python
import segmentation_models_pytorch as smp

model = smp.Unet(
    encoder_name="resnet34",        # choose encoder, e.g. mobilenet_v2 or efficientnet-b7
    encoder_weights="imagenet",     # use `imagenet` pre-trained weights for encoder initialization
    in_channels=1,                  # model input channels (1 for gray-scale images, 3 for RGB, etc.)
    classes=3,                      # model output channels (number of classes in your dataset)

## tools

| Name                                      | Link                                                                                           | Colab                                                                                           |
|-------------------------------------------|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| **Train** pets binary segmentation on OxfordPets     | [Notebook](https://github.com/qubvel/segmentation_models.pytorch/blob/main/examples/binary_segmentation_intro.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/qubvel/segmentation_models.pytorch/blob/main/examples/binary_segmentation_intro.ipynb) |
| **Train** cars binary segmentation on CamVid       | [Notebook](https://github.com/qubvel/segmentation_models.pytorch/blob/main/examples/cars%20segmentation%20(camvid).ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/qubvel/segmentation_models.pytorch/blob/main/examples/cars%20segmentation%20(camvid).ipynb) |
| **Train** multiclass segmentation on CamVid          | [Notebook](https://github.com/qubvel-org/segmentation_models.pytorch/blob/main/examples/camvid_segmentation_multiclass.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/qubvel-org/segmentation_models.pytorch/blob/main/examples/camvid_segmentation_multiclass.ipynb) |
| **Train** clothes binary segmentation by @ternaus   | [Repo](https://github.com/ternaus/cloths_segmentation)                                        |     |
| **Load and inference** pretrained Segformer | [Notebook](https://github.com/qubvel-org/segmentation_models.pytorch/blob/main/examples/segformer_inference_pretrained.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/qubvel/segmentation_models.pytorch/blob/main/examples/segformer_inference_pretrained.ipynb) |
| **Load and inference** pretrained DPT | [Notebook](https://github.com/qubvel-org/segmentation_models.pytorch/blob/main/examples/dpt_inference_pretrained.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/qubvel/segmentation_models.pytorch/blob/main/examples/dpt_inference_pretrained.ipynb) |
| **Load and inference** pretrained UPerNet | [Notebook](https://github.com/qubvel-org/segmentation_models.pytorch/blob/main/examples/upernet_inference_pretrained.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/qubvel/segmentation_models.pytorch/blob/main/examples/upernet_inference_pretrained.ipynb) |
| **Save and load** models locally / to HuggingFace Hub |[Notebook](https://github.com/qubvel-org/segmentation_models.pytorch/blob/main/examples/save_load_model_and_share_with_hf_hub.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/qubvel/segmentation_models.pytorch/blob/main/examples/save_load_model_and_share_with_hf_hub.ipynb)
| **Export** trained model to ONNX              | [Notebook](https://github.com/qubvel/segmentation_models.pytorch/blob/main/examples/convert_to_onnx.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/qubvel/segmentation_models.pytorch/blob/main/examples/convert_to_onnx.ipynb) |
