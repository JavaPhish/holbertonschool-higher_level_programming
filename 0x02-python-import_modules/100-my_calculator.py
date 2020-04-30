#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] == "+":
        total = int(argv[1]) + int(argv[3])
        print("{} + {} = {}".format(argv[1], argv[3], total))
    elif argv[2] == "-":
        difference = int(argv[1]) + int(argv[3])
        print("{} - {} = {}".format(argv[1], argv[3], difference))
    elif argv[2] == "/":
        difference = int(argv[1]) + int(argv[3])
        print("{} / {} = {}".format(argv[1], argv[3], difference))
    elif argv[2] == "*":
        difference = int(argv[1]) + int(argv[3])
        print("{} * {} = {}".format(argv[1], argv[3], difference))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
