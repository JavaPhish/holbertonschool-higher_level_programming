#!/bin/bash
# Sends a GET request with header variable
curl -s -X "GET" -H "X-HolbertonSchoolUser-Id: 98" "$1"
