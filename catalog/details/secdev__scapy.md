# secdev/scapy

Scapy: the Python-based interactive packet manipulation program & library.

## installation

Scapy is usable either as a **shell** or as a **library**.
For further details, please head over to [Getting started with Scapy](https://scapy.readthedocs.io/en/latest/introduction.html), which is part of the documentation.

### Shell demo

![Scapy install demo](https://secdev.github.io/files/doc/animation-scapy-install.svg)

Scapy can easily be used as an interactive shell to interact with the network.
The following example shows how to send an ICMP Echo Request message to
`github.com`, then display the reply source IP address:

```python
sudo ./run_scapy
Welcome to Scapy
>>> p = IP(dst="github.com")/ICMP()
>>> r = sr1(p)
Begin emission:
.Finished to send 1 packets.
*
Received 2 packets, got 1 answers, remaining 0 packets
>>> r[IP].src
'192.30.253.113'
```

### Resources

The [documentation](https://scapy.readthedocs.io/en/latest/) contains more
advanced use cases, and examples.

Other useful resources:

-   [Scapy in 20 minutes](https://github.com/secdev/scapy/blob/master/doc/notebooks/Scapy%20in%2015%20minutes.ipynb)
-   [Interactive tutorial](https://scapy.readthedocs.io/en/latest/usage.html#interactive-tutorial) (part of the documentation)
-   [The quick demo: an interactive session](https://scapy.readthedocs.io/en/latest/introduction.html#quick-demo) (some examples may be outdated)
-   [HTTP/2 notebook](https://github.com/secdev/scapy/blob/master/doc/notebooks/HTTP_2_Tuto.ipynb)
-   [TLS notebooks](https://github.com/secdev/scapy/blob/master/doc/notebooks/tls)

## [Installation](https://scapy.readthedocs.io/en/latest/installation.html)

Scapy works without any external Python modules on Linux and BSD like operating
systems. On Windows, you need to install some mandatory dependencies as
described in [the
documentation](http://scapy.readthedocs.io/en/latest/installation.html#windows).

On most systems, using Scapy is as simple as running the following commands:

```bash
git clone https://github.com/secdev/scapy
cd scapy
./run_scapy
```

To benefit from all Scapy features, such as plotting, you might want to install
Python modules, such as `matplotlib` or `cryptography`. See the
[documentation](http://scapy.readthedocs.io/en/latest/installation.html) and
follow the instructions to install them.

<!-- stop_ppi_description -->

## Packaging status

[![Packaging status](https://repology.org/badge/vertical-allrepos/scapy.svg?columns=4&exclude_unsupported=1&header=
)](https://repology.org/project/scapy/versions)

## License

Scapy's code, tests and tools are licensed under GPL v2.
The documentation (everything unless marked otherwise in `doc/`, and except the logo) is licensed under CC BY-NC-SA 2.5.

## Contributing

Want to contribute? Great! Please take a few minutes to
[read this](CONTRIBUTING.md)!
