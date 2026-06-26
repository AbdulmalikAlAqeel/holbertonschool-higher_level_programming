#!/usr/bin/python3
"""This module defines an abstract class Animal and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Base Class representing a generic animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by all subclasses."""
        pass


class Dog(Animal):
    """Subclass representing a Dog."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Subclass representing a cat."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
