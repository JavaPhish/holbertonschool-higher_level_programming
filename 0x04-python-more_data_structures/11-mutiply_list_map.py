#!/usr/bin/python3


def mutiply_list_map(my_list=[], number=0):
    new = list(map(lambda x: x * number, my_list))
    return new
