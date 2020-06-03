#!/usr/bin/python3
""" appends to a file """


def append_write(filename="", text=""):
    """ Appends rather than writes to a file """
    with open(filename, 'a') as file:
        return file.write(text)
