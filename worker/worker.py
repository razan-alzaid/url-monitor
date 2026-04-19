import time
import requests
from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("MONGO_URI"))
db = client.monitor
collection = db.urls

while True:
    urls = list(collection.find())

    for item in urls:
        url = item["url"]

        try:
            start = time.time()
            response = requests.get(url, timeout=5)
            response_time = round(time.time() - start, 2)

            collection.update_one(
                {"_id": item["_id"]},
                {"$set": {
                    "status": response.status_code,
                    "response_time": response_time
                }}
            )

        except:
            collection.update_one(
                {"_id": item["_id"]},
                {"$set": {
                    "status": "down",
                    "response_time": None
                }}
            )

    time.sleep(10)