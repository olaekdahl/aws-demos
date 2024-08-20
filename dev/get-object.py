import boto3

def get_object(bucket_name, key_name, download_path):
    # Create an S3 resource
    s3 = boto3.resource('s3')
    
    # Specify the bucket and object key
    bucket = s3.Bucket(bucket_name)
    obj = bucket.Object(key_name)
    
    # Download the object to a file
    obj.download_file(download_path)
    print(f'Downloaded {key_name} to {download_path}')

# Example usage
get_object('aws-dev-ola', 'cat1.jpg', 'orange_cat.jpg')