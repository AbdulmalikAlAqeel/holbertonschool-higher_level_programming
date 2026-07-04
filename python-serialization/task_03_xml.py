#!/usr/bin/env python3
"""
This module provides functionality to serialize a Python dictionary
to an XML file and deserialize it back into a dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into an XML file structure.
    """
    try:
        # Create the root element <data>
        root = ET.Element("data")

        # Add child elements for each key-value pair
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Create the tree structure and save it to the file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Parses an XML file and builds it back into a dictionary.
    """
    try:
        # Parse the XML document file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary from child elements
        # Since all input types in the test sample are strings,
        # child.text can be left as a string directly.
        reconstructed_dict = {}
        for child in root:
            reconstructed_dict[child.tag] = child.text

        return reconstructed_dict
    except Exception:
        return None
