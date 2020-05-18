#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    iter = 0
    new_l = []
    diff_a = 0

    while (iter < list_length):
        try:
            diff_a = my_list_1[iter] / my_list_2[iter]
        except TypeError:
            print("wrong type")
            diff_a = 0
        except ZeroDivisionError:
            print("division by 0")
            diff_a = 0
        except IndexError:
            print("out of range")
            diff_a = 0
        finally:
            new_l.append(diff_a)
            iter += 1

    return new_l
