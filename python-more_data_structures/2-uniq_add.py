#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return my_list
    set_mylist = set(my_list)
    summation = 0
    for i in set_mylist:
        summation += i
    return summation
