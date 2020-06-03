#!/usr/bin/python3
""" Geometry class stuff """


class BaseGeometry():
    """ sup """

    def area(self):
        """ Just supposed to leave this broken lol """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates a string """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
