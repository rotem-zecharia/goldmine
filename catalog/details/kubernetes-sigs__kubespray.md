# kubernetes-sigs/kubespray

Deploy a Production Ready Kubernetes Cluster

## installation

Below are several ways to use Kubespray to deploy a Kubernetes cluster.

### Docker

Ensure you have installed Docker then

```ShellSession
docker run --rm -it --mount type=bind,source="$(pwd)"/inventory/sample,dst=/inventory \
  --mount type=bind,source="${HOME}"/.ssh/id_rsa,dst=/root/.ssh/id_rsa \
  quay.io/kubespray/kubespray:v2.31.0 bash
# Inside the container you may now run the kubespray playbooks:
ansible-playbook -i /inventory/inventory.ini --private-key /root/.ssh/id_rsa cluster.yml
```

### Ansible

#### Usage

See [Getting started](/docs/getting_started/getting-started.md)

#### Collection

See [here](docs/ansible/ansible_collection.md) if you wish to use this repository as an Ansible collection

### Vagrant

For Vagrant we need to install Python dependencies for provisioning tasks.
Check that ``Python`` and ``pip`` are installed:

```ShellSession
python -V && pip -V
```

If this returns the version of the software, you're good to go. If not, download and install Python from here <https://www.python.org/downloads/source/>

