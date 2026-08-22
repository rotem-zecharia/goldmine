# PrefectHQ/prefect

Prefect is a workflow orchestration framework for building resilient data pipelines in Python.

## installation

Prefect requires Python 3.10+. To [install the latest version of Prefect](https://docs.prefect.io/v3/get-started/install), run one of the following commands:

```bash
pip install -U prefect
```

```bash
uv add prefect
```

Then create and run a Python file that uses Prefect `flow` and `task` decorators to orchestrate and observe your workflow - in this case, a simple script that fetches the number of GitHub stars from a repository:

```python
from prefect import flow, task
import httpx


@task(log_prints=True)
def get_stars(repo: str):
    url = f"https://api.github.com/repos/{repo}"
    count = httpx.get(url).json()["stargazers_count"]
    print(f"{repo} has {count} stars!")


@flow(name="GitHub Stars")
def github_stars(repos: list[str]):
    for repo in repos:
        get_stars(repo)


# run the flow!
if __name__ == "__main__":
    github_stars(["PrefectHQ/prefect"])
```

Fire up a Prefect server and open the UI at http://localhost:4200 to see what happened:

```bash
prefect server start
```

To run your workflow on a schedule, turn it into a deployment and schedule it to run every minute by changing the last line of your script to the following:

```python
if __name__ == "__main__":
    github_stars.serve(
        name="first-deployment",
        cron="* * * * *",
        parameters={"repos": ["PrefectHQ/prefect"]}
    )
```

You now have a process running locally that is looking for scheduled deployments!
Additionally you can run your workflow manually from the UI or CLI. You can even run deployments in response to [events](https://docs.prefect.io/latest/automate/?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none).

> [!TIP]
> Where to go next - check out our [documentation](https://docs.prefect.io/v3/get-started/index?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none) to learn more about:
> - [Deploying flows to production environments](https://docs.prefect.io/v3/deploy?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none)
> - [Adding error handling and retries](https://docs.prefect.io/v3/develop/write-tasks#retries?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none)
> - [Integrating with your existing tools](https://docs.prefect.io/integrations/integrations?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none)
> - [Setting up team collaboration features](https://docs.prefect.io/v3/manage/cloud/manage-users/manage-teams#manage-teams?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none)


## Prefect Cloud

Prefect Cloud provides workflow orchestration for the modern data enterprise. By automating over 200 million data tasks monthly, Prefect empowers diverse organizations — from Fortune 50 leaders such as Progressive Insurance to innovative disruptors such as Cash App — to increase engineering productivity, reduce pipeline errors, and cut data workflow compute costs.

Read more about Prefect Cloud [here](https://www.prefect.io/cloud-vs-oss?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none) or sign up to [try it for yourself](https://app.prefect.cloud?utm_source=oss&utm_medium=oss&utm_campaign=oss_gh_repo&utm_term=none&utm_content=none).

## prefect-client

If your use case is geared towards communicating with Prefect Cloud or a remote Prefect server, check out our
[prefect-client](https://pypi.org/project/prefect-client/). It is a lighter-weight option for accessing client-side functionality in the Prefect SDK and is ideal for use in ephemeral execution environments.

## Connect & Contribute
Join a thriving community of over 25,000 practitioners who solve data challenges with Prefect. Prefect's community is built on collaboration, technical innovation, and continuous improvement.

### Community Resources
🌐 **[Explore the Documentation](https://docs.prefect.io)** - Comprehensive guides a
