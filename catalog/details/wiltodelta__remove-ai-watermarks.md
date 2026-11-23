# wiltodelta/remove-ai-watermarks

Remove visible and invisible AI watermarks from images and video, clean supported audio watermarks, and strip AI provenance metadata. Python library, CLI, and agent skill for SynthID, C2PA, and other 

## installation

| Need | Install |
| --- | --- |
| Metadata inspection and stripping | `remove-ai-watermarks` |
| 10-provider source-export & model-version classification | `remove-ai-watermarks[source-classify]` |
| Visible detection and removal | `remove-ai-watermarks[visible]` |
| Visible video processing | `remove-ai-watermarks[video]` |
| Public VideoSeal/PixelSeal/ChunkySeal checks | `remove-ai-watermarks[video-detect]`, add `diffusion` for VAE |
| Video SynthID removal | `remove-ai-watermarks[video,diffusion]` |
| Audio sample processing and spectral disruption | `remove-ai-watermarks[audio]` |
| Compatible public audio watermark detection (AudioSeal) | `remove-ai-watermarks[audio-detect]` |
| Neural audio codec resynthesis (EnCodec / DAC / SNAC) | `remove-ai-watermarks[audio-codec]` |
| Torch-free DWT-DCT detection | `remove-ai-watermarks[detect]` |
| Direct local Paint InvisMark disruption | `remove-ai-watermarks[pixels]` |
| Invisible image removal (needs CUDA) | `remove-ai-watermarks[qwen-zimage]` |
| Production removal and default classifier backends | `remove-ai-watermarks[all]` |
| Optional OCR proposals for operator verification | `remove-ai-watermarks[text-draft]` |

