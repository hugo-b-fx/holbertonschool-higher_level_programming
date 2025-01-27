#!/usr/bin/python3
"""
script defining a square
"""

class Square:
    """
    ddd
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size  < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
