from fastapi import FastAPI
from api.speech_to_text import router
from pymongo.mongo_client import MongoClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:5173", "http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# # Create a new client and connect to the server
# uri = "mongodb://localhost:27017/"
# client = MongoClient(uri)


# # Send a ping to confirm a successful connection
# try:
#     client.admin.command("ping")
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

app.include_router(router)