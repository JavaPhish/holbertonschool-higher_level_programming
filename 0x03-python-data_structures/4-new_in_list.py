#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if (len(my_list) - 1 >= idx and idx >= 0):
        new_list = []
        for i in range(0, len(my_list)):
            if (idx == i):
                new_list = new_list + [element]
            else:
                new_list = new_list + [my_list[i]]

        return new_list
    else:
        return my_list
