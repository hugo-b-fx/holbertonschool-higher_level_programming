#!/usr/bin/python3
'''
Creation of a class: Square
Manipulations(getter, setter, my_print)
'''


class Square:
    '''Classe named Square'''

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__position = position
        if (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        area = self.__size * self.__size
        return area

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):

        if self.__size == 0:
            print()
        else:
            x, y = self.__position
            print(("\n" * y + (" " * x + "#" * self.__size + "\n")
                  * self.__size), end="")
