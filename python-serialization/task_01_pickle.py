#!/usr/bin/env python3
"""
This module demonstrates object serialization and deserialization
using Python's built-in pickle module for custom classes.
"""
import pickle


class CustomObject:
    """
    A custom class representing an object with name, age, and student status.
    Provides methods to serialize and deserialize its instances.
    """

    def __init__(self, name: str, age: int, is_student: bool):
        """Initializes a new instance of CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the attributes of the object in a structured format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serializes the current instance of CustomObject and saves it
        to the specified file in binary mode ('wb').
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance of CustomObject from a binary file ('rb').
        Handles non-existent or corrupted files safely by returning None.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (OSError, pickle.PickleError, EOFError, AttributeError):
            return None
