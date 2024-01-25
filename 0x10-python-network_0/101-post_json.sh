#!/bin/bash
# Creating a script that sending a JSON POST request
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
