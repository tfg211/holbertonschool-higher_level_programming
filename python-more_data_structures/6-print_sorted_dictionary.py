#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.
    """
    # 1st. It gets all keys, sort them, and loop through them.
    # sorted() takes the keys and returns a list ['a', 'b', 'c'...]
    for key in sorted(a_dictionary.keys()):
        # 2nd. It gets the value corresponding to the sorted key
        value = a_dictionary[key]

        # 3rd. It prints in the required format "Key: Value"
        print("{}: {}".format(key, value))
