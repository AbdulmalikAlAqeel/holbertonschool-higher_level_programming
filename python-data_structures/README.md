## Files & Tasks

| File | Prototype / Description |
| --- | --- |
| `0-print_list_integer.py` | `def print_list_integer(my_list=[]):`<br>Prints all integers of a list, one integer per line, using string formatting (`"{:d}".format()`). |
| `1-element_at.py` | `def element_at(my_list, idx):`<br>Retrieves an element from a list at a specific index like in C. Returns `None` if `idx` is negative or out of range. |
| `2-replace_in_list.py` | `def replace_in_list(my_list, idx, element):`<br>Replaces an element of a list at a specific position. Returns the original list if `idx` is negative or out of range. |
| `3-print_reversed_list_integer.py` | `def print_reversed_list_integer(my_list=[]):`<br>Prints all integers of a list in reverse order, one integer per line, using string formatting (`"{:d}".format()`). |
| `4-new_in_list.py` | `def new_in_list(my_list, idx, element):`<br>Replaces an element in a list at a specific position without modifying the original list. Returns a copy if `idx` is negative or out of range. |
| `5-no_c.py` | `def no_c(my_string):`<br>Removes all characters `c` and `C` from a string without using `str.replace()`. |
| `6-print_matrix_integer.py` | `def print_matrix_integer(matrix=[[]]):`<br>Prints a matrix of integers using `str.format()`, handling row alignment and skipping trailing whitespaces. |
| `7-add_tuple.py` | `def add_tuple(tuple_a=(), tuple_b=()):`<br>Adds 2 tuples based on their first two elements. Missing elements are safely padded with `0`, and extra elements are ignored. |
| `8-multiple_returns.py` | `def multiple_returns(sentence):`<br>Returns a tuple with the length of a string and its first character. If the string is empty, the first character returns `None`. |
| `9-max_integer.py` | `def max_integer(my_list=[]):`<br>Finds the biggest integer of a list without using the built-in `max()` function. Returns `None` if the list is empty. |
| `10-divisible_by_2.py` | `def divisible_by_2(my_list=[]):`<br>Finds all multiples of 2 in a list. Returns a new list of the same size containing `True` or `False`. |
| `11-delete_at.py` | `def delete_at(my_list=[], idx=0):`<br>Deletes the item at a specific position in a list without using `pop()`. Returns the same list if `idx` is negative or out of range. |
| `12-switch.py` | Source code completed to switch the values of variables `a` and `b` in-place using Pythonic tuple unpacking. The file is strictly 5 lines long. |
## Setup & Execution

1. **Make the script executable:**
   ```bash
   chmod +x 0-main.py 0-print_list_integer.py
