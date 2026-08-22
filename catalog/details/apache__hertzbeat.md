# apache/hertzbeat

An AI-powered next-generation open source real-time observability system.

## features

- Integrates **collection + analysis + alerting + notification** into one platform, with new AI-powered interactions and features under HertzBeat AI, and built-in MCP Server capabilities.
- Unified metrics platform, agentless, Prometheus-compatible, supports application services, programs, databases, caches, operating systems, big data, middleware, web servers, cloud-native, networks, custom monitoring and more.
- Unified logging platform, seamlessly integrates multiple log sources through OTLP protocol for reporting.
- Unified alerting platform, integrates internal alerts with various external alert sources, unified alert processing and analysis, flexible real-time and periodic threshold rules, grouping convergence, silence, suppression, etc.
- Unified message distribution, alerts processed by the alerting platform are distributed via `Email` `Discord` `Slack` `Telegram` `DingTalk` `WeChat` `FeiShu` `SMS` `Webhook` `ServerChan` and other methods.
- Makes protocols such as `Http, Jmx, Ssh, Snmp, Jdbc, Prometheus` configurable, allowing you to collect any metrics by simply configuring the template `YML` file online. Imagine being able to quickly adapt to a new monitoring type like K8s or Docker simply by configuring online with HertzBeat.
- High performance, supports horizontal expansion of multi-collector clusters, multi-isolated network monitoring and cloud-edge collaboration.
- Provides powerful status page building capabilities, easily communicate the real-time status of your service to users.

> HertzBeat's unified platform, AI intelligence, powerful customization, multi-type support, high performance, and easy expansion, aims to help users quickly and conveniently achieve observability requirements.

----

----

## 🥐 Architecture

![HertzBeat](home/static/img/docs/hertzbeat-arch.png)

## installation

- If you wish to deploy HertzBeat locally, please refer to the following Deployment Documentation for instructions.

### 🍞 Install HertzBeat

> HertzBeat supports installation through source code, docker or package, cpu support x86/arm64.

##### 1：Install quickly via docker

1. Just one command to get started

   ```shell
   docker run -d -p 1157:1157 -p 1158:1158 --name hertzbeat apache/hertzbeat
   ```

2. Access `http://localhost:1157` to start, default account: `admin/hertzbeat`

3. Deploy collector clusters (Optional)

   ```shell
   docker run -d -e IDENTITY=custom-collector-name -e MANAGER_HOST=127.0.0.1 -e MANAGER_PORT=1158 --name hertzbeat-collector apache/hertzbeat-collector
   ```

   - `-e IDENTITY=custom-collector-name` : set the collector unique identity name.
   - `-e MODE=public` : set the running mode(public or private), public cluster or private cloud-edge.
   - `-e MANAGER_HOST=127.0.0.1` : set the main hertzbeat server ip.
   - `-e MANAGER_PORT=1158` : set the main hertzbeat server port, default 1158.


Detailed config refer to [Install HertzBeat via Docker](https://hertzbeat.apache.org/docs/start/docker-deploy)

##### 2：Install via package

1. Download the release package `apache-hertzbeat-xx-bin.tar.gz` [Download](https://hertzbeat.apache.org/docs/download)
2. Configure the HertzBeat configuration yml file `hertzbeat/config/application.yml` (optional)
3. Run command `$ ./bin/startup.sh ` or `bin/startup.bat`
4. Access `http://localhost:1157` to start, default account: `admin/hertzbeat`
5. Deploy collector clusters (Optional)
    - Download the release package `apache-hertzbeat-collector-xx-bin.tar.gz` (JVM collector) or the native collector package for your platform, such as `apache-hertzbeat-collector-native-xx-linux-amd64-bin.tar.gz` or `apache-hertzbeat-collector-native-xx-windows-amd64-bin.zip`, to the new machine [Download](https://hertzbeat.apache.org/docs/download)
    - Configure the collector configuration yml file `hertzbeat-collector/config/application.yml`: unique `identity` name, running `mode` (public or private), hertzbeat `manager-host`, hertzbeat `manager-port`
      ```yaml
      collector:
        dispatch:
          entrance:
            netty:
              enabled: true
              identity: ${IDENTITY:}
              mode: ${MODE:public}
              manager-host: ${MANAGER_HOST:127.0.0.1}
              manager-port: ${MANAGER_PORT:1158}
      ```
    - If you do not provide JDBC drivers in `ext-lib`, MySQL, MariaDB, and OceanBase can use the built-in query engine and run on the native collector package as well. TiDB follows the same rule for its SQL query metric set.
    - If `mysql-connector-j` is present in `ext-lib`, the built-in server collector or JVM collector automatically prefers JDBC after restart for MySQL, MariaDB, and OceanBase. TiDB follows the same rule for its SQL query metric set, while its HTTP metrics are unchanged. Oracle and DB2 still require the JVM collector package because they depend on external JDBC drivers.
    - Run `$ ./bin/startup.sh ` or `bin/startup.bat` for the JVM collector package. Run `$ ./bin/startup.sh ` for Linux or macOS native collector packages, and `bin\\startup.bat` for the Windows native collector package.
    - Access `http://localhost:1157` and you will see the registered new collector in dashboard

Detailed config refer to [Install HertzBeat via Package](https://hertzbeat.apache.org/docs/start/package-deploy)

##### 3：Start via source code

1. Local source code debugging needs to start the back-end project `hertzbeat-startup` and the front-end project `web-app`.
2. Backend：need `maven3+`, `java25`, `lombok`, add VM options in IDE: ` --add-opens=java.base/java.nio=org.apache.arrow.memory.core,ALL-UNNAMED `, then start the `hertzbeat-startup` service.
3. Web：need `nodejs` and `pnpm` environment, run `pnpm install` then `pnpm start` in `web-app` directory after backend startup.
4. Access `http://localhost:4200` to start, default accoun
