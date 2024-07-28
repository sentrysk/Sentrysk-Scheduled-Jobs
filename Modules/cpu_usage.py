#!/usr/bin/env python3

# Libraries
##############################################################################
import logging
from datetime import datetime, timedelta
from db_connection import db
##############################################################################


##############################################################################
def delete_cpu_usage_data():
    # Access the 'cpu_usage' collection
    collection = db['cpu_usage']

    # Calculate the date X days ago from now
    x_days_ago = datetime.now() - timedelta(days=3)

    # Define the query to find documents with 'timestamp' date older than X days
    query = {"timestamp": {"$lt": x_days_ago}}
    
    # Perform the deletion
    result = collection.delete_many(query)
    
    # Print each session
    logging.info(f"Deleted {result.deleted_count} old cpu usage data.")
##############################################################################