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

    def area(self):
        """ area - Returns the area of the square """
        return self.__size * self.__size

    # getter
    def get_size(self):
        """ get_size - getter """
        return self.__size

    # setter
    def set_size(self, n_size=0):
        """ set_size - setter """
        if type(n_size) is not int:
            raise TypeError("size must be an integer")

        if n_size < 0:
            raise ValueError("size must be >= 0")

        self.__size = n_size

    size = property(get_size, set_size)
