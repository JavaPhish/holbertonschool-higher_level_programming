#!/usr/bin/python3
""" based on 12 and 11 """


class Student():
    """ student class """

    def __init__(self, first_name, last_name, age):
        """ initialization """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ converts into a json readable format.. without json... """
        if attrs is None:
            return self.__dict__

        filter_d = {}
        for key in attrs:
            if key in self.__dict__.keys():
                filter_d[key] = self.__dict__[key]

        return filter_d

    def reload_from_json(self, json):
        """ Reload from json """
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
