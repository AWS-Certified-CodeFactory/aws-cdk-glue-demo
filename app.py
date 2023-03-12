#!/usr/bin/env python3

from aws_cdk import App
from data_processing.data_processing_stack import DataProcessingStack

app = App()
DataProcessingStack(app, "aws-cdk-glue-demo-stack")
app.synth()