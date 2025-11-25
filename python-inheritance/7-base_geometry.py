#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    A class that defines the base geometry.
    """

    def area(self):
        """
        Raises an Exception indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name)))
