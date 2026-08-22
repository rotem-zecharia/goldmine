# cilium/cilium

eBPF-based Networking, Security, and Observability

## features

.. begin-functionality-overview

CNI (Container Network Interface)
---------------------------------

`Cilium as a CNI plugin <https://cilium.io/use-cases/cni/>`_ provides a
fast, scalable, and secure networking layer for Kubernetes clusters. Built
on eBPF, it offers several deployment options:

* **Overlay networking:** an encapsulation-based virtual network spanning all
  hosts with support for VXLAN and Geneve. It works on almost any network
  infrastructure as the only requirement is IP connectivity between hosts
  which is typically already given.

* **Native routing mode:** Use of the regular routing table of the Linux
  host. The network must be capable of routing the IP addresses
  of the application containers. It integrates with cloud routers, routing
  daemons, and IPv6-native infrastructure.

* **Flexible routing options:** Cilium can automate route learning and
  advertisement in common topologies such as using L2 neighbor discovery
  when nodes share a layer 2 domain, or BGP when routing across layer 3
  boundaries.

Each mode is designed for maximum interoperability with existing
infrastructure while minimizing operational burden.

Load Balancing
--------------

Cilium implements distributed load balancing for traffic between application
containers and to/from external services. The load balancing is implemented
in eBPF using efficient hash tables, enabling high service density and low
latency at scale.

* **East-west load balancing** rewrites service connections at the socket
  level (``connect()``), avoiding the overhead of per-packet NAT and fully
  `replacing kube-proxy <https://cilium.io/use-cases/kube-proxy/>`_.

* **North-south load balancing** supports XDP for high-throughput scenarios
  and `layer 4 load balancing <https://cilium.io/use-cases/load-balancer/>`_
  including Direct Server Return (DSR), and Maglev consistent hashing.

Cluster Mesh
------------

Cilium `Cluster Mesh <https://cilium.io/use-cases/cluster-mesh/>`_ enables
secure, seamless connectivity across multiple Kubernetes clusters. For
operators running hybrid or multi-cloud environments, Cluster Mesh ensures
a consistent security and connectivity experience.

* **Global service discovery**: Workloads across clusters can discover and
  connect to services as if they were local. This enables fault tolerance,
  like automatically failing over to backends in another cluster, and
  exposes shared services like logging, auth, or databases across
  environments.

* **Unified identity model:** Security policies are enforced based on
  identity, not IP address, across all clusters.

Network Policy
--------------

Cilium `Network Policy <https://cilium.io/use-cases/network-policy/>`_
provides identity-aware enforcement across L3-L7. Typical container
firewalls secure workloads by filtering on source IP addresses and
destination ports. This concept requires the firewalls on all servers to be
manipulated whenever a container is started anywhere in the cluster.

In order to avoid this situation which limits scale, Cilium assigns a
security identity to groups of application containers which share identical
security policies. The identity is then associated with all network packets
emitted by the application containers, allowing the identity to be validated
at the receiving node.

* **Identity-based security** removes reliance on brittle IP addresses.

* **L3/L4 policies** restrict traffic based on labels, protocols, and ports.

* **DNS-based policies:** Allow or deny traffic to FQDNs or wildcard domains
   (e.g., ``api.example.com``, ``*.trusted.com``). This is especially useful
   for securing egress traffic to third-party services.

* **L7-aware policies** allow filtering by HTTP method, URL path, gRPC call,
  and more:

  * Example: Allow only GET requests to ``/public/.*``.

  * Enforce the presence of headers like ``X-Token: [0-9]+``.

CIDR-based egress and ingress policies are also supported for controlling
access to external IPs, ideal for inte

## installation

* `Why Cilium?`_
* `Getting Started <gs_>`_
* `Architecture and Concepts`_
* `Installing Cilium`_
* `Frequently Asked Questions`_
* Contributing_

Community
=========

Slack
-----

Join the Cilium `Slack channel <https://slack.cilium.io>`_ to chat with
Cilium developers and other Cilium users. This is a good place to learn about
Cilium, ask questions, and share your experiences.

Special Interest Groups (SIG)
-----------------------------

