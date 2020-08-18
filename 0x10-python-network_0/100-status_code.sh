#!/bin/bash
# Outputs the status code returned by the server
curl -s -o /dev/null -I "$1" -w "%{http_code}"
