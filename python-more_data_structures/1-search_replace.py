#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    if new_list is None:
        return my_list
    for i, j in enumerate(new_list):
        if j != search:
            continue
        else:
            new_list[i] = replace
    return new_list
