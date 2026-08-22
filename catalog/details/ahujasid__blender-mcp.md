# ahujasid/blender-mcp

Community plugin to control Blender 3D with any LLM of your choice

## installation

Three steps: install `uv`, point your MCP client at the server, install the Blender addon.

**1. Install uv**

```bash

## features

| | |
|---|---|
| **Two-way communication** | Connect Claude AI to Blender through a socket-based server |
| **Object manipulation** | Create, modify, and delete 3D objects in Blender |
| **Material control** | Apply and modify materials and colors |
| **Scene inspection** | Get detailed information about the current Blender scene |
| **Code execution** | Run arbitrary Python code in Blender from Claude |
| **Asset & model generation** | Poly Haven assets, Sketchfab models, and AI-generated 3D models via Hyper3D Rodin and Hunyuan3D |

## requirements

- **Blender** 3.0 or newer
- **Python** 3.10 or newer
- **uv** package manager

<details>
<summary><b>Installing uv, per platform</b></summary>

**macOS**
```bash
brew install uv
```

**Windows**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then add uv to the user path in Windows (you may need to restart Claude Desktop after):

```powershell
$localBin = "$env:USERPROFILE\.local\bin"
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
[Environment]::SetEnvironmentVariable("Path", "$userPath;$localBin", "User")
```

**Linux**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

It lands in `~/.local/bin` — open a new shell so it's on your PATH.

Otherwise, installation instructions are on their website: [Install uv](https://docs.astral.sh/uv/getting-started/installation/)

On every OS, use uv's **official installer above — not `pip install uv`**, which may not create the `uvx` command and can hide uv inside an environment your client can't see.
</details>

> **Warning:** Do not proceed before installing uv.

## configuration

The following environment variables can be used to configure the Blender connection:

| Variable | Default | Description |
|---|---|---|
| `BLENDER_HOST` | `localhost` | Host address for Blender socket server |
| `BLENDER_PORT` | `9876` | Port number for Blender socket server |

Example:

```bash
export BLENDER_HOST='host.docker.internal'
export BLENDER_PORT=9876
```

---

## tools

Here are some examples of what you can ask Claude to do:

| Prompt | Demo |
|---|---|
| *"Create a low poly scene in a dungeon, with a dragon guarding a pot of gold"* | [Watch](https://www.youtube.com/watch?v=DqgKuLYUv00) |
| *"Create a beach vibe using HDRIs, textures, and models like rocks and vegetation from Poly Haven"* | [Watch](https://www.youtube.com/watch?v=I29rn92gkC4) |
| Give a reference image, and create a Blender scene out of it | [Watch](https://www.youtube.com/watch?v=FDRb03XPiRo) |
| *"Get information about the current scene, and make a threejs sketch from it"* | [Watch](https://www.youtube.com/watch?v=jxbNI5L7AH8) |
| *"Generate a 3D model of a garden gnome through Hyper3D"* | |
| *"Make this car red and metallic"* | |
| *"Create a sphere and place it above the cube"* | |
| *"Make the lighting like a studio"* | |
| *"Point the camera at the scene, and make it isometric"* | |

---

## limitations

> **Warning:** The `execute_blender_code` tool allows running arbitrary Python code in Blender, which can be powerful but potentially dangerous. Use with caution in production environments. **ALWAYS save your work before using it.**

- Poly Haven requires downloading models, textures, and HDRI images. If you do not want to use it, please turn it off in the checkbox in Blender.
- Complex operations might need to be broken down into smaller steps.
