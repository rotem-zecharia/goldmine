# dedsec1121fk/DedSec

Official repository of the DedSec Project.

## requirements

| Component | Minimum Specification |
| :-------- | :-------------------- |
| **Device** | Android phone or tablet with Termux installed |
| **Storage** | Minimum **6GB** free space |
| **RAM** | Minimum **2GB** |
| **Internet** | Needed for first installation and updates |

> **Installation time:** The first full installation can take approximately **20–50 minutes**, depending on your internet connection and device processor.

> **Storage warning:** The DedSec Project itself requires a minimum of **6GB** of free space. Some scripts can create additional output—such as captured photos, videos, audio, screenshots, downloads, logs, reports, backups, or other generated files—so actual storage usage can grow beyond 6GB depending on how you use the project.

## installation

#### Option 1: First-Time Full Install

Use this path if you are installing the DedSec Project for the first time.

##### 1. Install F-Droid, then install Termux and the recommended add-ons

- Download and install **F-Droid**.
- Open F-Droid.
- Search for **Termux** and install it.
- Recommended extras: **Termux:API** and **Termux:Styling**.

##### 2. Open Termux and prepare packages

Important: open the **Termux** app on your device before copying and pasting the command below.

Run:

```bash
pkg update -y && pkg upgrade -y && pkg install git nano -y && termux-setup-storage
```

What this does:

- updates package lists
- upgrades installed packages
- installs `git` and `nano`
- requests storage access inside Termux

##### 3. Clone the DedSec Project repository

Run:

```bash
git clone https://github.com/dedsec1121fk/DedSec
```

This downloads the full project into a folder named `DedSec`.

##### 4. Enter the project folder and run setup

Run:

```bash
cd DedSec && bash Setup.sh
```

The script will handle the complete installation. After setup, you must change the prompt, change the menu style (list or numbered menu styles are the best for new users), choose the language, and run the Save DedSec Project option on your first run so your backup package is created immediately. Save DedSec Project may take a while depending on your internet connection, and the terminal may stay blank until it is ready. Run Save DedSec Project again a few times every year to keep your saved DedSec Project package fresh and ready if you ever need it. After that, close Termux from your phone's notification panel using the exit button, then open Termux again. Tip: You can quickly open the menu by typing 'e' (English) or 'g' (Greek) in Termux.

##### 5. Complete the post-setup configuration

After setup finishes, do the following:

- change the **prompt**
- change the **menu style**
- for new users, **list** or **numbered** menu styles are the best choices
- choose your **language**
- run **Save DedSec Project** on your first run so your backup package is created immediately
- run **Save DedSec Project** again a few times every year to keep your saved package fresh and ready if you need it
- a manual **Save DedSec Project** operation may take a while depending on your internet connection, and the terminal may stay blank until it is ready
- fully close Termux from your phone's **notification panel** using the **exit button**
- open Termux again

##### 6. Quick launch tip after setup

After reopening Termux, you can quickly open the project menu by typing:

- `e` for **English**
- `g` for **Greek**

#### Option 2: Update an Existing Installation

Use this if the project is already installed and you only want the newest files.

First enter the project folder:

```bash
cd ~/DedSec
```

Then pull the newest changes:

```bash
git pull
```

Run setup again so the consolidated dependency manager checks local files, updates dependencies, and opens the menu:

```bash
bash Setup.sh
```

To update dependencies without opening the menu, use:

```bash
bash Setup.sh --update-only
```

This is useful after major project changes, new dependencies, or menu updates.

#### Option 3: Open the Project Later Without Reinstalling

If the project is already installed and configured, you usually do **not** need to reinstall it every time.

You can:

- open Termux and use the quick-launch command if it is already configured
- type `e` for **English** or `g` for **Greek** to open the menu quickly
- or manually enter the folder again:

```bash
cd ~/DedSec
```

If you need to run setup again manually:

```bash
bash Setup.sh
```

## configuration

