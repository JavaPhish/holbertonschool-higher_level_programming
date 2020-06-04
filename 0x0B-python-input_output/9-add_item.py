#!/usr/bin/python3
""" adds args to a list then json file """

import os.path
import sys
import json

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


json_file = "add_item.json"
json_data = []


with open(json_file, 'w+') as file:

    if os.path.exists(json_file):
        if ("[" in file.read()):
            json_data = load_from_json_file(json_file)

    json_data += sys.argv[1:]

    save_to_json_file(json_data, json_file)
