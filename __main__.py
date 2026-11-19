"""Main AWS Pulumi IaC (Python) Program."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import boto3  # noqa: F401 retained for future use
from botocore.exceptions import ClientError  # noqa: F401 retained for future use
import pulumi_aws as aws
import pulumi_awsx as awsx  # noqa: F401 retained for future use
from pulumi import (
    Config,
    ConfigMissingError,
    Output,
    export,
    get_project,
    get_stack,
    log,
)


project = get_project()
stack = get_stack()
config = Config(project)
aws_envs = {key: value for key, value in os.environ.items() if key.startswith("AWS_")}

caller = aws.get_caller_identity()
try:
    region = Config("aws").get("region") or aws.get_region().region
except Exception as error:
    error.add_note(
        "".join(["\n", "Failed to resolve the AWS region."]),
    )
    raise ExceptionGroup(
        "Runtime error. See the detailed error description below.", [error]
    )


def main() -> int:
    log.info(f"project: {project} [{stack}]")
    log.info(f"provider region: {region!r}")
    log.info("caller: {0!r}".format(caller.arn))

    return 0


if __name__ == "__main__":
    log.info(f"project directory: '{Path.cwd()!s}'")
    sys.exit(main())
