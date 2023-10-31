#!/usr/bin/python3

"""This module prints a name"""


def say_my_name(first_name, last_name=""):

    """This method prints the first and lastname of the user

        Args:
            first_name(str): the user's first name
            last_name(str): the user's last_name
        """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

