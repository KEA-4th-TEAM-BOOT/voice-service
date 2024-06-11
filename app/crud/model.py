import os
import requests
from dotenv import load_dotenv
from app.schemas.model import Model

load_dotenv()

def get_model(user_id: int) -> Model:
    api_url = f'{os.getenv("MODEL_URL")}/{user_id}'
    response = requests.get(api_url)

    if response.status_code == 200:
        json_response = response.json()
        model_link = json_response['model_link']
        index_link = json_response['index_link']
        return Model(user_id=user_id, model_link=model_link, index_link=index_link)
    else:
        raise Exception(f"HTTP Error: {response.status_code}")

