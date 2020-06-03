#!/usr/bin/python3
""" obj from json """


import json


def from_json_string(my_str):
    """ make object from json string """
    return json.loads(my_str)
