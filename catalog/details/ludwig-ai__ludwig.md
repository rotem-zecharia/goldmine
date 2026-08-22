# ludwig-ai/ludwig

Low-code framework for building custom LLMs, neural networks, and other AI models

## configuration

model_type: llm
base_model: meta-llama/Llama-3.1-8B
adapter:
  type: lora
trainer:
  type: finetune
  epochs: 3
input_features:
  - name: instruction
    type: text
output_features:
  - name: response
    type: text
```

```bash
ludwig train --config model.yaml --dataset my_data.csv
```

**Tech stack:** Python 3.12 · PyTorch 2.7+ · Pydantic 2 · Transformers 5 · Ray 2.54

Ludwig is hosted by the [Linux Foundation AI & Data](https://lfaidata.foundation/).

______________________________________________________________________

## What's New in Ludwig 0.16

| Feature                         | Description                                                                                            |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **PatchTST & N-BEATS encoders** | State-of-the-art timeseries forecasting encoders with MASE/sMAPE metrics                               |
| **Advanced PEFT adapters**      | PiSSA, EVA, CorDA/LoftQ initializers; TinyLoRA, OFT, HRA, WaveFT, LN-Tuning, VBLoRA, C3A adapter types |
| **VLM fine-tuning**             | Train LLaVA, Qwen2-VL, InternVL via `is_multimodal: true` with gated cross-attention                   |
| **HyperNetwork combiner**       | Conditioning-based feature fusion — one feature generates weights for others                           |
| **Nash-MTL & Pareto-MTL**       | Game-theoretic and preference-based multi-task loss balancing                                          |
| **LLM config generation**       | `ludwig generate_config "describe your task"` — LLM writes the YAML for you                            |
| **ModelInspector**              | Architecture analysis, weight collection, feature importance proxy                                     |
| **Ray Serve & KServe**          | Distributed and Kubernetes-native model deployment shims                                               |
| **GRPO alignment**              | Reward-model-free RLHF via Group Relative Policy Optimization                                          |
| **torchao quantization + QAT**  | PyTorch-native `int4/int8/float8` with Quantization-Aware Training                                     |
| **Multi-adapter PEFT**          | Multiple named LoRA adapters with weighted merging (TIES, DARE, SVD)                                   |
| **Native Optuna executor**      | GPT/TPE/CMA-ES samplers, pruning, resumable SQLite/PostgreSQL storage                                  |
| **Timeseries forecasting**      | `model.forecast(dataset, horizon=N)` API with `TimeseriesOutputFeature`                                |
| **Muon & ScheduleFreeAdamW**    | New optimizers for large-scale pretraining and fine-tuning                                             |
| **Image segmentation decoders** | UNet, SegFormer, FPN decoders for semantic segmentation                                                |

______________________________________________________________________

## installation

```bash
pip install ludwig           # core
pip install ludwig[full]     # all optional dependencies
pip install ludwig[llm]      # LLM fine-tuning only
```

Requires Python 3.12+. See [contributing](https://github.com/ludwig-ai/ludwig/blob/main/CONTRIBUTING.md) for a full dependency matrix.

______________________________________________________________________

## Quick Start

### Fine-tune an LLM (instruction tuning)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1c3AO8l_H6V_x37RwQ8V7M6A-RmcBf2tG?usp=sharing)

Ludwig supports the full LLM fine-tuning spectrum:

| Technique                         | Config key                                                               |
| --------------------------------- | ------------------------------------------------------------------------ |
| Supervised fine-tuning (SFT)      | `trainer.type: finetune`                                                 |
| DPO / KTO / ORPO / GRPO alignment | `trainer.type: dpo` (or `kto`, `orpo`, `grpo`)                           |
| LoRA / DoRA / VeRA / PiSSA        | `adapter.type: lora` (or `dora`, `vera`, `lora` + `init_weights: pissa`) |
| 4-bit QLoRA (bitsandbytes)        | `quantization.bits: 4`                                                   |
| torchao + QAT                     | `quantization.backend: torchao`                                          |
| Multi-adapter with merging        | `adapters:` dict + `merge:` block                                        |
| VLM (vision-language)             | `is_multimodal: true`                                                    |

```yaml
model_type: llm
base_model: meta-llama/Llama-3.1-8B

quantization:
  bits: 4

adapter:
  type: lora

prompt:
  template: |
    ### Instruction: {instruction}
    ### Input: {input}
    ### Response:

input_features:
  - name: prompt
    type: text

output_features:
  - name: output
    type: text

trainer:
  type: finetune
  learning_rate: 0.0001
  batch_size: 1
  gradient_accumulation_steps: 16
  epochs: 3
  learning_rate_scheduler:
    decay: cosine
    warmup_fraction: 0.01

backend:
  type: local
```

```bash
export HUGGING_FACE_HUB_TOKEN="<your_token>"
ludwig train --config model.yaml --dataset "ludwig://alpaca"
```

### Train a multimodal classifier

```yaml
input_features:
  - name: review_text
    type: text
    encoder:
      type: bert
  - name: star_rating
    type: number
  - name: product_image
    type: image
    encoder:
      type: dinov2

