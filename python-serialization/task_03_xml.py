#!/usr/bin/env python3
"""
The programme will serialize XML file to json file
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    the function serialize_to_xml
    """
    new = ET.Element('data')
    for key, value in dictionary.items():
        chd = ET.SubElement(new, key)
        chd.text = str(value)

    text = ET.ElementTree(new)
    text.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    the function deserialize_from_xml
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    dicty = {}
    for kid in root:
        dicty[kid.tag] = kid.text
    return dicty
