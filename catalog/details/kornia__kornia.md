# kornia/kornia

🐍 Geometric Computer Vision Library for Spatial AI

## installation

[![PyPI python](https://img.shields.io/pypi/pyversions/kornia)](https://pypi.org/project/kornia)
[![pytorch](https://img.shields.io/badge/PyTorch_2.0.0+-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)

### From pip

  ```bash
  pip install kornia
  ```

<details>
  <summary>Other installation options</summary>

#### From source with editable mode

  ```bash
  pip install -e .
  ```

#### For development with Pixi (Recommended)

For development, Kornia uses [pixi](https://pixi.sh) for fast Python package management and environment management. The project includes a `pixi.toml` configuration file for reproducible dependency management.

  ```bash
  # Install pixi (if not already installed)
  curl -fsSL https://pixi.sh/install.sh | bash

  # Install dependencies and set up the development environment
  pixi install

  # Run tests
  pixi run test

  # For CUDA development
  pixi run -e cuda install
  pixi run -e cuda test-cuda
  ```

This will set up a complete development environment with all dependencies. For more details on dependency management and available tasks, see [CONTRIBUTING.md](CONTRIBUTING.md).

#### From Github url (latest version)

  ```bash
  pip install git+https://github.com/kornia/kornia
  ```

</details>

## Quick Start

Kornia is not just another computer vision library — it's your gateway to effortless Computer Vision and AI.

<details>
<summary>Get started with Kornia image transformation and augmentation!</summary>

```python
import numpy as np
import kornia_rs as kr

from kornia.augmentation import AugmentationSequential, RandomAffine, RandomBrightness
from kornia.filters import StableDiffusionDissolving

# Load and prepare your image
img: np.ndarray = kr.read_image_any("img.jpeg")
img = kr.resize(img, (256, 256), interpolation="bilinear")

# alternatively, load image with PIL
# img = Image.open("img.jpeg").resize((256, 256))
# img = np.array(img)

img = np.stack([img] * 2)  # batch images

# Define an augmentation pipeline
augmentation_pipeline = AugmentationSequential(RandomAffine((-45.0, 45.0), p=1.0), RandomBrightness((0.0, 1.0), p=1.0))

# Leveraging StableDiffusion models
dslv_op = StableDiffusionDissolving()

img = augmentation_pipeline(img)
dslv_op(img, step_number=500)

dslv_op.save("Kornia-enhanced.jpg")
```

</details>

<details>
<summary>Find out Kornia ONNX models with ONNXSequential!</summary>

```python
import numpy as np
from kornia.onnx import ONNXSequential

# Chain ONNX models from HuggingFace repo and your own local model together
onnx_seq = ONNXSequential(
    "hf://operators/kornia.geometry.transform.flips.Hflip",
    "hf://models/kornia.models.detection.rtdetr_r18vd_640x640",  # Or you may use "YOUR_OWN_MODEL.onnx"
)
# Prepare some input data
input_data = np.random.randn(1, 3, 384, 512).astype(np.float32)
# Perform inference
outputs = onnx_seq(input_data)
# Print the model outputs
print(outputs)

# Export a new ONNX model that chains up all three models together!
onnx_seq.export("chained_model.onnx")
```
</details>

## Multi-framework support

You can now use Kornia with [TensorFlow](https://www.tensorflow.org/), [JAX](https://jax.readthedocs.io/en/latest/index.html), and [NumPy](https://numpy.org/). See [Multi-Framework Support](docs/source/get-started/multi-framework-support.rst) for more details.

```python
import kornia

tf_kornia = kornia.to_tensorflow()
```

<p align="center">
  Powered by
  <a href="https://github.com/ivy-llc/ivy" target="_blank">
    <div class="dark-light" style="display: block;" align="center">
      <img class="dark-light" width="15%" src="https://raw.githubusercontent.com/ivy-llc/assets/refs/heads/main/assets/logos/ivy-long.svg"/>
    </div>
  </a>
</p>

## Call For Contributors

Are you passionate about computer vision, AI, and open-source development? Join us in shaping the future of Kornia! We are actively seeking contributors to help strengthen the library — making it more correct, faster, and better specified. Whether
