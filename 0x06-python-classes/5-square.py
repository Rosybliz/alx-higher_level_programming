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
            return self.___size

        @size.setter
        def size(self, value):
            """Sets the size of the square"""
            if type(value) != int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
                else:
                self.__size = value

        def my_print(self):
            """Prints the square"""
            if self.size > 0:
                for i in range(0, self.size):
                    for k in range(0, self.size):
                        print("#",end="")
                    print()
            else:
                print()
