#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lastd = ((number * -1) % 10) * -1
else:
    lastd = number % 10
print("Last digit of {} is {} and is ".format(number, lastd), end="")

if lastd > 5:
    print("greater than 5")
elif lastd < 6 and lastd is not 0:
    print("less than 6 and not 0")
else:
    print("0")
