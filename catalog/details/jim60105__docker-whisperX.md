# jim60105/docker-whisperX

Dockerfile for WhisperX: Automatic Speech Recognition with Word-Level Timestamps and Speaker Diarization (Dockerfile, CI image build and test)

## tools

Mount the current directory as `/app` and run WhisperX with additional input arguments:

```bash
docker run --gpus all -it -v ".:/app" whisperx:large-v3-ja -- --output_format srt audio.mp3
```

> [!NOTE]  
> Remember to prepend `--` before the arguments.  
> `--model` and `--language` args are defined in Dockerfile, no need to specify.

## 📝 LICENSE

> The main program, WhisperX, is distributed under [the BSD-4 license](https://github.com/m-bain/whisperX/blob/main/LICENSE).  
> Please consult their repository for access to the source code and license.

The Dockerfile and CI workflow files in this repository are licensed under [the MIT license](LICENSE).
