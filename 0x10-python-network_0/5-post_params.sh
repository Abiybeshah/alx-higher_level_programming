#!/bin/bash
# a bash script that takes in a url
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
