#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    This module returns a new dictionary with all values multiplied by 2.
    """
    # We should use dictionary comprehension.
    # Syntax: { key: value_operation for key, value in dictionary.items() }
    # This reads: "Create a new pair where the key is the same,
    # but the value is multiplied by 2, for every item in the original."
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}

    return new_dict
