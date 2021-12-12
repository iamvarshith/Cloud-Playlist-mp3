import boto3

import os

def create_user(username):
    iam = boto3.client("iam")
    response = iam.create_user(UserName=username)
    print(response)
"Responce"
"""{'User': {'Path': '/', 'UserName': 'iamuser', 'UserId': 'AIDARZ4JYP3BNBJIOZRLE', 'Arn': 'arn:aws:iam::124306095810:user/iamuser', 'CreateDate': datetime.datetime(2021, 12, 6, 17, 55, 3
1, tzinfo=tzutc())}, 'ResponseMetadata': {'RequestId': '5a73913b-64b7-49b0-9e15-958986e0c1e3', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '5a73913b-64b7-49b0-9e15-95898
6e0c1e3', 'content-type': 'text/xml', 'content-length': '475', 'date': 'Mon, 06 Dec 2021 17:55:31 GMT'}, 'RetryAttempts': 0}}
"""
# print(create_user("iamuser"))

""" Second part"""

def attach_police(username):
    iam = boto3.client('iam')
    response = iam.attach_user_policy(
    UserName = username, #Name of user
    PolicyArn = 'arn:aws:iam::aws:policy/AmazonS3fullaccess'
# Policy ARN which you want to asign to user
)
    print(response)

# attach_police('iamuser')

#responce to second Question
"""{'ResponseMetadata': {'RequestId': '3d001803-6a9d-4b0f-bb49-0a1682219f44', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '3d001803-6a9d-4b0f-bb49-0a1682219f44', 'content-t
ype': 'text/xml', 'content-length': '212', 'date': 'Mon, 06 Dec 2021 17:59:22 GMT'}, 'RetryAttempts': 0}}
"""

def create_s3_bucket(bucket):
    s3 = boto3.resource('s3')
    s3.create_bucket(Bucket=bucket)

    s3.create_bucket(Bucket='mybucket', ACL='private', CreateBucketConfiguration={
    'LocationConstraint': 'ap-south-1'})

    ## listing the buckets


    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

# create_s3_bucket("niitcloudassignment")



s3 = boto3.resource(
    service_name='s3',
    region_name=os.getenv('AWS_DEFAULT_REGION'),
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)


def upload_file_s3(filename, key):
    s3.Bucket("cloud-niit-project").upload_file(Filename=filename, Key=key)





