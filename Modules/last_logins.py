#!/usr/bin/env python3

# Libraries
##############################################################################
import logging
from datetime import datetime, timedelta
from db_connection import db
from configs import LAST_LOGIN_DEL_PER
##############################################################################


##############################################################################
def delete_last_logins_data():
    # Access the 'Session' collection
    collection = db['session']

    # Calculate the date 7 days ago from now
    thirty_days_ago = datetime.now() - timedelta(days=LAST_LOGIN_DEL_PER)

    # Define the query to find documents with 'Created' date older than X days
    query = {"created": {"$lt": thirty_days_ago}}
    
    # Perform the deletion
    result = collection.delete_many(query)
    
    # Print each session
    logging.info(f"Deleted {result.deleted_count} old sessions.")
##############################################################################