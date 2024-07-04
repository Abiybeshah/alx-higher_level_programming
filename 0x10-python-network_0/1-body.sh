#!/bin/bash
# a bash script that takes in a URL and sends a GET request
if [ "$(curl -sLI "$1" -X GET | grep "200 OK" | cut -d' ' -f2)" = '200' ]; then curl -sL "$1"; fi
