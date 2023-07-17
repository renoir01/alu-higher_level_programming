#!/usr/bin/python3
def number_keys(a_dictionary):
    if a_dictionary is None:
        return a_dictionary
    list_key = list(a_dictionary)
    count = 0
    for i in list_key:
        count += 1
    return count
