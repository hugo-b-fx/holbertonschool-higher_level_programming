#!/usr/bin/python3
"""
ddd
"""


class Square:
    """
    empty
    """

    def __init__(self, size=0):
        """
        ddd
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
