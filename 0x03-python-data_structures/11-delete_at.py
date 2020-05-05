#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if (len(my_list) - 1 >= idx and idx >= 0):
        new_list = []
        for i in range(0, len(my_list)):
            if (i != idx):
                new_list = new_list + [my_list[i]]
        my_list = new_list
        return my_list
    else:
        return my_list
