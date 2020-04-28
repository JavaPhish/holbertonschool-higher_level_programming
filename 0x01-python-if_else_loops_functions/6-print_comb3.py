#!/usr/bin/python3

for frst in range(0, 9):
    for scnd in range(frst + 1, 10):
        if ((frst + scnd) != 17):
            print("{}{}".format(frst, scnd), end=", ")

print("{}".format(89))
