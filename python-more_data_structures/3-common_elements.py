#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.
    """
    # The '&' operator performs a mathematical intersection on two sets.
    # It returns a new set containing only items present in BOTH sets.
    return set_1 & set_2
