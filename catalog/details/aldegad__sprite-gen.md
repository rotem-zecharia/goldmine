# aldegad/sprite-gen

Generate clean 2D game sprites & animation atlases — component-row pipeline: state rows, alpha cleanup, frame extraction, runtime atlases. Codex/Claude skill.

## installation

```bash
# 0. install dependencies (Pillow, NumPy) into a fresh virtualenv
python3 -m venv .venv && source .venv/bin/activate
pip install -e .

# 1. prepare a run from a base image
python3 scripts/prepare_sprite_run.py --out-dir <run-dir> --character-id <id> --base-image base.png

# 2. generate one row image per state with the engine-owned provider CLI
python3 scripts/generate_sprite_image.py --provider codex \
  --prompt-file <run-dir>/prompts/<state>.txt \
  --out <run-dir>/raw/<state>.png \
  --ref <run-dir>/base-source.png \
  --ref <run-dir>/references/layout-guides/<state>.png
# 3. extract frames
python3 scripts/extract_sprite_row_frames.py --run-dir <run-dir>

# 4. (optional) curate frames in the webview
python3 scripts/serve_curation.py --run-dir <run-dir>

# 5. bake the runtime atlas
python3 scripts/compose_sprite_atlas.py --run-dir <run-dir>
```

### Editing a finished sheet

When only the combined sheet survives, rebuild a curator-ready run dir, then curate and export:

```bash
# rebuild frames: explicit --grid, --manifest rectangles, or alpha auto-detect (default)
python3 scripts/unpack_atlas_run.py --atlas sheet.png            # auto-detect
python3 scripts/unpack_atlas_run.py --manifest manifest.json     # exact rectangles
python3 scripts/unpack_atlas_run.py --pngs-dir furniture/        # import a loose PNG set

# after curating, bake corrections back to named PNGs
python3 scripts/export_curated_pngs.py --run-dir <run-dir>
```

Output defaults to a findable `<source>-curator` folder next to the input.

### Baking colourways of a finished sheet

Once the atlas is composed, swap selected colours into N finished sheets without
re-running generation. Dot art is exact-match by default; soft-edged art can opt
into a tolerance. Geometry and alpha never move — the base manifest describes
every variant.

```bash
# draft the opaque colours (edit into a recolor spec with kind "sprite-gen-recolor")
python3 -m sprite_gen.cli recolor-palette --base <run-dir>/sprite-sheet-alpha.png --out palette.draft.json

# bake every colourway into <run-dir>/variants/
python3 -m sprite_gen.cli recolor --run-dir <run-dir> --spec recolor.spec.json

# blink-compare and adopt in the curation view
python3 -m sprite_gen.cli curation --run-dir <run-dir>
```

Full spec/report contract and the adopt sidecar field: [`docs/recolor.md`](docs/recolor.md).

### Cutting a background off an imported image

Generated sprites are keyed off their own magenta/green background inside the
pipeline, so they never need this. `cutout` is the import/post-edit utility: an
image that arrived *with* an opaque uniform background (a hand-drawn icon, a
downloaded sprite, a screenshot) is turned into a clean transparent PNG.

<p align="center">
  <img src="docs/assets/cutout-demo.png" width="720" alt="cutout: a white-background game icon turned into a clean transparent PNG, glass highlights preserved" />
</p>

```bash
# routes on the corner colour: white/ivory -> matte, magenta/green -> extract engine
python3 -m sprite_gen.cli cutout icon.png --white-check
```

It reads the corner background colour and routes (`--key auto|white|magenta|green`):

- **white / ivory / solid** → position matte. A corner flood-fill keeps the
  connected background only (bright highlights *inside* the object survive, not
  holed), then a decontaminated soft alpha feathers the border. Tune with
  `--strength` (bevel removal), `--band` (edge depth), `--erode`.
- **magenta / green key** → the project's verified `extract` chroma engine is
  reused as-is. Key colours never appear in objects, so its colour-only cut is
  safe there — exactly where a white matte's flood-fill guard is *not* needed.

`--white-check` writes cyan/magenta/yellow composites so any leftover fringe
shows loudly. For uniform backgrounds; not for complex/non-uniform ones.

The full agent-facing workflow and contracts live in [`SKILL.md`](SKILL.md).

## Install

From Codex skill installer workflows, install this repository as a root 
