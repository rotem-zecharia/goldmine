# pascalorg/editor

Create and share 3D architectural projects.

## tools

Tools are activated via the toolbar and handle user input for specific operations:

- **SelectTool** - Selection and manipulation
- **WallTool** - Draw walls
- **ZoneTool** - Create zones
- **ItemTool** - Place furniture/fixtures
- **SlabTool** - Create floor slabs

### Selection Manager

The editor uses a custom selection manager with hierarchical navigation:

```
Site → Building → Level → Zone → Items
```

Each depth level has its own selection strategy for hover/click behavior.

### Editor-Specific Systems

- `ZoneSystem` - Controls zone visibility based on level mode
- Custom camera controls with node focusing

---

## Data Flow

```
User Action (click, drag)
       ↓
Tool Handler
       ↓
useScene.createNode() / updateNode()
       ↓
Node added/updated in store
Node marked dirty
       ↓
React re-renders NodeRenderer
useRegistry() registers 3D object
       ↓
System detects dirty node (useFrame)
Updates geometry via sceneRegistry
Clears dirty flag
```

---

## Building a Plugin

The editor is extensible: a plugin ships node kinds (schema, 3D/2D rendering, placement tools, inspector parametrics) and left-rail panels through the same `Plugin` manifest the built-ins use — there is no separate internal API.

- **Developer guide** — [Create a plugin](https://editor.pascal.app/docs/developers/plugins): the `Plugin` shape, panel contributions, discovery, lifecycle, and what's in/out of v1.
- **Worked example** — [`pascalorg/plugin-trees`](https://github.com/pascalorg/plugin-trees): a standalone plugin with procedural trees, flowers, grass, and a presets panel. Clone it as a starting point.

---

## Technology Stack

- **React 19** + **Next.js 16**
- **Three.js** (WebGPU renderer)
- **React Three Fiber** + **Drei**
- **Zustand** (state management)
- **Zod** (schema validation)
- **Zundo** (undo/redo)
- **three-bvh-csg** (Boolean geometry operations)
- **Turborepo** (monorepo management)
- **Bun** (package manager)

---

## installation

### Development

Run the development server from the **root directory** to enable hot reload for all packages:

```bash
# Install dependencies
bun install

# Run development server (builds packages + starts editor with watch mode)
bun dev

# This will:
# 1. Build @pascal-app/core and @pascal-app/viewer
# 2. Start watching both packages for changes
# 3. Start the Next.js editor dev server
# Open http://localhost:3002
```

**Important:** Always run `bun dev` from the root directory to ensure the package watchers are running. This enables hot reload when you edit files in `packages/core/src/` or `packages/viewer/src/`.

### Building for Production

```bash
# Build all packages
turbo build

# Build specific package
turbo build --filter=@pascal-app/core
```

### Publishing Packages

```bash
# Build packages
turbo build --filter=@pascal-app/core --filter=@pascal-app/viewer

# Publish to npm
npm publish --workspace=@pascal-app/core --access public
npm publish --workspace=@pascal-app/viewer --access public
```

---

## Key Files

| Path | Description |
|------|-------------|
| `packages/core/src/schema/` | Node type definitions (Zod schemas) |
| `packages/core/src/store/use-scene.ts` | Scene state store |
| `packages/core/src/hooks/scene-registry/` | 3D object registry |
| `packages/core/src/systems/` | Geometry generation systems |
| `packages/viewer/src/components/renderers/` | Node renderers |
| `packages/viewer/src/components/viewer/` | Main Viewer component |
| `apps/editor/components/tools/` | Editor tools |
| `apps/editor/store/` | Editor-specific state |

---

## Contributing

Bug fixes, features, docs and ideas are all welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md) for setup, code style and the PR flow.

- New node kinds and sidebar panels ship as [plugins](https://editor.pascal.app/docs/developers/plugins) rather than edits to the built-ins — [`pascalorg/plugin-trees`](https://github.com/pascalorg/plugin-trees) is a worked example
- Questions and ideas go to [Discussions](https://github.com/pascalorg/editor/discussions); reproducible bugs go to [Issues](https://github.com/pascalorg/editor/issues)
- Participation is covered by our [Code of Conduct](CODE_OF_CONDUCT.md)
- Security problems go to [SECURITY.md](SECURITY.md), not a public issue

---

## Contributors

<a href="https://github.com/Aymericr"><img src="https://avatars.githubusercontent.com/u/4444492?v=4" width="60" height="60" alt="Aymeric Rabot" style="border-radius:50%"></a>
<a href="https://github.com/wass08"><img src="https://avatars.githubusercontent.com/u/6551176?v=4" width="60" height="60" alt="Wassim Samad" style="border-radius:50%"></a>
<a href="https://github.com/sudhir9297"><img src="https://avatars.githubusercontent.com/sudhir9297?v=4" width="60" height="60" alt="Sudhir" style="border-radius:50%"></a>

---

<a href="https://trendshift.io/repositories/23831" target="_blank"><img src="https://trendshift.io/api/badge/repositories/23831" alt="pascalorg/editor | Trendshift" width="250" height="55"/></a>
