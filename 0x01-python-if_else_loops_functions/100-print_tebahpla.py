#!/usr/bin/env python3

flipflop = 0
for i in range(90, 64, -1):
    if flipflop == 0:
        flipflop = 32
    else:
        flipflop = 0
    print("{}".format(chr(i + flipflop)), end="")
