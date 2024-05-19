import openai, os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from config.database import collection

# Retrieve OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Convert audio to text
def convert_audio_to_text(audio_file):
        
        #save audio file to mongodb
        content = audio_file.read()
        file_audio = {"audio_file": content}
        collection.insert_one(file_audio)

        # create object trascript
        transcript = openai.Client().audio.transcriptions.create(
            model=os.getenv("SPEECH_TO_TEXT_MODEL"),
            file=audio_file,
            response_format="text"
        )
        print(transcript)
        return transcript