# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install any needed packages specified in requirements.txt (make sure gunicorn is in the file)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Make port 6079 available to the world outside this container
EXPOSE 10020

# Define environment variable
ENV FLASK_APP run.py
ENV FLASK_RUN_HOST 0.0.0.0

# Run run.py when the container launches
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:10020", "run:app"]


## docker build -t deltaweb . (run this everytime we build it again or changes )

## docker run -p 4985:4985 deltaweb


#uptome 

## wade1 / Celina@12