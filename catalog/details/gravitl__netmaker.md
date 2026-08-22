# gravitl/netmaker

Netmaker makes networks with WireGuard. Netmaker automates fast, secure, and distributed virtual networks.

## installation

These are the instructions for deploying a Netmaker server on your cloud VM as quickly as possible. For more detailed instructions, visit the [Install Docs](https://docs.netmaker.io/docs/server-installation/quick-install#quick-install-script).  

1. Get a cloud VM with Ubuntu 24.04 and a static public IP.
2. Allow inbound traffic on port 443,51821 TCP and UDP to the VM firewall in cloud security settings, and for simplicity, allow outbound on All TCP and All UDP.
3. (recommended) Prepare DNS - Set a wildcard subdomain in your DNS settings for Netmaker, e.g. *.netmaker.example.com, which points to your VM's public IP.
4. Run the script to setup open source version of Netmaker: 

`sudo wget -qO /root/nm-quick.sh https://raw.githubusercontent.com/gravitl/netmaker/master/scripts/nm-quick.sh && sudo chmod +x /root/nm-quick.sh && sudo /root/nm-quick.sh`

**<pre>To Install Self-Hosted PRO Version - https://docs.netmaker.io/docs/server-installation/netmaker-professional-setup</pre>** 



<p float="left" align="middle">
<img src="https://raw.githubusercontent.com/gravitl/netmaker-docs/master/images/netmaker-github/readme.gif" />
</p>

After installing Netmaker, check out the [Walkthrough](https://itnext.io/getting-started-with-netmaker-a-wireguard-virtual-networking-platform-3d563fbd87f0) and [Getting Started](https://docs.netmaker.io/docs/getting-started) guides to learn more about configuring networks. Or, check out some of our other [Tutorials](https://www.netmaker.io/blog) for different use cases, including Kubernetes.

## features

- Netmaker automates virtual networks between data centres, clouds, and edge devices, so you don't have to.

- Kernel WireGuard offers maximum speed, performance, and security. 

- Netmaker is built to scale from small businesses to enterprises. 

- Netmaker with WireGuard can be highly customized for peer-to-peer, site-to-site, Kubernetes, and more.
