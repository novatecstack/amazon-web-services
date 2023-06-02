# Description: This is a sample aws lambda function handler for listing all the lambda functions in current region
# Author: Novatec

import boto3

# create a service client object before making callout to the member functions
client = boto3.client('lambda')

def lambda_handler(event, context):
  response = client.list_functions()
  return response
