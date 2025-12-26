from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load the library so that the variable in the .env can have a direct connection
load_dotenv()

# MongoDB configuration on environment variable
uri = os.getenv('MONGODB_URL')

if not uri:
    raise ValueError("MONGODB_URL not found in .env file")

# Start the MongoDB Atlas
client = MongoClient(uri, server_api=ServerApi('1'))

# MongoDB Database
db = client[os.environ["MONGODB_DB"]]     

# Collection 
collection = db[os.environ["MONGODB_COLLECTION"]]      

def ping_db():
    try:
        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        print("Connected to MongoDB successfully!")
    except Exception as e:
        print(f"Error connecting: {e}")

# Execute ping check
ping_db()