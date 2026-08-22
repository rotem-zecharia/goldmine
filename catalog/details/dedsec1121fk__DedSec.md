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

### Before You Start

F-Droid is an alternative app store for Android that provides free and open-source software. It's the recommended way to install Termux and other security tools.

- Install **Termux from F-Droid** for the best compatibility.
- If you install APK files manually, allow installation from unknown apps in your Android settings.
- When Termux asks for storage permission, allow it if you want the project to access Downloads and saved files.
- For long installs, long-press inside Termux, tap **More**, and enable **Keep screen on**.
- You can also customize the terminal appearance by long-pressing inside Termux, tapping **More**, and selecting **Style**.

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

### Important Notes

- Keep an internet connection enabled during the first install.
- The first installation can take longer than normal because packages and tools may need to download.
- Run **Save DedSec Project** on the first run, then run it again a few times every year to keep the saved package fresh. It may take a while depending on your internet co

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

### GitHub Account Submenu

The GitHub section can install or use `gh`, start the official GitHub login flow, save the connected username, disconnect the saved account, and show combined repository stats such as repositories counted, total st

## tools

The usage stats section builds a local activity snapshot of your Termux workspace. On later scans, it compares changes and reports what was created, edited, or deleted. It also detects programming language usage by file extension, checks shell history commands, lists recent file activity, and highlights active folders.

### VPN & Tor Utilities

The network utilities section gives you optional controls for Tor and proxy-based VPN routing without root. Tor can be enabled or disabled from the menu. VPN routing can be enabled or disabled separately, uses a selectable country or refreshed proxy pool, and saves the chosen network state so it can be applied again when Termux starts. The status screen shows whether Tor and VPN routing are enabled, what country is selected, and which proxy is currently active.

### DedSec OS Mode

**DedSec OS** is the browser-based local workspace mode inside Settings.py. It adds a phone-first interface with a file browser, safe text editor, terminal view, session manager, DedSec apps launcher, Linux package store actions, notifications, fullscreen and split view controls, sidebar controls, wallpaper support, display name settings, terminal color settings, project/menu settings, menu auto-start controls, language controls, prompt controls, password login, optional authenticator-style 2FA, and password recovery through three security questions. It also includes project action buttons for updating both sources, updating packages/modules, accessing Sponsors-Only scripts, and opening credits.

## features

- **Chats, Groups & Stories:** Live direct messages, group chats, saved messages, GIFs, voice notes, file sharing, the discussion room, stories, and call flows where browser and device support allow it.
- **Security, Access & Control:** User approval, device access requests, remembered-device login, optional security-question 2FA, chat PIN locks, online status, reports, admin pages, and appearance or account settings.
- **Profiles, Vault & Tools:** Profile editing, an advanced private file vault, opt-in live locations, encrypted Profiler records with search, import, export, and combine tools, administrator bounty controls, and the built-in Face Detector.
- **Weather, Links & Sharing:** Search weather by place or current location, view detailed forecasts for up to 14 days, and use generated HTTPS, Cloudflared, or Tor links with downloadable QR codes. Vault files can also be shared through controlled links with optional passwords, expiry, and revocation.

### All ButSystem Areas
- **Navigation & Menu Flow:** The burger menu is the main control hub of ButSystem. From there you move between chats, saved messages, discussion, groups, calls, stories, live locations, files, news, weather, profiles, Profiler, reports, notifications, admin pages, settings, help, and login or logout actions, while the language toggle keeps the interface available in both English and Greek.
- **Authentication & Access:** ButSystem opens through its landing, loading, login, and signup flow, then adds extra access control where needed. That includes user approval, device access requests, remembered-device login, optional security-question two-factor checks, and password recovery or reset actions so access stays tied to approved users and approved devices.
- **Direct Messages:** The DM area is built for day-to-day private conversation. You can open a chat, write and send text, edit or delete messages, search conversation content, attach media or files, use GIFs, record or play voice notes, and work with chat protections such as PIN locks and visible online status where those controls are enabled.
- **Discussion Room:** Discussion works more like a shared stream than a one-to-one chat. It is the place for broader entries, category-based posting, search, refresh, loading more content, and opening a specific entry when you want a calmer shared space separate from normal DMs.
- **Groups:** The Groups area lets users build shared spaces with roles and moderation controls. You can create a group, invite or add members, check the member list, manage owner or admin actions such as promote, demote, or remove, leave a group when needed, and continue the conversation through the related group chat with messages and attachments.
- **Calls & Live Communication:** Where browser support and device permissions allow it, ButSystem includes call flows for starting, joining, accepting, denying, muting, and ending a live call. The exact experience depends on microphone permissions and the current browser environment, so the call layer is treated as a live feature area rather than a static page.
- **Stories & Live Locations:** ButSystem also covers lighter live-sharing tools. Stories provide creation, viewing, and reaction controls, while Live Locations is reserved for opt-in location sharing with start, stop, refresh, and clear consent or warning prompts before location data is actively shared.
- **Files, Vault & Saved Media:** The Files and Vault area works like a private server-style file manager. It supports folders and navigation, normal or chunked uploads with cancellation, search, categories, file-type filters, sorting, previews, opening and downloading, rename, move, bulk actions, deletion, comments, activity history, detailed size, MIME, and date metadata, optional SHA-256, and controlled share links with optional passwords, expiry times, and revocation.
- **Profile, Account & Appearance:** Your own profile area handles identity and account presentation. From there use
