#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    if my_string is None:
        return 2
    for i in range(len(my_string)):
        if 'C' == my_string[i] or 'c' == my_string[i]:
            continue
        new_string += my_string[i]
    return new_string
