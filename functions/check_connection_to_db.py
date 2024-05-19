from pymongo.mongo_client import MongoClient

# check connection to mongo db
def check_connection():
    # Create a new client and connect to the server
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)


    # Send a ping to confirm a successful connection
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return True
    
    except Exception as e:
        print(e)
        return False
    
