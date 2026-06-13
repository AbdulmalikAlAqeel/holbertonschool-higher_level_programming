#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list without modifying the original."""
    list_copy = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return list_copy
    list_copy[idx] = element
    return list_copy
