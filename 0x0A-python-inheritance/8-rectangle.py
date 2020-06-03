#!/usr/bin/python3
""" inherets from base_geo """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherets from base_geo """

    def __init__(self, width, height):
        """ init stuff """
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

        self.__width = width
        self.__height = height
