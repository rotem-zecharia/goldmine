# mltframework/mlt

MLT Multimedia Framework

## configuration

This repository provides a standardized development environment using the [Development Containers](https://containers.dev/) specification. It is compatible with **VS Code**, **CLion**, **DevPod**, and other IDEs supporting the `.devcontainer` standard.

## requirements

- Docker (or Podman)
- An IDE with Dev Container support.

## installation

Installation is triggered by running:

```bash
sudo cmake --install .
```

This installs the files generated in the `build/` directory, without affecting the project source tree.

> **Note**: After installation, some Linux systems may require running `sudo ldconfig`
> to refresh the shared library cache, especially if the install prefix is not already
> part of the system linker configuration.


---
