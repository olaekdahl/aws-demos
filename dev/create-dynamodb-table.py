import boto3

# Create the DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table with UserId as the partition key and NoteId as the sort key
# table = dynamodb.create_table(
#     TableName='Notes',
#     KeySchema=[
#         {
#             'AttributeName': 'UserId',
#             'KeyType': 'HASH'  # Partition key
#         },
#         {
#             'AttributeName': 'NoteId',
#             'KeyType': 'RANGE'  # Sort key
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'UserId',
#             'AttributeType': 'N'  # Number type
#         },
#         {
#             'AttributeName': 'NoteId',
#             'AttributeType': 'N'  # Number type
#         }
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )

# # Wait until the table exists
# table.meta.client.get_waiter('table_exists').wait(TableName='Notes')

# # Print out some data about the table
# print(f"Table status: {table.table_status}")
# print(f"Item count: {table.item_count}")

# # Insert sample data with a list and a map
# table.put_item(
#     Item={
#         'UserId': 1,
#         'NoteId': 101,
#         'Note': 'This is the first note',
#         'Favorite': True,
#         'Tags': ['personal', 'important'],  # List attribute
#         'Metadata': {  # Map attribute
#             'Author': 'User1',
#             'CreatedDate': '2024-08-18'
#         }
#     }
# )

# table.put_item(
#     Item={
#         'UserId': 1,
#         'NoteId': 102,
#         'Note': 'This is the second note',
#         'Favorite': False,
#         'Tags': ['work', 'meeting'],
#         'Metadata': {
#             'Author': 'User1',
#             'CreatedDate': '2024-08-17'
#         }
#     }
# )

# table.put_item(
#     Item={
#         'UserId': 2,
#         'NoteId': 201,
#         'Note': 'This is a note for another user',
#         'Favorite': True,
#         'Tags': ['shared', 'collaboration'],
#         'Metadata': {
#             'Author': 'User2',
#             'CreatedDate': '2024-08-16'
#         }
#     }
# )

table = dynamodb.Table('Notes')
# Query and print the inserted data
# response = table.scan()
# for item in response['Items']:
#     print(item)

response = table.query(KeyConditionExpression='UserId = :uid',  # Query by partition key
                       ExpressionAttributeValues={':uid': 1})
for item in response['Items']:
    print(item)