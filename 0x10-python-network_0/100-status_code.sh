#!/bin/bash 
# Creating a script sending an HTTP request.
curl -s -L -X HEAD -w "%{http_code}" "$1"
