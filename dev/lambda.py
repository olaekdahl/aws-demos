import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal
import os
import logging
logger = logging.getLogger()
logger.setLevel("INFO")

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Define the table name
table_name = 'Notes'
table = dynamodb.Table(table_name)

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return int(o) if o % 1 == 0 else float(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ['AWS_LAMBDA_LOG_GROUP_NAME'])
    logger.info(os.environ['AWS_LAMBDA_LOG_STREAM_NAME'])
    logger.info('## EVENT')
    logger.info(event)
    
    # Extract UserId and NoteId from the event
    user_id = event.get('UserId')
    note_id = event.get('NoteId')

    # Validate input
    if not user_id or not note_id:
        return {
            'statusCode': 400,
            'body': json.dumps('UserId and NoteId are required.')
        }

    try:
        # Query the DynamoDB table
        response = table.get_item(
            Key={
                'UserId': int(user_id),
                'NoteId': int(note_id)  # Ensure NoteId is an integer
            }
        )

        # Check if the item exists
        if 'Item' in response:
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'], cls=DecimalEncoder)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps('Note not found.')
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error retrieving note: {str(e)}')
        }