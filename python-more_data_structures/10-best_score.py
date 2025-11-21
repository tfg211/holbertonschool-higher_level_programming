#!/usr/bin/python3
def best_score(a_dictionary):
    """
    This module returns a key with the biggest integer value.
    """
    # 1nd. safety check: handle none or empty dictionary
    # If a_dictionary is None OR if it is empty {}, return None
    if not a_dictionary:
        return None

    # 2nd. initialize the "King of the Hill"
    # We need a variable to remember who is currently winning.
    # We can start by assuming the first key we find is the best,
    # or we can start with None/0.
    best_key = None
    biggest_value = 0

    # We create an iterator to grab the first element safely if we wanted,
    # but a simple loop is easier to read.

    for key, value in a_dictionary.items():
        # 3rd. the comparison
        # If best_key is still None (1 loop) OR current value beats the record
        if best_key is None or value > biggest_value:
            biggest_value = value
            best_key = key

    # 4th. return the name of the winner
    return best_key
