#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (once for each integer).
    """
    # 1st. Converts the list to a set. This removes all duplicate numbers.
    unique_numbers = set(my_list)

    # 2nd. Uses the built-in sum() function to add up the elements in the set.
    return sum(unique_numbers)
