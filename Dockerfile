# Set base image (host OS)
FROM python:3.13-alpine

# By default, listen on port 5328
EXPOSE 5328/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
ADD src .

# Specify the command to run on container start
CMD [ "flask", "--app", "app","run" ]
