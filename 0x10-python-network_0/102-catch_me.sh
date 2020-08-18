#!/bin/bash
# Finds a secret thing through redirects and data :)
curl -L -X PUT --data "user_id=98" -H "Origin: HolbertonSchool" "$1"
