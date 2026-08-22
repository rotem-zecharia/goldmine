# mozilla-ai/llamafile

Distribute and run LLMs with a single file.

## installation

Download and run your first llamafile in minutes:

```sh
# Download an example model (Qwen3.5 0.8B)
curl -LO https://huggingface.co/mozilla-ai/llamafile_0.10/resolve/main/Qwen3.5-0.8B-Q8_0.llamafile

# Make it executable (macOS/Linux/BSD)
chmod +x Qwen3.5-0.8B-Q8_0.llamafile

# Run it
./Qwen3.5-0.8B-Q8_0.llamafile
```

We chose this model because that's the smallest one we have
built a llamafile for, so most likely to work out-of-the-box for you.
If you have powerful hardware and/or GPUs, [feel free to choose](https://docs.mozilla.ai/llamafile/getting-started/pre-built-llamafiles)
larger and more expressive models which should provide more accurate
responses.

**Windows users:** Rename the file to add `.exe` extension before running.

**Note - Only executables under 4GB can run on Windows, so any llamafile above 4GB won't work. Download the [llamafile](https://github.com/mozilla-ai/llamafile/releases) binary and run it with any [external weights/models(GGUF)](https://docs.mozilla.ai/llamafile/getting-started/quickstart#using-llamafile-with-external-weights).**

## Documentation

Check the full documentation at [docs.mozilla.ai/llamafile](https://docs.mozilla.ai/llamafile), or directly jump into one of the following subsections:

- [Quickstart](https://docs.mozilla.ai/llamafile/getting-started/quickstart)
- [Pre-built llamafiles](https://docs.mozilla.ai/llamafile/getting-started/pre-built-llamafiles)
- [Running a llamafile](https://docs.mozilla.ai/llamafile/using-llamafile/running_llamafile)
- [Creating llamafiles](https://docs.mozilla.ai/llamafile/using-llamafile/creating_llamafiles)
- [Source installation](https://docs.mozilla.ai/llamafile/using-llamafile/source_installation)
- [Technical details](https://docs.mozilla.ai/llamafile/reference/technical_details)
- [Supported Systems](https://docs.mozilla.ai/llamafile/reference/support)
- [Troubleshooting](https://docs.mozilla.ai/llamafile/reference/troubleshooting)
- [Whisperfile](https://docs.mozilla.ai/llamafile/whisperfile)


## Licensing

While the llamafile project is Apache 2.0-licensed, our changes
to llama.cpp and whisper.cpp are licensed under MIT (just like the projects
themselves) so as to remain compatible and upstreamable in the future,
should that be desired.

The llamafile logo on this page was generated with the assistance of DALL·E 3.


[![Star History Chart](https://api.star-history.com/svg?repos=Mozilla-Ocho/llamafile&type=Date)](https://star-history.com/#Mozilla-Ocho/llamafile&Date)