- **About:** shows the latest DedSec Project update date, Termux storage usage, DedSec Project size, hardware details, internal storage, processor, RAM, carrier, kernel version, Android version, device model, manufacturer, uptime, battery status, and current Termux user.
- **DedSec Project Update (Source 1):** updates the installed project from the main `dedsec1121fk/DedSec` repository by fetching the newest files and applying the latest version.
- **DedSec Project Update (Source 2):** updates the installed project from the backup `sal-scar/DedSec` repository, useful when the first source is unavailable or when you want the mirror source.
- **Update Packages & Modules:** runs the consolidated `Setup.sh --no-run` dependency routine, which checks local Termux packages and Python modules first, updates installed items, and downloads anything still missing without opening a second menu process.
- **Access Sponsors-Only Scripts:** checks whether GitHub is connected in Termux, asks the user to connect GitHub if needed, verifies sponsor access, and downloads or replaces the local Sponsors-Only folder when access is confirmed. The $3 tier includes the current sponsor scripts, including Login Stealer.py, while the $9 tier includes all $3 scripts plus Widget Maker.py, Kraken Trader.py, and Noob Hacker.py. If the account does not have access, it returns the user to the settings menu without downloading anything.
- **Save DedSec Project:** creates a DedSec Project backup in your phone Downloads folder.
- **Transfer System:** creates privacy-filtered Core/Data ZIP archives plus `Install.sh` in `Downloads/Termux Transfer/` for offline migration to another compatible Termux device. SSH keys, GitHub authentication, credentials, tokens, `.env` files, and detected project secrets are excluded.
- **Change Prompt:** changes the username shown in the Termux prompt, sanitizes unsafe characters, updates `bash.bashrc`, and removes the default MOTD when needed.
- **GitHub Account:** opens a GitHub submenu for connecting with GitHub CLI, disconnecting the account, showing GitHub stats, and syncing the Termux prompt with the connected GitHub username.
- **Termux Usage Stats:** scans the local Termux workspace and shows tracked time, files scanned, files created, files edited, files deleted, latest created files, latest edited files, latest deleted files, programming languages used, shell commands found, and most active folders.
- **VPN & Tor Utilities:** provides optional no-root network privacy controls. It can enable or disable Tor, enable or disable proxy-based VPN routing, choose a VPN country, renew VPN proxies, update VPN/Tor tools, show connection status, and refresh shell exports so new Termux shells can reuse the selected network settings.
- **Change Menu Style:** lets you switch between **List Style**, **Grid Style**, **Choose By Number**, and **DedSec OS**. The selected style is saved so the project opens the same way next time.
- **Menu Auto-Start:** enables or disables automatic DedSec menu startup when Termux opens, depending on whether you want Termux to boot straight into the project menu or stay as a normal shell.
- **Choose Language / Επιλέξτε Γλώσσα:** saves the preferred language in `~/Language.json` and hides or shows the Greek folder depending on whether English or Greek is selected.
- **Credits:** displays the project creator, art artists, legal document credit, Discord server maintenance credit, and past help credits.
- **Uninstall DedSec Project:** restores backed-up Termux configuration when possible, removes project configuration files, cleans startup changes, and gives the final command needed to remove the project folder safely.
- **Exit:** closes Settings.py and returns you to Termux.

## tools

The usage stats section builds a local activity snapshot of your Termux workspace. On later scans, it compares changes and reports what was created, edited, or deleted. It also detects programming language usage by file extension, checks shell history commands, lists recent file activity, and highlights active folders.

## features

- **Chats, Groups & Stories:** Live direct messages, group chats, saved messages, GIFs, voice notes, file sharing, the discussion room, stories, and call flows where browser and device support allow it.
- **Security, Access & Control:** User approval, device access requests, remembered-device login, optional security-question 2FA, chat PIN locks, online status, reports, admin pages, and appearance or account settings.
- **Profiles, Vault & Tools:** Profile editing, an advanced private file vault, opt-in live locations, encrypted Profiler records with search, import, export, and combine tools, administrator bounty controls, and the built-in Face Detector.
- **Weather, Links & Sharing:** Search weather by place or current location, view detailed forecasts for up to 14 days, and use generated HTTPS, Cloudflared, or Tor links with downloadable QR codes. Vault files can also be shared through controlled links with optional passwords, expiry, and revocation.
