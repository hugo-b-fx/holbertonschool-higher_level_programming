#!/usr/bin/python3
"""
ddd
"""


def inherits_from(obj, a_class):
    """
    inherits_from
    """
    return not type(obj) is a_class and isinstance(obj, a_class)
