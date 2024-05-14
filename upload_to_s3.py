import boto3

s3_client=boto3.client('s3')
bucket_name='customer-rds-project'


def upload_to_s3(filename,datestr):
    file_path=f'raw_data/date={datestr}/{filename}'
    s3_client.upload(f'tmp/{filename}',bucket_name,file_path)
    print(f"File uploaded to S3 Bucket {bucket_name}/{file_path}")
    return
