#!/usr/bin/python3
"""
Module defining CountedIterator, a class that wraps an iterator
and tracks the number of elements iterated over.
"""


class CountedIterator:
    """
    Iterator wrapper that increments a counter on each successful
    iteration step.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable object.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        Return the total number of items iterated so far.
        """
        return self.counter

    def __next__(self):
        """
        Fetch the next item from the iterator and increment the counter.
        """
        item = next(self.iterator)
        self.counter += 1
        return item
