# tejaswigowda/ffmpeg-webCLI

A browser-based video editor powered by ffmpeg.wasm. No uploads, no servers -- all processing happens locally in your browser using WebAssembly.

## features

<img src='demos/features.png'/>


✓ **No Server Uploads** : All video processing happens entirely on your device

✓ **30+ Video Operations** : GIF creation, format conversion, compression, trimming, effects, filters, auto-captioning, and more

✓ **Batch Processing** : Process multiple videos at once with the same operation - or an entire **operation chain** - applied to every file; real-time progress, per-file preview, individual downloads, ZIP-all, and graceful fallback

✓ **Offline-First PWA** : Works completely offline after first use; install as a native app

✓ **Screen Wake Lock** : Screen stays active during video processing on any device

✓ **Live Previews** : See output size estimates and live settings adjustments

✓ **Multi-Format Support** : MP4, WebM, MKV, MOV, AVI, GIF, MP3, AAC, WAV, OGG, FLAC, JPG, PNG

✓ **Advanced Features** : Raw ffmpeg command access, subtitle embedding, concatenation, picture-in-picture, audio mixing

✓ **Fast & Responsive** : Uses Web Workers for background processing

✓ **Privacy First** : Zero data collection; works with your files locally

---

## tools

Cloud tools like CloudConvert, Kapwing, Ezgif, and Otter handle these same tasks. Every one of them uploads your file to a server. Some are free with ads, some charge, but all of them see your file, and all are subject to data breaches, subpoenas, and shifting privacy policies.

`ffmpeg-webCLI` does format conversion, trimming, compression, GIF creation, audio extraction, captioning, and more **all in your browser, for free**. Reach for it when your files are private, when you can't install software, or when you'd simply rather not upload. Your video never leaves your device.

---

## Use Cases

### ▶ GIF Maker
Convert any video clip into an animated GIF. Set the frame rate and output width; height scales automatically to preserve the aspect ratio. Uses a two-pass palette generation for the best possible color quality.

<img src='demos/makegif.gif'>

### ↻ Video Format Converter
Re-encode a video to a different container and codec:
- **MP4** : H.264 + AAC, widest compatibility
- **WebM** : VP9 + Opus, open format optimised for the web (~45% smaller than MP4 at similar quality)
- **MKV / MOV** : H.264 + AAC in alternative containers
- **AVI** : legacy compatibility

### ⊟ Video Compression
Reduce file size without changing the resolution. Dial in the quality with a **CRF slider** (18 = near-lossless → 51 = maximum compression) and pick an encoding **preset** (ultrafast → veryslow) to trade encoding speed for compression efficiency. A live size estimate updates as you adjust the settings.

### ▤ Video Trimming
Set a start and end point with the timeline sliders before running any operation. Trimming is applied on top of every other operation, so you can, for example, extract a short clip, compress it, and convert it to GIF all at once.

### ⊞ Resize & Compress
Change the output dimensions and compress in one pass. Width and height are auto-filled from the source video; edit either value or leave it blank to let ffmpeg maintain the aspect ratio. Combines a `scale` filter with CRF-based H.264 encoding.

### ♪ Audio Extraction
Pull the audio track out of any video into a standalone audio file:
- **MP3** : universal playback
- **AAC** : efficient lossy, great for mobile
- **WAV** : uncompressed PCM
- **OGG Vorbis** : open lossy format
- **FLAC** : lossless compression

### ⊘ Mute Video
Strip the audio stream entirely. Output is the original video with no audio track -- useful for silent loops, social media clips, or before replacing the audio elsewhere.

### ▶ Speed Change
Speed up or slow down playback (0.25× – 4×). Both the video PTS and the `atempo` audio filter chain are adjusted so audio pitch and sync are preserved. Chains multiple `atempo` stages automatically when the multiplier is outside the 0.5–2.0 range that a single filter accepts.

### ↻ Rotate / Flip
Correct orientation or create mirror effects without re-uploading. Options: 90° clockwise, 90° counter-clockwise, 180°, flip horizontal, flip vertical, or flip both axes.

<img src='demos/invert.gif'>

### ▤ Crop
Trim the frame to a specific region. X/Y offset and width/height are auto-filled from the source video dimensions so you can immediately drag values down rather than starting from scratch.

### ▭ Thumbnail Extractor
Pull a single frame from any point in the video and save it as a **JPEG** or **PNG** image. The timestamp field is pre-filled to the midpoint of the loaded clip.

The frame is always extracted as a PNG (ffmpeg's `-frames:v 1`); JPEG output is then produced in-browser via a canvas. This works around a crash (`memory access out of bounds`) in the WebAssembly core's MJPEG encoder, so JPEG thumbnails stay reliable across all clips, including high-frame-rate and variable-frame-rate sources.

### ⟲ Reverse
Play the video (and audio) backwards using ffmpeg's `reverse` + `areverse` filters. The reverse filter buffers the entire video into memory for processing, which combined with re-encoding makes it memory-intensive. Works in single mode; **not supported in