Lower-level and specialized extras include `pixels`, `heif`, `trustmark`,
`migan`, `lama`, `diffusion`, `source-classify`,
`audio-wavmark`, `audio-perth`, and `audio-silentcipher`. The
[installation guide](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/installation.md#feature-extras) documents their exact
dependency composition, Python compatibility, and model requirements.

## Quick start

Install the metadata-focused default CLI:

```bash
uv tool install remove-ai-watermarks
```

Inspect an image:

```bash
remove-ai-watermarks identify image.png
```

For an abstaining, CPU-only 10-provider source-export and model-version
classifier from pixels after metadata removal (`classify_source` and CLI
`classify-source`), install `source-classify`. `identify` never runs it, and it
is not a SynthID detector:

```bash
uv tool install --force "remove-ai-watermarks[source-classify]"
remove-ai-watermarks classify-source image.png
```

```python
import remove_ai_watermarks as raiw

result = raiw.classify_source("image.png")
print(result.label, result.version_subfamily, result.synthetic_detected, result.confidence)
```

Guide: [source-pipeline classification](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/source-classify.md). Model card and weights: [`wiltodelta/raiw-source-classify` on Hugging Face](https://huggingface.co/wiltodelta/raiw-source-classify) and [GitHub](https://github.com/wiltodelta/raiw-source-classify).

Signed provenance is the supported route for SynthID and `identify` reads it.
There is no local SynthID pixel detector in the package. Research on a
periodic lattice expert is in `scripts/synthid_runtime/` and
[synthid-detector-research.md](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/synthid-detector-research.md).

For visible watermark removal, install the pixel dependencies:

```bash
uv tool install --force "remove-ai-watermarks[visible]"
```

Then remove a known visible mark and AI metadata:

```bash
remove-ai-watermarks visible image.png -o clean.png
```

Strip metadata without running visible inpainting or diffusion:

```bash
remove-ai-watermarks metadata image.png --remove -o clean.png
```

Without `-o` this command overwrites the source in place.

Inspect or remove AI metadata from an MP4, MOV, M4V, WebM, MKV, AVI, or FLV
file:

```bash
remove-ai-watermarks video metadata input.mp4 --check
remove-ai-watermarks video metadata input.mp4 --remove -o clean.mp4
```

The `video metadata` command does not transcode video or audio streams. Unlike
the image command above, when `-o` is omitted it writes `<source>_clean` and
preserves the original. MP4 and MOV
inspection includes the native TC260 `AIGC` tag in
`moov.udta.meta.keys/ilst`, including a `moov` placed after the media payload,
plus the QuickTime-

## tools

### Visible Gemini mark

The `after` raster at the top of this page is generated from the tracked `before`
raster by the public path:

```bash
uv run remove-ai-watermarks visible demo_banana_before.png \
  --backend cv2 -o demo_banana_after.png
```

### High quality invisible removal

`qwen-zimage` is the default profile: a Qwen-Image-2512 Lightning pass under Canny
ControlNet, followed by SAM-masked Z-Image repair of any detected face. The
alternative, `sdxl-zimage`, swaps the global stage for SDXL and keeps the same face
stage. `chroma-zimage` uses the Apache-2.0 Chroma1 global pass with its own flat
vendor floors; see `docs/chroma1-engine-research.md` for the calibration. An opt-in
profile, `qwen21-zimage`, swaps the global stage for Qwen-Image-2.1 (with
`madebyollin/texture-fix-vae-for-qwen-image-2.1` and `Qwen-Image-2.1-Fun-Controlnet-Union`
Canny); because `Qwen/Qwen-Image-2.1` is released under the Qwen Research License,
`qwen21-zimage` is for non-commercial research, evaluation, and personal use only
(not for commercial use). `--pipeline auto` picks sdxl-zimage for Google,
chroma-zimage for Microsoft, and qwen-zimage otherwise, keeping `auto` commercial-safe.
All are CUDA only.

Since 0.57.0, `qwen21-zimage` includes bounded geometric alignment by default after the shared
Qwen-2.1 global and face stages, accepting a result only when both source MSE and local LPIPS improve.
It retains the Qwen Research License restrictions. Qualified text geometry can
be supplied through the Python API; the CLI does not run automatic OCR. See
[the fidelity profile](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/cli.md#fidelity-profile) for limits and fallback behavior.

```bash
uv tool install --force "remove-ai-watermarks[qwen-zimage]"
remove-ai-watermarks invisible image.png -o clean.png --force
```

| OpenAI example before | OpenAI example after |
| --- | --- |
| [![OpenAI portrait grid before qwen-zimage](https://raw.githubusercontent.com/wiltodelta/remove-ai-watermarks/main/data/synthid/originals/ChatGPT%20Image%20May%2030,%202026,%2010_31_08%20AM.png)](https://raw.githubusercontent.com/wiltodelta/remove-ai-watermarks/main/data/synthid/originals/ChatGPT%20Image%20May%2030,%202026,%2010_31_08%20AM.png) | [![OpenAI portrait grid after qwen-zimage](https://raw.githubusercontent.com/wiltodelta/remove-ai-watermarks/main/docs/images/qwen-zimage/ChatGPT/ChatGPT%20Image%20May%2030,%202026,%2010_31_08%20AM_full_clean.png)](https://raw.githubusercontent.com/wiltodelta/remove-ai-watermarks/main/docs/images/qwen-zimage/ChatGPT/ChatGPT%20Image%20May%2030,%202026,%2010_31_08%20AM_full_clean.png) |

| Gemini example before | Gemini example after |
| --- | --- |
| [![Gemini sign before qwen-zimage](https://raw.githubusercontent.com/wiltodelta/remove-ai-watermarks/main/data/synthid/originals/Gemini_Generated_Image_633uuy633uuy633u.png)](https://raw.githubusercontent.com/wiltodelta/remove-ai-watermarks/main/data/synthid/originals/Gemini_Generated_Image_633uuy633uuy633u.png) | [![Gemini sign after qwen-zimage](https://raw.githubusercontent.com/wiltodelta/remove-ai-watermarks/main/docs/images/qwen-zimage/Gemini/Gemini_Generated_Image_633uuy633uuy633u_full_clean.png)](https://raw.githubusercontent.com/wiltodelta/remove-ai-watermarks/main/docs/images/qwen-zimage/Gemini/Gemini_Generated_Image_633uuy633uuy633u_full_clean.png) |

These exact output files were checked with the matching provider verifiers. That
result applies to these files, not to every seed, image, or future watermark
version.

### Popular formats and invisible watermarks (images, video, audio, text)

One command (`remove-ai-watermarks all <file> -o <clean>`) handles visible marks,
provenance-triggered invisible removal, and metadata stripping across images
(`PNG`, `JPG`, `WebP`, `HEIC`, `TIFF`), video (`MP4`, `MOV`, `M4V`, `WebM`, `MKV`, `AVI`, `FLV`,
including 10-bit HEVC/HDR), audio (`WAV`, `FLAC`, `MP3`, `M4A`, `OGG`, `OGA`, `Opus`, `AAC`, `MKA`),
and text (`MD`, `HT

## limitations

- A missing local signal means unknown, not clean. Proprietary pixel
  watermarks may remain after metadata has been stripped.
  [What each path leaves behind](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/known-limitations.md#what-each-path-leaves-behind)
  lists, per command, what may remain and how to check it.
- Visible removal reconstructs a small region. Results depend on the background
  and selected fill backend.
- Invisible removal changes the whole image and may alter faces, text, or fine
  detail.
- Visible video removal recognizes the moving Sora 2 wordmark, the current Veo
  diamond plus legacy `Veo` text, the Seedance boxed `AI` label, and the fixed
  Doubao, Dola, Hailuo AI, Vidu, and Kling AI labels. It does not recognize the older Sora Turbo
  corner swirl or unregistered layouts from those providers.
  The classical OpenCV backend can smear structured backgrounds; use MI-GAN or
  LaMa when recovery quality matters.
- Video SynthID regeneration changes resolution, frame rate, and image detail.
  The shipped profile is oracle-certified, but no public local decoder can
  certify an arbitrary output at runtime. Recheck unusually important outputs
  after provider changes.
- Invisible-watermark removal through the CLI and high-level API requires CUDA.
  All diffusion profiles refuse any other device at construction rather than
  falling back to one that cannot run them. The specialized local Paint API,
  visible removal, metadata stripping and `identify` run without CUDA.
- Provider watermark systems can change. Validate important outputs with the
  provider's own verifier when one is available.

The shipped `video invisible` command uses the certified `noise_std=0.15`
profile. The companion `scripts/video_synthid_sweep.py` research harness builds
a matched re-encode control plus VAE-regenerated candidates and leaves the
verifier verdict blank:

```bash
uv run --extra video --extra diffusion python scripts/video_synthid_sweep.py input.mp4 -o sweep/
```

To score what an output actually cost, use `scripts/video_fidelity_probe.py`:
the engine's own PSNR is measured after the input resize and before final
encoding, so only the probe sees the delivered picture.

```bash
uv run --extra video python scripts/video_fidelity_probe.py input.mp4 input_clean.mp4
```

The control must still be SynthID-positive before a negative candidate can
count as removal evidence. In the 2026-07-29 two-clip calibration, both matched
controls were positive in Gemini's built-in SynthID verifier; the stronger
candidate was negative on both carriers, while a weaker candidate was
negative on one. A later adversarial follow-up that asked ordinary Gemini to
reinterpret the pixel result returned `UNAVAILABLE`; that follow-up was not a
verifier rerun and does not invalidate the built-in verdicts. A 2026-07-31
full-clip check on a public eight-second Veo sample found `0.10` still detected
and `0.15` not detected, so `0.15` is now the certified default. The
reproducible hashes and verdicts for that full-clip check -- one carrier, two
rows -- live in `data/evaluations/video-synthid-oracle.csv`. The earlier
two-clip calibration is narrative only: its verdicts were not recorded in a
tracked manifest, so treat the certified default as resting on the 2026-07-31
rows.

## Documentation

Start with the [documentation index](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/index.md).

- [Installation](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/installation.md)
- [CLI guide](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/cli.md)
- [Python API](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/python-api.md)
- [Supported signals](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/supported-signals.md)
- [Known limitations](https://github.com/wiltodelta/remove-ai-watermarks/blob/main/docs/known-limitations.md)
- [Scope, safety, and legal notes](https://
