import boto3

def multipart_upload_with_resource(bucket_name, file_path, key_name):
    # Create an S3 resource
    s3 = boto3.resource('s3')
    
    # Get the bucket and object to be uploaded
    bucket = s3.Bucket(bucket_name)
    
    # Step 1: Initiate the multipart upload
    multipart_upload = bucket.initiate_multipart_upload(Key=key_name)
    upload_id = multipart_upload.id
    print(f'Initiated multipart upload with Upload ID: {upload_id}')
    
    # Step 2: Upload parts
    parts = []
    part_number = 1
    chunk_size = 5 * 1024 * 1024  # 5 MB chunks

    try:
        with open(file_path, 'rb') as file:
            while True:
                data = file.read(chunk_size)
                if not data:
                    break

                # Upload each part using the multipart upload ID
                part = multipart_upload.Part(part_number)
                response = part.upload(Body=data)
                
                # Store the part number and ETag for later
                parts.append({
                    'PartNumber': part_number,
                    'ETag': response['ETag']
                })
                print(f'Uploaded part {part_number} with ETag: {response["ETag"]}')
                part_number += 1

        # Step 3: Complete the multipart upload
        multipart_upload.complete(MultipartUpload={'Parts': parts})
        print('Multipart upload completed successfully!')

    except Exception as e:
        # If there is an error, abort the upload
        print(f'Error occurred: {e}')
        multipart_upload.abort()
        print('Multipart upload aborted.')

# Example usage
multipart_upload_with_resource('mybucket', 'path/to/largefile.zip', 'uploads/largefile.zip')