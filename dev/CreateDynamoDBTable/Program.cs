using System;
using System.Threading;
using Amazon.DynamoDBv2;
using Amazon.DynamoDBv2.Model;

class Program
{
    static void Main(string[] args)
    {
        // Initialize AmazonDynamoDBClient
        var client = new AmazonDynamoDBClient();

        // Create a table request
        var request = new CreateTableRequest
        {
            TableName = "ExampleTable",
            KeySchema = new List<KeySchemaElement>
            {
                new KeySchemaElement
                {
                    AttributeName = "Id",
                    KeyType = "HASH" // Partition key
                }
            },
            AttributeDefinitions = new List<AttributeDefinition>
            {
                new AttributeDefinition
                {
                    AttributeName = "Id",
                    AttributeType = "S" // String type
                }
            },
            ProvisionedThroughput = new ProvisionedThroughput
            {
                ReadCapacityUnits = 5,
                WriteCapacityUnits = 5
            }
        };

        // Create the table
        var response = client.CreateTableAsync(request).Result;
        var tableDescription = response.TableDescription;

        // Initial status of the table
        var status = tableDescription.TableStatus;

        // Wait until the table becomes active
        while (status != "ACTIVE")
        {
            // After the table is created, its status is set to ACTIVE
            Thread.Sleep(5000); // Wait 5 seconds

            // Get the latest table information
            var describeTableResponse = client.DescribeTableAsync(new DescribeTableRequest
            {
                TableName = "ExampleTable"
            }).Result;

            Console.WriteLine("Table name: {0}, status: {1}",
                describeTableResponse.Table.TableName,
                describeTableResponse.Table.TableStatus);

            status = describeTableResponse.Table.TableStatus;
        }

        Console.WriteLine("Table creation completed. Status: ACTIVE");
    }
}