import boto3
import os
from botocore.exceptions import ClientError

def generate_presigned_url(file_name, expire=3600):
    print("✅ file_name recibido:", file_name)
    print("✅ Bucket:", os.environ.get('AWS_STORAGE_BUCKET_NAME'))
    print("✅ Access Key:", os.environ.get('AWS_ACCESS_KEY_ID'))
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
            region_name=os.environ.get('AWS_REGION', 'us-east-1')
        )

        url = s3.generate_presigned_url(
            ClientMethod='put_object',
            Params={
                'Bucket': os.environ.get('AWS_STORAGE_BUCKET_NAME'),
                'Key': file_name,
                'ContentType': 'video/mp4'
            },
            ExpiresIn=expire
        )
        print("AWS BUCKET NAME:", os.environ.get('AWS_STORAGE_BUCKET_NAME'))
        return url
    except ClientError as e:
        print(f"Error generating presigned URL: {e}")
        return None
