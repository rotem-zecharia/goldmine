# p-e-w/heretic

Fully automatic censorship removal for language models

## tools

Prepare a Python 3.10+ environment with PyTorch 2.2+ installed as appropriate
for your hardware. Then run:

```sh
pip install -U heretic-llm
heretic Qwen/Qwen3-4B-Instruct-2507
```

Replace `Qwen/Qwen3-4B-Instruct-2507` with whatever model you want to decensor.

> [!IMPORTANT]
>
> While PyTorch 2.2 is the minimum version of PyTorch needed for Heretic to work,
> some models and configurations might require features only found in
> later versions. For example, loading MXFP4-quantized models like gpt-oss
> uses `torch.accelerator`, which was added in PyTorch 2.6.

> [!TIP]
>
> Heretic uses [uv](https://docs.astral.sh/uv/) for dependency management,
> and the repository includes a `uv.lock` file pinning every package version.
> If you already use uv (and you probably should!), you can just clone the repo
> and run Heretic with `uv run heretic`, which ensures that your dependencies
> match those used by the developers, improving reliability and security.

The process is fully automatic and does not require configuration; however,
Heretic has a variety of configuration parameters that can be changed for
greater control. Run `heretic --help` to see available command-line options,
or look at [`config.default.toml`](config.default.toml) if you prefer to use
a configuration file.

At the start of a program run, Heretic benchmarks the system to determine
the optimal batch size to make the most of the available hardware.
On an RTX 3090, with the default configuration, decensoring
[Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507)
takes about 20-30 minutes. Note that Heretic supports model quantization with
bitsandbytes, which can drastically reduce the amount of VRAM required to process
models. Set the `quantization` option to `bnb_4bit` to enable quantization.

After Heretic has finished decensoring a model, you are given the option to
save the model, upload it to Hugging Face, chat with it to test how well it works,
run standard benchmarks on it, or any combination of those actions.

## features

In addition to its primary function of removing model censorship, Heretic also
provides features designed to support research into the semantics of model internals
(interpretability). To use those features, you need to install Heretic with the
optional `research` extra:

```sh
pip install -U 'heretic-llm[research]'
```

This gives you access to the following functionality:
