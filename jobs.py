#!/usr/bin/env python3

# Libraries
##############################################################################
import schedule
import time

from Modules.last_logins import delete_last_logins_data
from configs import SCHEDULED_JOBS as scheduled_jobs
##############################################################################

# Configs
##############################################################################

##############################################################################

# Main
##############################################################################

# Run the functions before scheduling
delete_last_logins_data()

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