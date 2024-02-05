from fastapi import FastAPI
from api.speech_to_text import router

app = FastAPI()
app.include_router(router)