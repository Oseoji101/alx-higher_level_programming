#!/usr/bin/python3
""" creates class Square """


class Square:
    """ Square class"""
    def __init__(self, size=0):
        """set size to private instance variable

        Args:
            size (int): the size of the square
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return self.__size * self.__size
