#!/usr/bin/python3
""" checks if a class is the same instance of an obj """


def is_same_class(obj, a_class):
    """ checks if a class is the same instance of an obj """
    if (type(obj) is a_class):
        return True
    return False
