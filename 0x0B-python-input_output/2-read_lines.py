#!/usr/bin/python3
""" read lines """


def read_lines(filename="", nb_lines=0):
    """ Reads a specified number of lines in a file """
    with open(filename, 'r') as file:

        if (nb_lines == 0):
            print(file.read())
        else:
            for ln in range(0, nb_lines):
                print(file.readline(), end="")
