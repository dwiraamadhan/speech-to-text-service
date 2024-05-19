from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv, find_dotenv
from functions.convert_audio_to_text import convert_audio_to_text
from functions.check_connection_to_db import check_connection
from functions.check_kafka_connection import check_kafka_connection
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


# check health
@router.get("/health")
async def health_check():
    return JSONResponse(status_code=200, content={"status": "healthy"})

# check readiness
@router.get("/ready")
async def readiness_check():
    # check connection to mongoDB
    isReady = check_connection() and check_kafka_connection()
    if isReady:
        return JSONResponse(status_code=200, content={"status": "ready"})
    else:
        return JSONResponse(status_code=503, content={"status": "not ready"})