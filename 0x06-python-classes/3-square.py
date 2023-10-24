#!/usr/bin/python3

"""A class that contains the definition of a sqaure"""


class Square:
    """This Square class will be used to create a square shape"""

    def __init__(self, size=0):

        """instantiation with optional size =0

        Args:
            size(int): the size of the square
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size > 0
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):

        """A public instance method that returns the current square area

        Returns:
            int: the square of one of its sides
        """
        return self.__size ** 2

