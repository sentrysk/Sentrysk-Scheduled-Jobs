#!/usr/bin/env python3

# Libraries
##############################################################################
import json
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
SCHEDULED_JOBS = config['scheduled_jobs']

# Get DB Configs from Config
DB_ATTRS = config['database']

# Deletion Periods
DELETION_PERIODS = config['deletion_periods']
##############################################################################
