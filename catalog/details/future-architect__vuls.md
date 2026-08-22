# future-architect/vuls

Agent-less vulnerability scanner for Linux, FreeBSD, Container, WordPress, Programming language libraries, Network devices

## features

### Scan for any vulnerabilities in Linux/FreeBSD/Windows/macOS

[Supports major Linux/FreeBSD/Windows/macOS](https://vuls.io/docs/en/supported-os.html)

- Alpine, Amazon Linux, CentOS, AlmaLinux, Rocky Linux, Debian, Oracle Linux, Raspbian, RHEL, openSUSE, openSUSE Leap, SUSE Enterprise Linux, Fedora, and Ubuntu
- FreeBSD
- Windows
- macOS
- Cloud, on-premise, Running Docker Container

### High-quality scan

- Vulnerability Database
  - [NVD](https://nvd.nist.gov/)
  - [JVN(Japanese)](http://jvndb.jvn.jp/apis/myjvn/)

- OVAL
  - [Red Hat](https://www.redhat.com/security/data/oval/)
  - [Debian](https://www.debian.org/security/oval/)
  - [Ubuntu](https://security-metadata.canonical.com/oval/)
  - [SUSE](http://ftp.suse.com/pub/projects/security/oval/)
  - [Oracle Linux](https://linux.oracle.com/security/oval/)

- Security Advisory
  - [Alpine-secdb](https://git.alpinelinux.org/cgit/alpine-secdb/)
  - [Red Hat Security Advisories](https://access.redhat.com/security/security-updates/)
  - [Debian Security Bug Tracker](https://security-tracker.debian.org/tracker/)
  - [Ubuntu CVE Tracker](https://people.canonical.com/~ubuntu-security/cve/)
  - [Microsoft CVRF](https://api.msrc.microsoft.com/cvrf/v2.0/swagger/index)

- Commands(yum, zypper, pkg-audit)
  - RHSA / ALAS / ELSA / FreeBSD-SA
  - Changelog

- PoC, Exploit
  - [Exploit Database](https://www.exploit-db.com/)
  - [Metasploit-Framework modules](https://www.rapid7.com/db/?q=&type=metasploit)
  - [qazbnm456/awesome-cve-poc](https://github.com/qazbnm456/awesome-cve-poc)
  - [nomi-sec/PoC-in-GitHub](https://github.com/nomi-sec/PoC-in-GitHub)
  - [gmatuz/inthewilddb](https://github.com/gmatuz/inthewilddb)
  - [projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates)

- CERT
  - [US-CERT](https://www.us-cert.gov/ncas/alerts)
  - [JPCERT](http://www.jpcert.or.jp/at/2019.html)

- KEV
  - CISA(Cybersecurity & Infrastructure Security Agency): [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
  - VulnCheck: [VulnCheck KEV](https://vulncheck.com/kev)

- Cyber Threat Intelligence(MITRE ATT&CK and CAPEC)
  - [mitre/cti](https://github.com/mitre/cti)

- Libraries
  - [aquasecurity/vuln-list](https://github.com/aquasecurity/vuln-list)

- WordPress
  - [wpscan](https://wpscan.com/api)

### Scan mode

[Fast Scan](https://vuls.io/docs/en/architecture-fast-scan.html)

- Scan without root privilege, no dependencies
- Almost no load on the scan target server
- Offline mode scan with no internet access. (CentOS, Alma Linux, Rocky Linux, Debian, Oracle Linux, Red Hat, Fedora, and Ubuntu)

[Fast Root Scan](https://vuls.io/docs/en/architecture-fast-root-scan.html)

- Scan with root privilege
- Almost no load on the scan target server
- Detect processes affected by update using yum-ps (Amazon Linux, CentOS, Alma Linux, Rocky Linux, Oracle Linux, Fedora, and RedHat)
- Detect processes which updated before but not restarting yet using checkrestart of debian-goodies (Debian and Ubuntu)
- Offline mode scan with no internet access. (CentOS, Alma Linux, Rocky Linux, Debian, Oracle Linux, Red Hat, Fedora, and Ubuntu)

### [Remote, Local scan mode, Server mode](https://vuls.io/docs/en/architecture-remote-local.html)

[Remote scan mode](https://vuls.io/docs/en/architecture-remote-scan.html)

- User is required to only set up one machine that is connected to other target servers via SSH

[Local scan mode](https://vuls.io/docs/en/architecture-local-scan.html)

- If you don't want the central Vuls server to connect to each server by SSH, you can use Vuls in the Local Scan mode.

[Server mode](https://vuls.io/docs/en/usage-server.html)

- First, start Vuls in server mode and listen as an HTTP server.
- Next, issue a command on the scan target server to collect software information. Then send the result to Vuls Server via HTTP. You receive the scan results as JSON format.
- No SSH needed, No Scanner needed. Only issuing Linux com
