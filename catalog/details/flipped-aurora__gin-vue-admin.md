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
