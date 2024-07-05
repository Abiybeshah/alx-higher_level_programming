#!/bin/bash
# a bash script that sends a DELETE request to the URL passed as
# first argument
curl -sX "DELETE" "$1"
