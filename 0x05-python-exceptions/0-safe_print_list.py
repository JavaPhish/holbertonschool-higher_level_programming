#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    iter = 0
    try:
        while (iter < x):
            print("{}".format(my_list[iter]), end="")
            iter = iter + 1
    except:
        print("")
        return iter
    print("")
    return iter
