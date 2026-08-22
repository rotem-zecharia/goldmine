# wiltodelta/remove-ai-watermarks

Remove visible and invisible AI watermarks and provenance metadata from images and video. Python library and CLI for SynthID, C2PA, EXIF, IPTC, XMP, and common generative-AI marks.

## installation

| Need | Install |
| --- | --- |
| Metadata inspection and stripping | `remove-ai-watermarks` |
| Visible detection and removal | `remove-ai-watermarks[visible]` |
| Visible video processing | `remove-ai-watermarks[video]` |
| Video SynthID removal | `remove-ai-watermarks[video,diffusion]` |
| Torch-free DWT-DCT detection | `remove-ai-watermarks[detect]` |
| Invisible image removal (needs CUDA) | `remove-ai-watermarks[qwen-zimage]` |
| Every production feature available on the active Python | `remove-ai-watermarks[all]` |

Lower-level and specialized extras include `pixels`, `heif`, `trustmark`,
`migan`, `lama`, and `diffusion`. The
[installation guide](docs/installation.md#feature-extras) documents their exact
dependency composition, Python compatibility, and model requirements.

## tools

The visible-removal API requires `remove-ai-watermarks[visible]`.

```python
import remove_ai_watermarks as raiw

result, removed = raiw.remove_visible("watermarked.png", "clean.png")
print(removed)

provenance = raiw.identify_video("input.mp4")
report = raiw.inspect_video_metadata("input.mp4")
complete = raiw.remove_video_all("input.mp4", "clean.mp4")
batch = raiw.remove_video_batch("videos", "videos_clean")
cleaned = raiw.remove_video_metadata("input.mp4")
synthid_cleaned = raiw.remove_video_invisible("input.mp4", "synthid_clean.mp4")
visible = raiw.remove_video_visible("input.mp4", "clean.mp4")
print(visible.mark)
veo = raiw.remove_video_visible("veo.mp4", "veo_clean.mp4", mark="veo")
seedance = raiw.remove_video_visible(
    "seedance.mp4",
    "seedance_clean.mp4",
    mark="seedance",
)
dola = raiw.remove_video_visible("dola.mp4", "dola_clean.mp4", mark="dola")
```

The high level API accepts a file path or a BGR NumPy array. For path inputs it
also reads provenance metadata, preserves alpha, and can strip AI metadata from
the written result.

See the [Python API guide](docs/python-api.md) for visible removal, the full
`remove_all` and `remove_batch` pipeline, provenance inspection, metadata
stripping, and diffusion usage.

## limitations

- A missing local signal means unknown, not clean. Proprietary pixel
  watermarks may remain after metadata has been stripped.
- Visible removal reconstructs a small region. Results depend on the background
  and selected fill backend.
- Invisible removal changes the whole image and may alter faces, text, or fine
  detail.
- Visible video removal recognizes the moving Sora 2 wordmark, the current Veo
  diamond plus legacy `Veo` text, the Seedance boxed `AI` label, and the fixed
  Dola, Hailuo, and Kling labels. It does not recognize the older Sora Turbo
  corner swirl or unregistered layouts from those providers.
  The classical OpenCV backend can smear structured backgrounds; use MI-GAN or
  LaMa when recovery quality matters.
- Video SynthID regeneration changes resolution, frame rate, and image detail.
  The shipped profile is oracle-certified, but no public local decoder can
  certify an arbitrary output at runtime. Recheck unusually important outputs
  after provider changes.
- Invisible-watermark removal requires CUDA. Both profiles refuse any other
  device at construction rather than falling back to one that cannot run them.
  Visible removal, metadata stripping and `identify` still run anywhere.
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
the engine's own PSNR is measured before the resize and the encode, so only the
probe sees the delivered picture.

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
reproducible hashes and verdicts live in
`data/evaluations/video-synthid-oracle.csv`.
