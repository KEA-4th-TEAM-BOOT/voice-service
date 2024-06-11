from fastapi import APIRouter, Depends
#from sqlalchemy.orm import Session
from dotenv import load_dotenv
#from database.voice import get_db
from app.crud.model import get_model
from app.core.download import download_model
from app.core.polly import polly_voice
from app.core.convert import mp3_to_wav
from app.core.inference import inference_voice
from app.schemas.post import Post

load_dotenv()

router = APIRouter()

@router.post('/{user_id}')
def inference(user_id: int, post: Post):
    model = get_model(user_id)
    model_path, index_path = download_model(model)
    mp3 = polly_voice(post)
    wav = mp3_to_wav(mp3, post.post_id)
    inference_voice(wav, model_path)









