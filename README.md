<p align="left">
  <a href="https://www.pulumi.com/product/infrastructure-as-code/" alt="Pulumi">
    <img src="https://img.shields.io/badge/pulumi-%3E%3D3.275-blue"/></a>
  <a href="https://opensource.org/licenses/MIT" alt="License">
    <img src="https://img.shields.io/github/license/amarienko/Pulumi-AWS-Python-Template?color=yellow"/></a>
</p>

# Pulumi-AWS-Python-Template
Basic Pulumi AWS template with support for AWS Boto3 SDK

The main basic Pulumi template with support of the Amazon Web Services (AWS) core framework [`@pulumi/aws`](https://pypi.org/project/pulumi/) and the AWS resource provider for Pulumi [`@pulumi/aws`](https://pypi.org/project/pulumi-aws/) and main Pulumi's framework for AWS infrastructure [`@pulumi/awsx`](https://pypi.org/project/pulumi-awsx/).

The template also includes support for [Boto3](https://pypi.org/project/boto3/) AWS Software Development Kit (SDK) for Python.

## Basic Usage
You could create a new Pulumi project by passing the fully-qualified URL path to the repository to `pulumi new` command, like this:
```zsh
❯ pulumi new --generate-only https://github.com/{your-org}/{your-repo}.git
```
After the command is successfully executed, only a new project is created; option `--generate-only` do not create a stack, save config, or install dependencies (an example of the output is presented below).

```
❯ pulumi new --generate-only https://github.com/amarienko/Pulumi-AWS-Python-Template.git
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

Project name (aws-iac-project): aws_ecs
Project description (A minimal Pulumi AWS Python project with Boto3 Support): AWS ECS Deployment 
Created project 'aws_ecs'

Your new project is ready to go! ✨

To perform an initial deployment, run the following commands:

   1. pulumi install
   2. pulumi stack init

Then, run `pulumi up`

```
The next step is install packages and plugins for the current Pulumi project with `pulumi install` command:
```
❯ pulumi install                                                                                              
Installing dependencies...

Using CPython 3.14.9
Creating virtual environment at: .venv
Resolved 41 packages in 21ms
Installed 40 packages in 230ms
 + ast-serialize==0.13.1
 + boto3==1.44.4
 + boto3-stubs==1.44.3
 + botocore==1.44.4
 + botocore-stubs==1.43.126
 + debugpy==1.8.22
 + dill==0.4.1
 + googleapis-common-protos==1.76.0
 + grpcio==1.85.1
 + jmespath==1.1.0
 + librt==0.16.0
 + mypy==2.4.1
 + mypy-extensions==1.2.0
 + opentelemetry-api==1.45.2
 + opentelemetry-exporter-otlp-common==0.66b2
 + opentelemetry-exporter-otlp-proto-common==1.45.2
 + opentelemetry-exporter-otlp-proto-grpc==1.45.2
 + opentelemetry-instrumentation==0.66b2
 + opentelemetry-instrumentation-grpc==0.66b2
 + opentelemetry-proto==1.45.2
 + opentelemetry-sdk==1.45.2
 + opentelemetry-semantic-conventions==0.66b2
 + packaging==26.3
 + parver==1.0.1.post0
 + pathspec==1.1.1
 + protobuf==6.33.6
 + pulumi==3.276.0
 + pulumi-aws==7.55.0
 + pulumi-awsx==3.13.0
 + pulumi-docker==4.11.2
 + pulumi-docker-build==0.0.23
 + python-dateutil==2.9.0.post0
 + pyyaml==6.0.3
 + s3transfer==0.19.3
 + semver==3.1.2
 + six==1.17.0
 + types-s3transfer==0.19.3
 + typing-extensions==4.16.0
 + urllib3==2.8.0
 + wrapt==2.5.2
Finished installing dependencies

Downloading provider docker: 22.16 MiB / 22.16 MiB [=================] 100.00% 4s
Unpacking provider docker: 22.16 MiB / 22.16 MiB [===================] 100.00% 0s
Downloading provider docker-build: 26.43 MiB / 26.43 MiB [===========] 100.00% 5s
Unpacking provider docker-build: 26.43 MiB / 26.43 MiB [=============] 100.00% 0s
Downloading provider awsx: 47.79 MiB / 47.79 MiB [===================] 100.00% 7s
Unpacking provider awsx: 47.79 MiB / 47.79 MiB [=====================] 100.00% 0s
Downloading provider aws: 174.44 MiB / 174.44 MiB [=================] 100.00% 14s
Unpacking provider aws: 174.44 MiB / 174.44 MiB [====================] 100.00% 3s

```
After successfully installing the dependencies, the final step is to create the project stack(s) using the `pulumi stack init <stack_name>` command.

An alternative installation method that does not use the `--generate-only` option. In this approach, a single command performs three operations: deploying the project, installing dependencies, and creating the initial stack.

### Versions
| Name | Version |
|------|-------------|
| pulumi | >= 3.275.0 |
| pulumi-aws | >=7.55.0 |
| pulumi-awsx | >=3.13.0 |
| boto3 | >=1.44.0 |

### References
* [Pulumi project file reference](https://www.pulumi.com/docs/iac/concepts/projects/project-file/)
* [aws.Provider](https://www.pulumi.com/registry/packages/aws/api-docs/provider/)
* [awsx.Provider](https://www.pulumi.com/registry/packages/awsx/api-docs/provider/)
