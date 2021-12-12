import os

import boto3

s3 = boto3.resource(
    service_name='s3',
    region_name=os.getenv('AWS_DEFAULT_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)


def upload_file_s3(filename, key):
    s3.Bucket("cloud-niit-project").upload_file(Filename=filename, Key=key)

