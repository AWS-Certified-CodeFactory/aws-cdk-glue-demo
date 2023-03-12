import aws_cdk as cdk
from constructs import Construct
from aws_cdk import aws_s3 as s3

class DataProcessingStack(cdk.Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        s3.Bucket(self, "dev.codefactory.data-processing", removal_policy=cdk.RemovalPolicy.DESTROY)