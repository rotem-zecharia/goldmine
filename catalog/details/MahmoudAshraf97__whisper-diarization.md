# MahmoudAshraf97/whisper-diarization

Automatic Speech Recognition with Speaker Diarization based on OpenAI Whisper

## installation

Python >= `3.10` is needed, `3.9` will work but you'll need to manually install the requirements one by one.

`FFMPEG` and `Cython` are needed as prerequisites to install the requirements
```shell
pip install cython
```
or
```shell
sudo apt update && sudo apt install cython3
```
```shell
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg

# on Windows using WinGet (https://github.com/microsoft/winget-cli)
winget install ffmpeg
```
```shell
pip install -c constraints.txt -r requirements.txt
```

## tools

```shell
python diarize.py -a AUDIO_FILE_NAME
```

If your system has enough VRAM (>=10GB), you can use `diarize_parallel.py` instead, the difference is that it runs NeMo in parallel with Whisper, this can be beneficial in some cases and the result is the same since the two models are nondependent on each other. This is still experimental, so expect errors and sharp edges. Your feedback is welcome.

## configuration

- `-a AUDIO_FILE_NAME`: The name of the audio file to be processed
- `--no-stem`: Disables source separation
- `--whisper-model`: The model to be used for ASR, default is `medium.en`
- `--suppress_numerals`: Transcribes numbers in their pronounced letters instead of digits, improves alignment accuracy
- `--device`: Choose which device to use, defaults to "cuda" if available
- `--language`: Manually select language, useful if language detection failed
- `--batch-size`: Batch size for batched inference, reduce if you run out of memory, set to 0 for non-batched inference

## limitations

- Overlapping speakers are yet to be addressed, a possible approach would be to separate the audio file and isolate only one speaker, then feed it into the pipeline but this will need much more computation
- There might be some errors, please raise an issue if you encounter any.

## Future Improvements
- Implement a maximum length per sentence for SRT

## Acknowledgements
Special Thanks for [@adamjonas](https://github.com/adamjonas) for supporting this project
This work is based on [OpenAI's Whisper](https://github.com/openai/whisper) , [Faster Whisper](https://github.com/guillaumekln/faster-whisper) , [Nvidia NeMo](https://github.com/NVIDIA/NeMo) , and [Facebook's Demucs](https://github.com/facebookresearch/demucs)

## Citation
If you use this in your research, please cite the project:

```bibtex
@unpublished{hassouna2024whisperdiarization,
  title={Whisper Diarization: Speaker Diarization Using OpenAI Whisper},
  author={Ashraf, Mahmoud},
  year={2024}
}
```