output_features:
  - name: recommended
    type: binary
```

```bash
ludwig train --config model.yaml --dataset reviews.csv
```

## tools

```bash
ludwig serve --model_path results/experiment_run/model
# POST http://localhost:8000/predict
```

______________________________________________________________________

## features

<details>
<summary><strong>LLM Fine-Tuning</strong></summary>

- **Supervised fine-tuning (SFT)** on instruction/response pairs
- **Alignment training**: DPO, KTO, ORPO, GRPO (reward-model-free RLHF)
- **PEFT adapters**: LoRA, DoRA, VeRA, LoRA+, TinyLoRA, OFT, HRA, WaveFT, LN-Tuning, VBLoRA, C3A
- **LoRA initializers**: PiSSA, EVA, CorDA, LoftQ for improved convergence
- **Multi-adapter PEFT**: multiple named adapters on one base model, switchable at runtime; merge with TIES, DARE, SVD, magnitude pruning
- **Quantization**: 4-bit/8-bit QLoRA (bitsandbytes), torchao int4/int8/float8 with QAT
- **VLM fine-tuning**: LLaVA, Qwen2-VL, InternVL via `is_multimodal: true`
- **Sequence packing** for efficient training on variable-length inputs
- **Paged and 8-bit optimizers** for memory-efficient training

</details>

<details>
<summary><strong>Multimodal & Tabular Models</strong></summary>

- **Input modalities**: text, numbers, categories, binary, sets, bags, sequences, images, audio, timeseries, vectors, dates
- **Text encoders**: any HuggingFace Transformer (BERT, RoBERTa, ModernBERT, Qwen3, Llama-3.1, etc.), plus Mamba-2, Jamba
- **Image encoders**: DINOv2, ConvNeXt, EfficientNet, ViT, CAFormer, ConvFormer, PoolFormer, TIMM (1000+ models)
- **Timeseries encoders**: PatchTST, N-BEATS, CNN, RNN, Transformer; MASE and sMAPE metrics; `model.forecast()` API
- **Combiners**: concat, transformer, tab_transformer, FT-Transformer, TabNet, TabPFN v2, HyperNetwork, ProjectAggregate, GatedFusion, Perceiver
- **Multi-task learning**: multiple output features in a single model; Nash-MTL, Pareto-MTL, FAMO, GradNorm, uncertainty loss balancing
- **Image segmentation**: UNet, SegFormer, FPN decoders

</details>

<details>
<summary><strong>Training Infrastructure</strong></summary>

- **Distributed training**: HuggingFace Accelerate with DDP, FSDP, DeepSpeed (zero-code changes)
- **Ray backend**: training across a Ray cluster, larger-than-memory datasets via Ray Data
- **Automatic batch size selection** and learning rate range test
- **Mixed precision** (fp16/bf16), gradient checkpointing, gradient accumulation
- **Optimizers**: AdamW, Adafactor, SGD, Muon, ScheduleFreeAdamW, Lion, paged/8-bit variants
- **Learning rate schedulers**: cosine, linear, polynomial, reduce-on-plateau, OneCycleLR
- **Model Soup**: uniform and greedy checkpoint averaging for better generalization at zero inference cost
- **Modality dropout** for robust multimodal models

</details>

<details>
<summary><strong>Hyperparameter Optimization</strong></summary>

- **Executors**: Ray Tune (ASHA, PBT, Bayesian) and native Optuna (auto/GP/TPE/CMA-ES)
- **Optuna persistence**: SQLite or PostgreSQL for resumable HPO runs
- **Pruning** with Optuna's MedianPruner and HyperbandPruner
- **Search spaces**: uniform, log-uniform, choice, randint, quantized
- **Full Ludwig config** is searchable — any nested parameter can be a hyperparameter

</details>

<details>
<summary><strong>Production & Deployment</strong></summary>

- **REST API**: FastAPI server with Prometheus metrics and structured logging (`ludwig serve`)
- **vLLM serving**: OpenAI-compatible API with PagedAttention and continuous batching
- **Ray Serve**: distributed deployment with auto-scaling and traffic splitting
- **KServe**: Kubernetes-native deployment with Open Inference Protocol v2
- **Model export**: SafeTensors (default), `torch.export` `.pt2` bundles, ONNX
- **HuggingFace Hub**: `ludwig upload hf_hub` — push model + auto-generated model card
- **Docker**: prebuilt containers at [ludwigai/ludwig](https://hub.docker.com/u/ludwigai)

</details>

<details>
<summary><strong>Tooling & Integrations</strong></summary>

- **Experiment tracking**: TensorBoard, Weights & Biases, Comet ML, MLflow, Aim Stack
- **Model inspection**: `ModelInspector` — weight enumeration, architecture summary, feature importance proxy
- **Visualizations**: learning curves, confusion matrices, calibration plots, ROC curves, hyperopt analysis
- **Au
