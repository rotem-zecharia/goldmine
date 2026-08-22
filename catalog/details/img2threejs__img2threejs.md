# img2threejs/img2threejs

Rebuild the object in a reference image as a code-only, procedural, quality-gated, animation-ready Three.js model. Token-efficient image-to-3D.

## features

You give it one reference image of an object. It produces a `THREE.Group` factory written in TypeScript that recreates that object from primitives, procedural shaders, and generated geometry — with a runtime hierarchy (pivots, sockets, colliders) so the result is ready to animate, not an inert lump.

It runs under Claude Code, Codex, or OpenCode. It is agent-agnostic: wherever the docs say "agent vision" or "agent browser tool", it uses whatever the host provides — native image reading, a browser MCP, the project preview, or a user-supplied screenshot.

## installation

1. **Install** — place this folder in your skills directory:

   ```bash
   git clone https://github.com/img2threejs/img2threejs.git ~/.claude/skills/img2threejs
   ```

   If you use more than one host, keep a single checkout and point each entrypoint at it as a
   symlink, so they cannot drift apart:

   ```text
   ~/.claude/skills/img2threejs -> <your checkout>
   ~/.codex/skills/img2threejs  -> <your checkout>
   ```

2. **Invoke** — in Claude Code, attach or point to an object image and run:

   ```
   /img2threejs Rebuild this object as a Three.js model, keep the proportions, angles, and colours.
   ```

   That is enough: the skill classifies the subject, runs the detail inventory, and gates every pass on its own.

3. **Follow the pipeline** — the skill validates the image, writes an assessment and spec, generates the factory pass by pass, and shows you a side-by-side comparison at each step until the render matches.

   For a multi-session reconstruction, create a local state index first:

   ```bash
   python3 forge/state.py init --reference <image> --profile character --spec object-sculpt-spec.json
   python3 forge/next.py --state .img2threejs/state.json
   ```

## limitations

**Shipped:**

- **v1.0** — object pipeline: staged sculpt, render-vs-reference review loop, action-ready hierarchy.
- **v1.1** — detail-first analysis: required detail inventory, strict-quality gate.
- **v1.2** — humanoid character generator: anatomy track, proportion-lock and feature-placement passes.
- **v1.3** — quality & efficiency: the Divine Eye deterministic review harness, input-integrity and geometry-truth gates, reference-grounded texture and gradient analysis, CIEDE2000 colour math.
- **v1.4 — The Weapon Update** — CS2 image-matched reconstruction: provenance-aware intake, projection-first finishes, family-specific weapon adapters, and structural review gates.
- **v1.4.1** — CS2 hardening: explicit component coverage, a dedicated Glock-18 assembly contract, map-stripped blockout evidence, and stricter geometry-integrity checks.
- **creature generator** — 4 body plans (quadruped / avian / winged-dragon / serpentine), `animalAnatomy` spec, spine-loft geometry, ΔE00 colour gates.

**Next — one theme per release:**

- **v1.5 — The Character Update** *(in progress)*: character reconstruction, facial features, rigging-ready topology, blendshape preparation, hair and clothing.
- **v1.6 — The Environment Update**: buildings, rooms, streets, vegetation, terrain-aware and multi-object reconstruction.
- **v1.7 — The Game Pipeline Update**: Unity and Unreal exporters, a Blender bridge, LOD and collision-mesh generation.
- **v1.8 — The Animation Update**: auto rigging, auto skin weights, Mixamo compatibility, facial rig.
- **v1.9 — The AI Studio Update**: web UI, batch processing, visual prompt builder, cloud rendering.
- **v2.0 — The Procedural World Update**: multi-view reconstruction, procedural city generation, semantic world understanding, plugin ecosystem and API.

The arc: assets (v1.4–v1.5) → worlds (v1.6–v1.7) → production (v1.8–v1.9) → an AI game-asset platform that generates playable worlds from reference images (v2.0).

**→ Full roadmap** — per-version detail, the four-phase long view, and the tracked capability gaps: **[ROADMAP.md](ROADMAP.md)**. Technical specification: [docs/UPGRADE_PLAN.md](docs/UPGRADE_PLAN.md).

---
