# MaaAssistantArknights/MaaAssistantArknights

《明日方舟》小助手，全日常一键长草！/ A one-click tool for the daily tasks of Arknights, supporting all clients.

## tools

- [C 接口](include/AsstCaller.h)：[集成示例](src/Cpp/main.cpp)
- [Python 接口](src/Python/asst/asst.py)：[集成示例](src/Python/sample.py)
- [Golang 接口](src/Golang)：[集成示例](src/Golang/maa/maa.go)
- [Dart 接口](src/Dart)
- [Java 接口](src/Java/src/main/java/com/iguigui/maaj/easySample/MaaCore.java)：[集成示例](src/Java/src/main/java/com/iguigui/maaj/easySample/MaaJavaSample.java)
- [Java HTTP 接口](src/Java/Readme.md)
- [Rust 接口](src/Rust/src/maa_sys)：[HTTP 接口](src/Rust)
- [TypeScript 接口](https://github.com/MaaAssistantArknights/MaaX/tree/main/packages/main/coreLoader)
- [Woolang 接口](src/Woolang/maa.wo)：[集成示例](src/Woolang/demo.wo)
- [集成文档](https://docs.maa.plus/zh-cn/protocol/integration.html)
- [回调消息协议](https://docs.maa.plus/zh-cn/protocol/callback-schema.html)
- [任务流程协议](https://docs.maa.plus/zh-cn/protocol/task-schema.html)
- [自动战斗协议](https://docs.maa.plus/zh-cn/protocol/copilot-schema.html)

### 外服适配

请参阅 [外服适配教程](https://docs.maa.plus/zh-cn/develop/overseas-client-adaptation.html)，对于国服已支持的功能，绝大部分的外服适配工作仅需要截图 + 简单的 JSON 修改即可。

### Issue bot

请参阅 [Issue Bot 使用方法](https://docs.maa.plus/zh-cn/develop/issue-bot-usage.html)

## 致谢

### 开源库

- 图像识别库：[opencv](https://github.com/opencv/opencv.git)
- ~~文字识别库：[chineseocr_lite](https://github.com/DayBreak-u/chineseocr_lite.git)~~
- 文字识别库：[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- 深度学习部署库：[FastDeploy](https://github.com/PaddlePaddle/FastDeploy)
- 机器学习加速器：[onnxruntime](https://github.com/microsoft/onnxruntime)
- ~~关卡掉落识别：[企鹅物流识别](https://github.com/penguin-statistics/recognizer)~~
- 地图格子识别：[Arknights-Tile-Pos](https://github.com/yuanyan3060/Arknights-Tile-Pos)
- C++ JSON 库：[meojson](https://github.com/MistEO/meojson.git)
- C++ 运算符解析器：[calculator](https://github.com/kimwalisch/calculator)
- ~~C++ base64 编解码：[cpp-base64](https://github.com/ReneNyffenegger/cpp-base64)~~
- C++ 解压压缩库：[zlib](https://github.com/madler/zlib)
- C++ Gzip 封装：[gzip-hpp](https://github.com/mapbox/gzip-hpp)
- 安卓触控事件器：[Minitouch](https://github.com/DeviceFarmer/minitouch)
- 安卓触控事件器：[MaaTouch](https://github.com/MaaAssistantArknights/MaaTouch)
- WPF MVVM 框架：[Stylet](https://github.com/canton7/Stylet)
- WPF 控件库：[HandyControl](https://github.com/HandyOrg/HandyControl) -> [HandyControls](https://github.com/ghost1372/HandyControls)
- C# 日志：[Serilog](https://github.com/serilog/serilog)
- C# JSON 库：[Newtonsoft.Json](https://github.com/JamesNK/Newtonsoft.Json) & [System.Text.Json](https://github.com/dotnet/runtime)
- ~~下载器：[aria2](https://github.com/aria2/aria2)~~

### 数据源

- ~~公开招募数据：[明日方舟工具箱](https://www.bigfun.cn/tools/aktools/hr)~~
- ~~干员及基建数据：[PRTS Wiki](http://prts.wiki/)~~
- 关卡数据：[企鹅物流数据统计](https://penguin-stats.cn/)
- 游戏数据及资源：[明日方舟客户端素材](https://github.com/yuanyan3060/ArknightsGameResource)
- 游戏数据：[《明日方舟》Yostar游戏数据](https://github.com/ArknightsAssets/ArknightsGamedata)

### 贡献/参与者

感谢所有参与到开发/测试中的朋友们，是大家的帮助让 MAA 越来越好！ (\*´▽｀)ノノ

[![Contributors](https://contributors-img.web.app/image?repo=MaaAssistantArknights/MaaAssistantArknights&max=105&columns=15)](https://github.com/MaaAssistantArknights/MaaAssistantArknights/graphs/contributors)

## 声明

- 本软件使用 [GNU Affero General Public License v3.0 only](https://spdx.org/licenses/AGPL-3.0-only.html) 开源，并附带额外 [用户协议](https://github.com/MaaAssistantArknights/MaaAssistantArknights/blob/dev-v2/terms-of-service.md)。
- 本软件 logo 并非使用 AGPL 3.0 协议开源，[耗毛](https://weibo.com/u/3251357314)、vie 两位画师及软件全体开发者保留所有权利。不得以 AGPL 3.0 协议已授权为由在未经授权的情况下使用本软件 logo，不得在未经授权的情况下将本软件 logo 用于任何商业用途。
- 本软件开源、免费，仅供学习交流使用。若您遇到商家使用本软件进行代练并收费，可能是设备与时间等费用，产生的问题及后果与本软件无关。

### DirectML 支持说明

本软件支持 GPU 加速功能，其在 Windows 平台上依赖于 Microsoft 提供的独立组件 [DirectML](https://learn.microsoft.com/en-us/windows/ai/directml/)。DirectML 并非本项目的开源部分，也不受 AGPL 3.0 的约束。为方便用户，我们随安装包附带了一个未经修改的 DirectML.dll 文件。如果您无需 GPU 加速功能，可安全删除该 DLL 文件，软件的核心功能仍可正常运行。

## 广告

用户交流 QQ 群：[MAA 使用 & 粥游交流 QQ 群](https://api.maa.plus/MaaAssistantArknights/api/qqgroup/index.html)  
Discord 服务器: [邀请链接](https://discord.gg/23DfZ9uA4V)  
用户交流 TG 群：[Telegram 群](https://t.me/+Mgc2Zngr-
