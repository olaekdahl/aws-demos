import boto3

def list_client():
    # Create an S3 client
    s3client = boto3.client('s3')
    
    # List objects within a specified bucket
    response = s3client.list_objects_v2(Bucket='config-bucket-397188165174')
    
    # Check if the bucket contains any objects
    if 'Contents' in response:
        for content in response['Contents']:
            # Print the object key and its last modified date
            print(content['Key'], content['LastModified'])
    else:
        print("The bucket is empty or does not exist.")

def list_resource():
    # Create an S3 resource
    s3resource = boto3.resource('s3')
    
    # Specify the bucket
    bucket = s3resource.Bucket('config-bucket-397188165174')
    
    # Iterate through all objects in the bucket
    for obj in bucket.objects.all():
        # Print the object key and its last modified date
        print(obj.key, obj.last_modified)


list_client()
list_resource()



# export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY_ID
# export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_ACCESS_KEY
# export AWS_DEFAULT_REGION=YOUR_REGION

import boto3

# s3client = boto3.resource(
#     's3',
#     aws_access_key_id='YOUR_ACCESS_KEY_ID',
#     aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
#     region_name='YOUR_REGION'
# )


