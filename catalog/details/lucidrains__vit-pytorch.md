# lucidrains/vit-pytorch

Implementation of Vision Transformer, a simple way to achieve SOTA in vision classification with only a single transformer encoder, in Pytorch

## installation

```bash
$ pip install vit-pytorch
```

## tools

```python
import torch
from vit_pytorch import ViT

v = ViT(
    image_size = 256,
    patch_size = 32,
    num_classes = 1000,
    dim = 1024,
    depth = 6,
    heads = 16,
    mlp_dim = 2048,
    dropout = 0.1,
    emb_dropout = 0.1
)

img = torch.randn(1, 3, 256, 256)

preds = v(img) # (1, 1000)
```

## Parameters

- `image_size`: int.
Image size. If you have rectangular images, make sure your image size is the maximum of the width and height
- `patch_size`: int.
Size of patches. `image_size` must be divisible by `patch_size`.
The number of patches is: ` n = (image_size // patch_size) ** 2` and `n` **must be greater than 16**.
- `num_classes`: int.
Number of classes to classify.
- `dim`: int.
Last dimension of output tensor after linear transformation `nn.Linear(..., dim)`.
- `depth`: int.
Number of Transformer blocks.
- `heads`: int.
Number of heads in Multi-head Attention layer.
- `mlp_dim`: int.
Dimension of the MLP (FeedForward) layer.
- `channels`: int, default `3`.
Number of image's channels.
- `dropout`: float between `[0, 1]`, default `0.`.
Dropout rate.
- `emb_dropout`: float between `[0, 1]`, default `0`.
Embedding dropout rate.
- `pool`: string, either `cls` token pooling or `mean` pooling


## Simple ViT

<a href="https://arxiv.org/abs/2205.01580">An update</a> from some of the same authors of the original paper proposes simplifications to `ViT` that allows it to train faster and better.

Among these simplifications include 2d sinusoidal positional embedding, global average pooling (no CLS token), no dropout, batch sizes of 1024 rather than 4096, and use of RandAugment and MixUp augmentations. They also show that a simple linear at the end is not significantly worse than the original MLP head

You can use it by importing the `SimpleViT` as shown below

```python
import torch
from vit_pytorch import SimpleViT

v = SimpleViT(
    image_size = 256,
    patch_size = 32,
    num_classes = 1000,
    dim = 1024,
    depth = 6,
    heads = 16,
    mlp_dim = 2048
)

img = torch.randn(1, 3, 256, 256)

preds = v(img) # (1, 1000)
```

## NaViT

<img src="./images/navit.png" width="450px"></img>

<a href="https://arxiv.org/abs/2307.06304">This paper</a> proposes to leverage the flexibility of attention and masking for variable lengthed sequences to train images of multiple resolution, packed into a single batch. They demonstrate much faster training and improved accuracies, with the only cost being extra complexity in the architecture and dataloading. They use factorized 2d positional encodings, token dropping, as well as query-key normalization.

You can use it as follows

```python
import torch
from vit_pytorch.na_vit import NaViT

v = NaViT(
    image_size = 256,
    patch_size = 32,
    num_classes = 1000,
    dim = 1024,
    depth = 6,
    heads = 16,
    mlp_dim = 2048,
    dropout = 0.1,
    emb_dropout = 0.1,
    token_dropout_prob = 0.1  # token dropout of 10% (keep 90% of tokens)
)

# 5 images of different resolutions - List[List[Tensor]]

# for now, you'll have to correctly place images in same batch element as to not exceed maximum allowed sequence length for self-attention w/ masking

images = [
    [torch.randn(3, 256, 256), torch.randn(3, 128, 128)],
    [torch.randn(3, 128, 256), torch.randn(3, 256, 128)],
    [torch.randn(3, 64, 256)]
]

preds = v(images) # (5, 1000) - 5, because 5 images of different resolution above

```

Or if you would rather that the framework auto group the images into variable lengthed sequences that do not exceed a certain max length

```python
images = [
    torch.randn(3, 256, 256),
    torch.randn(3, 128, 128),
    torch.randn(3, 128, 256),
    torch.randn(3, 256, 128),
    torch.randn(3, 64, 256)
]

preds = v(
    images,
    group_images = True,
    group_max_seq_len = 64
) # (5, 1000)
```

Finally, if you would like to make use of a flavor of NaViT using <a href="https://pytorch.org/tutorials/prototype/nestedtensor.html">nested tensors</a> (which will omit a lot of the masking
