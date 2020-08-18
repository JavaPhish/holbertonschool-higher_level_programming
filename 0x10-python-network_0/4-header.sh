#!/bin/bash
# Sends a GET request with header variable
curl -X -s "GET" "$1" -H "X-HolbertonSchoolUser-Id: 98"
