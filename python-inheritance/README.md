# 0x0A. Python - Inheritance - Task 0

This directory contains the implementation of Task 0 for the Python Inheritance project.

## Requirements

* **Operating System:** Ubuntu 20.04 LTS
* **Language:** Python 3.8.5
* **Style Guide:** `pycodestyle` version 2.7.*
* **Executables:** All scripts must be executable and end with a new line.

---

## Tasks

### 0. Lookup (Mandatory)
A Python function that returns the list of available attributes and methods of an object.

* **File:** `0-lookup.py`
* **Prototype:** `def lookup(obj):`
* **Returns:** A list object.
* **Constraints:** No modules can be imported.

---

## Example Usage

```bash
$ cat 0-main.py
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

print(lookup(MyClass1))

$ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
