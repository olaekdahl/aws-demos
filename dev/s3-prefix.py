import boto3

def list_objects_by_prefix(bucket_name, prefix):
    # Create an S3 resource
    s3 = boto3.resource('s3')

    # If you need to specify the region, you can pass it as an argument
    # s3 = boto3.resource('s3', region_name='us-west-1', 
    #                     aws_access="YOUR_ACCESS_KEY_ID", 
    #                     aws_secret_access="YOUR_SECRET_ACCESS_KEY")
    
    # Specify the bucket
    bucket = s3.Bucket(bucket_name)
    
    # List objects that start with the specified prefix
    for obj in bucket.objects.filter(Prefix=prefix):
        print(obj.key)

# Example usage
list_objects_by_prefix('bah-demo-001', '')