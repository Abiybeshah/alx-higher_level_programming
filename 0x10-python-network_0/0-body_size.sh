#!/bin/bash
# a bash script that takes in a URL sends a request
curl -sI "$1" | awk '/Content-Length/ {print $2}'
