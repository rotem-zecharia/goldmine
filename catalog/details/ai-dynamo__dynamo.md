# ai-dynamo/dynamo

A Datacenter Scale Distributed Inference Serving Framework

## features

| Capability | What it does | Why it matters |
|------------|-------------|----------------|
| [**Disaggregated Prefill/Decode**](https://docs.nvidia.com/dynamo/dev/knowledge-base/concepts/system-architecture/disaggregated-serving) | Separates prefill and decode into independently scalable GPU pools | Maximizes GPU utilization; each phase runs on hardware tuned for its workload |
| [**KV-Aware Routing**](https://docs.nvidia.com/dynamo/components/router) | Routes requests based on worker load and KV cache overlap | Eliminates redundant prefill computation — 2x faster TTFT |
| [**KV Block Manager (KVBM)**](https://docs.nvidia.com/dynamo/components/kvbm) | Offloads KV cache across GPU → CPU → SSD → remote storage | Extends effective context length beyond GPU memory |
| [**ModelExpress**](https://github.com/ai-dynamo/modelexpress) | Streams model weights GPU-to-GPU via NIXL/NVLink | 7x faster cold-start for new replicas |
| [**Planner**](https://docs.nvidia.com/dynamo/components/planner/planner-guide) | SLA-driven autoscaler that profiles workloads and right-sizes pools | Meets latency targets at minimum total cost of ownership (TCO) |
| [**Grove**](https://github.com/ai-dynamo/grove) | K8s operator for topology-aware gang scheduling (NVL72) | Places workloads optimally across racks, hosts, and NUMA nodes |
| [**AIConfigurator**](https://github.com/ai-dynamo/aiconfigurator) | Simulates 10K+ deployment configs in seconds | Finds optimal serving config without burning GPU-hours |
| [**Fault Tolerance**](https://docs.nvidia.com/dynamo/user-guides/fault-tolerance/request-migration) | Canary health checks + in-flight request migration | Workers fail; user requests don't |

## installation

> This repo ships agent skills: if you work with an AI coding agent (Claude Code, Codex,
> Cursor), clone the repo and ask it to deploy, troubleshoot, benchmark, or optimize a Dynamo
> deployment. The skills activate automatically; no setup required.

## configuration

apiVersion: nvidia.com/v1beta1
kind: DynamoGraphDeploymentRequest
metadata:
  name: my-model
spec:
  model: Qwen/Qwen3-0.6B
  backend: vllm
  sla:
    ttft: 200.0   # ms
    itl: 20.0     # ms
  autoApply: true
```

Pre-built recipes for common models:

| Model | Framework | Mode | Recipe |
|-------|-----------|------|--------|
| Llama-3-70B | vLLM | Aggregated | [View](recipes/llama-3-70b/vllm/) |
| DeepSeek-R1 | SGLang | Disaggregated | [View](recipes/deepseek-r1/sglang/) |
| Qwen3-32B-FP8 | TensorRT-LLM | Aggregated | [View](recipes/qwen3-32b-fp8/trtllm/) |

See [recipes/](recipes/README.md) for the full list. Cloud-specific guides: [AWS EKS](docs/fern/pages/kubernetes/installation/managed-kubernetes/eks/eks-setup.mdx) · [Google GKE](docs/fern/pages/kubernetes/installation/managed-kubernetes/gcp/gke-setup.mdx) · [Azure AKS](docs/fern/pages/kubernetes/installation/managed-kubernetes/azure/aks-setup.mdx) · [Amazon ECS](docs/fern/pages/kubernetes/installation/managed-kubernetes/eks/ecs.mdx)

## tools

The OpenAI-compatible frontend exposes an OpenAPI 3 spec at `/openapi.json`. To generate without running the server:

```bash
cargo run -p dynamo-llm --bin generate-frontend-openapi
```

This writes to `docs/reference/api/openapi.json`.
