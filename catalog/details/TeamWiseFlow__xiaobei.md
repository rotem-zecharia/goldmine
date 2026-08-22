# TeamWiseFlow/xiaobei

为OPC/中小微企业量身打造的自媒体获客智能体

## tools

推荐开通 [阿里云百炼「Token Plan」套餐](https://www.aliyun.com/benefit/ai/aistar?clubBiz=subTask..12766005..10274..)——一个套餐覆盖 DeepSeek-V4-Flash、GLM-5.2、Qwen3.6-Flash 等主流模型，**无月限额、不限购**，xiaobei 默认主力模型 DeepSeek-V4-Flash 即走此通道。开通后获得 `AWK_API_KEY`，主力模型、视觉模型、替补模型**一个 key 全覆盖**。

> 💡 **套餐选择**：前期熟悉安装可选 **Lite 版 39 元/月**；正常使用建议 **Standard 版 139 元/月**。想继续使用火山CodePlan见下方 "模型费用说明"

> 🎬 **想用视频生成能力？** 开通百炼Token Plan后，会免费获得一定额度的 `happyhorse-1.1` ，只需把对应 key（`MODELSTUDIO_API_KEY`）配置到 `daemon.env`。

> 除了阿里云的`happyhorse`系列，我们现在也支持 minimax 的H3！详见下方[视频生成模型配置](#-视频生成模型配置)

### 推荐：一键脚本安装（预构建 tarball 路线）

一行命令，全程无需预装 Node / pnpm / git（tarball 自带 portable Node + pnpm）。脚本完成后**唯一人工输入**是填 `AWK_API_KEY`（「TOKEN PLAN」套餐的 key）。

**macOS / Linux（bash，一行命令）：**

```bash
# GitHub 线路（适合能正常访问 GitHub 的网络环境）
bash -c "$(curl -fsSL https://raw.githubusercontent.com/TeamWiseFlow/xiaobei/master/scripts/install.sh)"
# 国内 atomgit 线路（tarball 走 atomgit.com → GitCode CDN，全程国内直连，脚本也从 raw.atomgit.com 拉取）
bash -c "$(curl -fsSL https://raw.atomgit.com/wiseflow/xiaobei/raw/master/scripts/install-atomgit.sh)"
```

**Windows（PowerShell）：**

> **Windows 用户请以管理员身份运行 PowerShell 再安装**（右键 PowerShell → "以管理员身份运行"）。
> 原因：安装过程中创建 NTFS 符号链接需要管理员权限（或开启开发者模式）；非管理员也能装，软链失败会自动回退拷贝。

```powershell
# GitHub 线路（适合能正常访问 GitHub 的网络环境）
irm https://raw.githubusercontent.com/TeamWiseFlow/xiaobei/master/scripts/install.ps1 | iex
# 国内 atomgit 线路（tarball 走 atomgit.com → GitCode CDN，全程国内直连，脚本也从 raw.atomgit.com 拉取）
irm https://raw.atomgit.com/wiseflow/xiaobei/raw/master/scripts/install-atomgit.ps1 | iex
```

> 按网络环境选一条命令即可：能正常访问 GitHub 走 GitHub 线路（脚本 `install.sh` / `install.ps1`）；国内网络走 atomgit 线路（脚本 `install-atomgit.sh` / `install-atomgit.ps1`，全程不经 GitHub）。两条线路安装产物完全一致，只是下载源不同。

> install 脚本默认拉最新 release tag + 下载 tarball。指定版本：`export XIAOBEI_TAG=v5.6.3`（PowerShell：`$env:XIAOBEI_TAG="v5.6.3"`）。

> 💡 **下载中断 / 安装失败？多试几次就好。** tarball 体积较大（~140MB），首装还要下 Firefox 反指纹浏览器（~557MB），网络偶发中断属正常。脚本幂等，重跑会续上已下的部分。

> ⚠️ **Windows 必须装 bash**（Git Bash 或 WSL）。install.ps1 / install-atomgit.ps1 用 `tar`（Win10 1803+ 自带）解压 tarball，但 `setup-crew.sh` 是 bash 脚本，部署 crew workspace 离不开 bash。无 bash 时脚本会跳过 crew 模板部署并提示手动补跑——此时小贝团队起不来。装 Git Bash：https://git-scm.com （安装时勾选 "Add to PATH"）。

> 完整步骤：先装 Git Bash（安装时勾选 "Add to PATH"，让 bash 进 PowerShell 的 PATH）→ 再在 PowerShell 跑上面那条 `irm | iex`。

> 💡 **Windows 建议打开「开发者模式」**（设置 → 隐私和安全 → 开发者选项 → 开启开发人员模式，Win10 1703+ 支持）。安装脚本会创建两条软链：仓内 `skills/` → `~/.openclaw/skills`、各 crew 的 `skills/` → `~/.openclaw/workspace-<crew>/skills/`，让 openclaw 的 skill loader 拾取技能、且仓内改完即生效无需重跑安装。软链在 Windows 上需要开发者模式（或管理员 PowerShell）；两者都没打开时脚本会自动回退为拷贝——功能正常但技能不会随仓更新自动同步，重跑安装才会刷新。

装好后脚本最后会自动出微信绑定二维码——用手机微信扫一下、点确认，小贝就能用了。已绑过的机器自动跳过这一步。

> **目录职责**：`~/xiaobei/` = 程序（引擎 + 模板 + 脚本 + 工具 + wrapper）；`~/.openclaw/` = 运行数据（openclaw.json + daemon.env + workspaces + logs）。两者分开，升级只换 `~/xiaobei/`，用户数据不动。可用 `XIAOBEI_HOME` / `OPENCLAW_HOME` env 覆盖。

> **系统要求**：推荐 Ubuntu 22.04；支持 WSL2 / macOS（arm64 + x64）；Windows 10 1803+（x64，需 Git Bash 或 WSL）。WSL2 下脚本自动注入 GUI 显示变量。

> 🖥️ **部署机器建议**：推荐用一台 **7×24 小时常开**的电脑部署，上面**不要放置个人隐私 / 机密文件**。若你希望在日常办公电脑上安装、且只在用时启动——可以期待我们即将推出的**官方 Docker 镜像**，具体可扫下方二维码咨询掌柜👇。

> **调试模式**（前台单次启动，适合测试，不走 launchd/systemd 服务）：`~/xiaobei/bin/openclaw gateway run`

> 排障见 [`docs/install-troubleshooting.md`](docs/install-troubleshooting.md)

### 微信换绑 / 增加绑定

装好后想**换一个微信号**（换绑）或**再加一个号**，都用 `channels login` 重新出二维码。`openclaw` 不在 PATH，下面命令用全路径 `~/xiaobei/bin/openclaw`（把 `~/xiaobei/bin` 加进 PATH 后可直接敲 `openclaw`）。

**换绑（替换成新号）**：先停 gateway、清掉旧账号数据，再重新 login 出码：

```bash
~/xiaobei/bin/openclaw gateway stop
rm -rf ~/.openclaw/openclaw-weixin/
~/xiaobei/bin/openclaw gateway start
~/xiaobei/bin/openclaw channels login --channel openclaw-weixin
```

> `channels login` 出码后 8 分钟内有效，扫码慢会自动刷新，用新微信扫一下、点确认即完成。

**增加绑定（保留旧号、再加一个）**：直接再跑一次 login，用另一个微信扫：

```bash
~/xiaobei/bin/openclaw channels login --channel openclaw-weixin
```

> ⚠️ 多账号时，若两个号都能匹配同一个收件人，发消息会报 `ambiguous — N accounts matched`。所以**换号场景建议用上面的"换绑"流程清掉旧号**，避免歧义；只在确实要多号并存时用"增加绑定"。

### 升级

**已装用户
