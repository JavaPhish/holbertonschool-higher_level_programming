#!/usr/bin/python3
""" Inherets from Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square """

    def __init__(self, size):
        """ init """
        Rectangle.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """ override from rectangle """
        return self.__size * self.__size

    def __str__(self):
        """ str """
        return "[Square] {}/{}".format(self.__size, self.__size)
