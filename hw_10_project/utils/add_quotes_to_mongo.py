import json
import configparser
from urllib.parse import quote_plus

from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient('mongodb://localhost') 

db = client.hw_8

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)


for quote in quotes:
    author = db.author.find_one({'fullname': quote['author']})
    if author:
        db.quote.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])

        })