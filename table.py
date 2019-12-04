import json
import boto3
import os

ddb = boto3.resource('dynamodb',endpoint_url='http://localhost:8000',region_name="us-west-2")

try:
    response = ddb.create_table(
                TableName = os.environ.get('DYNAMO_TABLE'),
                KeySchema = [{
                    'AttributeName' : "pk",
                    'KeyType'       : "HASH"
                },
                {
                    'AttributeName' : "sk",
                    'KeyType'       : "RANGE"
                }],
                AttributeDefinitions = [
                    {
                        'AttributeName' : "pk",
                        'AttributeType' : "S"
                    },
                    {
                        'AttributeName' : "sk",
                        "AttributeType" : "S"
                    },
                    {
                        'AttributeName' : 'user',
                        'AttributeType' : "S"
                    },
                    {
                        'AttributeName' : "data",
                        'AttributeType' : "S"
                    },
                    {
                        'AttributeName' : "statustime",
                        'AttributeType' : "S"
                    }
                ],
                GlobalSecondaryIndexes = [
                    {
                        'IndexName' : "gsi_1",
                        'KeySchema' : [
                            {
                                'AttributeName' : 'sk',
                                'KeyType'       : 'HASH'
                            },
                            {
                                'AttributeName' : 'data',
                                'KeyType'       : 'RANGE'
                            }
                        ],
                        'Projection' : {
                            'ProjectionType' : 'ALL'
                        }
                    }
                ],
                BillingMode = 'PAY_PER_REQUEST'
    )
    print("Table created successfully")
except:
    print("Creation resulted in an error")    