#!/usr/bin/python3
""" Load a json object from a file """


import json


def load_from_json_file(filename):
    """ Load a json object from a file """
    with open(filename, 'r') as file:
        return json.loads(file.read())
