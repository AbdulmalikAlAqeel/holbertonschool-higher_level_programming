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
## Setup & Execution

1. **Make the script executable:**
   ```bash
   chmod +x 0-main.py 0-print_list_integer.py
