#!/usr/bin/python3
"""
appends string at the end
"""


def append_write(filename="", text=""):
    """
    append_file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
