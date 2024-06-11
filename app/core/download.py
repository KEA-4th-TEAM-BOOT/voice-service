import os
import boto3
from dotenv import load_dotenv
from app.schemas.model import Model

load_dotenv()

def download_model(model: Model):
    try:
        model_path = f'models/RVC/{os.path.basename(model.model_link)}'
        index_path = f'models/RVC/.index/{os.path.basename(model.index_link)}'

        bucket = boto3.resource('s3').Bucket(os.getenv('AWS_BUCKET'))
        bucket.download_file(model.model_link, model_path)
        bucket.download_file(model.index_link, index_path)

        return model_path, index_path

    except Exception as e:
        print(e)

