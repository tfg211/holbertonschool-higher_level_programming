#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    This module converts a Roman numeral to an integer.
    """
    # 1st. safety check: ensure input is a valid string
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # 2nd. the map: define the values
    roman_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    result = 0
    length = len(roman_string)

    # 3rd. loop through the string by index (so we can peek ahead)
    for i in range(length):
        # get the value of the current symbol
        current_val = roman_dict[roman_string[i]]

        # the lookahead:
        # checking if we are not at the last character AND
        # if the current value is smaller than the next value.
        if i < length - 1 and current_val < roman_dict[roman_string[i + 1]]:
            # Case: IV (4) -> We subtract 1
            result -= current_val
        else:
            # case: VI (6) or last char -> We add the value
            result += current_val

    return result
