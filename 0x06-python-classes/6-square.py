#!/usr/bin/python3


class Square:
    """ Square: a class. """

    def __init__(self, size=0, position=(0, 0)):
        """ Init - init method """
        self.set_size(size)
        self.set_position(position)

    def area(self):
        """ area - Returns the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ my_print - Prints a square """

        if (self.__size is 0):
            print("")
        else:
            line = (((" " * self.__position[0]) + ("#" * self.__size) + "\n"))
            print("\n" * self.__position[1], end="")
            print(self.__size * line, end="")

    # setter
    def set_position(self, n_position):
        """ set_position - Sets the position """
        if (type(n_position) is not tuple or len(n_position) < 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (n_position[0] < 0 or n_position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = n_position

    # getter
    def get_position(self):
        """ get_position - gets the position """
        return (self.__position)

    position = property(get_position, set_position)

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
