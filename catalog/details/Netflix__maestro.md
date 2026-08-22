# Netflix/maestro

Maestro: Netflix’s Workflow Orchestrator

## requirements

- Git
- Java 21
- Gradle
- Docker


## Build it
- `./gradlew build`

## Run it
- `./gradlew bootRun`

## Run it with AWS module
- `docker compose -f maestro-aws/docker-compose.yml up`
- `./gradlew bootRun --args='--spring.profiles.active=aws'`

## Create a sample workflow
- `curl --header "user: tester" -X POST 'http://127.0.0.1:8080/api/v3/workflows' -H "Content-Type: application/json" -d @maestro-server/src/test/resources/samples/sample-dag-test-1.json`

## Get the sample workflow definition
- `curl -X GET 'http://127.0.0.1:8080/api/v3/workflows/sample-dag-test-1/versions/latest'`

## Trigger to run the sample workflow
- `curl --header "user: tester" -X POST 'http://127.0.0.1:8080/api/v3/workflows/sample-dag-test-1/versions/latest/actions/start' -H "Content-Type: application/json" -d '{"initiator": {"type": "manual"}}'`

## Get the sample workflow instance
- `curl -X GET 'http://127.0.0.1:8080/api/v3/workflows/sample-dag-test-1/instances/1/runs/1'`

## Delete the sample workflow and its data
- `curl --header "user: tester" -X DELETE 'http://127.0.0.1:8080/api/v3/workflows/sample-dag-test-1'`

## Run it with maestro-extensions (foreach flattening service)
The `maestro-extensions` module runs as a separate Spring Boot service that listens to maestro
events via SQS (subscribed to the SNS topic maestro-server publishes to) and provides additional
functionality such as foreach step flattening views.

To run maestro-server and maestro-extensions together locally:
1. Start LocalStack (provides local SQS/SNS):
   - `docker compose -f maestro-aws/docker-compose.yml up -d`
2. Start maestro-server (port 8080):
   - `./gradlew :maestro-server:bootRun --args='--spring.profiles.active=aws'`
3. Start maestro-extensions (port 8081):
   - `./gradlew :maestro-extensions:bootRun`

Once both services are running, maestro-extensions will consume step instance status change events
from the `maestro-event` SQS queue and process foreach flattening. Query the flattened views via
the extensions REST API on port 8081.

## Run it with Kubernetes support
- setup kubernetes configs so the kubectl command works
- `./gradlew bootRun`
- `curl --header "user: tester" -X POST 'http://127.0.0.1:8080/api/v3/workflows' -H "Content-Type: application/json" -d @maestro-server/src/test/resources/samples/sample-kubernetes-wf.json`
- `curl --header "user: tester" -X POST 'http://127.0.0.1:8080/api/v3/workflows/sample-kubernetes-wf/versions/latest/actions/start' -H "Content-Type: application/json" -d '{"initiator": {"type": "manual"}}'`

## Python SDK client

## installation

```bash
pip install maestro-sdk
```

### Creating a workflow

```python
from maestro import Workflow, Job

wf = Workflow(id="test-wf")
wf.owner("tester").tags("test")
wf.job(Job(id="job1", type='NoOp'))
wf_yaml = wf.to_yaml()
```

### Pushing a workflow to Maestro server

```python
from maestro import Workflow, Job, MaestroClient

wf = Workflow(id="test-wf")
wf.owner("tester").tags("test")
wf.job(Job(id="job1", type='NoOp'))
wf_yaml = wf.to_yaml()

client = MaestroClient(base_url="http://127.0.0.1:8080", user="tester")
response = client.push_yaml(wf_yaml)
print(response)
```

### Starting a workflow

```python
from maestro import MaestroClient

client = MaestroClient(base_url="http://127.0.0.1:8080", user="tester")
response = client.start(workflow_id="test-wf", run_params={"foo": {"value": "bar", "type": "STRING"}})
print(response)
```

Please check [Maestro python](https://github.com/jun-he/maestro-python) project for more details.


## Get in touch
Join our community [Slack workspace](https://join.slack.com/t/maestro-oss/shared_invite/zt-3is5iwz9e-Px3UqLfzG8lEoWhTk5D4yA) for discussions!

# License
Copyright 2024 Netflix, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
