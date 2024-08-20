import asyncio
import aioboto3

async def create_dynamodb_table():
    # Create an async session with aioboto3
    async with aioboto3.Session().resource('dynamodb', region_name='us-west-1') as dynamodb:
        # Create the DynamoDB table asynchronously
        table = await dynamodb.create_table(
            TableName='Notes',
            KeySchema=[
                {
                    'AttributeName': 'ID',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'ID',
                    'AttributeType': 'S'  # String type
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        # Wait until the table exists using an async waiter
        waiter = table.meta.client.get_waiter('table_exists')
        await waiter.wait(TableName='Notes')

        # Print out some data about the table
        print(f"Table status: {table.table_status}")
        print(f"Item count: {table.item_count}")

# Run the async function
asyncio.run(create_dynamodb_table())