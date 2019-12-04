import boto3
import pprint
import os
from boto3.dynamodb.conditions import Key,Attr

ddb = boto3.resource('dynamodb',endpoint_url='http://localhost:8000',region_name="us-west-2")
table = os.environ.get('DYNAMO_TABLE')

response = table.scan()

# response = table.query(KeyConditionExpression=Key('pk').eq('your_key'))

#response = table.query(KeyConditionExpression = Key('pk') & Key('sk').begins_with(your_data))

# response = table.query(IndexName='gsi_1',KeyConditionExpression=Key('sk').eq('your query'))

# response = table.query(IndexName='gsi_1',KeyConditionExpression=Key('sk').eq('your_data') & Key('data').begins_with('you pattern'))


pprint.pprint(response['Items'])
