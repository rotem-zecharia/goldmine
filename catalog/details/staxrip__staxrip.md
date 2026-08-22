# staxrip/staxrip

🎞 Video encoding GUI for Windows.

## features

- Please try the [Latest Release](https://github.com/staxrip/staxrip/releases/latest) first. Usually you will find that many outstanding bugs are already fixed in the latest release versions.
- You can also have a look at the [Changelog](https://github.com/staxrip/staxrip/blob/master/CHANGELOG.md) to see if there is an entry already made for the bug/feature request you are experiencing/desiring.
    - Supporters please use the [Changelog for Supporters](https://github.com/staxrip/staxrip/blob/master/CHANGELOG-SUPPORTER.md) instead.
- If the [Latest Release](https://github.com/staxrip/staxrip/releases/latest) does not solve your problem, please use the [Issue Tracker](https://github.com/staxrip/staxrip/issues). You need to be as precise as possible using the Issue Tracker template when opening a thread in it.

## requirements

- Many tools and filters need a specific version of Microsoft Visual C++ Redistributable Runtimes. Due to the frequent changing and replacing of tools and filters, it is impossible to provide precise details about the right dependency. So if StaxRip doesn't start or you get error messages due to missing runtime files or dependencies, we recommend to download and install the Microsoft Visual C++ Redistributable Runtimes from:
    - https://gitlab.com/stdout12/vcredist/-/releases or
    - https://www.techpowerup.com/download/visual-c-redistributable-runtime-package-all-in-one

- OS limitations: **Windows 7** users can use StaxRip only partly. The following tools are included and don't have official **Windows 7** support anymore. You in case you don't want to upgrade your system, you can replace these tools with an older, compatible, version, which should work, but of course with some limited usability:
    - StaxRip itself
        - The new Blu-ray ISO image opening and mounting feature requires at least Windows 8 to work, so in case of Windows 7 you should avoid that feature.
    - MKVToolNix
        - Latest working version is reported to be `v64.0`. Last (complete) working StaxRip version is *StaxRip v2.10.0 (2021-10-06)* including *MKVToolNix v61.0*
        - Nevertheless `mkvtoolnix-64-bit-68.0.0-revision-001-g6a55c58d2` is reported to work, you can download it here: https://mkvtoolnix.download/windows/continuous/64-bit/68.0.0/
    - VapourSynth
        - Latest working version is `R73`. For most use-cases you should be fine downgrading to `R73` and use the plugins as usual.
    - Python
        - Needed for VapourSynth. Last **Windows 7** compatible version was used in *StaxRip v2.25.0 (2023-08-02)*. As of now using VapourSynth R63 it could be possible to downgrade Python to `v3.8.*`that is **Windows 7** compatible, but requires experienced users.
             
     Alternatively you can download an old StaxRip release, but then you don't benefit from new functions and bug fixes.

## tools

StaxRip is a portable application, so almost everything it needs is already included. 
This also means, that StaxRip does not have to (and cannot) be installed. 
You simply extract the [given archive](https://github.com/staxrip/staxrip/releases/latest) and when you start, StaxRip asks you where to store the settings.

It is recommended to choose the first option, which creates a subfolder in the existing startup folder where `StaxRip.exe` is in that you start.
This ensures, that you start with fresh/new settings as the settings of different versions could be imcompatible with each other,
which can lead to unwanted side effects like missing functionality or changing encoder parameters. 
It is also **very important** to **not** run existing jobs on a different StaxRip version as some encoder parameters could have been changed
and mess up the values. This is pretty rare, but it can happen.

Since `v2.37.0` the versioning has changed a little bit.  
Releases with the same second number (for example `v2.39.0`, `v2.39.2` and `v2.39.3`) are basically compatible with each other,
means that you can overwrite the existing files of your old instance and use the same/old settings.
Whenever this is possible an `UPDATE` archive is also released so you can just download the files that are needed to overwrite.
