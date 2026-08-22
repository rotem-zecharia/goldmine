# QwenAudio/SenseVoice

Open-source SenseVoiceSmall model for Mandarin, Cantonese, English, Japanese, and Korean ASR, language ID, emotion recognition, and audio event detection.

## requirements

```shell
pip install -r requirements.txt
```

SenseVoiceSmall examples and the composed FunASR diarization path require `funasr>=1.3.26`. If you installed this repository earlier, run `pip install -U "funasr>=1.3.26"` before retrying the demos.

<a name="Usage"></a>

## installation

from pathlib import Path
from funasr_onnx import SenseVoiceSmall
from funasr_onnx.utils.postprocess_utils import rich_transcription_postprocess


model_dir = "iic/SenseVoiceSmall"

model = SenseVoiceSmall(model_dir, batch_size=10, quantize=True)

## tools

```shell
export SENSEVOICE_DEVICE=cuda:0
fastapi run --port 50000
```