See `Special Interest Groups
<https://github.com/cilium/community/blob/main/sigs.yaml>`_ for a list of all SIGs and their meeting times.

Developer meetings
------------------
The Cilium developer community hangs out on Zoom to chat. Everyone is welcome.

* Weekly, Wednesday,
  5:00 pm `Europe/Zurich time <https://time.is/Canton_of_Zurich>`__ (CET/CEST),
  usually equivalent to 8:00 am PT, or 11:00 am ET. `Meeting Notes and Zoom Info`_
* Third Wednesday of each month, 9:00 am `Japan time <https://time.is/Tokyo>`__ (JST). `APAC Meeting Notes and Zoom Info`_

eBPF & Cilium Office Hours livestream
-------------------------------------
We host a weekly community `YouTube livestream called eCHO <https://www.youtube.com/channel/UCJFUxkVQTBJh3LD1wYBWvuQ>`_ which (very loosely!) stands for eBPF & Cilium Office Hours. Join us live, catch up with past episodes, or head over to the `eCHO repo <https://github.com/isovalent/eCHO>`_ and let us know your ideas for topics we should cover.

Governance
----------
The Cilium project is governed by a group of `Maintainers and Committers <https://raw.githubusercontent.com/cilium/cilium/main/MAINTAINERS.md>`__.
How they are selected and govern is outlined in our `governance document <https://github.com/cilium/community/blob/main/GOVERNANCE.md>`__.

Adopters
--------
A list of adopters of the Cilium project who are deploying it in production, and of their use cases,
can be found in file `USERS.md <https://github.com/cilium/cilium/blob/main/USERS.md>`__.

License
=======

.. _apache-license: LICENSE
.. _bsd-license: bpf/LICENSE.BSD-2-Clause
.. _gpl-license: bpf/LICENSE.GPL-2.0

The Cilium user space components are licensed under the
`Apache License, Version 2.0 <apache-license_>`__.
The BPF code templates are dual-licensed under the
`General Public License, Version 2.0 (only) <gpl-license_>`__
and the `2-Clause BSD License <bsd-license_>`__
(you can use the terms of either license, at your option).

.. _Cilium Upgrade Guide: https://docs.cilium.io/en/stable/operations/upgrade/
.. _Why Cilium?: https://docs.cilium.io/en/stable/overview/intro
.. _gs: https://docs.cilium.io/en/stable/#getting-started
.. _Architecture and Concepts: https://docs.cilium.io/en/stable/overview/component-overview/
.. _Installing Cilium: https://docs.cilium.io/en/stable/gettingstarted/k8s-install-default/
.. _Frequently Asked Questions: https://github.com/cilium/cilium/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3Akind%2Fquestion+
.. _Contributing: https://docs.cilium.io/en/stable/contributing/development/
.. _Prerequisites: https://docs.cilium.io/en/stable/operations/system_requirements/
.. _eBPF: https://ebpf.io
.. _eBPF.io: https://ebpf.io
.. _Meeting Notes and Zoom Info: https://docs.google.com/document/d/1IqLRvTvnK5SQ1SMM8g8R_k2TeeRUwWmOYqjYWZs6MiM/edit#
.. _APAC Meeting Notes and Zoom Info: https://docs.google.com/document/d/1egv4qLydr0geP-GjQexYKm4tz3_tHy-LCBjVQcXcT5M/edit#

.. |go-report| image:: https://goreportcard.com/badge/github.com/cilium/cilium
    :alt: Go Report Card
    :target: https://goreportcard.com/report/github.com/cilium/cilium

.. |go-doc| image:: https://godoc.org/github.com/cilium/cilium?status.svg
    :alt: GoDoc
    :target: https://godoc.org/github.com/cilium/cilium

.. |rtd| image:: https://readthedocs.org/projects/docs/badge/?version=latest
    :alt: Read the Docs
    :target: https://docs.cilium.io/

.. |apache| image:: https://img.shields.io/badge/license-Apache-blue.svg
    :alt: Apache licensed
    :target: apache-license_

.. |bsd| image:: https://img.shiel
