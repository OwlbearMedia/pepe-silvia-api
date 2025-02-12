# Set base image (host OS)
FROM python:3.13-alpine

# Set the working directory in the container
WORKDIR /pepe-silvia

# Copy the dependencies file to the working directory
COPY /requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the app to the working directory
COPY /app /pepe-silvia/app
COPY pepe-silvia.py .

ENV FLASK_APP pepe-silvia.py
ENV AWS_DEFAULT_REGION us-west-2

# By default, listen on port 5328
EXPOSE 5328/tcp

# Specify the command to run on container start
CMD [ "flask", "run", "-p", "5328", "--host", "0.0.0.0" ]
