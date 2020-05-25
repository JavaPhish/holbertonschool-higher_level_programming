#!/usr/bin/python3
""" AAAAAAHHHHH """


class Rectangle:
    """ Rectangle: a class. """

    def __init__(self, width=0, height=0):
        """ init for rectangle """
        self.set_height(height)
        self.set_width(width)

    # setter
    def set_width(self, n_width):
        if type(n_width) is not int:
            raise TypeError("width must be an integer")
        if n_width < 0:
            raise ValueError("width must be >= 0")

        self.__width = n_width

    # getter
    def get_width(self):
        return self.__width

    width = property(get_width, set_width)

    # setter
    def set_height(self, n_height):
        if type(n_height) is not int:
            raise TypeError("height must be an integer")
        if n_height < 0:
            raise ValueError("height must be >= 0")

        self.__height = n_height

    # getter
    def get_height(self):
        return self.__height

    height = property(get_height, set_height)
