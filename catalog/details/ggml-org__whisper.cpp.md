# ggml-org/whisper.cpp

Port of OpenAI's Whisper model in C/C++

## installation

First clone the repository:

```bash
git clone https://github.com/ggml-org/whisper.cpp.git
```

Navigate into the directory:

```
cd whisper.cpp
```

Then, download one of the Whisper [models](models/README.md) converted in [`ggml` format](#ggml-format). For example:

```bash
sh ./models/download-ggml-model.sh base.en
```

Now build the [whisper-cli](examples/cli) example and transcribe an audio file like this:

```bash
# build the project
cmake -B build
cmake --build build -j --config Release

# transcribe an audio file
./build/bin/whisper-cli -f samples/jfk.wav
```

---

For a quick demo, simply run `make base.en`.

The command downloads the `base.en` model converted to custom `ggml` format and runs the inference on all `.wav` samples in the folder `samples`.

For detailed usage instructions, run: `./build/bin/whisper-cli -h`

Note that the [whisper-cli](examples/cli) example currently runs only with 16-bit WAV files, so make sure to convert your input before running the tool.
For example, you can use `ffmpeg` like this:

```bash
ffmpeg -i input.mp3 -ar 16000 -ac 1 -c:a pcm_s16le output.wav
```

## More audio samples

If you want some extra audio samples to play with, simply run:

```
make -j samples
```

This will download a few more audio files from Wikipedia and convert them to 16-bit WAV format via `ffmpeg`.

You can download and run the other models as follows:

```
make -j tiny.en
make -j tiny
make -j base.en
make -j base
make -j small.en
make -j small
make -j medium.en
make -j medium
make -j large-v1
make -j large-v2
make -j large-v3
make -j large-v3-turbo
```

## tools

| Model  | Disk    | Mem     |
| ------ | ------- | ------- |
| tiny   | 75 MiB  | ~273 MB |
| base   | 142 MiB | ~388 MB |
| small  | 466 MiB | ~852 MB |
| medium | 1.5 GiB | ~2.1 GB |
| large  | 2.9 GiB | ~3.9 GB |

## POWER VSX Intrinsics

`whisper.cpp` supports POWER architectures and includes code which
significantly speeds operation on Linux running on POWER9/10, making it
capable of faster-than-realtime transcription on underclocked Raptor
Talos II. Ensure you have a BLAS package installed, and replace the
standard cmake setup with:

```bash
# build with GGML_BLAS defined
cmake -B build -DGGML_BLAS=1
cmake --build build -j --config Release
./build/bin/whisper-cli [ .. etc .. ]
```

## Quantization

`whisper.cpp` supports integer quantization of the Whisper `ggml` models.
Quantized models require less memory and disk space and depending on the hardware can be processed more efficiently.

Here are the steps for creating and using a quantized model:

```bash
# quantize a model with Q5_0 method
cmake -B build
cmake --build build -j --config Release
./build/bin/quantize models/ggml-base.en.bin models/ggml-base.en-q5_0.bin q5_0

# run the examples as usual, specifying the quantized model file
./build/bin/whisper-cli -m models/ggml-base.en-q5_0.bin ./samples/gb0.wav
```

## Core ML support

On Apple Silicon devices, the Encoder inference can be executed on the Apple Neural Engine (ANE) via Core ML. This can result in significant
speed-up - more than x3 faster compared with CPU-only execution. Here are the instructions for generating a Core ML model and using it with `whisper.cpp`:

- Install Python dependencies needed for the creation of the Core ML model:

  ```bash
  pip install ane_transformers
  pip install openai-whisper
  pip install coremltools
  ```

  - To ensure `coremltools` operates correctly, please confirm that [Xcode](https://developer.apple.com/xcode/) is installed and execute `xcode-select --install` to install the command-line tools.
  - Python 3.11 is recommended.
  - MacOS Sonoma (version 14) or newer is recommended, as older versions of MacOS might experience issues with transcription hallucination.
  - [OPTIONAL] It is recommended to utilize a Python version management system, such as [Miniconda](https://docs.conda.io/en/latest/miniconda.html) for this step:
    - To create an environment, use: `conda create -n py311-whisper python=3.11 -y`
    - To activate the environment, use: `conda activate py311-whisper`

- Generate a Core ML model. For example, to generate a `base.en` model, use:

  ```bash
  ./models/generate-coreml-model.sh base.en
  ```

  This will generate the folder `models/ggml-base.en-encoder.mlmodelc`

- Build `whisper.cpp` with Core ML support:

  ```bash
  # using CMake
  cmake -B build -DWHISPER_COREML=1
  cmake --build build -j --config Release
  ```

- Run the examples as usual. For example:

  ```text
  $ ./build/bin/whisper-cli -m models/ggml-base.en.bin -f samples/jfk.wav

  ...

  whisper_init_state: loading Core ML model from 'models/ggml-base.en-encoder.mlmodelc'
  whisper_init_state: first run on a device may take a while ...
  whisper_init_state: Core ML model loaded

  system_info: n_threads = 4 / 10 | AVX = 0 | AVX2 = 0 | AVX512 = 0 | FMA = 0 | NEON = 1 | ARM_FMA = 1 | F16C = 0 | FP16_VA = 1 | WASM_SIMD = 0 | BLAS = 1 | SSE3 = 0 | VSX = 0 | COREML = 1 |

  ...
  ```

  The first run on a device is slow, since the ANE service compiles the Core ML model to some device-specific format.
  Next runs are faster.

For more information about the Core ML implementation please refer to PR [#566](https://github.com/ggml-org/whisper.cpp/pull/566).

## OpenVINO support

On platforms that support [OpenVINO](https://github.com/openvinotoolkit/openvino), the Encoder inference can be executed
on OpenVINO-supported devices including x86 CPUs and Intel GPUs (integrated & discrete).

This can result in significant speedup in encoder performance. Here are the instructions for generating the Open

## requirements

Supported Platforms

- **Windows 11**
- **Linux** (Ubuntu 24.04 LTS, Python 3.12)

Install the XRT runtime and FlexML runtime for your platform:

- **XRT**: provides the NPU kernel driver and `xrt-smi` diagnostic tool — on Windows this is bundled with the NPU driver; on Linux install it separately following the [NPU driver installation guide](https://ryzenai.docs.amd.com/en/latest/linux.html#install-npu-drivers)
- **FlexML runtime** (`flexmlrt`): VitisAI inference engine used by whisper.cpp — download from the [FlexML runtime releases](https://github.com/lemonade-sdk/whisper.cpp-rocm/releases/tag/deps)

After installing, source the setup scripts in every shell you use to build or run whisper.cpp:

```bash
# Linux
source /opt/xilinx/xrt/setup.sh
source /path/to/flexmlrt/setup.sh
```

```cmd
:: Windows
cd /path/to/flexmlrt && call setup.bat
```

You can verify the NPU is visible with:

```bash
xrt-smi examine
```

### Download models

Download the ggml model and the matching prebuilt VitisAI encoder cache:

```bash
# Linux / macOS
sh ./models/download-ggml-model.sh base
sh ./models/download-vitisai-model.sh base
```

```cmd
:: Windows
.\models\download-ggml-model.cmd base
.\models\download-vitisai-model.cmd base
```

Use the same model name with both scripts. To see all available VitisAI encoder caches:

```bash
sh ./models/download-vitisai-model.sh --list
```

```cmd
.\models\download-vitisai-model.cmd --list
```

The VitisAI script queries the [AMD Ryzen AI Whisper NPU collection on Hugging Face](https://huggingface.co/collections/amd/ryzen-ai-whisper-npu-optimized-onnx-models) and downloads the `.rai` encoder cache as `models/ggml-<model>-encoder-vitisai.rai`.

> Depending on the `.rai` cache, VitisAI may offload the encoder only, or the encoder plus cross-projection layers. whisper.cpp detects this at runtime and logs the selected offload mode during model initialization.

### Build

```bash
cmake -B build -DWHISPER_VITISAI=1
cmake --build build -j --config Release
```

### Run

```bash
./build/bin/whisper-cli -m models/ggml-base.bin -f samples/jfk.wav
```

For more information see the [Ryzen AI documentation](https://ryzenai.docs.amd.com/en/latest/).


## NVIDIA GPU support

With NVIDIA cards the processing of the models is done efficiently on the GPU via cuBLAS and custom CUDA kernels.
First, make sure you have installed `cuda`: https://developer.nvidia.com/cuda-downloads

Now build `whisper.cpp` with CUDA support:

```
cmake -B build -DGGML_CUDA=1
cmake --build build -j --config Release
```

or for newer NVIDIA GPU's (RTX 5000 series):
```
cmake -B build -DGGML_CUDA=1 -DCMAKE_CUDA_ARCHITECTURES="86"
cmake --build build -j --config Release
```

## Vulkan GPU support
Cross-vendor solution which allows you to accelerate workload on your GPU.
First, make sure your graphics card driver provides support for Vulkan API.

Now build `whisper.cpp` with Vulkan support:
```
cmake -B build -DGGML_VULKAN=1
cmake --build build -j --config Release
```

## AMD ROCm GPU support

With AMD GPUs the processing can be accelerated via HIP/ROCm.
First, make sure you have installed [ROCm](https://rocm.docs.amd.com/en/latest/).

Now build `whisper.cpp` with HIP support:

```
cmake -B build -DGGML_HIP=1 -DAMDGPU_TARGETS="gfx1201"
cmake --build build -j --config Release
```

Replace `gfx1201` with your GPU architecture. You can find it with:

```
rocminfo | grep "gfx"
```

Common architectures: `gfx1100` (RX 7900 XTX), `gfx1101` (RX 7800 XT), `gfx1201` (RX 9070 XT).
For multiple GPUs with different architectures: `-DAMDGPU_TARGETS="gfx1100;gfx1201"`.

## BLAS CPU support via OpenBLAS

Encoder processing can be accelerated on the CPU via OpenBLAS.
First, make sure you have installed `openblas`: https://www.openblas.net/

Now build `whisper.cpp` with OpenBLAS support:

```
cmake -B build -DGGML_BLAS=1
cmake --build build -j --config Release
```

## Ascend NPU support

Ascend NPU provides inference acceleration via [`CANN`](https://www.hiascend.com/en/

## limitations

- Inference only

## Real-time audio input example

This is a naive example of performing real-time inference on audio from your microphone.
The [stream](examples/stream) tool samples the audio every half a second and runs the transcription continuously.
More info is available in [issue #10](https://github.com/ggml-org/whisper.cpp/issues/10).
You will need to have [sdl2](https://wiki.libsdl.org/SDL2/Installation) installed for it to work properly.

```bash
cmake -B build -DWHISPER_SDL2=ON
cmake --build build -j --config Release
./build/bin/whisper-stream -m ./models/ggml-base.en.bin -t 8 --step 500 --length 5000
```

https://user-images.githubusercontent.com/1991296/194935793-76afede7-cfa8-48d8-a80f-28ba83be7d09.mp4

## Confidence color-coding

Adding the `--print-colors` argument will print the transcribed text using an experimental color coding strategy
to highlight words with high or low confidence:

```bash
./build/bin/whisper-cli -m models/ggml-base.en.bin -f samples/gb0.wav --print-colors
```

<img width="965" alt="image" src="https://user-images.githubusercontent.com/1991296/197356445-311c8643-9397-4e5e-b46e-0b4b4daa2530.png">

## Controlling the length of the generated text segments (experimental)

For example, to limit the line length to a maximum of 16 characters, simply add `-ml 16`:

```text
$ ./build/bin/whisper-cli -m ./models/ggml-base.en.bin -f ./samples/jfk.wav -ml 16

whisper_model_load: loading model from './models/ggml-base.en.bin'
...
system_info: n_threads = 4 / 10 | AVX2 = 0 | AVX512 = 0 | NEON = 1 | FP16_VA = 1 | WASM_SIMD = 0 | BLAS = 1 |

main: processing './samples/jfk.wav' (176000 samples, 11.0 sec), 4 threads, 1 processors, lang = en, task = transcribe, timestamps = 1 ...

[00:00:00.000 --> 00:00:00.850]   And so my
[00:00:00.850 --> 00:00:01.590]   fellow
[00:00:01.590 --> 00:00:04.140]   Americans, ask
[00:00:04.140 --> 00:00:05.660]   not what your
[00:00:05.660 --> 00:00:06.840]   country can do
[00:00:06.840 --> 00:00:08.430]   for you, ask
[00:00:08.430 --> 00:00:09.440]   what you can do
[00:00:09.440 --> 00:00:10.020]   for your
[00:00:10.020 --> 00:00:11.000]   country.
```

## Word-level timestamp (experimental)

The `--max-len` argument can be used to obtain word-level timestamps. Simply use `-ml 1`:

```text
$ ./build/bin/whisper-cli -m ./models/ggml-base.en.bin -f ./samples/jfk.wav -ml 1

whisper_model_load: loading model from './models/ggml-base.en.bin'
...
system_info: n_threads = 4 / 10 | AVX2 = 0 | AVX512 = 0 | NEON = 1 | FP16_VA = 1 | WASM_SIMD = 0 | BLAS = 1 |

main: processing './samples/jfk.wav' (176000 samples, 11.0 sec), 4 threads, 1 processors, lang = en, task = transcribe, timestamps = 1 ...

[00:00:00.000 --> 00:00:00.320]
[00:00:00.320 --> 00:00:00.370]   And
[00:00:00.370 --> 00:00:00.690]   so
[00:00:00.690 --> 00:00:00.850]   my
[00:00:00.850 --> 00:00:01.590]   fellow
[00:00:01.590 --> 00:00:02.850]   Americans
[00:00:02.850 --> 00:00:03.300]  ,
[00:00:03.300 --> 00:00:04.140]   ask
[00:00:04.140 --> 00:00:04.990]   not
[00:00:04.990 --> 00:00:05.410]   what
[00:00:05.410 --> 00:00:05.660]   your
[00:00:05.660 --> 00:00:06.260]   country
[00:00:06.260 --> 00:00:06.600]   can
[00:00:06.600 --> 00:00:06.840]   do
[00:00:06.840 --> 00:00:07.010]   for
[00:00:07.010 --> 00:00:08.170]   you
[00:00:08.170 --> 00:00:08.190]  ,
[00:00:08.190 --> 00:00:08.430]   ask
[00:00:08.430 --> 00:00:08.910]   what
[00:00:08.910 --> 00:00:09.040]   you
[00:00:09.040 --> 00:00:09.320]   can
[00:00:09.320 --> 00:00:09.440]   do
[00:00:09.440 --> 00:00:09.760]   for
[00:00:09.760 --> 00:00:10.020]   your
[00:00:10.020 --> 00:00:10.510]   country
[00:00:10.510 --> 00:00:11.000]  .
```

## Speaker segmentation via tinydiarize (experimental)

More information about this approach is available here: https://github.com/ggml-org/whisper.cpp/pull/1058

Sample usage:

```py
# download a tinydiarize compatible model
./models/download-ggml-model.sh small.en-tdrz

# run as usual, adding the "-tdrz" com

## configuration

* --vad-threshold: Threshold probability for speech detection. A probability
for a speech segment/frame above this threshold will be considered as speech.

* --vad-min-speech-duration-ms: Minimum speech duration in milliseconds. Speech
segments shorter than this value will be discarded to filter out brief noise or
false positives.

* --vad-min-silence-duration-ms: Minimum silence duration in milliseconds. Silence
periods must be at least this long to end a speech segment. Shorter silence
periods will be ignored and included as part of the speech.

* --vad-max-speech-duration-s: Maximum speech duration in seconds. Speech segments
longer than this will be automatically split into multiple segments at silence
points exceeding 98ms to prevent excessively long segments.

* --vad-speech-pad-ms: Speech padding in milliseconds. Adds this amount of padding
before and after each detected speech segment to avoid cutting off speech edges.

* --vad-samples-overlap: Amount of audio to extend from each speech segment into
the next one, in seconds (e.g., 0.10 = 100ms overlap). This ensures speech isn't
cut off abruptly between segments when they're concatenated together.
