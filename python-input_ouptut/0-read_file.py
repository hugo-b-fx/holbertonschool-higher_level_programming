#!/usr/bin/python3
"""
function to read txt files
"""


def read_file(filename=""):
    """
    read_file
    """
    with open(filename, encoding="utf-8") as file:
        readfile = file.read()
        print(readfile, end="")
        file.close()
