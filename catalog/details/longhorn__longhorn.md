# longhorn/longhorn

Cloud-Native distributed storage built on and for Kubernetes

## limitations

https://github.com/longhorn/longhorn/wiki/Roadmap

# Components

Longhorn is 100% open-source software. Project source code is spread across several repositories:

* Manager: [![Build Status](https://github.com/longhorn/longhorn-manager/actions/workflows/build.yml/badge.svg)](https://github.com/longhorn/longhorn-manager/actions/workflows/build.yml)[![Go Report Card](https://goreportcard.com/badge/github.com/longhorn/longhorn-manager)](https://goreportcard.com/report/github.com/longhorn/longhorn-manager)[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B162%2Flonghorn-manager.svg?type=shield&issueType=license)](https://app.fossa.com/projects/custom%2B162%2Flonghorn-manager?ref=badge_shield&issueType=license)
* Instance Manager: [![Build Status](https://github.com/longhorn/longhorn-instance-manager/actions/workflows/build.yml/badge.svg)](https://github.com/longhorn/longhorn-instance-manager/actions/workflows/build.yml)[![Go Report Card](https://goreportcard.com/badge/github.com/longhorn/longhorn-instance-manager)](https://goreportcard.com/report/github.com/longhorn/longhorn-instance-manager)[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B162%2Flonghorn-instance-manager.svg?type=shield&issueType=license)](https://app.fossa.com/projects/custom%2B162%2Flonghorn-instance-manager?ref=badge_shield&issueType=license)
* Engine: [![Build Status](https://github.com/longhorn/longhorn-engine/actions/workflows/build.yml/badge.svg)](https://github.com/longhorn/longhorn-engine/actions/workflows/build.yml)[![Go Report Card](https://goreportcard.com/badge/github.com/longhorn/longhorn-engine)](https://goreportcard.com/report/github.com/longhorn/longhorn-engine)[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B162%2Flonghorn-engine.svg?type=shield&issueType=license)](https://app.fossa.com/projects/custom%2B162%2Flonghorn-engine?ref=badge_shield&issueType=license)
* Share Manager: [![Build Status](https://github.com/longhorn/longhorn-share-manager/actions/workflows/build.yml/badge.svg)](https://github.com/longhorn/longhorn-share-manager/actions/workflows/build.yml)[![Go Report Card](https://goreportcard.com/badge/github.com/longhorn/longhorn-share-manager)](https://goreportcard.com/report/github.com/longhorn/longhorn-share-manager)[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B162%2Flonghorn-share-manager.svg?type=shield&issueType=license)](https://app.fossa.com/projects/custom%2B162%2Flonghorn-share-manager?ref=badge_shield&issueType=license)
* Backing Image Manager: [![Build Status](https://github.com/longhorn/backing-image-manager/actions/workflows/build.yml/badge.svg)](https://github.com/longhorn/backing-image-manager/actions/workflows/build.yml)[![Go Report Card](https://goreportcard.com/badge/github.com/longhorn/backing-image-manager)](https://goreportcard.com/report/github.com/longhorn/backing-image-manager)[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B162%2Flonghorn-backing-image-manager.svg?type=shield&issueType=license)](https://app.fossa.com/projects/custom%2B162%2Flonghorn-backing-image-manager?ref=badge_shield&issueType=license)
* UI: [![Build Status](https://github.com/longhorn/longhorn-ui/actions/workflows/build.yml/badge.svg)](https://github.com/longhorn/longhorn-ui/actions/workflows/build.yml)[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B162%2Flonghorn-ui.svg?type=shield&issueType=license)](https://app.fossa.com/projects/custom%2B162%2Flonghorn-ui?ref=badge_shield&issueType=license)
* CLI: [![build](https://github.com/longhorn/cli/actions/workflows/build.yml/badge.svg)](https://github.com/longhorn/cli/actions/workflows/build.yml)[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B162%2Flonghorn-cli.svg?type=shield&issueType=license)](https://app.fossa.com/projects/custom%2B162%2Flonghorn-cli?ref=badge_shield&issueType=license)

| Component                      | What it does                                                           | GitHub repo 

## requirements

For the installation requirements, refer to the [Longhorn documentation.](https://longhorn.io/docs/latest/deploy/install/#installation-requirements)

## installation

> **NOTE**: 
> Please note that the master branch is for the upcoming feature release development. 
> For an official release installation or upgrade, please take a look at the ways below.

Longhorn can be installed on a Kubernetes cluster in several ways:

- [Rancher App Marketplace](https://longhorn.io/docs/latest/deploy/install/install-with-rancher/)
- [kubectl](https://longhorn.io/docs/latest/deploy/install/install-with-kubectl/)
- [Helm](https://longhorn.io/docs/latest/deploy/install/install-with-helm/)

## Documentation

The official Longhorn documentation is [here.](https://longhorn.io/docs)

# Get Involved

## Discussion, Feedback

If having any discussions or feedback, feel free to [file a discussion](https://github.com/longhorn/longhorn/discussions).

## features

If having any issues, feel free to [file an issue](https://github.com/longhorn/longhorn/issues/new/choose).
We have a weekly community issue review meeting to review all reported issues or enhancement requests.

When creating a bug issue, please help upload the support bundle to the issue or send it to
[longhorn-support-bundle](mailto:longhorn-support-bundle@suse.com).

## Report Vulnerabilities

If any vulnerabilities are found, please report them to [longhorn-security](mailto:longhorn-security@suse.com).

# Community

Longhorn is open-source software, so contributions are greatly welcome.
Please read [Code of Conduct](./CODE_OF_CONDUCT.md) and [Contributing Guideline](./CONTRIBUTING.md) before contributing.

Contributing code is not the only way of contributing. We value feedback very much and many of the Longhorn features originated from users' feedback.
If you have any feedback, feel free to [file an issue](https://github.com/longhorn/longhorn/issues/new/choose).

## Slack

You can also provide feedback or join the conversation with other developers, users, and contributors on the [CNCF](https://slack.cncf.io/) [#longhorn](https://cloud-native.slack.com/messages/longhorn) Slack channel.
This is a good place to learn about Longhorn, ask questions, and share your experiences.

## Community Meeting and Office Hours

We host a monthly community meeting on the **3rd Thursday**, alternating between *AMER/EU-friendly* and *APAC-friendly times* - at **4 PM UTC** and **6 AM UTC** respectively. 

Everyone is welcome to join us. You can find the calendar invite [here](https://zoom-lfx.platform.linuxfoundation.org/meetings/longhorn?view=list)

## Longhorn Mailing List

Subscribe to our [developer](https://lists.cncf.io/g/cncf-longhorn-dev) and [users](https://lists.cncf.io/g/cncf-longhorn-users) to stay updated with the latest news and events.

You can read more about our community and its events here: https://github.com/longhorn/community

# License

Copyright (c) 2014-2026 The Longhorn Authors

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

[http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

## Longhorn is a [CNCF Incubating Project](https://www.cncf.io/projects/)

![Longhorn is a CNCF Incubating Project](https://github.com/cncf/artwork/blob/main/other/cncf/horizontal/color/cncf-color.png)
