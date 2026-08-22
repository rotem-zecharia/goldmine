# infiniflow/infinity

The AI-native database built for LLM applications, providing incredibly fast hybrid search of dense vector, sparse vector, tensor (multi-vector), and full-text.

## features

Infinity comes with high performance, flexibility, ease-of-use, and many features designed to address the challenges facing the next-generation AI applications:

## requirements

- CPU: x86_64 with AVX2 support.
- OS:
  - Linux with glibc 2.17+.
  - Windows 10+ with WSL/WSL2.
  - MacOS
- Python: Python 3.11+.

## installation

#### Linux x86_64 & MacOS x86_64

```bash
sudo mkdir -p /var/infinity && sudo chown -R $USER /var/infinity
docker pull infiniflow/infinity:nightly
docker run -d --name infinity -v /var/infinity/:/var/infinity --ulimit nofile=500000:500000 --network=host infiniflow/infinity:nightly
```
#### Windows

If you are on Windows 10+, you must enable WSL or WSL2 to deploy Infinity using Docker. Suppose you've installed Ubuntu in WSL2:

1. Follow [this](https://learn.microsoft.com/en-us/windows/wsl/systemd) to enable systemd inside WSL2.
2. Install docker-ce according to the [instructions here](https://docs.docker.com/engine/install/ubuntu).
3. If you have installed Docker Desktop version 4.29+ for Windows: **Settings** **>** **Features in development**, then select **Enable host networking**.
4. Pull the Docker image and start Infinity: 

   ```bash
   sudo mkdir -p /var/infinity && sudo chown -R $USER /var/infinity
   docker pull infiniflow/infinity:nightly
   docker run -d --name infinity -v /var/infinity/:/var/infinity --ulimit nofile=500000:500000 --network=host infiniflow/infinity:nightly
   ```

## limitations

See the [Infinity Roadmap 2025](https://github.com/infiniflow/infinity/issues/2393)
