import os

import boto3
import dotenv

s3_client = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
    region_name=os.getenv("AWS_REGION")
)

aws_bucket_name = os.getenv("AWS_BUCKET_NAME")

def upload_s3(file, filename):
    s3_client.upload_fileobj(file, aws_bucket_name, filename)
    return s3_client.generate_presigned_url("get_object", Params={"Bucket": aws_bucket_name, "Key": filename}, ExpiresIn=3600)