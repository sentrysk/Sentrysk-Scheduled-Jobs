#!/usr/bin/env python3

# Libraries
##############################################################################
import logging
from datetime import datetime, timedelta
from db_connection import db
from configs import DISK_USAGE_DEL_PER
##############################################################################


##############################################################################
def delete_disk_usage_data():
    # Access the 'disk_usage' collection
    collection = db['disk_usage']

    # Calculate the date 7 days ago from now
    seven_days_ago = datetime.now() - timedelta(days=DISK_USAGE_DEL_PER)

    # Define the query to find documents with 'Created' date older than X days
    query = {"timestamp": {"$lt": seven_days_ago}}
    
    # Perform the deletion
    result = collection.delete_many(query)
    
    # Print each session
    logging.info(f"Deleted {result.deleted_count} old disk usage data.")
##############################################################################