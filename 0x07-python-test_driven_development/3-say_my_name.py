#!/usr/bin/python3
""" not a reference to a very popular tv series on netflix """


def say_my_name(first_name, last_name=""):
    """ I can't read it without hearing Walts raspy voice """

    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")
    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
