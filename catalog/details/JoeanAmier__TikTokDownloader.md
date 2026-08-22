# JoeanAmier/TikTokDownloader

抖音 / TikTok 平台作品下载/数据采集工具

## tools

![WebAPI模式截图](docs/screenshot/WebAPI模式截图CN1.png)
*****
![WebAPI模式截图](docs/screenshot/WebAPI模式截图CN2.png)

> **启动该模式后，访问 `http://127.0.0.1:5555/docs` 或者 `http://127.0.0.1:5555/redoc` 可以查阅自动生成的文档！**

### API 调用示例代码

```python
from httpx import post
from rich import print


def demo():
    headers = {"token": ""}
    data = {
        "detail_id": "0123456789",
        "pages": 2,
    }
    api = "http://127.0.0.1:5555/douyin/comment"
    response = post(api, json=data, headers=headers)
    print(response.json())


demo()
```

# 📋 项目说明

## 快速入门

<p>⭐ Mac OS、Windows 10 及以上用户可前往 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 或者 <a href="https://github.com/JoeanAmier/TikTokDownloader/actions">Actions</a> 下载已编译的程序，开箱即用！</p>
<p>⭐ 本项目包含自动构建可执行文件的 GitHub Actions，使用者可以随时使用 GitHub Actions 将最新源码构建为可执行文件！</p>
<p>⭐ 自动构建可执行文件教程请查阅本文档的 <code>构建可执行文件指南</code> 部分；如果需要更加详细的图文教程，请 <a href="https://mp.weixin.qq.com/s/TorfoZKkf4-x8IBNLImNuw">查阅文章</a>！</p>
<p><strong>注意：由于 Mac OS 平台的可执行文件 <code>main</code> 未经过代码签名，首次运行时会受到系统安全限制。请先在终端执行 <code>xattr -cr 项目文件夹路径</code> 命令移除安全标记，执行一次后即可正常运行。</strong></p>
<hr>
<ol>
<li><b>运行可执行文件</b> 或者 <b>配置环境运行</b>（二选一）
<ol><b>运行可执行文件</b>
<li>下载 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 或者 Actions 构建的可执行文件压缩包</li>
<li>解压后打开程序文件夹，双击运行 <code>main</code></li>
</ol>
<ol><b>配置环境运行</b>
<li>安装不低于 <code>3.12</code> 版本的 <a href="https://www.python.org/">Python</a> 解释器</li>
<li>下载最新的源码或 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 发布的源码至本地</li>
<ol><b>使用 pip 安装项目依赖</b>
<li>运行 <code>python -m venv venv</code> 命令创建虚拟环境（可选）</li>
<li>运行 <code>.\venv\Scripts\activate.ps1</code> 或者 <code>venv\Scripts\activate</code> 命令激活虚拟环境（可选）</li>
<li>运行 <code>pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt</code> 命令安装程序所需模块</li>
<li>运行 <code>python .\main.py</code> 或者 <code>python main.py</code> 命令启动 DouK-Downloader</li>
</ol>
<ol><b>使用 uv 安装项目依赖（推荐）</b>
<li>运行 <code>uv sync --no-dev</code> 命令同步环境依赖</li>
<li>运行 <code>uv run main.py</code> 命令启动 DouK-Downloader</li>
</ol>
</ol>
</li>
<li>阅读 DouK-Downloader 的免责声明，根据提示输入内容</li>
<li>将 Cookie 信息写入配置文件
<ol><b>手动输入 Cookie</b>
<li>参考 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">Cookie 提取教程</a>，复制所需 Cookie 至剪贴板</li>
<li>选择 <code>手动输入 Cookie</code> 选项，粘贴 Cookie 内容后按照程序提示操作</li>
</ol>
<ol><b>从剪贴板读取 Cookie</b>
<li>参考 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">Cookie 提取教程</a>，复制所需 Cookie 至剪贴板</li>
<li>选择 <code>从剪贴板读取 Cookie</code> 选项，程序会自动读取剪贴板的 Cookie 并写入配置文件</li>
</ol>
<ol><b><del>从浏览器读取 Cookie（弃用）</del></b>
<li><del>选择 <code>从浏览器读取 Cookie</code> 选项，按照提示输入浏览器类型或序号</del></li>
</ol>
<ol><b><del>扫码登录获取 Cookie</del>（失效）</b>
<li><del>选择 <code>扫码登录获取 Cookie</code> 选项，程序会显示登录二维码图片，并使用默认应用打开图片</del></li>
<li><del>使用抖音 APP 扫描二维码并登录账号</del></li>
<li><del>按照提示操作，程序会自动将 Cookie 写入配置文件</del></li>
</ol>
</li>
<li>返回程序界面，依次选择 <code>终端交互模式</code> -> <code>批量下载链接作品</code> -> <code>手动输入待采集的作品链接</code></li>
<li>输入抖音作品链接即可下载作品文件（TikTok 平台需要更多初始设置，详见文档）</li>
<li>更多详细说明请查看 <b><a href="https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation">项目文档</a></b></li>
</ol>
<p>⭐ 推荐使用 <a href="https://learn.microsoft.com/zh-cn/windows/terminal/install">Windows 终端</a>（Windows 11 自带默认终端）</p>

### Docker 容器

<ol>
<li>获取镜像</li>
<ul>
<li>方式一：使用 <code>Dockerfile</code> 文件构建镜像</li>
<li>方式二：使用 <code>docker pull joeanamier/tiktok-downloader</code> 命令拉取镜像</li>
<li>方式三：使用 <code>docker pull ghcr.io/joeanamier/tiktok-downloader</code> 命令拉取镜像</li>
</ul>
<li>创建容器：<code>docker run --name 容器名称(可选) -p 主机端口号:5555 -v tiktok_downloader_volume:/app/Volume -it &lt;镜像名称&gt;</code>
</li>
<br><b>注意：</b>此处的 <code>&lt;镜像名称&gt;</code> 需与您在第一步中使用的镜像名称保持一致（例如 <code>joeanamier/tiktok-downloader</code> 或 <code>ghcr.io/joeanamier/tiktok-downloader</code>）
<li>运行容器
<ul>

