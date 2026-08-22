# StarTrail-org/LEANN

[MLsys2026]: RAG on Everything with LEANN. Enjoy 97% storage savings while running a fast, accurate, and 100% private RAG application on your personal device.

## features

<p align="center">
  <img src="assets/effects.png" alt="LEANN vs Traditional Vector DB Storage Comparison" width="70%">
</p>

> **The numbers speak for themselves:** Index 60 million text chunks in just 6GB instead of 201GB. From emails to browser history, everything fits on your laptop. [See detailed benchmarks for different applications below ↓](#-storage-comparison)


🔒 **Privacy:** Your data never leaves your laptop. No OpenAI, no cloud, no "terms of service".

🪶 **Lightweight:** Graph-based recomputation eliminates heavy embedding storage, while smart graph pruning and CSR format minimize graph storage overhead. Always less storage, less memory usage!

📦 **Portable:** Transfer your entire knowledge base between devices (even with others) with minimal cost - your personal AI memory travels with you.

📈 **Scalability:** Handle messy personal data that would crash traditional vector DBs, easily managing your growing personalized data and agent generated memory!

✨ **No Accuracy Loss:** Maintain the same search quality as heavyweight solutions while using 97% less storage.

## installation

[Install uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) first if you don't have it. Typically, you can install it with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## configuration

$env:CMAKE_PREFIX_PATH = "$env:VCPKG_ROOT\installed\x64-windows"
$env:PKG_CONFIG_PATH = "$env:VCPKG_ROOT\installed\x64-windows\lib\pkgconfig"
$env:PKG_CONFIG_EXECUTABLE = "C:\ProgramData\chocolatey\bin\pkg-config.exe"
$env:OPENBLAS_LIB = "$env:VCPKG_ROOT\installed\x64-windows\lib\openblas.lib"
$env:PATH += ";$env:VCPKG_ROOT\installed\x64-windows\bin"
$env:PATH += ";$env:VCPKG_ROOT\installed\x64-windows\tools\protobuf"

uv sync --extra diskann
```

</details>

## tools

--index-dir DIR              # Directory to store the index (default: current directory)
--query "YOUR QUESTION"      # Single query mode. Omit for interactive chat (type 'quit' to exit), and now you can play with your index interactively
--max-items N                # Limit data preprocessing (default: -1, process all data)
--force-rebuild              # Force rebuild index even if it exists
