#!/bin/bash
# Takeing a URL and sends a request to that URL
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
