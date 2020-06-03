#!/usr/bin/python3
""" save to json file """


import json


def save_to_json_file(my_obj, filename):
    """ save an object to a json file """
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))
