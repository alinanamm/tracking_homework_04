import boto3
from botocore.client import Config

client = boto3.client(
    's3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='minioadmin',
    aws_secret_access_key='minioadmin',
    config=Config(signature_version='s3v4'),
    region_name='us-east-1',
)

client.create_bucket(Bucket='models')
client.upload_file('model_v1.pth', 'models', 'model_v1.pth')
client.upload_file('model_v2.pth', 'models', 'model_v2.pth')
print('Done')