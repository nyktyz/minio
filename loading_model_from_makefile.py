import os
from pathlib import Path

import minio
from dotenv import load_dotenv


load_dotenv()


def upload_to_minio(
    minio_client: minio.Minio,
    file_path: Path | str, 
    bucket_name: str,
    object_name: str
):
    if not minio_client.bucket_exists(bucket_name=bucket_name):
        print(f"бакет {bucket_name} не существует, создаем его")
        minio_client.make_bucket(bucket_name)
        print("бакет успешно создан")
    minio_client.fput_object(
        bucket_name=bucket_name,
        object_name=object_name,
        file_path=file_path
    )


def main():
    minio_client = minio.Minio(
        endpoint=os.environ["S3_ENDPOINT"],
        access_key=os.environ["AWS_ACCESS_KEY_ID"],
        secret_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        secure=os.environ["S3_IS_SECURE"] == "True"
    )
    upload_to_minio(
    minio_client,
    os.environ["FILE_PATH"],
    os.environ["BUCKET_NAME"],
    os.environ["OBJECT_NAME"]
    )


if __name__ == "__main__":
    main()
