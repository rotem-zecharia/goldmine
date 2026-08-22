# CISOfy/lynis

Lynis - Security auditing tool for Linux, macOS, and UNIX-based systems. Assists with compliance testing (HIPAA/ISO27001/PCI DSS) and system hardening. Agentless, and installation optional.

## installation

There are multiple options available to install Lynis.

### Software package

For systems running Linux, BSD, and macOS, there is typically a package available. This is the preferred method of obtaining Lynis, as it is quick to install and easy to update. The Lynis project itself also provides [packages](https://packages.cisofy.com/) in RPM or DEB format suitable for systems systems running:
`CentOS`, `Debian`, `Fedora`, `OEL`, `openSUSE`, `RHEL`, `Ubuntu`, and others.

Some distributions may also have Lynis in their software repository: [![Repology](https://repology.org/badge/tiny-repos/lynis.svg)](https://repology.org/project/lynis/versions)

Note: Some distributions don't provide an up-to-date version. In that case it is better to use the CISOfy software repository, download the tarball from the website, or download the latest GitHub release.

### Git

The very latest developments can be obtained via git.

1. Clone or download the project files (**no compilation nor installation** is required) ;

        git clone https://github.com/CISOfy/lynis

2. Execute:

        cd lynis && ./lynis audit system

If you want to run the software as `root` (or sudo), we suggest changing the ownership of the files. Use `chown -R 0:0` to recursively alter the owner and group and set it to user ID `0` (`root`). Otherwise Lynis will warn you about the file permissions. After all, you are executing files owned by a non-privileged user.


## Documentation

Have a look at the [Lynis documentation](https://cisofy.com/documentation/lynis/) to learn more about the configuration and usage of Lynis. When you are interested in reading more articles about Linux security, then check out the [Linux security blog](https://linux-audit.com/) named Linux Audit. For some suggestions by Lynis, this is also the source used to learn more about specific findings.

## Customization

If you want to create your own tests, have a look at the [Lynis software development kit](https://github.com/CISOfy/lynis-sdk).

## Security

We participate in the [CII best practices](https://www.bestpractices.dev/en/projects/96) badge program of the Linux Foundation.

## Media and Awards

Lynis is collecting some awards along the way and we are proud of that.

* 2016
  * [Best of Open Source Software Awards 2016](http://www.infoworld.com/article/3121251/open-source-tools/bossie-awards-2016-the-best-open-source-networking-and-security-software.html#slide13).
  * Article by TechRepublic, considering Lynis a "must-have" tool: [How to quickly audit a Linux system from the command line](http://www.techrepublic.com/article/how-to-quickly-audit-a-linux-system-from-the-command-line/)
  * [![ToolsWatch Best Tools (top 10)](https://www.toolswatch.org/badges/toptools/2016.svg)](https://www.toolswatch.org/2017/02/2016-top-security-tools-as-voted-by-toolswatch-org-readers/)

* 2015
  * [![ToolsWatch Best Tools (second place)](https://www.toolswatch.org/badges/toptools/2015.svg)](https://www.toolswatch.org/2016/02/2015-top-security-tools-as-voted-by-toolswatch-org-readers/)
  * [Best of Open Source Software Awards 2015](http://www.idgenterprise.com/news/press-release/infoworld-announces-the-2015-best-of-open-source-software-awards/) ([mirror](https://web.archive.org/web/20210313082124/https://www.idg.com/news/infoworld-announces-the-2015-best-of-open-source-software-awards/)).

* 2014
  * [![ToolsWatch Best Tools (third place)](https://www.toolswatch.org/badges/toptools/2014.svg)](https://www.toolswatch.org/2015/01/2014-top-security-tools-as-voted-by-toolswatch-org-readers/)

* 2013
  * [![ToolsWatch Best Tools (sixth place)](https://www.toolswatch.org/badges/toptools/2013.svg)](https://www.toolswatch.org/2013/12/2013-top-security-tools-as-voted-by-toolswatch-org-readers/)

## Contribute

> We love contributors.

Do you have something to share? Want to help out with translating Lynis into your own language? Create an issue or pull request on GitHub, or send us an e-mail: lynis-dev@cisofy.com.

Mor
