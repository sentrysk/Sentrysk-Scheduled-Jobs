#!/usr/bin/env python3

# Libraries
##############################################################################
from pymongo import MongoClient
from configs import DB_ATTRS
##############################################################################


##############################################################################
# Database Attributes
try:
    username = DB_ATTRS.get('USERNAME')
    password = DB_ATTRS.get('PASSWORD')
    host = DB_ATTRS.get('HOST')
    port = DB_ATTRS.get('PORT')
    database = DB_ATTRS.get('DB')
except Exception as e:
    print(f'Error getting DB Attrs from config, {e}')

# MongoDB connection details
MONGODB_URI = f'mongodb://{username}:{password}@{host}:{port}'

try:
    # Create a MongoDB client
    client = MongoClient(MONGODB_URI)

    # Access the database
    db = client[database]
except Exception as e:
    print(f'Error connecting to Database, {e}')
##############################################################################