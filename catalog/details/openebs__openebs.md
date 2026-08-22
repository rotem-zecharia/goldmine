# openebs/openebs

A popular & widely deployed Open Source Container Native Storage platform for Stateful Persistent Applications on Kubernetes.

## features

OpenEBS is an open-source Container Native Storage solution that provides persistent storage for Kubernetes workloads. It enables dynamic provisioning of storage resources using containerized storage controllers, making it highly flexible and cloud-native. OpenEBS supports various storage engines, including LocalPVs for direct node storage and Replicated PV advanced data replication and resilience. It is designed to integrate seamlessly with Kubernetes, offering benefits like storage policies, resize, thin-provisioning, snapshots, and restore capabilities, making it an ideal choice for stateful applications.

OpenEBS offers two primary storage approaches for Kubernetes workloads: Local Storage and Replicated Storage. Below is a comparative overview:

| Feature                     | Local Storage                                                                 | Replicated Storage                                                                 |
|-----------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Data Availability**       | Limited to the node where the volume is provisioned; not suitable for high-availability requirements.| Synchronously replicates data across multiple nodes, ensuring high availability and durability. |
| **Use Cases**               | Ideal for applications managing their own replication and availability, such as distributed databases like MongoDB and Cassandra. | Suitable for stateful workloads requiring storage-level replication and high availability, like Percona/ Standalone DBs, and GitLab. |
| **Performance**             | Provides near-disk performance with minimal overhead. | Designed for high performance, leveraging NVMe-oF semantics for low-latency access. |
| **Limitations**             | Not highly available; node failure leads to data unavailability. | Requires sufficient resources (CPU, RAM, NVMe) for optimal performance. |
| **Snapshot and Cloning**    | Supported when backed by advanced filesystems like LVM or ZFS. | Supported, providing enterprise storage capabilities. |
| **Backup and Restore**      | Supported via Velero, using Restic for local volumes. | Supported via Velero, ensuring data protection and recovery.|

In summary, **Local Storage** is a good choice when your application can manage its own replication and high availability, and **Replicated Storage** when you require storage-level replication, enhanced data durability and network-based storage access.

Below are the sub-projects or the major storage solutions under the OpenEBS Umbrella. Visit the individual repositories to learn more about their usage and architecture.

| Sub-Project | [Local PV Hostpath](https://github.com/openebs/dynamic-localpv-provisioner) | [Local PV ZFS](https://github.com/openebs/zfs-localpv) | [Local PV LVM](https://github.com/openebs/lvm-localpv)  | [Local PV Rawfile (_**Experimental**_)](https://github.com/openebs/rawfile-localpv) | [Mayastor](https://github.com/openebs/mayastor) |
| :---:  | :---              | :---         | :---         | :---:            | :---:                  |
| Type   | Single-node       | Single-node  | Single-node  |  Single-node     | Multi-node             |
| What is it for?   | Replacement for in-Tree Kubernetes CSI Hostpath       | Storage engine for ZFS managed backend storage  | Storage engine for LVM2 managed backend storage  |  Experimental engine for using an extent file as block storage     | General purpose replicated enterprise storage           |
| Designed for | Developers or DevOps | ZFS users and production deployments | LVM2 users and production deployments | Developers | Enterprises and production deployments |
| Features | Everything in Kubernetes Hostpath, plus: - Dynamic provisioning, Zero configuration, No CSI driver | Provision ZFS datasets, Provision ZFS volumes, Dynamic provisioning, ZFS resilience, ZFS R
