import io
import json
import boto3
import fastavro

from fastavro import reader as avro_reader

def get_metadata(file_name: str,
                endpoint_url: str="http://minio:9000",
                aws_access_key_id: str="admin",
                aws_secret_access_key: str="password",
                bucket: str="warehouse",
                database: str="my_database",
                table: str="my_table",) -> dict:
    # MinIO S3 클라이언트 생성
    s3 = boto3.client(
        "s3",
        endpoint_url=endpoint_url,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    
    # Iceberg metadata.json 파일 읽기
    obj = s3.get_object(
        Bucket=bucket,
        Key=f"{database}/{table}/metadata/{file_name}"
    )
    return obj

def print_avro_item(obj: dict) -> fastavro._read.reader:
    bio = io.BytesIO(obj["Body"].read())
    avro_rdr = avro_reader(bio)
    for manifest in avro_rdr:
        print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return avro_rdr