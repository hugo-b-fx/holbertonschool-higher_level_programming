#!/usr/bin/env python3
"""
The programme will serialize with pickles module
"""
import pickle


class CustomObject:
    """
    Class CustomObject
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("name: {}".format(self.name))
        print("age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as x:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception as x:
            return None
