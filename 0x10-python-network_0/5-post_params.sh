#!/bin/bash
# Sends a GET request with header variable
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