Install Ansible according to [Ansible installation guide](/docs/ansible/ansible.md#installing-ansible)
then run the following step:

```ShellSession
vagrant up
```

## Documents

- [Requirements](#requirements)
- [Kubespray vs ...](docs/getting_started/comparisons.md)
- [Getting started](docs/getting_started/getting-started.md)
- [Setting up your first cluster](docs/getting_started/setting-up-your-first-cluster.md)
- [Ansible inventory and tags](docs/ansible/ansible.md)
- [Integration with existing ansible repo](docs/operations/integration.md)
- [Deployment data variables](docs/ansible/vars.md)
- [DNS stack](docs/advanced/dns-stack.md)
- [HA mode](docs/operations/ha-mode.md)
- [Network plugins](#network-plugins)
- [Vagrant install](docs/developers/vagrant.md)
- [Flatcar Container Linux bootstrap](docs/operating_systems/flatcar.md)
- [Fedora CoreOS bootstrap](docs/operating_systems/fcos.md)
- [openSUSE setup](docs/operating_systems/opensuse.md)
- [Downloaded artifacts](docs/advanced/downloads.md)
- [Equinix Metal](docs/cloud_providers/equinix-metal.md)
- [OpenStack](docs/cloud_controllers/openstack.md)
- [vSphere](docs/cloud_controllers/vsphere.md)
- [Large deployments](docs/operations/large-deployments.md)
- [Adding/replacing a node](docs/operations/nodes.md)
- [Upgrades basics](docs/operations/upgrades.md)
- [Air-Gap installation](docs/operations/offline-environment.md)
- [NTP](docs/advanced/ntp.md)
- [Hardening](docs/operations/hardening.md)
- [Mirror](docs/operations/mirror.md)
- [Roadmap](docs/roadmap/roadmap.md)

## Supported Linux Distributions

- **Flatcar Container Linux by Kinvolk**
- **Debian** Bookworm, Bullseye, Trixie
- **Ubuntu** 22.04, 24.04
- **CentOS Stream / RHEL** 9, 10
- **Fedora** 39, 40, 41, 42
- **Fedora CoreOS** (see [fcos Note](docs/operating_systems/fcos.md))
- **openSUSE** Leap 15.x/Tumbleweed
- **Oracle Linux** 9, 10
- **Alma Linux** 9, 10
- **Rocky Linux** 9, 10 (experimental in 10: see [Rocky Linux 10 notes](docs/operating_systems/rhel.md#rocky-linux-10))
- **Kylin Linux Advanced Server V10** (experimental: see [kylin linux notes](docs/operating_systems/kylinlinux.md))
- **Amazon Linux 2** (experimental: see [amazon linux notes](docs/operating_systems/amazonlinux.md))
- **UOS Linux** (experimental: see [uos linux notes](docs/operating_systems/uoslinux.md))
- **openEuler** (experimental: see [openEuler notes](docs/operating_systems/openeuler.md))

Note:

- Upstart/SysV init based OS types are not supported.
- [Kernel requirements](docs/operations/kernel-requirements.md) (please read if the OS kernel version is < 4.19).

## Supported Components

<!-- BEGIN ANSIBLE MANAGED BLOCK -->

- Core
  - [kubernetes](https://github.com/kubernetes/kubernetes) 1.36.4
  - [etcd](https://github.com/etcd-io/etcd) 3.6.14
  - [docker](https://www.docker.com/) 28.3
  - [containerd](https://containerd.io/) 2.3.4
  - [cri-o](https://cri-o.io/) 1.36.3 (experimental: see [CRI-O Note](docs/CRI

## requirements

- **Minimum required version of Kubernetes is v1.34.0**

- **Ansible v2.14+, Jinja 2.11+ and python-netaddr is installed on the machine that will run Ansible commands**
- The target servers must have **access to the Internet** in order to pull docker images. Otherwise, additional configuration is required (See [Offline Environment](docs/operations/offline-environment.md))
- The target servers are configured to allow **IPv4 forwarding**.
- If using IPv6 for pods and services, the target servers are configured to allow **IPv6 forwarding**.
- The **firewalls are not managed**, you'll need to implement your own rules the way you used to.
    in order to avoid any issue during deployment you should disable your firewall.
- If kubespray is run from non-root user account, correct privilege escalation method
    should be configured in the target servers. Then the `ansible_become` flag
    or command parameters `--become or -b` should be specified.

Hardware:
These limits are safeguarded by Kubespray. Actual requirements for your workload can differ. For a sizing guide go to the [Building Large Clusters](https://kubernetes.io/docs/setup/cluster-large/#size-of-master-and-master-components) guide.

- Control Plane
  - Memory: 2 GB
- Worker Node
  - Memory: 1 GB

## Network Plugins

You can choose among ten network plugins. (default: `calico`, except Vagrant uses `flannel`)

- [flannel](docs/CNI/flannel.md): gre/vxlan (layer 2) networking.

- [Calico](https://docs.tigera.io/calico/latest/about/) is a networking and network policy provider. Calico supports a flexible set of networking options
    designed to give you the most efficient networking across a range of situations, including non-overlay
    and overlay networks, with or without BGP. Calico uses the same engine to enforce network policy for hosts,
    pods, and (if using Istio and Envoy) applications at the service mesh layer.

- [cilium](http://docs.cilium.io/en/latest/): layer 3/4 networking (as well as layer 7 to protect and secure application protocols), supports dynamic insertion of BPF bytecode into the Linux kernel to implement security services, networking and visibility logic.

- [kube-ovn](docs/CNI/kube-ovn.md): Kube-OVN integrates the OVN-based Network Virtualization with Kubernetes. It offers an advanced Container Network Fabric for Enterprises.

- [kube-router](docs/CNI/kube-router.md): Kube-router is a L3 CNI for Kubernetes networking aiming to provide operational
    simplicity and high performance: it uses IPVS to provide Kube Services Proxy (if setup to replace kube-proxy),
    iptables for network policies, and BGP for ods L3 networking (with optionally BGP peering with out-of-cluster BGP peers).
    It can also optionally advertise routes to Kubernetes cluster Pods CIDRs, ClusterIPs, ExternalIPs and LoadBalancerIPs.

- [macvlan](docs/CNI/macvlan.md): Macvlan is a Linux network driver. Pods have their own unique Mac and Ip address, connected directly the physical (layer 2) network.

- [multus](docs/CNI/multus.md): Multus is a meta CNI plugin that provides multiple network interface support to pods. For each interface Multus delegates CNI calls to secondary CNI plugins such as Calico, macvlan, etc.

- [custom_cni](roles/network-plugin/custom_cni/) : You can specify some manifests that will be applied to the clusters to bring you own CNI and use non-supported ones by Kubespray.
  See `tests/files/custom_cni/README.md` and `tests/files/custom_cni/values.yaml`for an example with a CNI provided by a Helm Chart.

The network plugin to use is defined by the variable `kube_network_plugin`. There is also an
option to leverage built-in cloud provider networking instead.
See also [Network checker](docs/advanced/netcheck.md).

## Ingress Plugins

- [metallb](docs/ingress/metallb.md): the MetalLB bare-metal service LoadBalancer provider.

## Community docs and resources

- [kubernetes.io/docs/setup/production-environment/tools/kubespray/](https://kubernetes.io/docs/setup/pr

## tools

- [Digital Rebar Provision](https://github.com/digitalrebar/provision/blob/v4/doc/integrations/ansible.rst)
- [Terraform Contrib](https://github.com/kubernetes-sigs/kubespray/tree/master/contrib/terraform)
- [Kubean](https://github.com/kubean-io/kubean)

## CI Tests

[![Build graphs](https://gitlab.com/kargo-ci/kubernetes-sigs-kubespray/badges/master/pipeline.svg)](https://gitlab.com/kargo-ci/kubernetes-sigs-kubespray/-/pipelines)

CI/end-to-end tests sponsored by: [CNCF](https://cncf.io), [Equinix Metal](https://metal.equinix.com/), [OVHcloud](https://www.ovhcloud.com/), [ELASTX](https://elastx.se/).

See the [test matrix](docs/developers/test_cases.md) for details.
