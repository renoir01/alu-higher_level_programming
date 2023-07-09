#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if value > 5:
    print(f"Last digit of {number:d} is {value:d} and is greater than 5")
elif value == 0:
    print(f"Last digit of {number:d} is {value:d} and is 0")
else value < 6 and value != 0:
    print(f"Last digit of {number:d} is {value:d} \
and is less than 6 and not 0")
