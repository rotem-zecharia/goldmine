# loft-sh/vcluster

vCluster - Create fully functional virtual Kubernetes clusters - Each vcluster runs inside a namespace of the underlying k8s cluster. It's cheaper than creating separate full-blown clusters and it off

## installation

```bash

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
