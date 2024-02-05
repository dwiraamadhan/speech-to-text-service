import openai, os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Retrieve OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Convert audio to text
def convert_audio_to_text(audio_file):
    # try:
        transcript = openai.Client().audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="json"
        )
        print(transcript)
        return transcript
    # except Exception as e:
    #     return str(e)