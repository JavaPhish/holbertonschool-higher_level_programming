#!/usr/bin/python3
""" base class """


import json
import os.path


class Base:
    """ yeet """

    id = 0

    def __init__(self, id=None):
        """ init class """
        self.__nb_objects = 0
        if id is None:
            Base.id += 1
        else:
            self.__nb_objects = 0
            self.id = id

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation """

        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """ Creates instances based on the contents of <classname>.json """
        instance_list = []
        filename = "{}.json".format(cls.__name__)
        if (os.path.isfile(filename) is False):
            return instance_list

        with open(filename, 'r') as file:
            file_out = cls.from_json_string(file.read())
            for inst_data in file_out:
                new_inst = cls.create(inst_data)
                instance_list += new_inst

        return instance_list

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ is "Rectangle":
            new_rect = cls(1, 1)
            uid = dictionary['id']
            uwid = dictionary['width']
            uhei = dictionary['height']
            ux = dictionary['x']
            uy = dictionary['y']

            new_rect.update(uid, uwid, uhei, ux, uy)
            return new_rect

        if cls.__name__ is "Square":
            new_sqr = cls(1)
            uid = dictionary['id']
            uwid = dictionary['size']
            ux = dictionary['x']
            uy = dictionary['y']

            new_sqr.update(uid, uwid, ux, uy)
            return new_sqr

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves all class instances to JSON file """
        json_str = "["
        with open("{}.json".format(cls.__name__), 'w') as file:
            for objs in range(0, len(list_objs)):
                if (objs == 0):
                    obj_dict = list_objs[objs].to_dictionary()
                    json_str += Base.to_json_string(obj_dict)
                else:
                    json_str += ", "
                    obj_dict = list_objs[objs].to_dictionary()
                    json_str += Base.to_json_string(obj_dict)
            json_str += "]"
            file.write(json_str)

    @staticmethod
    def to_json_string(my_obj):
        """ json representation of a string """
        return json.dumps(my_obj)
