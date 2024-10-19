
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "<Here, enter your mongodb url>"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.tools_db
collection = db["todo_data"]
