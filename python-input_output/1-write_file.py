#!/usr/bin/python3
"""
function to write in txt files
"""


def write_file(filename="", text=""):
    """
    write_file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
