#!/usr/bin/python3
"""
geometry
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    shape
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    circle
    """
    def __init__(self, radius):
        self.__radius = abs(radius)

    def area(self):
        return (self.__radius ** 2) * math.pi

    def perimeter(self):
        return self.__radius * math.pi * 2


class Rectangle(Shape):
    """
    rectangle
    """
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return (self.__height * 2) + (self.__width * 2)


def shape_info(Shape):
    """
    shape infos
    """
    print("Area: {}".format(Shape.area()))
    print("Perimeter: {}".format(Shape.perimeter()))
