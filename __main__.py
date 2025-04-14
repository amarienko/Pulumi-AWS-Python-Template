"""An AWS Python Pulumi program"""

import os
import sys
import boto3
from botocore.exceptions import ClientError

# import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx
from pulumi import Config, Output, export


config = Config()
