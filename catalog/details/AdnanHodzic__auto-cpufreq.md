# AdnanHodzic/auto-cpufreq

Automatic CPU speed & power optimizer for Linux

## features

One of the problems with Linux today on laptops is that the CPU will run in an unoptimized manner which will negatively impact battery life. For example, the CPU may run using the "performance" governor with turbo boost enabled regardless of whether it's plugged into a power outlet or not.

These issues can be mitigated by using tools like [indicator-cpufreq](https://itsfoss.com/cpufreq-ubuntu/) or [cpufreq](https://github.com/konkor/cpufreq), but those still require manual action from your side which can be daunting and cumbersome.

Tools like [TLP](https://github.com/linrunner/TLP) (which I used for numerous years) can help extend battery life, but may also create their own set of problems, such as losing turbo boost.

Given all of the above, I needed a simple tool that would automatically make CPU frequency-related changes and save battery life, but let the Linux kernel do most of the heavy lifting. That's how auto-cpufreq was born.

Please note: auto-cpufreq aims to replace TLP in terms of functionality, so after you install auto-cpufreq _it's recommended to remove TLP_. Using both for the same functionality (i.e., to set CPU frequencies) will lead to unwanted results like overheating. Hence, only use [both tools in tandem](https://github.com/AdnanHodzic/auto-cpufreq/discussions/176) if you know what you're doing.

One tool/daemon that does not conflict with auto-cpufreq in any way, and is even recommended to have running alongside, is [thermald](https://wiki.debian.org/thermald).

#### Supported architectures and devices

Only devices with an Intel, AMD, or ARM CPU are supported. This tool was developed to improve performance and battery life on laptops, but running it on desktops/servers (to lower power consumption) should also be possible.

## Features

- Monitoring
  - Basic system information
  - CPU frequency (system total & per core)
  - CPU usage (system total & per core)
  - CPU temperature (total average & per core)
  - Battery state
  - System load
- CPU frequency scaling, governor, and [turbo boost](https://en.wikipedia.org/wiki/Intel_Turbo_Boost) management based on
  - Battery state
  - CPU usage (total & per core)
  - CPU temperature in combination with CPU utilization/load (to prevent overheating)
  - System load
- Automatic CPU & power optimization (temporary and persistent)
- Settings battery charging thresholds (limited support)

## installation

### auto-cpufreq-installer

> As auto-cpufreq relies on git based versioning, users are advised to install `auto-cpufreq`  using `git clone` method only. Downloading source code as a zip/from release will emit build error like [these](https://github.com/AdnanHodzic/auto-cpufreq/issues/623).

Get source code, run installer, and follow on-screen instructions:

```
git clone https://github.com/AdnanHodzic/auto-cpufreq.git
cd auto-cpufreq && sudo ./auto-cpufreq-installer
```

### Snap Store

*Please note: while all [auto-cpufreq >= v2.0 CLI functionality](https://www.youtube.com/watch?v=SPGpkZ0AZVU&t=295s) will work as intended, [the GUI won't be available on Snap package installs](http://foolcontrol.org/wp-content/uploads/2023/10/auto-cpufreq-v2-snap-deprecation-notice.png) due to [Snap package confinement limitations](https://forum.snapcraft.io/t/pkexec-not-found-python-gtk-gnome-app/36579). Hence, please consider installing auto-cpufreq using [auto-cpufreq-installer](#auto-cpufreq-installer)*.

auto-cpufreq is available on the [Snap Store](https://snapcraft.io/auto-cpufreq) or via CLI:

```
sudo snap install auto-cpufreq
```

**Please note:**
- Make sure [snapd](https://snapcraft.io/docs/installing-snapd) is installed and `snap version` is >= 2.44 for `auto-cpufreq` to fully work due to [recent snapd changes](https://github.com/snapcore/snapd/pull/8127).

- Fedora users will [encounter the following error](https://twitter.com/killyourfm/status/1291697985236144130) due to `cgroups v2` [being in development](https://github.com/snapcore/snapd/pull/7825). This problem can be resolved by either running `sudo snap run auto-cpufreq` after the snap installation or by using the [auto-cpufreq-installer](#auto-cpufreq-installer) which doesn't have this issue.

### AUR package (Arch based distributions)

[![AUR package](https://repology.org/badge/version-for-repo/aur/auto-cpufreq.svg)](https://aur.archlinux.org/packages/auto-cpufreq)

The AUR [Release Package](https://aur.archlinux.org/packages/auto-cpufreq) is currently being maintained by [MusicalArtist12](https://github.com/MusicalArtist12), [liljaylj](https://github.com/liljaylj), and [parmjotsinghrobot](https://github.com/parmjotsinghrobot). 

**Notices**

- The [Git Package](https://aur.archlinux.org/packages/auto-cpufreq-git) is seperately maintained and was last updated on version 1.9.6. 
- The build process links to `/usr/share/` instead of `/usr/local/share/`
- The daemon installer provided does not work, instead start the daemon with 

``` 
# systemctl enable --now auto-cpufreq 
```
- The GNOME Power Profiles daemon is [automatically disabled by auto-cpufreq-installer](https://github.com/AdnanHodzic/auto-cpufreq#1-power_helperpy-script-snap-package-install-only) due to it's conflict with auto-cpufreq.service. However, this doesn't happen with AUR installs, which can lead to problems (e.g., [#463](https://github.com/AdnanHodzic/auto-cpufreq/issues/463)) if not masked manually.
  - Open a terminal and run `sudo systemctl mask power-profiles-daemon.service` (then `enable` and `start` the auto-cpufreq.service if you haven't already).
- The TuneD daemon(enabled by default with Fedora 41) is [automatically disabled by auto-cpufreq-installer](https://github.com/AdnanHodzic/auto-cpufreq#1-power_helperpy-script-snap-package-install-only) due to it's conflict with auto-cpufreq.service.

### Gentoo Linux (GURU Repository)

New versions of auto-cpufreq were recently added to GURU, Gentoo's official community-maintained ebuild repository. The [ebuild](https://github.com/gentoo-mirror/guru/tree/master/sys-power/auto-cpufreq) is maintaned by [S41G0N](https://github.com/S41G0N) and other [GURU contributors](https://bugs.gentoo.org), who can respond in case of issues.

In order to build auto-cpufreq, it is necessary to add & sync GURU repository first. Adding ~amd64 keyword is also needed to unmask the package.

``` 
# echo "sys-power/auto-cpufreq ~amd64" >> /etc/portage/package.accept_keywords


## configuration

{inputs, pkgs, ...}: {
    # ---Snip---
    programs.auto-cpufreq.enable = true;
    # optionally, you can configure your auto-cpufreq settings, if you have any
    programs.auto-cpufreq.settings = {
    charger = {
      governor = "performance";
      turbo = "auto";
    };

    battery = {
      governor = "powersave";
      turbo = "auto";
    };
  };
    # ---Snip---
}
```
</details>

<details>
<summary>Nixpkgs</summary>
<br>

There is a nixpkg available, but it is more prone to being outdated, whereas the flake pulls from the latest commit. You can install it in your `configuration.nix` and enable the system service:
```nix
# configuration.nix

# ---Snip---
environment.systemPackages = with pkgs; [
    auto-cpufreq
];

services.auto-cpufreq.enable = true;
# ---Snip---
```
</details>

## tools

# example: for 1GHz = 1000 MHz = 1000000 kHz -> scaling_max_freq = 1000000
