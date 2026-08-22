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
