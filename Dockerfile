# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable for Scrapy
ENV PYTHONUNBUFFERED=1

# Define the command to run the Scrapy spider
CMD ["scrapy", "crawl", "quotes"]
