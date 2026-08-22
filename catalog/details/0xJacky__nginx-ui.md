# 0xJacky/nginx-ui

Yet another WebUI for Nginx

## features

- Online statistics for server indicators such as CPU usage, memory usage, load average, and disk usage.
- Automatic configuration backup after changes, with version comparison and restore capabilities
- Cluster management supporting mirroring operations to multiple nodes, making multi-server environments easy to manage
- Export encrypted Nginx / Nginx UI configurations for quick deployment and recovery to new environments
- Enhanced online **ChatGPT** assistant supporting multiple models, including Deepseek-R1's chain-of-thought display to help you better understand and optimize configurations
- **MCP** (Model Context Protocol) provides special interfaces for AI agents to interact with Nginx UI, enabling automated configuration management and service control.
- One-click deployment and automatic renewal Let's Encrypt certificates.
- Online editing websites configurations with our self-designed **NgxConfigEditor** which is a user-friendly block editor for nginx configurations or **Ace Code Editor** which supports **LLM Code Completion** and highlighting nginx configuration syntax.
- Online view Nginx logs
- Written in Go and Vue, distribution is a single executable binary.
- Automatically test configuration file and reload nginx after saving configuration.
- Web Terminal
- Dark Mode
- Responsive Web Design

## installation

Nginx UI is available on the following platforms:

- macOS 11 Big Sur and later (amd64 / arm64)
- Windows 10 and later (amd64 / arm64)
- Linux 2.6.23 and later (x86 / amd64 / arm64 / armv5 / armv6 / armv7 / mips32 / mips64 / riscv64 / loongarch64)
  - Including but not limited to Debian 7 / 8, Ubuntu 12.04 / 14.04 and later, CentOS 6 / 7, Arch Linux
- FreeBSD
- OpenBSD
- Dragonfly BSD
- Openwrt

You can visit [latest release](https://github.com/0xJacky/nginx-ui/releases/latest) to download the latest distribution, or just use [installation scripts for Linux](#script-for-linux).

## tools

In the first runtime of Nginx UI, please visit `http://<your_server_ip>:<listen_port>`
in your browser to complete the follow-up configurations.

#### From Executable
**Run Nginx UI in Terminal**

```shell
nginx-ui -config app.ini
```
Press `Control+C` in the terminal to exit Nginx UI.

**Run Nginx UI in Background**

```shell
nohup ./nginx-ui -config app.ini &
```
Stop Nginx UI with the follow command.

```shell
kill -9 $(ps -aux | grep nginx-ui | grep -v grep | awk '{print $2}')
```

#### With Systemd
If you are using the [installation script for Linux](#script-for-linux), the Nginx UI will be installed as `nginx-ui` service in systemd. Please use the `systemctl` command to control it.

**Start Nginx UI**

```shell
systemctl start nginx-ui
```
**Stop Nginx UI**

```shell
systemctl stop nginx-ui
```
**Restart Nginx UI**

```shell
systemctl restart nginx-ui
```

#### With Docker
Our docker image [uozi/nginx-ui:latest](https://hub.docker.com/r/uozi/nginx-ui) is based on the latest nginx image and
can be used to replace the Nginx on the host. By publishing the container's port 80 and 443 to the host,
you can easily make the switch.

##### Note
1. When using this container for the first time, ensure that the volume mapped to /etc/nginx is empty.
2. If you want to host static files, you can map directories to container.
3. If you are upgrading from an older image, see the [Docker WebSocket fix guide](https://nginxui.com/guide/docker-websocket-fix.html) for required `conf.d/nginx-ui.conf` updates.

<details>
<summary><b>Deploy with Docker</b></summary>

1. [Install Docker.](https://docs.docker.com/install/)

2. Then deploy nginx-ui like this:

```bash
docker run -dit \
  --name=nginx-ui \
  --restart=always \
  -e TZ=Asia/Shanghai \
  -v /mnt/user/appdata/nginx:/etc/nginx \
  -v /mnt/user/appdata/nginx-ui:/etc/nginx-ui \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -p 8080:80 -p 8443:443 \
  uozi/nginx-ui:latest
```

3. When your docker container is running, Log in to nginx-ui panel with `http://<your_server_ip>:8080/install`.
   If you change the port mapping, access Nginx UI through the host port mapped to container port `80` instead.
</details>

<details>
<summary><b>Deploy with Docker-Compose</b></summary>

1. [Install Docker-Compose.](https://docs.docker.com/compose/install/)

2. Create a docker-compose.yml file like this:

```yml
services:
    nginx-ui:
        stdin_open: true
        tty: true
        container_name: nginx-ui
        restart: always
        environment:
            - TZ=Asia/Shanghai
        volumes:
            - '/mnt/user/appdata/nginx:/etc/nginx'
            - '/mnt/user/appdata/nginx-ui:/etc/nginx-ui'
            - '/var/www:/var/www'
            - '/var/run/docker.sock:/var/run/docker.sock'
        ports:
            - 8080:80
            - 8443:443
        image: 'uozi/nginx-ui:latest'
```

3. Then creat your container by:
```bash
docker compose up -d
```

4. When your docker container is running, Log in to nginx-ui panel with `http://<your_server_ip>:8080/install`.
   If you change the port mapping, access Nginx UI through the host port mapped to container port `80` instead.

</details>

## requirements

- Make

- Golang 1.23+

- node.js 21+

  ```shell
  npx browserslist@latest --update-db
  ```

## configuration

```nginx
server {
    listen          80;
    listen          [::]:80;

    server_name     <your_server_name>;
    rewrite ^(.*)$  https://$host$1 permanent;
}

map $http_upgrade $connection_upgrade {
    default upgrade;
    ''      close;
}

server {
    listen  443       ssl;
    listen  [::]:443  ssl;
    http2   on;

    server_name         <your_server_name>;

    ssl_certificate     /path/to/ssl_cert;
    ssl_certificate_key /path/to/ssl_cert_key;

    location / {
        proxy_set_header    Host                $host;
        proxy_set_header    X-Real-IP           $remote_addr;
        proxy_set_header    X-Forwarded-For     $proxy_add_x_forwarded_for;
        proxy_set_header    X-Forwarded-Proto   $scheme;
        proxy_http_version  1.1;
        proxy_set_header    Upgrade             $http_upgrade;
        proxy_set_header    Connection          $connection_upgrade;
        proxy_pass          http://127.0.0.1:9000/;
    }
