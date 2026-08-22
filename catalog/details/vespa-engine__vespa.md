# vespa-engine/vespa

The AI search platform

## installation

Deploy your Vespa applications to the cloud service: [console.vespa-cloud.com](https://console.vespa-cloud.com/),
or run your own Vespa instance: [https://docs.vespa.ai/en/getting-started.html](https://docs.vespa.ai/en/getting-started.html)

## tools

- The application created in the getting started guides linked above is fully functional and production-ready, but you may want to [add more nodes](https://docs.vespa.ai/en/multinode-systems.html) for redundancy.
- See [developing applications](https://docs.vespa.ai/en/developer-guide.html) on adding your own Java components to your Vespa application.
- [Vespa APIs](https://docs.vespa.ai/en/api.html) is useful to understand how to interface with Vespa
- Explore the [sample applications](https://github.com/vespa-engine/sample-apps/tree/master)
- Follow the [Vespa Blog](https://blog.vespa.ai/) for feature updates / use cases
- Join the [Vespa Slack community](https://slack.vespa.ai/) to ask questions and share feedback

Full documentation is at [https://docs.vespa.ai](https://docs.vespa.ai).

## Contribute

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) to learn how to contribute.

If you want to contribute to the documentation, see
[https://github.com/vespa-engine/documentation](https://github.com/vespa-engine/documentation)

## Building

You do not need to build Vespa to use it, but if you want to contribute you need to be able to build the code.
This section explains how to build and test Vespa. To understand where to make changes, see [Code-map.md](Code-map.md).
Some suggested improvements with pointers to code are in [TODO.md](TODO.md).

## configuration

C++ and Java building is supported on AlmaLinux 8.
The Java source can also be built on any platform having Java 17 and Maven 3.8+ installed.
Use the following guide to set up a complete development environment using Docker
for building Vespa, running unit tests and running system tests:
[Vespa development on AlmaLinux 8](https://github.com/vespa-engine/docker-image-dev#vespa-development-on-almalinux-8).

#### Java environment for Mac
1. Install [JDK17](https://openjdk.org/projects/jdk/17/), 
   [Maven Version Manager](https://bitbucket.org/mjensen/mvnvm/src/master/) and [jEnv](https://www.jenv.be)
   through [Homebrew](https://brew.sh/).
```sh
brew install jenv mvnvm openjdk@17
```

2. For the system Java wrappers to find this JDK, symlink it with
```sh
sudo ln -sfn /opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-17.jdk
```

3. Follow "Configure your shell" in https://www.jenv.be. Configuration is shell specific. For `zsh` use the below commands:
```sh
echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(jenv init -)"' >> ~/.zshrc
eval "$(jenv init -)"
jenv enable-plugin export
exec $SHELL -l
```

4. Add JDK17 to jEnv
```sh
jenv add $(/usr/libexec/java_home -v 17)
```

5. Verify configuration with Maven by executing below command in the root of the source code.
   Output should refer to the JDK and Maven version specified in the [.java-version](.java-version) and [mvnvm.properties](mvnvm.properties).
```sh
mvn -v
```

### Build Java modules

    export MAVEN_OPTS="-Xms128m -Xmx1024m"
    ./bootstrap.sh java
    mvn install --threads 1C

Use this if you only need to build the Java modules, otherwise follow the complete development guide above.

### Run tests for shell scripts (on Mac)
Shell scripts are tested with [BATS](https://bats-core.readthedocs.io/en/stable/).
To run the tests locally, install the testing framework and its plugins.:
```bash
brew install node
sudo npm install -g bats bats-assert bats-support bats-mock
```
Export the `BATS_PLUGIN_PATH` environment variable to point to the global npm modules directory, which contains the BATS plugins:
```bash
export BATS_PLUGIN_PATH="$(npm root -g)"
```
Then run all tests with the following command (from the root of the repository):
```bash
bats -r .
```
To run a specific test, use:
```bash
bats test_dir/test_name.bats
```
Tests can also be run in IntelliJ IDEA with the [BashSupport Pro](https://plugins.jetbrains.com/plugin/13841-bashsupport-pro)
plugin. Ensure the `BATS_PLUGIN_PATH` environment variable is exported before launching the IDE
to avoid setting it in each run configuration.

## License

Code licensed under the Apache 2.0 license. See [LICENSE](LICENSE) for terms.
