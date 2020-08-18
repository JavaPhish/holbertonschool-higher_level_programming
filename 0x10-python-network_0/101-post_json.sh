#!/bin/bash
# Posts a json file to a given URL
curl -X "POST" "$1" -d @"$2" -H 'Content-Type: application/json' 
