#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) is 0:
        return None

    max = my_list[0]
    for num in my_list:
        if (max < num):
            max = num

    return max
