## Files & Tasks

| File | Prototype / Description |
| --- | --- |
| `0-safe_print_list.py` | `def safe_print_list(my_list=[], x=0):`<br>Prints `x` elements of a list on the same line followed by a new line. Safely handles out-of-bounds indices using `try: / except IndexError:` blocks without using the built-in `len()` function. Returns the real number of elements printed. |
| `1-safe_print_integer.py` | `def safe_print_integer(value):`<br>Prints an integer using the strict `"{:d}".format()` specifier followed by a new line. Catches `ValueError` and `TypeError` using explicit exception handling blocks without using `type()`. Returns `True` if successful, otherwise `False`. |
## Setup & Execution

1. **Make the scripts executable:**
   ```bash
   chmod +x *.py
