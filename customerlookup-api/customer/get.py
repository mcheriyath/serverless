from __future__ import print_function
import os
import json
import logging
from customer import decimalencoder

import boto3
client = boto3.client('dynamodb')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def get(event, context):
    # fetch Items from the database
    result = client.get_item(
        TableName=os.environ['DYNAMODB_TABLE'],
        Key={
            'phonenumber': {"N": event['pathParameters']['phonenumber']}
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'],
                           cls=decimalencoder.DecimalEncoder)
    }
    return response
