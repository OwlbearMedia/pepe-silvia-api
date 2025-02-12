#!/bin/zsh

aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 640550388417.dkr.ecr.us-west-2.amazonaws.com