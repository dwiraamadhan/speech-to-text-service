from fastapi import APIRouter, UploadFile, File
from dotenv import load_dotenv, find_dotenv
from functions.convert_audio_to_text import convert_audio_to_text

router = APIRouter()
load_dotenv(find_dotenv())

# Create endpoint for speech-to-text
@router.post("/speech-to-text")
async def transcribe_audio(audio_file : UploadFile = File(...)):

    with open(audio_file.filename, "wb") as buffer:
        buffer.write(audio_file.file.read())
    audio_input = open(audio_file.filename, "rb")
    
    message_decode = convert_audio_to_text(audio_input)

    return message_decode