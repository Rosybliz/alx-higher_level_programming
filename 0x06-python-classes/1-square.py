#!/usr/bin/python3

"""A class that contains the definition of a Square"""


class Square:
    """This Square class will be used to create a square shape"""

    def __init__(self, size):
        """Instantiation of the attributes

        Args:
            size(int): this is the size of the square instantiated to private
        """
        self.__size = size
