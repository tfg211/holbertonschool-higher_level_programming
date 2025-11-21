#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    """
    # This single line handles both 'Update' and 'Insert' logic.
    # If 'key' is there, it changes the value.
    # If 'key' is missing, it adds the key with the value.
    a_dictionary[key] = value

    # It returns the dictionary so the main file can assign it to a variable
    return a_dictionary
