#!/bin/bash
# a bash script that makes a request to  0.0.0.0:5000/catch_me
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
