#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    num_c = 0
    iter = 0

    while (iter < x):
        try:
            print("{:d}".format(my_list[iter]), end="")
            num_c += 1
            iter += 1
        except IndexError as e:
            raise
        except:
            iter += 1

    print("")
    return (num_c)
