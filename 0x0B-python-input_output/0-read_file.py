#!/usr/bin/python3
""" Contains read_file """


def read_file(filename=""):
    """ Reads a file and prints to stdout """
    with open(filename, 'r') as file:
        print(file.read(), end="")
