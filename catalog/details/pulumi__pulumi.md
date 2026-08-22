# pulumi/pulumi

Pulumi - Infrastructure as Code in any programming language 🚀

## installation

[![Watch the video](/youtube_preview_image.png)](https://www.youtube.com/watch?v=Q8tw6YTD3ac)

See the [Get Started](https://www.pulumi.com/docs/get-started/) guide to quickly get started with
Pulumi on your platform and cloud of choice.

Otherwise, the following steps demonstrate how to deploy your first Pulumi program, using AWS
Serverless Lambdas, in minutes:

1. **Install**:

    To install the latest Pulumi release, run the following (see full
    [installation instructions](https://www.pulumi.com/docs/install/) for additional installation options):

    ```bash
    curl -fsSL https://get.pulumi.com/ | sh
    ```

2. **Create a Project**:

    After installing, you can get started with the `pulumi new` command:

    ```bash
    mkdir pulumi-demo && cd pulumi-demo
    pulumi new serverless-aws-typescript
    ```

    The `new` command offers [templates](https://github.com/pulumi/templates/) for all languages and clouds.  Run it without an argument and it'll prompt
    you with available projects.  This command creates an AWS Serverless Lambda project written in TypeScript.

3. **Deploy to the Cloud**:

    Run `pulumi up` to get your code to the cloud:

    ```bash
    pulumi up
    ```

    This makes all cloud resources needed to run your code.  Simply make edits to your project, and subsequent
    `pulumi up`s will compute the minimal diff to deploy your changes.

4. **Use Your Program**:

    Now that your code is deployed, you can interact with it.  In the above example, we can curl the endpoint:

    ```bash
    curl $(pulumi stack output url)
    ```

5. **Access the Logs**:

    If you're using containers or functions, Pulumi's unified logging command will show all of your logs:

    ```bash
    pulumi logs -f
    ```

6. **Destroy your Resources**:

    After you're done, you can remove all resources created by your program:

    ```bash
    pulumi destroy -y
    ```

To learn more, head over to [pulumi.com](https://www.pulumi.com/) for much more information, including
[tutorials](https://www.pulumi.com/tutorials/), [examples](https://github.com/pulumi/examples), and
details of the core Pulumi CLI and [programming model concepts](https://www.pulumi.com/docs/iac/concepts/).
