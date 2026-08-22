# QwenAudio/Fun-ASR

Open-source LLM-based ASR model family for Chinese, dialect, accent, and multilingual speech, with FunASR, vLLM, streaming, and llama.cpp runtimes.

## features

**Fun-ASR** focuses on high-precision speech recognition, checkpoint-specific multilingual support, and industry customization capabilities.

- **Far-field High-noise Recognition:** Deeply optimized for far-distance sound pickup and high-noise scenarios (such as conference rooms, in-vehicle environments, industrial sites, etc.), improving recognition accuracy to **93%**.
- **Chinese Dialects and Regional Accents:**
  - Supports **7 major dialects**: Wu, Cantonese, Min, Hakka, Gan, Xiang, Jin
  - Covers **26 regional accents**: including Henan, Shaanxi, Hubei, Sichuan, Chongqing, Yunnan, Guizhou, Guangdong, Guangxi and more than 20 other regions
- **Checkpoint-specific language coverage:** Fun-ASR-Nano supports Chinese, English, Japanese, and Chinese dialects and accents. Fun-ASR-MLT-Nano supports **31 languages**, with emphasis on East and Southeast Asian languages.
- **Music Background Lyric Recognition:** Enhanced speech recognition performance under music background interference, supporting accurate recognition of lyric content in songs.

## installation

```shell
git clone https://github.com/QwenAudio/Fun-ASR.git
cd Fun-ASR
pip install -r requirements.txt
```

<a name="usage-tutorial"></a>
