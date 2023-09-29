from pymongo import MongoClient


def get_mongodb():
    client = MongoClient('mongodb://localhost') 

    db = client.web_hw_8
    return db
 