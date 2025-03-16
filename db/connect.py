# python
# db/connect.py
from pymongo import MongoClient
import logging

class Connect:
    def __call__(self, mongo_uri, db_name):
        try:
            logging.info("Connecting to MongoDB...")
            client = MongoClient(mongo_uri)
            db = client[db_name]
            logging.info("Connected to MongoDB at %s (DB: %s).", mongo_uri, db_name)
            return db
        except Exception as e:
            logging.error("Failed to connect to MongoDB: %s", str(e))
            return None