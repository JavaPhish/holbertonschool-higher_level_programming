#!/bin/bash
# Sends a GET request with header variable
curl -s -H "GET" -H "X-HolbertonSchool-User-Id: 98" "$1"
