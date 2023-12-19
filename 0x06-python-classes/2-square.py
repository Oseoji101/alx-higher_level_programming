#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """class that creates a square"""

    def __init__(self, size=0):
        """initialises square class
        Args: size- size of square created
        """

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        elif size < 0:

            raise ValueError("size must be >=0")

        self.__size = size
