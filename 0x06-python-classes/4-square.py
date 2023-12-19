#!/usr/bin/python3
"""creates class square"""


class Square:
    """class that creates a square"""

    def __init__(self, size=0):
        """initialises square class
        Args: size - size of square created
        """

        if not isinstance(size, int):

            raise TypeError("size must be an integer")
        elif size < 0:

            raise ValueError("size must be >=0")

        self.__size = size

        def area(self):
            """calculate area of the square
            Returns: the square of the size
            """
            return (self.__size * self.__size)

        @property
        def size(self):
            """getter that get the size of variable"""

            return(self.__size)

        @size.setter
        def size(self, value):
            """set the size to the value
            Args: value - the value to reset
            """

            if not isinstance(size, int):
                raise TypeError("size must be an integer")

            elif size < 0:
                raise ValueError("size must be >=0")
            self.__size = size
