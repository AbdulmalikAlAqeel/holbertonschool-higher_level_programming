#!/usr/bin/python3
"""
Module that defines the VerboseList class, extending the built-in list
to provide notifications on modifications.
"""


class VerboseList(list):
    """
    A custom list class that prints a notification message whenever
    items are added or removed.
    """

    def append(self, item):
        """
        Add an item to the end of the list and print a notification.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable
        and print a notification with the number of items added.
        """
        initial_length = len(self)
        super().extend(iterable)
        items_added = len(self) - initial_length
        print("Extended the list with [{}] items.".format(items_added))

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list
        and print a notification before doing so.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return the item at the given index (default last item),
        printing a notification before doing so.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
