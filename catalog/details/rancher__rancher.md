# rancher/rancher

Complete container management platform

## installation

sudo docker run -d --restart=unless-stopped -p 80:80 -p 443:443 --privileged rancher/rancher

Open your browser to https://localhost

## requirements

* Operating Systems
  * Please see [Support Matrix](https://rancher.com/support-matrix/) for specific OS versions for each Rancher version. Note that the link will default to the support matrix for the latest version of Rancher. Use the left navigation menu to select a different Rancher version. 
* Hardware & Software
  * Please see [Installation Requirements](https://ranchermanager.docs.rancher.com/getting-started/installation-and-upgrade/installation-requirements) for hardware and software requirements.

## configuration

Refer to the [build docs](docs/build.md) on how to customize the building and packaging of Rancher.
