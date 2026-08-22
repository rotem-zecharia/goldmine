# bee-san/RustScan

🤖 The Modern Port Scanner 🤖

## installation

You can install RustScan's binary from our [releases page](https://github.com/RustScan/RustScan/releases).

We would prefer you to install with a package manager so it is tested and works for your system.

RustScan is in many repositories already. Install it with whatever tools you wish:

[![Packaging status](https://repology.org/badge/vertical-allrepos/rustscan.svg)](https://repology.org/project/rustscan/versions)

RustScan only officially supports Cargo installations, if you want to use that please install Rust and then `cargo install rustscan`

Example installations include:

MacOS:

```
  brew install rustscan
```

Arch:

```
  pacman -S rustscan
```

## features

- Scans all 65k ports in **3 seconds**.
- Full scripting engine support. Automatically pipe results into Nmap, or use our scripts (or write your own) to do whatever you want.
- Adaptive learning. RustScan improves the more you use it. No bloated machine learning here, just basic maths.
- The usuals you would expect. IPv6, CIDR, file input and more.
- Automatically pipes ports into Nmap.

## ‼️ Important Links

|         <!--Installation Guide-->          |          <!--Documentation-->          |       <!--Discord-->        |
| :----------------------------------------: | :------------------------------------: | :-------------------------: |
| :book: [Installation Guide][toc-install] | :books: [Documentation][links-table-2] | :parrot: [Discord][discord] |

## 🙋 Table of Contents

- 📖 [Installation Guide][toc-install]
- 🐋 [Docker Usage][toc-docker-usage]
- 🦜 [Discord][discord]
- 🤸 [Usage][usage-1]

# 🔭 Why RustScan?

RustScan is a modern take on the port scanner. Sleek & fast. All while providing extensive extendability to you.

Not to mention RustScan uses Adaptive Learning to improve itself over time, making it the best port scanner for **you**.

## 🧋 Speed

![fast][speed-1]

Speed is guaranteed via RustScan. However, if you want to run a slow scan due to stealth, that is possible too.

Firstly, let's talk code.

We have tests that check to see if RustScan is significantly slower than the previous version. If it is, the continuous integration fails, and we can't commit code to master unless we make it faster.

[HyperFine][speed-2] is used to monitor RustScan's performance over time to answer the question, "Are we getting faster? Are we getting slower?".

Every pull request is reviewed by **one** person, but more often than not, **two** people review it. We test it manually and ensure the code doesn't negatively affect performance.

[Read more here][speed-3].

## ⚙️ Extensible

![scripts][extensible-1]

### _RustScan piping results into the custom Python script_

RustScan has a new scripting engine that allows anyone to write scripts in most languages. Python, Lua, and Shell are all supported.

Want to take your found ports and pipe them into Nmap for further analysis? That's possible. Want to run `smb-enum` if SMB is found open? Possible.

The possibilities are endless -- and you can write scripts in whatever language you feel comfortable with.

[Read more here][extensible-2].

## 🌊 Adaptive

![adaptive][adaptive-1]

### _RustScan automatically fine-tunes itself to match the host OS_

RustScan has a cool set of features called "Adaptive Learning". These features "learn" about the environment you are scanning and how _you_ use RustScan to **improve itself over time**.

We use this umbrella term for any feature that fits this criterion. The list constantly changes, so [check out our wiki for more information][adaptive-learning].

## 👩‍🦯 Accessible

![fast][accessible-1]

RustScan is one of the first penetration testing tools that aims to be entirely accessible.

[Most penetration testing tools are not accessible][accessible-2], which negatively affects the whole industry.

RustScan has continuous integration testing that aims to ensure it is accessible, and we are constantly working on ways to improve our accessibility and ensure _everyone_ can use RustScan.

## tools

We have 2 usage guides. [Basic Usage][usage-1] and [Things you may want to do][usage-2].

We also have documentation about our config file [here][config-file-here].

# 🎪 Community

[Contributing][community-1] Read this to learn how.

## Contributors ✨

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-26-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://skerritt.blog"><img src="https://avatars3.githubusercontent.com/u/10378052?v=4" width="100px;" alt=""/><br /><sub><b>Bee</b></sub></a><br /><a href="#infra-beeskerritt" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/RustScan/RustScan/commits?author=beeskerritt" title="Tests">⚠️</a> <a href="https://github.com/RustScan/RustScan/commits?author=beesan" title="Code">💻</a> <a href="#design-beeskerritt" title="Design">🎨</a></td>
    <td align="center"><a href="https://sakiir.ovh"><img src="https://avatars1.githubusercontent.com/u/9950578?v=4" width="100px;" alt=""/><br /><sub><b>SakiiR</b></sub></a><br /><a href="https://github.com/RustScan/RustScan/commits?author=SakiiR" title="Code">💻</a> <a href="https://github.com/RustScan/RustScan/issues?q=author%3ASakiiR" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/smackhack"><img src="https://avatars2.githubusercontent.com/u/48143394?v=4" width="100px;" alt=""/><br /><sub><b>smackhack</b></sub></a><br /><a href="#ideas-smackhack" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-smackhack" title="Examples">💡</a></td>
    <td align="center"><a href="http://bernardoamc.github.io/"><img src="https://avatars0.githubusercontent.com/u/428984?v=4" width="100px;" alt=""/><br /><sub><b>Bernardo Araujo</b></sub></a><br /><a href="https://github.com/RustScan/RustScan/commits?author=bernardoamc" title="Code">💻</a> <a href="https://github.com/RustScan/RustScan/issues?q=author%3Abernardoamc" title="Bug reports">🐛</a> <a href="#design-bernardoamc" title="Design">🎨</a></td>
    <td align="center"><a href="https://github.com/Isona"><img src="https://avatars2.githubusercontent.com/u/11759523?v=4" width="100px;" alt=""/><br /><sub><b>Izzy Whistlecroft</b></sub></a><br /><a href="https://github.com/RustScan/RustScan/issues?q=author%3AIsona" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://imlonghao.com"><img src="https://avatars1.githubusercontent.com/u/4951333?v=4" width="100px;" alt=""/><br /><sub><b>imlonghao</b></sub></a><br /><a href="https://github.com/RustScan/RustScan/issues?q=author%3Aimlonghao" title="Bug reports">🐛</a> <a href="#maintenance-imlonghao" title="Maintenance">🚧</a></td>
    <td align="center"><a href="https://github.com/royharoush"><img src="https://avatars3.githubusercontent.com/u/8113056?v=4" width="100px;" alt=""/><br /><sub><b>royharoush</b></sub></a><br /><a href="#ideas-royharoush" title="Ideas, Planning, & Feedback">🤔</a> <a href="#design-royharoush" title="Design">🎨</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/Atul9"><img src="https://avatars1.githubusercontent.com/u/3390330?v=4" width="100px;" alt=""/><br /><sub><b>Atul Bhosale</b></sub></a><br /><a href="https://github.com/RustScan/RustScan/commits?author=Atul9" title="Code">💻</a></td>
    <td align="center"><a href="https://tgotwig.dev"><img src="https://avatars0.githubusercontent.com/u/30773779?v=4" width="100px;" alt=""/><br /><sub><b>Thomas Gotwig</b></sub></a><br /><a href="#platform-TGotwig" title="Packaging/porting to new platform">📦</a></td>
    <td align="center"><a href="https://github.com/remigourdon"><img src="https://
