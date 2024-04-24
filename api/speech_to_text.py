from fastapi import APIRouter, UploadFile, File, HTTPException
from dotenv import load_dotenv, find_dotenv
from functions.convert_audio_to_text import convert_audio_to_text
from kafka.producer import send_to_kafka

router = APIRouter()

# Load environment variables
load_dotenv(find_dotenv())

# Create endpoint for speech-to-text
@router.post("/speech-to-text")
async def transcribe_audio(audio_file : UploadFile = File(...)):
    try:
        # Open the audio file as a buffer
        with open(audio_file.filename, "wb") as buffer:
            buffer.write(audio_file.file.read())
        audio_input = open(audio_file.filename, "rb")
    
        # Convert audio to text by calling convert_audio_to_text function
        message_decode = convert_audio_to_text(audio_input)
        
        # send transcription to kafka
        send_to_kafka(message_decode)

        return {
            "text": message_decode
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))