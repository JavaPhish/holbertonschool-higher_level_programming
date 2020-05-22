#!/usr/bin/python3
""" Just contains print_square """


def print_square(size):
    """ print_square - Prints a square based on size """

    if (type(size) is not int):
        raise TypeError("size must be an integer")

    if (size < 0):
        raise ValueError("size must be >= 0")

    print(size * ((size * "#") + "\n"), end="")
