## Files & Tasks

| File | Prototype / Description |
| --- | --- |
| `0-safe_print_list.py` | `def safe_print_list(my_list=[], x=0):`<br>Prints `x` elements of a list on the same line followed by a new line. Safely handles out-of-bounds indices using `try: / except IndexError:` blocks without using the built-in `len()` function. Returns the real number of elements printed. |
| `1-safe_print_integer.py` | `def safe_print_integer(value):`<br>Prints an integer using the strict `"{:d}".format()` specifier followed by a new line. Catches `ValueError` and `TypeError` using explicit exception handling blocks without using `type()`. Returns `True` if successful, otherwise `False`. |
| `2-safe_print_list_integers.py` | `def safe_print_list_integers(my_list=[], x=0):`<br>Prints the first `x` integers of a list. Silently skips non-integer values using `try: / except (ValueError, TypeError):`. Intentionally allows `IndexError` to propagate if `x` exceeds list bounds. Returns the count of successfully printed integers. |
| `3-safe_print_division.py` | `def safe_print_division(a, b):`<br>Divides two integers and prints the result. Uses the `finally:` block to ensure "Inside result: [value]" is always printed, even if a `ZeroDivisionError` occurs. |
| `4-list_division.py` | `def list_division(my_list_1, my_list_2, list_length):`<br>Divides element by element two lists. Handles multiple exceptions (`TypeError`, `ZeroDivisionError`, `IndexError`) and uses `finally:` to ensure a new list of length `list_length` is returned. |
## Setup & Execution

1. **Make the scripts executable:**
   ```bash
   chmod +x *.py
