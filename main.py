from fastapi import FastAPI
from api.speech_to_text import router
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

origins = ["http://localhost:5173", os.getenv("WEB_URL")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add router
app.include_router(router)