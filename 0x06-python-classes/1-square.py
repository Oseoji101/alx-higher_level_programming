#!/usr/bin/python3
"""A square that defines a private instance attribute"""


class Square:
    """class to create square"""

    def __init__(self, size):

        """intialises the instance of the class
        Args: size- the size of the square created
        """

        self.__size = size
