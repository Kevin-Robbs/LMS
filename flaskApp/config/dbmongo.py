import os
import certifi
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
load_dotenv('variables.env')
uri = f"mongodb+srv://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@weg-cluster-01.qmkxpsf.mongodb.net/?retryWrites=true&w=majority&appName=WEG-Cluster-01"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFILE=certifi.where())
db = client['wedgify']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)