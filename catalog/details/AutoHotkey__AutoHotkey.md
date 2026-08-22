# AutoHotkey/AutoHotkey

AutoHotkey - macro-creation and automation-oriented scripting utility for Windows.

## configuration

AutoHotkeyx.vcxproj contains several combinations of build configurations.  The main configurations are:

  - **Debug**: AutoHotkey.exe in debug mode.
  - **Release**: AutoHotkey.exe for general use.
  - **Self-contained**: AutoHotkeySC.bin, used for compiled scripts.

Secondary configurations are:

  - **(mbcs)**: ANSI (multi-byte character set). Configurations without this suffix are Unicode.
  - **.dll**: Builds an experimental dll for use hosting the interpreter, such as to enable the use of v1 libraries in a v2 script. See [README-LIB.md](README-LIB.md).
