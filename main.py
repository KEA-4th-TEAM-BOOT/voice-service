import os
import uvicorn
from fastapi import FastAPI
from app import config
from app.api import main
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

port = int(os.environ.get("VOICE_PORT", 8004))

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # cross-origin request에서 cookie를 포함할 것인지 (default=False)
    allow_methods=["*"],     # cross-origin request에서 허용할 method들을 나타냄. (default=['GET']
    allow_headers=["*"],     # cross-origin request에서 허용할 HTTP Header 목록
)

app.include_router(main.api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)