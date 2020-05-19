#!/usr/bin/python3


class Square:
    """ Square: a class. """

    def __init__(self, size=0):
        """ Init - init method """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
