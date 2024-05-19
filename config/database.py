from pymongo import MongoClient
import os

# Create a new client and connect to the server
client = MongoClient(os.getenv("MONGODB_URL"))
db = client["audio_ml"]
collection = db["audio_file"]