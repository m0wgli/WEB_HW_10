import json
import configparser
from urllib.parse import quote_plus
import logging

from pymongo import MongoClient
from bson.objectid import ObjectId


logging.basicConfig(filename='app.log', level=logging.ERROR)  

client = MongoClient('mongodb://localhost') 

db = client.hw_8

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)


for quote in quotes:
    try:
        author = db.authors.find_one({'fullname': quote['author']})
        if author:
            print(f"Found author: {quote['author']}")
            db.quotes.insert_one({
                'quote': quote['quote'],
                'tags': quote['tags'],
                'author': ObjectId(author['_id'])
            })
        else:
            print(f"Author not found for: {quote['author']}")
            authors_fullnames = [a['fullname'] for a in db.authors.find()]
            print(f"Authors in the 'authors' collection: {authors_fullnames}")
    except Exception as e:
        print(f"Error: {str(e)}")


