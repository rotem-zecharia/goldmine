# flipped-aurora/gin-vue-admin

🚀Vite+Vue3+Gin拥有AI辅助的基础开发平台，企业级业务AI+开发解决方案，内置mcp辅助服务，内置skills管理，支持TS和JS混用。它集成了JWT鉴权、权限管理、动态路由、显隐可控组件、分页封装、多点登录拦截、资源权限、上传下载、代码生成器、表单生成器和可配置的导入导出等开发必备功能。

## tools

#### 2.3.1 安装 swagger

```bash
go install github.com/swaggo/swag/cmd/swag@latest
```

#### 2.3.2 生成API文档

```bash
cd server
swag init
```

> 执行上面的命令后，server目录下会出现docs文件夹里的 `docs.go`, `swagger.json`, `swagger.yaml` 三个文件更新，启动go服务之后, 在浏览器输入 [http://localhost:8888/swagger/index.html](http://localhost:8888/swagger/index.html) 即可查看swagger文档

### 2.4 VSCode工作区

#### 2.4.1 开发
使用 `VSCode` 打开根目录下的工作区文件 `gin-vue-admin.code-workspace`，在边栏可以看到三个虚拟目录：`backend`、`frontend`、`root`。

#### 2.4.2 运行/调试
在运行和调试中也可以看到三个 task：`Backend`、`Frontend`、`Both (Backend & Frontend)`。运行 `Both (Backend & Frontend)` 可以同时启动前后端项目。

#### 2.4.3 settings
在工作区配置文件中有 `go.toolsEnvVars` 字段，是用于 `VSCode` 自身的 go 工具环境变量。此外在多 go 版本的系统中，可以通过 `gopath`、`go.goroot` 指定运行版本。

```json
    "go.gopath": null,
    "go.goroot": null,
```

## 3. 技术选型

- 前端：用基于 [Vue](https://vuejs.org) 的 [Element](https://github.com/ElemeFE/element) 构建基础页面。
- 后端：用 [Gin](https://gin-gonic.com/) 快速搭建基础restful风格API，[Gin](https://gin-gonic.com/) 是一个go语言编写的Web框架。
- 数据库：采用 `MySQL` 或 `MariaDB`（5.7+），数据库引擎 InnoDB，使用 [gorm](http://gorm.cn) 实现对数据库的基本操作。
- 缓存：使用 `Redis` 实现记录当前活跃用户的 jwt 令牌并实现多点登录限制。
- API文档：使用 `Swagger` 构建自动化文档。
- 配置文件：使用 [fsnotify](https://github.com/fsnotify/fsnotify) 和 [viper](https://github.com/spf13/viper) 实现 yaml 格式的配置文件。
- 日志：使用 [zap](https://github.com/uber-go/zap) 实现日志记录。

## 4. 项目架构

### 4.1 系统架构图

![系统架构图](http://qmplusimg.henrongyi.top/gva/gin-vue-admin.png)

### 4.2 详细设计图 （提供者:<a href="https://github.com/baobeisuper">baobeisuper</a>）

![详细设计图](http://qmplusimg.henrongyi.top/naotu.png)

### 4.3 目录结构

*(详细目录结构请见源码...)*

## 5. 主要功能

- 权限管理：基于 `jwt` 和 `casbin` 实现的权限管理。
- 文件上传下载：实现基于 `七牛云`, `阿里云`, `腾讯云` 的文件上传操作。
- 分页封装：前端使用 `mixins` 封装分页，分页方法调用即可。
- 用户管理：系统管理员分配用户角色和角色权限。
- 角色管理：创建权限控制的主要对象，可以给角色分配不同 api 权限和菜单权限。
- 菜单管理：实现用户动态菜单配置，实现不同角色不同菜单。
- api管理：不同用户可调用的 api 接口的权限不同。
- 配置管理：配置文件可前台修改(在线体验站点不开放此功能)。
- 条件搜索：增加条件搜索示例。
- restful示例：可以参考用户管理模块中的示例 API。
- 多点登录限制：借助 Redis 配合对应配置限制多端登录状态。
- 分片上传：提供文件分片上传和大文件分片上传功能示例。
- 表单生成器：表单生成器借助 [@Variant Form](https://github.com/vform666/variant-form)。
- 代码生成器：后台基础逻辑以及简单 curd 的代码生成器。

## 6. 知识库 

### 6.1 团队博客

> [https://www.yuque.com/flipped-aurora](https://www.yuque.com/flipped-aurora)
> 内有前端框架教学视频。如果觉得项目对您有所帮助可以添加我的个人微信: shouzi_1994。

### 6.2 教学视频

1. **手把手教学视频**: [https://www.bilibili.com/video/BV1Rg411u7xH/](https://www.bilibili.com/video/BV1Rg411u7xH/)
2. **后端目录结构调整介绍以及使用方法**: [https://www.bilibili.com/video/BV1x44y117TT/](https://www.bilibili.com/video/BV1x44y117TT/)
3. **golang基础教学视频**: [bilibili](https://space.bilibili.com/322210472/channel/detail?cid=108884)
4. **gin框架基础教学**: [bilibili](https://space.bilibili.com/322210472/channel/detail?cid=126418&ctype=0)
5. **gin-vue-admin 版本更新介绍视频**: [bilibili](https://www.bilibili.com/video/BV1kv4y1g7nT)

## 7. 联系方式

- **QQ交流群**: `971857775`
- **[关于我们](https://www.gin-vue-admin.com/about/join.html)**

### 微信交流群

<img width="150" src="http://qmplusimg.henrongyi.top/qrjjz.png"> 

防止广告进群，添加微信，输入以下代码执行结果（请勿转码为string）：

```go
str := "5Yqg5YWlR1ZB5Lqk5rWB576k"
decodeBytes, err := base64.StdEncoding.DecodeString(str)
fmt.Println(decodeBytes, err)
```

## 8. 贡献者

感谢您对gin-vue-admin的贡献!

<a href="https://openomy.app/github/flipped-aurora/gin-vue-admin" target="_blank" style="display: block; width: 100%;" align="center">
  <img src="https://openomy.app/svg?repo=flipped-aurora/gin-vue-admin&chart=bubble&latestMonth=3" target="_blank" alt="Contribution Leaderboard" style="display: block; width: 100%;" />
</a>

## 9. 捐赠

如果你觉得这个项目对你有帮助，你可以请作者喝饮料 :tropical_drink: [点我](https://www.gin-vue-admin.com/coffee/index.html)

## 10. 注意事项

请遵守 BSL 1.1 许可证要求并保留作品声明；商用、生产使用或去除版权信息请务必[获取授权](https://plugin.gin-vue-admin.com/license)  
未授权超出许可范围使用将依法追究法律责任。
