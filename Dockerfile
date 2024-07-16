# Use an official Python runtime as a parent image
FROM python:3.10-alpine

# Update and upgrade system packages
RUN apk update && apk upgrade

# Set the working directory in the container
WORKDIR /scheduled_jobs

# Copy the current directory contents into the container at /app
COPY . /scheduled_jobs/

# Upgrade Pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run your application
CMD ["python3","jobs.py"]