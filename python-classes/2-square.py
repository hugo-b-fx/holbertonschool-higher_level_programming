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
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
