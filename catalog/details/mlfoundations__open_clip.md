# mlfoundations/open_clip

An open source implementation of CLIP.

## tools

```
pip install open_clip_torch
```

```python
import torch
from PIL import Image
import open_clip

model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
model.eval()  # model in train mode by default, impacts some models with BatchNorm or stochastic depth active
tokenizer = open_clip.get_tokenizer('ViT-B-32')

image = preprocess(Image.open("docs/CLIP.png")).unsqueeze(0)
text = tokenizer(["a diagram", "a dog", "a cat"])

with torch.no_grad(), torch.autocast("cuda"):
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)

    text_probs = (100.0 * image_features @ text_features.T).softmax(dim=-1)

print("Label probs:", text_probs)  # prints: [[1., 0., 0.]]
```

If model uses `timm` image encoders (convnext, siglip, eva, etc) ensure the latest timm is installed. Upgrade `timm` if you see 'Unknown model' errors for the image encoder.

If model uses transformers tokenizers, ensure `transformers` is installed.

See also this [[Clip Colab]](https://colab.research.google.com/github/mlfoundations/open_clip/blob/master/docs/Interacting_with_open_clip.ipynb).

To compute billions of embeddings efficiently, you can use [clip-retrieval](https://github.com/rom1504/clip-retrieval) which has openclip support.

### Pretrained models

We offer a simple model interface to instantiate both pre-trained and untrained models.
To see which pretrained models are available, use the following code snippet.
More details about our pretrained models are available [here](docs/PRETRAINED.md).

```python
>>> import open_clip
>>> open_clip.list_pretrained()
```

You can find more about the models we support (e.g. number of parameters, FLOPs) in [this table](docs/model_profile.csv).

NOTE: Many existing checkpoints use the QuickGELU activation from the original OpenAI models. This activation is actually less efficient than native torch.nn.GELU in recent versions of PyTorch. The model defaults are now nn.GELU, so one should use model definitions with `-quickgelu` postfix for the OpenCLIP pretrained weights. All OpenAI pretrained weights will always default to QuickGELU. One can also use the non `-quickgelu` model definitions with pretrained weights using QuickGELU but there will be an accuracy drop, for fine-tune that will likely vanish for longer runs.
Future trained models will use nn.GELU.

### Loading models

Models can be loaded with `open_clip.create_model_and_transforms`, as shown in the example below. The model name and corresponding `pretrained` keys are compatible with the outputs of `open_clip.list_pretrained()`. 

The `pretrained` argument also accepts local paths, for example `/path/to/my/b32.pt`.
You can also load checkpoints from huggingface this way. To do so, download the `open_clip_pytorch_model.bin` file (for example, [https://huggingface.co/laion/CLIP-ViT-L-14-DataComp.XL-s13B-b90K/tree/main](https://huggingface.co/laion/CLIP-ViT-L-14-DataComp.XL-s13B-b90K/blob/main/open_clip_pytorch_model.bin)), and use `pretrained=/path/to/open_clip_pytorch_model.bin`.

```python
# pretrained also accepts local paths
model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k') 
```

## Fine-tuning on classification tasks

This repository is focused on training CLIP models. To fine-tune a *trained* zero-shot model on a downstream classification task such as ImageNet, please see [our other repository: WiSE-FT](https://github.com/mlfoundations/wise-ft). The [WiSE-FT repository](https://github.com/mlfoundations/wise-ft) contains code for our paper on [Robust Fine-tuning of Zero-shot Models](https://arxiv.org/abs/2109.01903), in which we introduce a technique for fine-tuning zero-shot models while preserving robustness under distribution shift.

## Data

To download datasets as webdataset, we recommend [img2d

## installation

We advise you first create a virtual environment with:

```
python3 -m venv .env
source .env/bin/activate
pip install -U pip
```

You can then install openclip for training with `pip install 'open_clip_torch[training]'`.

#### Development

If you want to make changes to contribute code, you can clone openclip then run `make install` in openclip folder (after creating a virtualenv)

Install pip PyTorch as per https://pytorch.org/get-started/locally/

You may run `make install-training` to install training deps

#### Testing

Test can be run with `make install-test` then `make test`

`python -m pytest -x -s -v tests -k "training"` to run a specific test

Running regression tests against a specific git revision or tag:
1. Generate testing data
    ```sh
    python tests/util_test.py --model RN50 RN101 --save_model_list models.txt --git_revision 9d31b2ec4df6d8228f370ff20c8267ec6ba39383
    ```
    **_WARNING_: This will invoke git and modify your working tree, but will reset it to the current state after data has been generated! \
    Don't modify your working tree while test data is being generated this way.**

2. Run regression tests
    ```sh
    OPEN_CLIP_TEST_REG_MODELS=models.txt python -m pytest -x -s -v -m regression_test
    ```

### Sample single-process running code:

```bash
python -m open_clip_train.main \
    --save-frequency 1 \
    --zeroshot-frequency 1 \
    --report-to tensorboard \
    --train-data="/path/to/train_data.csv"  \
    --val-data="/path/to/validation_data.csv"  \
    --csv-img-key filepath \
    --csv-caption-key title \
    --imagenet-val=/path/to/imagenet/root/val/ \
    --warmup 10000 \
    --batch-size=128 \
    --lr=1e-3 \
    --wd=0.1 \
    --epochs=30 \
    --workers=8 \
    --model RN50
```

Note: `imagenet-val` is the path to the *validation* set of ImageNet for zero-shot evaluation, not the training set!
You can remove this argument if you do not want to perform zero-shot evaluation on ImageNet throughout training. Note that the `val` folder should contain subfolders. If it does not, please use [this script](https://raw.githubusercontent.com/soumith/imagenetloader.torch/master/valprep.sh).

### torch.compile

Training supports `torch.compile` via `--torchcompile`. Use `--torchcompile-strategy task` for the common case: it compiles the task train/eval forward callables while keeping the `TrainingTask` object itself unwrapped for checkpointing, batch preparation, eval, and zero-shot helpers. Use `--torchcompile-strategy model` when you want the lower-risk pre-DDP behavior of compiling only the underlying trainable module, especially for fp16 AMP runs that need a `GradScaler`. Use `--torchcompile-strategy step` for the most aggressive single-batch path: it compiles forward, loss, backward, optional grad clipping, optimizer step, and logit-scale clamp, but requires `--accum-freq 1` and a precision mode without `GradScaler` such as the default `amp_bf16` or `fp32`. `--torchcompile-backend` and `--torchcompile-mode` are passed through to `torch.compile`.

### Multi-GPU and Beyond

This code has been battle tested up to 1024 A100s and offers a variety of solutions
for distributed training. We include native support for SLURM clusters.

As the number of devices used to train increases, so does the space complexity of
the the logit matrix. Using a naïve all-gather scheme, space complexity will be
`O(n^2)`. Instead, complexity may become effectively linear if the flags
`--gather-with-grad` and `--local-loss` are used. This alteration results in one-to-one
numerical results as the naïve method.

#### Epochs

For larger datasets (eg Laion2B), we recommend setting `--train-num-samples` to a lower value than the full epoch, for example `--train-num-samples 135646078` to 1/16 of an epoch in conjunction with `--dataset-resampled` to do sampling with replacement. This allows having frequent checkpoints to evaluate more often.

#### Patch Dropout

<a href="https://arxiv.org/abs/2212.00794">Recent research</
