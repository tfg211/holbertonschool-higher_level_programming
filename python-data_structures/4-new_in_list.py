#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # create a copy of the list
    new_list = my_list.copy()

    # invalid index -> return copy without changes
    if idx < 0 or idx >= len(my_list):
        return new_list

    # valid index -> replace only in the copy
    new_list[idx] = element
    return new_list
