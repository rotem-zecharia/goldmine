# doocs/md

✍ WeChat Markdown Editor / 一款高度简洁的微信 Markdown 编辑器：支持 Markdown 语法、自定义主题样式、内容管理、多图床、AI 助手等特性

## tools

pnpm utools:package

# Cloudflare Workers 开发与部署
pnpm web wrangler:dev
pnpm web wrangler:deploy
```

## 私有化部署

### 方式一：npm cli

```sh
# 全局安装
npm i -g @doocs/md-cli

# 启动（默认端口 8800）
md-cli

# 指定端口启动
md-cli port=8899
```

支持的命令行参数：

- `port`：监听端口，默认 `8800`，端口被占用时自动随机选取
- `spaceId`：dcloud 服务空间配置
- `clientSecret`：dcloud 服务空间配置

### 方式二：Docker

```sh
docker run -d -p 8080:80 doocs/md:latest
```

启动后访问 http://localhost:8080 即可。Docker 镜像的更多信息，请参考 https://github.com/doocs/docker-md

## Star 趋势

<a href="https://github.com/doocs/md/stargazers" target="_blank"><img src="./images/starcharts.svg" alt="Stargazers over time" /></a>

## 谁在使用

请查看 [USERS.md](USERS.md)，了解使用本项目的公众号列表。

## 参与贡献

欢迎提交 PR 或 Issue，请参阅 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解贡献流程与规范。

## 支持我们

如果本项目对你有所帮助，欢迎通过以下方式支持我们持续维护。

<table style="margin: 0 auto">
  <tbody>
    <tr>
      <td align="center" style="width: 260px">
        <img
          src="https://cdn-doocs.oss-cn-shenzhen.aliyuncs.com/gh/doocs/md/images/support1.jpg"
          alt="support1"
          style="width: 200px"
        /><br />
      </td>
      <td align="center" style="width: 260px">
        <img
          src="https://cdn-doocs.oss-cn-shenzhen.aliyuncs.com/gh/doocs/md/images/support2.jpg"
          alt="support2"
          style="width: 200px"
        /><br />
      </td>
    </tr>
  </tbody>
</table>

## 反馈与交流

使用中遇到问题或有功能建议，欢迎在 [Issues](https://github.com/doocs/md/issues) 中反馈。也可扫码加入微信交流群，若二维码失效，请添加好友并备注 `md`。

<table style="margin: 0 auto">
  <tbody>
    <tr>
      <td align="center" style="width: 260px">
        <img
          src="https://cdn-doocs.oss-cn-shenzhen.aliyuncs.com/gh/doocs/md/images/doocs-md-wechat-group.jpg"
          alt="doocs-md-wechat-group"
          style="width: 200px"
        /><br />
      </td>
      <td align="center" style="width: 260px">
        <img
          src="https://cdn-doocs.oss-cn-shenzhen.aliyuncs.com/gh/doocs/md/images/wechat-ylb.jpg"
          alt="wechat-ylb"
          style="width: 200px"
        /><br />
      </td>
    </tr>
  </tbody>
</table>
