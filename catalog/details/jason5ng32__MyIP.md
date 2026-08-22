# jason5ng32/MyIP

The best IP Toolbox. Check your IP address & geolocation, test IP for WebRTC and DNS IP leaks, run an IP quality check, browser fingerprint check, website availability check, network speed test, globa

## features

* 🛜 **View Your IPs**: Detects and displays your local IPs, sourcing from multiple IPv4 and IPv6 providers.
* 🔍 **Search IP Information**: Provides a tool for querying information about any IP address. 
* 🕵️ **IP Information**: Presents detailed information for all IP addresses, including country, region, ASN, geographic location, and more.
* 🛰️ **ASN History & Upstream Topology**: View historical AS announcements for an IP prefix, and visualize the upstream paths from an ASN to the Tier 1 backbone networks.
* 🚦 **Availability Check**: Tests the accessibility of various websites, such as Google, GitHub, YouTube, ChatGPT, and others.
* 📡 **Service Status**: Shows the live availability of well-known services (Claude, OpenAI, GitHub, Cloudflare, and more) from their official status pages, with per-service status and recent incidents.
* 🚥 **WebRTC Detection**: Identifies the IP address used during WebRTC connections.
* 🛑 **DNS Leak Test**: Shows DNS endpoint data to evaluate the risk of DNS leaks when using VPNs or proxies.
* 🚀 **Speed Test**：Test your network speed with edge networks.
* 🚏 **Proxy Rule Testing**: Test the rule settings of proxy software to ensure their correctness.
* ⏱️ **Global Latency Test**: Performe lantency tests on servers located in different regions around the world.
* 🚉 **MTR Test**: Perform MTR tests on servers located in different regions around the world.
* 🔦 **DNS Resolver**: Performs DNS resolution of a domain name from multiple sources and obtains real-time resolution results that can be used for contamination determination.
* 🚧 **Censorship Check**: Check if a website is blocked in some countries.
* 📓 **Whois Search**: Perform whois information search for domain names or IP addresses
* 📀 **MAC Lookup**: Query information of a physical address
* 🖥️ **Browser Fingerprints**：Multiple ways to caculate your browser fingerprint
* 📋 **Cybersecurity Checklist**：A comprehensive cybersecurity checklist with a total of 258 items

## configuration

Make sure you have Node.js installed.

Clone the code:

```bash
git clone https://github.com/jason5ng32/MyIP.git
```

Install and build. This project uses pnpm — if you don't have it, install it first (npm ships with Node, so this command always works):

```bash
npm install -g pnpm
pnpm install && pnpm run build
```

Run:

```bash
pnpm start
```

The program will run on port 18966.

## tools

If you're using a proxy for internet access, consider adding this rule to your proxy configuration (modify it according to your client). This setup lets you check both your real IP and the IP when using the proxy:

```ini
