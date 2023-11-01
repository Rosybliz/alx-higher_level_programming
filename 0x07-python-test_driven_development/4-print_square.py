#!/usr/bin/python3

def print_square(size):
    """This method prints a square with the # character

        Args:
            size(int): the size if the sides of the square- all sides equal
        """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
