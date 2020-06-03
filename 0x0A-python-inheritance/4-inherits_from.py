#!/usr/bin/python3
""" Checks if an object is inhereted """


def inherits_from(obj, a_class):
    """ see top """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
