#!/usr/bin/python3


def element_at(my_list, idx):
    if (len(my_list) - 1 >= idx and idx >= 0):
        return my_list[idx]
    else:
        return None
