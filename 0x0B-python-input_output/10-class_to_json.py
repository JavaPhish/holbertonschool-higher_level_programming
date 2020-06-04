#!/usr/bin/python3
""" class to json """


import json


def class_to_json(obj):
    """ Stores a class in json """
    return json.dumps(obj.__dict__)
