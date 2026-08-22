# dmMaze/BallonsTranslator

深度学习辅助漫画翻译工具, 支持一键机翻和简单的图像/文本编辑 / Yet another computer-aided comic/manga translation tool powered by deeplearning

## features

> [!IMPORTANT]  
> **如打算公开分享本工具的机翻结果，且没有有经验的译者进行过完整的翻译或校对，请在显眼位置注明机翻。**


* 一键机翻  
  - 译文回填参考对原文排版的估计，包括颜色，轮廓，角度，朝向，对齐方式等
  - 最后效果取决于文本检测，识别，抹字，机翻四个模块的整体表现  
  - 支持日漫和美漫
  - 英译中，日译英排版已优化，文本布局以提取到的背景泡为参考，中文基于 pkuseg 进行断句，日译中竖排待改善
  
* 图像编辑  
  支持掩膜编辑和修复画笔
  
* 文本编辑  
  - 支持所见即所得地富文本编辑和一些基础排版格式调整、[字体样式预设](https://github.com/dmMaze/BallonsTranslator/pull/311)
  - [文本变形](https://github.com/dmMaze/BallonsTranslator/pull/1238)、全文/原文/译文查找替换
  - 支持导入导出 word 文档

* <details>
  <summary><i>支持上下文和术语表的 LLM 翻译</i></summary>

  **翻译历史**

  - 将 **LLM 上下文** 设为 **+翻译历史** 后，`LLMTranslator` 会参考之前已完成的页面，有助于统一人名、术语和语气。继续运行和选定范围也可使用范围之前符合条件的页面。
  - **Token 预算** 控制加入多少较早的译文，并优先保留较新的页面。当前页面、指令、术语表和生成回复还需要额外的上下文空间。默认值为 `4096`。
  - 较大预算可提供更多剧情上下文并减少旧页淘汰，但会发送更多输入，可能需要更长时间。本地模型还可能显著增加内存/显存占用。默认值 `4096` 是特意设置的保守选择；DeepSeek 等具有较大上下文窗口的主流服务通常可以使用更高上限。模型上下文上限的约 70% 可作为合理上限（128K 模型约为 `90000`）。
  - 历史预算也会影响提示词缓存。历史在预算内增长时，连续请求会保留相同的开头，OpenAI、DeepSeek 等服务可按折扣价复用这些输入 token，并可能降低延迟。预算迫使程序淘汰旧页后，公共开头会改变，缓存复用随之重置。较大预算可减少重置次数，但也会发送更多历史，因此总费用不一定更低。

  下表以 DeepSeek 为例，对普通漫画页面进行粗略估算；其缓存输入 token 的价格为普通输入 token 的 10%。实际结果会因项目、模型和服务商而异。

  | 历史预算 (tokens) | 预计保留的翻译历史（页） | 相对不使用历史的预计总费用 |
  |---:|---:|---:|
  | `2048` | 3–4 | 1.65× |
  | `4096` | 6–9 | 1.79× |
  | `8192` | 12–19 | 2.10× |
  | `16384` | 23–38 | 2.66× |

  **可复用术语表**

  - 在运行对话框中设置 **术语表**，可使用 UTF-8 编码的 `.json`、`.txt` 或 `.tsv` 文件。文件只会被读取，并可在多个项目间复用。
  - **仅匹配** 只发送原词出现在相关页面中的条目；**全表** 会发送全部条目，可能明显增加 token 用量。
  - 支持以下格式：

    ```text
    # Sakura 格式文本
    原词->译词 # 可选备注

    # 制表符分隔文本
    原词<TAB>译词<TAB>可选备注
    ```

    ```json
    [
      {"src": "原词", "dst": "译词", "info": "可选备注"}
    ]
    ```

  - 匹配不区分大小写，并按字面文本匹配。条目冲突、文件格式错误、不支持的扩展名或文件不存在时，翻译会在发送 LLM 请求前停止。
  - 历史页面上下文和术语表注入只对 `LLMTranslator` 生效，其他翻译器会忽略这些设置。

  </details>

* 适用于条漫

# 使用说明

## Windows

**方式 A（一键自动配置本地环境，需要系统支持 PowerShell）**：
该脚本会在执行目录安装 `BallonsTranslator`：
```powershell
irm https://raw.githubusercontent.com/dmMaze/BallonsTranslator/dev/scripts/install.ps1 | iex
```
或者在系统的命令提示符 (`cmd.exe`) 中运行：
```cmd
powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://raw.githubusercontent.com/dmMaze/BallonsTranslator/dev/scripts/install.ps1 | iex"
```

**方式 B（下载免配置压缩包）**：
从 [GitHub Releases](https://github.com/dmMaze/BallonsTranslator/releases) 下载 `Ballonstranslator_win_minium.zip`，解压并双击运行 `launch_win.bat` 启动程序。  
  
以上方式不支持 Windows 7，Windows 7 用户需要自行安装 [Python 3.8](https://www.python.org/downloads/release/python-3810/) 运行源码。 


如果遇到 `msvcp140.dll`、`c10.dll` 或 `[WinError 1114]` 相关错误，请安装或更新 [Microsoft Visual C++ Redistributable x64](https://aka.ms/vc14/vc_redist.x64.exe)（Visual Studio 2015-2022；[官方下载说明](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist)）。  

## macOS / Linux

该脚本会在执行目录安装 `BallonsTranslator`：
```bash
curl -fLO https://raw.githubusercontent.com/dmMaze/BallonsTranslator/dev/scripts/install.sh && chmod +x install.sh && ./install.sh
```

如果系统没有 `curl`，也可以用 `wget -O ...` 下载脚本。安装完成后会自动启动程序；之后可运行 `cd BallonsTranslator && ./launch.sh` 再次启动。  

启动程序会检查核心依赖；选择需要额外库的模块时，程序会提示安装缺失的可选依赖（也可在设置中启用自动安装）。

## 一键翻译
**建议在命令行终端下运行程序**，首次运行请先配置好源语言/目标语言，打开一个带图片的文件夹，点击 Run 等待翻译完成  
<img src="https://github.com/user-attachments/assets/ee92fbdc-718c-4e04-a876-0eff3ee2a989">  

一键机翻嵌字格式如大小、颜色等默认是由程序决定的，可以在设置面板->嵌字菜单中改用全局设置。全局字体格式就是未编辑任何文本块时右侧字体面板显示的格式:  
<img src="https://github.com/user-attachments/assets/fb8a8b2c-54e4-4579-8319-42a172296c80"> 

## 画板

## 修复画笔
<img src="https://github.com/user-attachments/assets/de0bc35d-6651-4f2f-985c-cfe9bfafb124">
<p align = "center">
修复画笔
</p>

### 矩形工具
<img src="https://github.com/user-attachments/assets/6c47f46f-ffd3-41fd-b667-5442be304c79">
<p align = "center">
矩形工具
</p>

按下鼠标左键拖动矩形框抹除框内文字，按下右键拉框清除框内修复结果。  
抹除结果取决于算法(gif 中的"方法1"和"方法2")对文字区域估算的准确程度，一般拉的框最好稍大于需要抹除的文本块。两种方法都比较玄学，能够应付绝大多数简单文字简单背景，部分复杂背景简单文字/简单背景复杂文字，少数复杂背景复杂文字，可以多拉几次试试。  
勾选"自动"拉完框立即修复，否则需要按下"修复"或者空格键才进行修复，或 ```Ctrl+D``` 删除矩形选框。 

## 文本编辑
<img src="https://github.com/user-attachments/assets/0f688abe-41f7-416a-85c8-e0dd696
