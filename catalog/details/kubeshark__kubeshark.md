# kubeshark/kubeshark

eBPF-powered network observability for Kubernetes. Indexes L4/L7 traffic with full K8s context, decrypts TLS without keys. Queryable by AI agents via MCP and humans via dashboard.

## tools

Kubeshark indexes cluster-wide network traffic by parsing it according to protocol specifications, with support for HTTP, gRPC, Redis, Kafka, DNS, and more. A single [KFL query](https://docs.kubeshark.com/en/v2/kfl2) can combine all three semantic layers — Kubernetes identity, API context, and network attributes — to pinpoint exactly the traffic you need. No code instrumentation required.

![KFL query combining API, Kubernetes, and network semantics](https://github.com/kubeshark/assets/raw/master/png/kfl-semantics.png)

[KFL reference →](https://docs.kubeshark.com/en/v2/kfl2) · [Traffic indexing →](https://docs.kubeshark.com/en/v2/l7_api_dissection)

### Workload Dependency Map

A visual map of how workloads communicate, showing dependencies, traffic volume, and protocol usage across the cluster.

![Service Map](https://github.com/kubeshark/assets/raw/master/png/servicemap.png)

[Learn more →](https://docs.kubeshark.com/en/v2/service_map)

### Traffic Retention & PCAP Export

Capture and retain raw network traffic cluster-wide, including decrypted TLS. Download PCAPs scoped by time range, nodes, workloads, and IPs — ready for Wireshark or any PCAP-compatible tool. Store snapshots in cloud storage (S3, Azure Blob, GCS) for long-term retention and cross-cluster sharing.

![Traffic Retention](https://github.com/kubeshark/assets/raw/master/png/snapshots-list.png)

[Snapshots guide →](https://docs.kubeshark.com/en/v2/traffic_snapshots) · [Cloud storage →](https://docs.kubeshark.com/en/snapshots_cloud_storage)

---

## features

| Feature | Description |
|---------|-------------|
| [**Traffic Snapshots**](https://docs.kubeshark.com/en/v2/traffic_snapshots) | Point-in-time snapshots with cloud storage (S3, Azure Blob, GCS), PCAP export for Wireshark |
| [**Traffic Indexing**](https://docs.kubeshark.com/en/v2/l7_api_dissection) | Real-time and delayed L7 indexing with request/response matching and full payloads |
| [**Protocol Support**](https://docs.kubeshark.com/en/protocols) | HTTP, gRPC, GraphQL, Redis, Kafka, DNS, and more |
| [**TLS Decryption**](https://docs.kubeshark.com/en/encrypted_traffic) | eBPF-based decryption without key management, included in snapshots |
| [**AI Integration**](https://docs.kubeshark.com/en/mcp) | MCP server + open-source AI skills for network RCA and traffic filtering |
| [**KFL Query Language**](https://docs.kubeshark.com/en/v2/kfl2) | CEL-based query language with Kubernetes, API, and network semantics |
| [**100% On-Premises**](https://docs.kubeshark.com/en/air_gapped) | Air-gapped support, no external dependencies |

---

## installation

| Method | Command |
|--------|---------|
| Helm | `helm repo add kubeshark https://helm.kubeshark.com && helm install kubeshark kubeshark/kubeshark` |
| Homebrew | `brew install kubeshark && kubeshark tap` |
| Binary | [Download](https://github.com/kubeshark/kubeshark/releases/latest) |

[Installation guide →](https://docs.kubeshark.com/en/install)

---

## Contributing

We welcome contributions. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[Apache-2.0](LICENSE)
