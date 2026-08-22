# SeleniumHQ/docker-selenium

Provides a simple way to run Selenium Grid with Chrome, Firefox, and Edge using Container Platform, making it easier to perform browser automation at scale

## installation

1. Start a Docker container with Firefox

```bash
docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-firefox:4.47.0-20260808
```

2. Point your WebDriver tests to http://localhost:4444

3. That's it! 

4. (Optional) To see what is happening inside the container, head to <http://localhost:7900/?autoconnect=1&resize=scale&password=secret>.

For more details about visualising the container activity, check the [Debugging](#debugging) section.

:point_up: When executing `docker run` for an image that contains a browser please use 
the flag `--shm-size=2g` to use the host's shared memory.
  
:point_up: Always use a Docker image with a full tag to pin a specific browser and Grid version.
See [Tagging Conventions](https://github.com/SeleniumHQ/docker-selenium/wiki/Tagging-Convention) for details.

## configuration

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/SeleniumHQ/docker-selenium)

___

## features

| Environment variable          | Default value                                | Description                                                                               |
|-------------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------|
| `SE_UPLOAD_RETAIN_LOCAL_FILE` | `false`                                      | Keep local file after uploading successfully                                              |
| `SE_UPLOAD_COMMAND`           | `copy`                                       | RCLONE command is used to transfer file. Enforce `move` when retain local file is `false` |
| `SE_UPLOAD_OPTS`              | `-P --cutoff-mode SOFT --metadata --inplace` | Other options belong to RCLONE command can be set.                                        |
| `SE_UPLOAD_CONFIG_FILE_NAME`  | `upload.conf`                                | Config file for remote host instead of set via env variable prefix SE_RCLONE_*            |
| `SE_UPLOAD_CONFIG_DIRECTORY`  | `/opt/bin`                                   | Directory of config file (change it when conf file in another directory is mounted)       |

## tools

Relaying commands to a service endpoint that supports WebDriver.
It is useful to connect an external service that supports WebDriver to Selenium Grid. An example of such service could be a cloud provider or an Appium server. 
In this way, Grid can enable more coverage to platforms and versions not present locally.

The following is an en example of configuration relay commands.

[docker-compose-v3-test-node-relay.yml](tests/docker-compose-v3-test-node-relay.yml)

If you want to relay commands only, `selenium/node-base` is suitable and lightweight for this purpose.
In case you want to configure node with both browsers and relay commands, respective node images can be used.

To use environment variables for generate relay configs, set `SE_NODE_RELAY_URL` and other variables as below. Those will be used to generate the default relay config in TOML format looks like below.

```toml
[relay]
url = "${SE_NODE_RELAY_URL}"
status-endpoint = "${SE_NODE_RELAY_STATUS_ENDPOINT}"
protocol-version = "${SE_NODE_RELAY_PROTOCOL_VERSION}"
configs = [ '${SE_NODE_RELAY_MAX_SESSIONS}', '{"browserName": "${SE_NODE_RELAY_BROWSER_NAME}", "platformName": "${SE_NODE_RELAY_PLATFORM_NAME}", "appium:platformVersion": "${SE_NODE_RELAY_PLATFORM_VERSION}"}' ]
```

Instead of input value for each environment variable to construct the default relay stereotype, you can use the `SE_NODE_RELAY_STEREOTYPE` environment variable to overwrite the default relay stereotype with your custom stereotype.

In another case, if you want to retain the default relay stereotype and append additional capabilities, you can use the `SE_NODE_RELAY_STEREOTYPE_EXTRA` environment variable to set your capabilities. Those will be merged to the default relay stereotype.

To run a sample test with the relayed node, you can clone the project and try below command:

```bash
make test_node_relay
```
