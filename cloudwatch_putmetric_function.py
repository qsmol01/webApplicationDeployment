import os
import boto3
import datetime

def lambda_handler(event, context):
    # Read Metric Info from environment variables
    env = dict(os.environ.items())

    # Create count for metrics measurement
    count = datetime.datetime.now().minute
    # It can be replaced with any other value retrieved from API. In this case datetime.minute is implemented, no realistic meaning.

    # Create CloudWatch client
    cloudwatch = boto3.client('cloudwatch')

    # Put custom metrics
    cloudwatch.put_metric_data(
        MetricData=[
            {
                'MetricName': env['MetricName'],
                'Unit': 'Count',
                'Value': count,
                'StorageResolution': 60
            },
        ],
        Namespace=env['Namespace']
    )
    return None
