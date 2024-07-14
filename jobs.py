#!/usr/bin/env python3

# Libraries
##############################################################################
import json
import os
import logging
import schedule
import requests
import time
from mongoengine import connect
##############################################################################

# Configs
##############################################################################
def load_config(file_path):
    with open(file_path, 'r') as file:
        config_data = json.load(file)
    return config_data

# Specify the path to your JSON configuration file
config_file_path = 'config.json'

# Load configuration from the JSON file
config = load_config(config_file_path)

# Get Scheduled Jobs from Config
scheduled_jobs = config['scheduled_jobs']

# Get DB Configs from Config
db_attrs = config['database']

# DB Config
try:
    db = connect(
        host     = db_attrs.get('HOST'),
        port     = db_attrs.get('PORT'),
        db       = db_attrs.get('DB'),
        username = db_attrs.get('USERNAME'), 
        password = db_attrs.get('PASSWORD')
    )
    print("DB connection successful")
except Exception as e:
    print(f'MongoDB connection failed: {e}')
##############################################################################

# 
