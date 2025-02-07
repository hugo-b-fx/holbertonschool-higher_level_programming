#!/usr/bin/env python3
"""
countediterator
"""


class CountedIterator:
    """
    class
    """
    def __init__(self, item):
        self.iterator = iter(item)
        self.__count = 0

    def __next__(self):
        item = next(self.iterator)
        self.__count += 1
        return item

    def get_count(self):
        return self.__count
