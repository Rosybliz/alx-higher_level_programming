#!/usr/bin/python3

"""A class that contains the definition of a sqaure"""


class Square:
    """This Square class will be used to create a square shape"""

    def __init__(self, size=0):

        """instantiation with optional size =0

        Args:
            size(int): the size of the square
        """
        self.size = size

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Sets this square position"""
        if ((type(value) is tuple) and
           (len(value) == 2) and
           (type(value[0]) is int) and
           (type(value[1]) is int) and
           (value[0] >= 0) and
           (value[1] >= 0)):
            self.__position = value
         else:
            raise TypeError("position must be a tuple of 2 positive integers")
