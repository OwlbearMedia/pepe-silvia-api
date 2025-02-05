#!/bin/zsh

# Get auth token
aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 640550388417.dkr.ecr.us-west-2.amazonaws.com
# then pull
docker pull 640550388417.dkr.ecr.us-west-2.amazonaws.com/pepe-silvia:latest
