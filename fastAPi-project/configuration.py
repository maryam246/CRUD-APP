
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://khanammaryam036:<YourPassword>@crud-app.pwgz0.mongodb.net/?retryWrites=true&w=majority&appName=CRUD-app"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.tools_db
collection = db["todo_data"]
