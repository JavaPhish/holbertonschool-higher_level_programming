#!/usr/bin/python3
""" number of lines """


def number_of_lines(filename=""):
    """ returns the nubmer of lines in a file """
    lines = 0
    with open(filename, 'r') as file:
        for ln in file:
            lines += 1

    return lines
