#!/usr/bin/python3


def search_replace(my_list, search, replace):
    new_list = []

    for iter in range(0, len(my_list)):
        if (my_list[iter] == search):
            new_list.append(replace)
        else:
            new_list.append(my_list[iter])

    return new_list
