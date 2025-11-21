#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one of the sets.
    """
    # The '^' operator (caret) performs a Symmetric Difference.
    # It answers the question: "What is unique to Set A OR unique to Set B?"
    return set_1 ^ set_2
