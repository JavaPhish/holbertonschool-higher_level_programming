#!/usr/bin/python3


def uniq_add(my_list=[]):
    total = 0
    used_ints = []

    for i in my_list:
        if i not in used_ints:
            total = total + i
            used_ints.append(i)

    return total
