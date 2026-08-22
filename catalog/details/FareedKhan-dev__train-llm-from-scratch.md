# FareedKhan-dev/train-llm-from-scratch

A straightforward method for training your LLM, from downloading data to generating text.

## requirements

You need a basic understanding of object oriented programming, neural networks, and PyTorch. Below are some resources to help you get started:

| Topic               | Video Link                                                |
|---------------------|-----------------------------------------------------------|
| OOP                 | [OOP Video](https://www.youtube.com/watch?v=Ej_02ICOIgs) |
| Neural Network      | [Neural Network Video](https://www.youtube.com/watch?v=Jy4wM2X21u0) |
| Pytorch             | [Pytorch Video](https://www.youtube.com/watch?v=V_xro1bcAuA) |

You will need a GPU to train. A free Colab or Kaggle T4 is enough for the 13 million parameter model, but it will not fit a billion parameter model. Here is a rough guide:

| GPU Name                 | Memory | 2B LLM Training | 13M LLM Training | Max Practical LLM Size (Training) |
|--------------------------|--------|-----------------|------------------|-----------------------------------|
| NVIDIA A100              | 40 GB  | ✔               | ✔                | ~6B to 8B                          |
| NVIDIA V100              | 16 GB  | ✘               | ✔                | ~2B                               |
| NVIDIA RTX 4090          | 24 GB  | ✔               | ✔                | ~4B                               |
| NVIDIA RTX 5090          | 32 GB  | ✔               | ✔                | 13M verified, larger configs TBD  |
| NVIDIA RTX 3090          | 24 GB  | ✔               | ✔                | ~3.5B to 4B                        |
| NVIDIA RTX 4080          | 16 GB  | ✘               | ✔                | ~2B                               |
| NVIDIA RTX 4060          | 8 GB   | ✘               | ✔                | ~1B                               |
| Tesla T4                 | 16 GB  | ✘               | ✔                | ~1.5B to 2B                        |

If a large config runs out of memory, the pretraining script has opt-in flags (`--amp`, `--grad-checkpointing`, `--grad-accum`) that bring the memory down a lot. More on those later.

## installation

Clone the repository and install it in editable mode. The editable install puts `config`, `src`, `data_loader`, and `ui` on your import path, so you do not need to set `PYTHONPATH` by hand anymore:

```bash
git clone https://github.com/FareedKhan-dev/train-llm-from-scratch.git
cd train-llm-from-scratch
pip install -e .
```

There are optional extras for the parts you want:

```bash
pip install -e ".[train]"   # datasets + wandb, for downloading data and logging
pip install -e ".[ui]"      # streamlit + pandas + altair, for the control panel
pip install -e ".[docs]"    # mkdocs, for the documentation site
pip install -e ".[all]"     # everything
```

There are two config systems, and it helps to know which is which from the start:

- `config/config.py` is the original, simple config for the legacy pretraining script `scripts/train_transformer.py`. It is plain Python constants.
- `config/post_training_config.py` plus the JSON files in `configs/` drive everything else (pretraining the bigger base, SFT, reward, DPO, PPO, GRPO). You edit a small JSON file per stage, and any field can also be overridden on the command line, for example `--lr 2e-5 --batch_size 16`.

For fast checks there is a tiny `configs/smoke/` variant of every stage that shrinks the model so a full run finishes in seconds on a CPU or a single GPU.

## Code Structure

```bash
train-llm-from-scratch/
├── src/
│   ├── models/                  # the Transformer, built from small pieces
│   │   ├── mlp.py               # the feed-forward block
│   │   ├── attention.py         # single head and multi head attention
│   │   ├── transformer_block.py # one block: attention + MLP + residuals
│   │   └── transformer.py       # the full model: embeddings + blocks + lm_head
│   └── post_training/           # SFT, reward model, PPO, DPO, GRPO, eval, inference
├── config/
│   ├── config.py                # legacy pretraining config (plain constants)
│   ├── post_training_config.py  # dataclasses for every post-training stage
│   └── loader.py                # merges defaults < base.json < stage.json < CLI
├── configs/                     # editable JSON, one file per stage (+ smoke/)
├── data_loader/                 # batch iterators for each kind of data
├── scripts/                     # every runnable step lives here
├── ui/                          # the Streamlit control panel
├── docs/                        # the MkDocs site (theory + diagrams)
├── images/                      # the diagrams in this README (+ the generator)
└── pyproject.toml               # pip install -e .
```

## Step 1: Preparing the Data

A model only ever sees integers. So the first job is always the same: take text, turn it into token ids, and store those ids on disk in a format that is fast to read during training. We do this four times, once for each kind of training we will do later.

![The data pipeline](images/01_data.png)

The four streams are:

1. **Pretraining text** from [The Pile](https://huggingface.co/datasets/monology/pile-uncopyrighted), stored as a flat array of token ids in an HDF5 file.
2. **Instruction data** (Alpaca, Dolly, GSM8K) for SFT, packed into fixed length rows with a mask that says which tokens are the assistant's answer.
3. **Preference pairs** (Anthropic HH-RLHF, UltraFeedback) for the reward model and DPO, stored as `{prompt, chosen, rejected}`.
4. **RL prompts** (GSM8K and a small arithmetic warm-up) for PPO and GRPO, stored as `{prompt, gold}`.

### Tokenization

We use the `r50k_base` tokenizer from OpenAI's `tiktoken`, the same one GPT-3 used. Text becomes a list of integers, and we append a special `<|endoftext|>` token (id 50256) at the end of every document so the model learns where one piece of text stops and the next begins.

![Tokenization](images/02_tokenization.png)

For the legacy path, download a slice of The Pile and tokenize it into HDF5:

```bash
python scripts/data_download.py            # downloads the validation file + 1 training shard
python scri
