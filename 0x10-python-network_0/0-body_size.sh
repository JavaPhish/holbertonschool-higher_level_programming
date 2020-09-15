#!/bin/bash
# Outputs the size of an http response (in bytes)
curl -s -o /dev/null "$1" -w '%{size_download}\n'
