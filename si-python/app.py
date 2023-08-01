from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo
from dotenv import load_dotenv
import os
import certifi
import json
ca = certifi.where()
load_dotenv()
uri = os.getenv('MONGO_URI')
db_name = 'insights-db'
collection_name = 'insights'
json_file_path = 'bse_announcements_data.json'

with open(json_file_path, "r") as file:
    data = json.load(file)
 # Connect to MongoDB
client = MongoClient(uri, server_api=ServerApi('1'),tlsCAFile=ca)
    
    # Access the database
db = client[db_name]
    
    # Access or create the collection
collection = db[collection_name]
    

print('start')
collection.insert_many(data)
print('end')





