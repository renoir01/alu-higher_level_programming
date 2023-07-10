#!/usr/bin/python3
def print_last_digit(number):
    value = None
    if number > 0:
        value = number % 10
    else:
        number = -number
        value = number % 10
    print("{}".format(value), end="")
    return value
