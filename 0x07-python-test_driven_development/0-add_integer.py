#!/usr/bin/python3

"""This module contains the add integer function"""


def add_integer(a, b=98):
    """This method adds two integers and returns their result
        Args:
            a: an integer or float
            b: an integer or float
        """

    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")

    if type(a) == float or type(b) == float:
        return int(a) + int(b)
    else:
        return a + b
