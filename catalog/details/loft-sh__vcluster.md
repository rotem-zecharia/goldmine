# loft-sh/vcluster

vCluster - Create fully functional virtual Kubernetes clusters - Each vcluster runs inside a namespace of the underlying k8s cluster. It's cheaper than creating separate full-blown clusters and it off

## installation

```bash
# Install vCluster CLI
brew install loft-sh/tap/vcluster

# Create a Tenant Cluster
vcluster create my-vcluster --namespace team-x

# Use kubectl as usual — you're now in your Tenant Cluster
kubectl get namespaces
```

**Prerequisites:** A running Kubernetes cluster and `kubectl` configured.

👉 **[Full Quickstart Guide](https://www.vcluster.com/docs/get-started)**

### 🐳 Run Locally with Docker — [vind](https://github.com/loft-sh/vind)

No Kubernetes cluster? Run vCluster directly on Docker with **vind** (vCluster in Docker) — like `kind`, but with the full vCluster feature set (UI, sleep/resume, LoadBalancer, image cache):

```bash
vcluster create my-vcluster --driver docker
kubectl get namespaces
```

### 🎮 Try in the Browser

[![Try on Killercoda](https://img.shields.io/badge/Try%20on-Killercoda-22B573?style=for-the-badge&logo=kubernetes&logoColor=white)](https://killercoda.com/vcluster)

### 🎁 vCluster Free Tier

Real usage, not a gated demo. Unlimited Tenant Clusters up to 64 CPUs / 32 GPUs, plus the full vCluster Platform UI — for free. **[Get Started Free →](https://www.vcluster.com/free)**

---

## 🆕 What's New

| Version | Feature | Description |
|---------|---------|-------------|
| **v0.34** | [Multi-Region Platform & Standalone Snapshots](https://www.vcluster.com/releases/changelog/vcluster-platform-v49-vcluster-v034-multi-region-platform-snapshot-support) | Active/active vCluster Platform across regions (Route 53 + RDS), Standalone snapshots (S3 / OCI / local), first-class template parameters |
| **v0.33** | [Enterprise Reliability & Storage](https://github.com/loft-sh/vcluster/releases/tag/v0.33.0) | Automatic leaf-cert regeneration, Azure Blob snapshot destinations, workload-level sleep annotations |
| **v0.32** | [Docker Driver & DRA](https://github.com/loft-sh/vcluster/releases/tag/v0.32.0) | Run vCluster on Docker, Dynamic Resource Allocation (DRA) for GPU workloads, in-place pod resizing |
| **v0.31** | [Snapshots & Cross-Cluster APIs](https://github.com/loft-sh/vcluster/releases/tag/v0.31.0) | Expanded snapshot/restore lifecycle, PDBs for Tenant Cluster control planes, cross-cluster resource proxying |
| **v0.30** | [vCluster VPN & Netris Integration](https://www.vcluster.com/releases/en/changelog/platform-v45-and-vcluster-v030-secure-cloud-bursting-on-prem) | Tailscale-powered overlay networking and automated hardware isolation via Netris |
| **v0.27–v0.29** | [Architecture Foundations](https://www.vcluster.com/docs/vcluster/introduction/architecture/) | [Private Nodes](https://www.vcluster.com/docs/vcluster/deploy/worker-nodes/private-nodes) (v0.27, CNI/CSI isolation), [Auto Nodes](https://www.vcluster.com/docs/vcluster/deploy/worker-nodes/private-nodes/auto-nodes/) (v0.28, Karpenter autoscaling), [Standalone Mode](https://www.vcluster.com/docs/vcluster/deploy/control-plane/binary/) (v0.29, no Control Plane Cluster — dedicated infrastructure or bare metal) |

👉 **[Full Changelog](https://www.vcluster.com/releases)**

---

## 🎯 Use Cases

| Use Case | Description | Learn More |
|----------|-------------|------------|
| **AI Factory** | Run AI on-prem where your data and GPUs live. Give every team the GPU access they need without multiplying infrastructure. | [View →](https://www.vcluster.com/solutions/ai-factory) |
| **AI Cloud Providers** | Launch a hyperscaler-like Kubernetes experience for your GPU customers. Isolated, production-grade, in minutes. | [View →](https://www.vcluster.com/solutions/gpu-cloud-providers) |
| **Internal GPU Platform** | Maximize GPU utilization without sacrificing isolation. Self-service Kubernetes for AI/ML teams. | [View →](https://www.vcluster.com/solutions/internal-gpu-platform) |
| **Bare Metal Kubernetes** | Run production Kubernetes on bare metal with zero VMs. Isolation without expensive virtualization overhead. | [View →](https://www.vcluster.com/solutions/bare-metal-kubernetes) |
| **Software Vendors** | Ship Kubernetes-native products. Each customer gets thei

## configuration

<details>
<summary>🔹 Shared Nodes — Maximum density, minimum cost</summary>
Tenant Clusters share the Control Plane Cluster's nodes. Workloads run as regular pods in a namespace.
<div align="center">
<img src="./assets/vcluster-architecture-shared-nodes.png" alt="Shared Nodes Architecture" width="600">
</div>

```yaml
sync:
  fromHost:
    nodes:
      enabled: false  # Uses pseudo nodes
```
</details>
<details>
<summary>🔹 Dedicated Nodes — Isolated compute on labeled node pools</summary>
Tenant Clusters get their own set of labeled nodes on the Control Plane Cluster. Workloads are isolated but still managed by the Control Plane Cluster.
<div align="center">
<img src="./assets/vcluster-architecture-dedicated-nodes.png" alt="Dedicated Nodes Architecture" width="600">
</div>

```yaml
sync:
  fromHost:
    nodes:
      enabled: true
      selector:
        labels:
          tenant: my-tenant
```
</details>
<details>
<summary>🔹 Private Nodes <sup>v0.27+</sup> — Full CNI/CSI isolation</summary>
External nodes join the Tenant Cluster directly with their own CNI, CSI, and networking stack. Complete workload isolation from the Control Plane Cluster.
<div align="center">
<img src="./assets/vcluster-architecture-private-nodes.png" alt="Private Nodes Architecture" width="600">
</div>

```yaml
privateNodes:
  enabled: true
controlPlane:
  service:
    spec:
      type: NodePort
```
</details>
<details>
<summary>🔹 vCluster Standalone <sup>v0.29+</sup> — No Control Plane Cluster required</summary>
Run vCluster without any Control Plane Cluster. Deploy the Virtual Control Plane directly on bare metal or VMs. The highest level of isolation — vCluster becomes the cluster.
<div align="center">
<img src="./assets/vcluster-architecture-standalone.png" alt="Standalone Architecture" width="600">
</div>

```yaml
controlPlane:
  standalone:
    enabled: true
    joinNode:
      enabled: true
privateNodes:
  enabled: true
```
</details>
<details>
<summary>⚡ Auto Nodes <sup>v0.28+</sup> — Karpenter-powered dynamic autoscaling</summary>
Automatically provision and deprovision private nodes based on workload demand. Works across public cloud, private cloud, hybrid, and bare metal environments.
<div align="center">
<img src="./assets/vcluster-architecture-auto-nodes.png" alt="Auto Nodes Architecture" width="600">
</div>

```yaml
autoNodes:
  enabled: true
  nodeProvider: <provider>
privateNodes:
  enabled: true
```
</details>

---

## features

| Feature | Description |
|---------|-------------|
| **🎛️ Isolated Virtual Control Plane** | Each Tenant Cluster gets its own API server, controller manager, and data store — complete Kubernetes API isolation |
| **🔗 Shared Platform Stack** *(Shared / Dedicated Nodes)* | Leverage the Control Plane Cluster's CNI, CSI, ingress, and other infrastructure — no duplicate platform components |
| **🔒 Strong Tenant Isolation** | Tenants get admin access inside their Tenant Cluster while having minimal permissions on the Control Plane Cluster |
| **🔄 Resource Syncing** *(Shared / Dedicated Nodes)* | Bidirectional sync of any Kubernetes resource — pods, services, secrets, configmaps, CRDs, and more |
| **💤 Sleep Mode** | Pause inactive Tenant Clusters to save resources. Instant wake when needed |
| **🖥️ Standalone Deployment** | Run without a Control Plane Cluster on dedicated infrastructure or bare metal — purpose-built for AI factories and on-prem GPU fleets |
| **🧩 Integrations** | Native support for cert-manager, external-secrets, KubeVirt, Istio, and metrics-server (host-side integrations apply in Shared / Dedicated Nodes modes) |
| **📊 High Availability** | Multiple replicas with leader election. Embedded etcd or external databases (PostgreSQL, MySQL, RDS) |

> *Shared Platform Stack, Resource Syncing, and host-cluster integrations apply only in **Shared** and **Dedicated Nodes** modes, where the Tenant Cluster shares the Control Plane Cluster's CNI, CSI, and platform stack. **Private Nodes** and **Standalone** deployments bring their own CNI, CSI, and platform components.*

---

## 🌐 The vCluster Platform

vCluster is the foundation of a broader platform for running production Kubernetes and AI infrastructure on your own hardware — from a single rack to 100K-GPU supercomputers.

| Product | What it does |
|---------|--------------|
| **[vCluster](https://www.vcluster.com)** | Tenant Clusters — Virtual Control Planes with API, data, and (optionally) network isolation |
| **[vNode](https://www.vnode.com/)** | Runtime-level isolation. Kernel-enforced boundaries (seccomp, cgroups, namespaces, AppArmor) without VM overhead |
| **[vMetal](https://www.vmetal.ai/)** | Zero-touch bare metal provisioning for GPU fleets. Turns GPU racks into a cloud platform |
| **[Netris](https://www.vcluster.com/solutions/netris-kubernetes-network-automation)** *(integration)* | Hardware-enforced network isolation via programmatic VLANs, VRFs, and ACLs |

Together these provide a complete foundation for AI factories — certified Kubernetes stacks, isolated Tenant Clusters, runtime workload sandboxing, and GPU infrastructure operations — the same pattern used to run production AI on hundreds of AI clouds and Fortune 500 on-prem platforms.

---

## 🏢 Trusted By

<table>
<tr>
<td align="center"><a href="https://www.vcluster.com/case-studies/atlan"><strong>Atlan</strong></a><br/>100 → 1 clusters</td>
<td align="center"><a href="https://www.vcluster.com/case-studies/aussie-broadband"><strong>Aussie Broadband</strong></a><br/>99% faster provisioning</td>
<td align="center"><a href="https://www.vcluster.com/case-studies/coreweave"><strong>CoreWeave</strong></a><br/>GPU cloud at scale</td>
</tr>
<tr>
<td align="center"><a href="https://www.vcluster.com/case-studies/lintasarta"><strong>Lintasarta</strong></a><br/>170+ Tenant Clusters in prod</td>
<td align="center"><a href="https://www.vcluster.com/case-studies/fortune-500-insurance-company"><strong>Fortune 500 Insurance</strong></a><br/>70% reduction in Kubernetes cost</td>
<td align="center"><a href="https://www.vcluster.com/case-studies/scanmetrix"><strong>Scanmetrix</strong></a><br/>99% faster deployments</td>
</tr>
<tr>
<td align="center"><a href="https://www.vcluster.com/case-studies/deloitte"><strong>Deloitte</strong></a><br/>Enterprise K8s platform</td>
<td align="center"><a href="https://www.vcluster.com/case-studies/ada-cx"><strong>Ada</strong></a><br/>10x Developer Productivity</td>
<td align="center"><a
