#!/bin/bash
# Outputs all HTTP methods accepted by server
curl -I -s "$1" | grep "Allow:" | cut -c 8-
