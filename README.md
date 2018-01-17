# webApplicationDeployment
This repository includes the AWS Cloudformation template and AWS Lambda function to deploy a dynamically scalable application.

cloudwatch_putmetric_function.py
The lambda function to put metric to AWS Cloudwatch. Compress this file into a zip file and store it in S3 Bucket.

SecurityStack.yml
The stack to create a lambda role.

webApplicationDeployment.yaml
Main stack to deploy a dynamically scalable application. 
