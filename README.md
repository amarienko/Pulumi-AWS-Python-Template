<p align="left">
  <a href="https://www.pulumi.com/product/infrastructure-as-code/" alt="Pulumi">
    <img src="https://img.shields.io/badge/pulumi-%3E%3D3.160-blue"/></a>
  <a href="https://opensource.org/licenses/MIT" alt="License">
    <img src="https://img.shields.io/github/license/amarienko/Pulumi-AWS-Python-Template?color=yellow"/></a>
</p>

# Pulumi-AWS-Python-Template
Basic Pulumi AWS template with support for AWS Boto3 SDK

The main basic Pulumi template with support of the Amazon Web Services (AWS) core framework [`@pulumi/aws`](https://pypi.org/project/pulumi/) and the AWS resource provider for Pulumi [`@pulumi/aws`](https://pypi.org/project/pulumi-aws/) and main Pulumi's framework for AWS infrastructure [`@pulumi/awsx`](https://pypi.org/project/pulumi-awsx/).

The template also includes support for [Boto3](https://pypi.org/project/boto3/) AWS Software Development Kit (SDK) for Python.

### Basic Usage
You could create a new Pulumi project by passing the fully-qualified URL path to the repository to `pulumi new` command, like this:
```zsh
❯ pulumi new https://github.com/{your-org}/{your-repo}.git
```
After the command is successfully executed, a new project and stack will be created (an example of the output is presented below).
```
❯ pulumi new https://github.com/amarienko/Pulumi-AWS-Python-Template.git

This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

Project name (route53): aws-route53
Project description (A minimal Pulumi AWS Python with Boto3 Template): AWS Route53 Zone
Created project 'aws-route53'

Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
Stack name (dev): prod
Created stack 'prod'

The AWS region to deploy into (aws:region) (us-east-1): ca-central-1
Saved config

Installing dependencies...

Creating virtual environment...
Finished creating virtual environment
Updating pip, setuptools, and wheel in virtual environment...
Requirement already satisfied: pip in ./venv/lib/python3.13/site-packages (24.3.1)
Collecting pip
  Using cached pip-25.0.1-py3-none-any.whl.metadata (3.7 kB)
Collecting setuptools
  Downloading setuptools-78.1.0-py3-none-any.whl.metadata (6.6 kB)
Collecting wheel
  Downloading wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Using cached pip-25.0.1-py3-none-any.whl (1.8 MB)
Downloading setuptools-78.1.0-py3-none-any.whl (1.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 2.4 MB/s eta 0:00:00
Downloading wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools, pip
  Attempting uninstall: pip
    Found existing installation: pip 24.3.1
    Uninstalling pip-24.3.1:
      Successfully uninstalled pip-24.3.1
Successfully installed pip-25.0.1 setuptools-78.1.0 wheel-0.45.1
Finished updating
Installing dependencies in virtual environment...
Collecting pulumi<4.0.0,>=3.160.0 (from -r requirements.txt (line 1))
  Downloading pulumi-3.162.0-py3-none-any.whl.metadata (3.7 kB)
Collecting pulumi-aws<7.0.0,>=6.70.0 (from -r requirements.txt (line 2))
  Downloading pulumi_aws-6.76.0-py3-none-any.whl.metadata (10 kB)
Collecting pulumi-awsx<3.0.0,>=2.20.0 (from -r requirements.txt (line 3))
  Downloading pulumi_awsx-2.21.1-py3-none-any.whl.metadata (7.4 kB)
Collecting boto3>=1.35.0 (from -r requirements.txt (line 4))
  Downloading boto3-1.37.33-py3-none-any.whl.metadata (6.7 kB)
Collecting botocore>=1.35.0 (from -r requirements.txt (line 5))
  Downloading botocore-1.37.33-py3-none-any.whl.metadata (5.7 kB)
Collecting debugpy~=1.8.7 (from pulumi<4.0.0,>=3.160.0->-r requirements.txt (line 1))
  Downloading debugpy-1.8.14-py2.py3-none-any.whl.metadata (1.4 kB)
Collecting dill~=0.3 (from pulumi<4.0.0,>=3.160.0->-r requirements.txt (line 1))
  Downloading dill-0.3.9-py3-none-any.whl.metadata (10 kB)
Collecting grpcio~=1.66.2 (from pulumi<4.0.0,>=3.160.0->-r requirements.txt (line 1))
  Downloading grpcio-1.66.2-cp313-cp313-macosx_10_13_universal2.whl.metadata (3.9 kB)
Requirement already satisfied: pip<26,>=24.3.1 in ./venv/lib/python3.13/site-packages (from pulumi<4.0.0,>=3.160.0->-r requirements.txt (line 1)) (25.0.1)
Collecting protobuf~=4.21 (from pulumi<4.0.0,>=3.160.0->-r requirements.txt (line 1))
  Downloading protobuf-4.25.6-cp37-abi3-macosx_10_9_universal2.whl.metadata (541 bytes)
Collecting pyyaml~=6.0 (from pulumi<4.0.0,>=3.160.0->-r requirements.txt (line 1))
  Downloading PyYAML-6.0.2-cp313-cp313-macosx_11_0_arm64.whl.metadata (2.1 kB)
Collecting semver~=3.0 (from pulumi<4.0.0,>=3.160.0->-r requirements.txt (line 1))
  Downloading semver-3.0.4-py3-none-any.whl.metadata (6.8 kB)
Collecting parver>=0.2.1 (from pulumi-aws<7.0.0,>=6.70.0->-r requirements.txt (line 2))
  Downloading parver-0.5-py3-none-any.whl.metadata (2.7 kB)
Collecting pulumi-docker<5.0.0,>=4.6.0 (from pulumi-awsx<3.0.0,>=2.20.0->-r requirements.txt (line 3))
  Downloading pulumi_docker-4.6.2-py3-none-any.whl.metadata (2.4 kB)
Collecting pulumi-docker-build<1.0.0,>=0.0.8 (from pulumi-awsx<3.0.0,>=2.20.0->-r requirements.txt (line 3))
  Downloading pulumi_docker_build-0.0.11-py3-none-any.whl.metadata (2.6 kB)
Collecting jmespath<2.0.0,>=0.7.1 (from boto3>=1.35.0->-r requirements.txt (line 4))
  Using cached jmespath-1.0.1-py3-none-any.whl.metadata (7.6 kB)
Collecting s3transfer<0.12.0,>=0.11.0 (from boto3>=1.35.0->-r requirements.txt (line 4))
  Using cached s3transfer-0.11.4-py3-none-any.whl.metadata (1.7 kB)
Collecting python-dateutil<3.0.0,>=2.1 (from botocore>=1.35.0->-r requirements.txt (line 5))
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting urllib3!=2.2.0,<3,>=1.25.4 (from botocore>=1.35.0->-r requirements.txt (line 5))
  Downloading urllib3-2.4.0-py3-none-any.whl.metadata (6.5 kB)
Collecting arpeggio>=1.7 (from parver>=0.2.1->pulumi-aws<7.0.0,>=6.70.0->-r requirements.txt (line 2))
  Downloading Arpeggio-2.0.2-py2.py3-none-any.whl.metadata (2.4 kB)
Collecting attrs>=19.2 (from parver>=0.2.1->pulumi-aws<7.0.0,>=6.70.0->-r requirements.txt (line 2))
  Downloading attrs-25.3.0-py3-none-any.whl.metadata (10 kB)
Collecting six>=1.5 (from python-dateutil<3.0.0,>=2.1->botocore>=1.35.0->-r requirements.txt (line 5))
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading pulumi-3.162.0-py3-none-any.whl (328 kB)
Downloading pulumi_aws-6.76.0-py3-none-any.whl (10.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.3/10.3 MB 1.8 MB/s eta 0:00:00
Downloading pulumi_awsx-2.21.1-py3-none-any.whl (119 kB)
Downloading boto3-1.37.33-py3-none-any.whl (139 kB)
Downloading botocore-1.37.33-py3-none-any.whl (13.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.5/13.5 MB 3.5 MB/s eta 0:00:00
Downloading debugpy-1.8.14-py2.py3-none-any.whl (5.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.3/5.3 MB 2.8 MB/s eta 0:00:00
Downloading dill-0.3.9-py3-none-any.whl (119 kB)
Downloading grpcio-1.66.2-cp313-cp313-macosx_10_13_universal2.whl (10.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.8/10.8 MB 3.5 MB/s eta 0:00:00
Using cached jmespath-1.0.1-py3-none-any.whl (20 kB)
Downloading parver-0.5-py3-none-any.whl (15 kB)
Downloading protobuf-4.25.6-cp37-abi3-macosx_10_9_universal2.whl (394 kB)
Downloading pulumi_docker-4.6.2-py3-none-any.whl (110 kB)
Downloading pulumi_docker_build-0.0.11-py3-none-any.whl (43 kB)
Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading PyYAML-6.0.2-cp313-cp313-macosx_11_0_arm64.whl (171 kB)
Using cached s3transfer-0.11.4-py3-none-any.whl (84 kB)
Downloading semver-3.0.4-py3-none-any.whl (17 kB)
Downloading urllib3-2.4.0-py3-none-any.whl (128 kB)
Downloading Arpeggio-2.0.2-py2.py3-none-any.whl (55 kB)
Downloading attrs-25.3.0-py3-none-any.whl (63 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: arpeggio, urllib3, six, semver, pyyaml, protobuf, jmespath, grpcio, dill, debugpy, attrs, python-dateutil, pulumi, parver, pulumi-docker-build, pulumi-docker, pulumi-aws, botocore, s3transfer, pulumi-awsx, boto3
Successfully installed arpeggio-2.0.2 attrs-25.3.0 boto3-1.37.33 botocore-1.37.33 debugpy-1.8.14 dill-0.3.9 grpcio-1.66.2 jmespath-1.0.1 parver-0.5 protobuf-4.25.6 pulumi-3.162.0 pulumi-aws-6.76.0 pulumi-awsx-2.21.1 pulumi-docker-4.6.2 pulumi-docker-build-0.0.11 python-dateutil-2.9.0.post0 pyyaml-6.0.2 s3transfer-0.11.4 semver-3.0.4 six-1.17.0 urllib3-2.4.0
Finished installing dependencies
Finished installing dependencies

Your new project is ready to go! ✨

To perform an initial deployment, run `pulumi up`

```
