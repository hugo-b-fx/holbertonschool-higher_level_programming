#!/usr/bin/python3
"""
script defining a square
"""


class Square:
    """
    ddd
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if not self.size:
            print()
        else:
            for row in range(self.size):
                for column in range(self.size):
                    print("#", end="")
                print()
