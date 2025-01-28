#!/bin/zsh

aws lightsail create-container-service-deployment --service-name pepe-silvia-api --containers file://containers.json --public-endpoint file://public-endpoint.json
