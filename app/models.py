from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["webhook_db"]
collection = db["events"]

def save_event(event):
    event["timestamp"] = datetime.utcnow()
    collection.insert_one(event)

def get_all_events():
    return list(collection.find({}, {"_id": 0}))
