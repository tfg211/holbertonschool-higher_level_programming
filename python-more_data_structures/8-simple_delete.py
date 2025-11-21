#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    This module deletes a key in a dictionary.
    """
    # 1st. safety check: specific verification that the key exists
    if key in a_dictionary:
        # 2nd. It deletes the key only if we found it
        del a_dictionary[key]

    # 3rd. It returns the dictionary (whether changed or not)
    return a_dictionary
