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

## installation

```bash
pip install ludwig           # core
pip install ludwig[full]     # all optional dependencies
pip install ludwig[llm]      # LLM fine-tuning only
```

Requires Python 3.12+. See [contributing](https://github.com/ludwig-ai/ludwig/blob/main/CONTRIBUTING.md) for a full dependency matrix.

______________________________________________________________________

## tools

```bash
ludwig serve --model_path results/experiment_run/model

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
