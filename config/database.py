from pymongo import MongoClient

# Create a new client and connect to the server
client = MongoClient("mongodb://localhost:27017")
db = client["audio_ml"]
collection = db["audio_file"]