# AaronL725/grok-register

批量稳定注册 Grok 账号，支持 WebUI/GUI/CLI、多邮箱服务、多线程并发、账号级多协议代理池、grok2api 入池、SSO 风控筛查与CPA OIDC 凭证导出。

## tools

所有入池功能都是可选的。

### 本地池

```json
{
  "grok2api_auto_add_local": true,
  "grok2api_local_token_file": "",
  "grok2api_pool_name": "ssoBasic"
}
```

### 远端池

远端支持两种凭据方式，二选一：

1. `grok2api_remote_app_key`
2. `grok2api_remote_admin_username` + `grok2api_remote_admin_password`

```json
{
  "grok2api_auto_add_remote": true,
  "grok2api_remote_base": "https://你的-grok2api-域名",
  "grok2api_remote_app_key": "",
  "grok2api_remote_admin_username": "admin",
  "grok2api_remote_admin_password": "你的管理员密码",
  "grok2api_pool_name": "ssoBasic",
  "grok2api_allow_legacy_full_save": false
}
```

两套远端凭据不能同时填写。远程地址要求 HTTPS；本机地址可以使用 HTTP。

## CPA / xAI OIDC 导出

```json
{
  "cpa_export_enabled": true,
  "cpa_auth_dir": "./cpa_auths",
  "cpa_copy_to_hotload": false,
  "cpa_hotload_dir": "",
  "cpa_base_url": "https://cli-chat-proxy.grok.com/v1",
  "cpa_proxy": "",
  "cpa_headless": false,
  "cpa_force_standalone": true,
  "cpa_mint_cookie_inject": true
}
```

- `cpa_copy_to_hotload=true` 时必须填写 `cpa_hotload_dir`。
- 显式 `cpa_proxy` 始终优先。
- 未配置 `cpa_proxy` 且当前账号使用 Proxy Lease 时，CPA 会继承同一个出口，包括高级协议对应的 localhost runtime。
- CPA 导出失败只记录后处理警告，不会删除已保存账号。

## 输出与 pending 恢复

| 文件 / 目录 | 内容 |
| --- | --- |
| `accounts_*.txt` | 已成功保存的账号、密码和 SSO token |
| `sso_risk_rejected.txt` | 被 `botFlagSource=1/2` 或 `policy=deny` 隔离的 SSO |
| `mail_credentials.txt` | 临时邮箱地址与邮箱凭据 |
| `*.pending.jsonl` | 已注册但主结果文件未成功写入的账号 |
| 本地 `token.json` | 可选 grok2api 本地 token 池 |
| `cpa_auths/xai-*.json` | 可选 CPA xAI OIDC 凭证 |
| `cpa_auths/cpa_auth_failed.txt` | CPA 导出失败记录 |
| `screenshots/` | CPA 浏览器失败调试截图 |

### 恢复 pending

```bash
python grok_register_ttk.py retry-pending <pending文件> [输出文件]
```

恢复过程使用文件锁、去重和原子替换，重复执行不会重复写入已经恢复成功的同一账号。

## 项目结构

```text
.
├── grok_register_ttk.py       # GUI / CLI 入口与主适配层
├── registration_flow.py       # 串行批量注册编排
├── registration_parallel.py   # 可选多线程协调器
├── registration_browser.py    # 主注册浏览器流程
├── browser_runtime.py         # HTTP、Chromium options 与代理适配
├── proxy_pool.py              # 代理池、健康度、Lease、订阅与探测
├── proxy_protocols.py         # HTTP/SOCKS/VLESS/VMess/Trojan/HY2/TUIC 订阅解析
├── proxy_protocol_runtime.py  # 高级协议 lazy sing-box → localhost HTTP 适配
├── mail_service.py            # 四种邮箱服务
├── app_config.py              # 默认配置、校验、加载与保存
├── account_outputs.py         # 账号、pending 与 token 输出
├── sso_risk.py                # SSO botFlag / policy 早停
├── cpa_export.py              # CPA/OIDC 导出入口
├── cpa_xai/                   # CPA 浏览器、OAuth、代理桥与凭证写入
├── web/
│   ├── server.py              # FastAPI WebUI 控制层
│   ├── index.html             # WebUI 页面
│   ├── proxy-pool.js          # 代理池 WebUI 交互
│   └── proxy-pool.css         # 代理池 WebUI 样式
├── docs/proxy-pool.md         # 代理池详细说明
├── config.example.json        # 完整配置示例
├── requirements.txt           # 核心依赖
├── requirements-web.txt       # WebUI 可选依赖
└── tests/                     # 单元与兼容回归测试
```

## 常见问题

### CLI 为什么仍然打开浏览器？

CLI 只是不启动 Tk GUI。注册页交互、验证码提交和 SSO cookie 获取仍依赖真实 Chromium / Chrome。

### GUI 无法启动怎么办？

确认 Python 环境包含 Tkinter。Linux 发行版可能需要单独安装 `python3-tk`。也可以改用 CLI 或 WebUI。

### 为什么高级协议节点显示 unavailable？

VLESS / VMess / Trojan / Hysteria2 / TUIC 需要本地 sing-box。默认从系统 `PATH` 查找，也可以在 WebUI / `config.json` 设置 `proxy_singbox_path`。HTTP/SOCKS 不受影响。

### 为什么某些 V2Ray 订阅节点会被跳过？

WebUI 会显示订阅协议数量和解析错误。无法映射的 transport 或无效 URI 会只跳过对应节点，不影响同一订阅里的其他有效节点。详细映射范围见 [`docs/proxy-pool.md`](docs/proxy-pool.md)。

### 为什么配置文件不完整时 GUI / WebUI 仍能打开？

配置保存和运行校验分开。界面允许先打开并编辑配置，开始注册时才检查当前启用服务所需字段。

### 注册成功后 grok2api 或 CPA 失败怎么办？

账号本身仍然属于成功。此类错误只计入“后处理警告”。

### NSFW 开启失败会丢失账号吗？

不会。NSFW 是可选步骤，失败后仍会继续保存账号。

### 代理池为什么显示用户名和密码？

当前 WebUI 按个人部署场景设计，会显示完整代理节点和认证信息。不要把 WebUI 暴露到不受信任的网络环境。

### 如何查看代理池更详细的参数？

参见 [`docs/proxy-pool.md`](docs/proxy-pool.md)。

### 为什么账号会进入 pending？

表示注册已经完成，但主结果文件没有成功写入。使用 `retry-pending` 恢复即可，不需要重新注册。

## License

[MIT](LICENSE).

## Acknowledgments

Thanks to [linux.do](https://linux.do) — a vibrant tech community where this project is shared and discussed.

## Star History

<a href="https://www.sta
