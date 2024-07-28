#!/usr/bin/env python3

# Libraries
##############################################################################
import schedule
import time
import logging

from Modules.last_logins import delete_last_logins_data
from Modules.disk_usage import delete_disk_usage_data
from Modules.memory_usage import delete_memory_usage_data
from Modules.cpu_usage import delete_cpu_usage_data

from configs import SCHEDULED_JOBS as scheduled_jobs
##############################################################################

# Configs
##############################################################################
# Logging Format
FORMAT = '%(asctime)s :: %(levelname)-6s :: %(name)s :: [%(filename)s:%(lineno)s - %(funcName)s()] :: %(message)s'

# Logfile
logfile_path = 'jobs_logs.log'

# Configure logging to write logs to a log file
logging.basicConfig(
    filename=logfile_path, 
    level=logging.INFO,
    format=FORMAT,
    encoding='utf-8'
)
##############################################################################

# Main
##############################################################################

# Run the functions before scheduling
delete_last_logins_data()
delete_disk_usage_data()
delete_memory_usage_data()

# Schedule jobs
for job_name, job_config in scheduled_jobs.items():
    if "interval" in job_config:
        interval = job_config["interval"]
        unit = job_config.get("unit", "minutes")
        getattr(schedule.every(interval), unit).do(eval(job_name))
    elif "time" in job_config:
        time_str = job_config["time"]
        schedule.every().day.at(time_str).do(eval(job_name))

# Run 
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every 60 seconds
##############################################################################