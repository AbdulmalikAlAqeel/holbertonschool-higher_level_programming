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




# 0x0A. Python - Inheritance - Task 1

This directory contains the implementation and test cases for Task 1 of the Python Inheritance project. It demonstrates how to inherit from Python's built-in `list` class and extend its functionality by adding a custom method.

## Requirements

* **Operating System:** Ubuntu 20.04 LTS
* **Language:** Python 3.8.5
* **Style Guide:** `pycodestyle` version 2.7.*
* **Executables:** All scripts must be executable and end with a new line.
* **Testing:** Test cases must be text-based (`.txt`) and placed inside the `tests` directory.

---

## Tasks

### 1. My list (Mandatory)
A Python class `MyList` that inherits from the built-in `list` class.

* **File:** `1-my_list.py`
* **Test File:** `tests/1-my_list.txt`
* **Public Instance Method:** `def print_sorted(self):`
    * Prints the elements of the list in ascending sorted order.
    * Assumes all elements in the list are integers.
    * Does **not** modify the original order of the list.
* **Constraints:** No modules can be imported.

---

## Code Example

```python
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)

print(my_list)
my_list.print_sorted()
print(my_list)



# 0x0A. Python - Inheritance - Task 2

This directory contains the implementation for Task 2 of the Python Inheritance project. It focuses on precise type checking in Python without considering class inheritance.

## Requirements

* **Operating System:** Ubuntu 20.04 LTS
* **Language:** Python 3.8.5
* **Style Guide:** `pycodestyle` version 2.7.*
* **Executables:** All scripts must be executable and end with a new line.

---

## Tasks

### 2. Exact same object (Mandatory)
A Python function that checks if an object is exactly an instance of the specified class.

* **File:** `2-is_same_class.py`
* **Prototype:** `def is_same_class(obj, a_class):`
* **Returns:** `True` if the object is exactly an instance of the specified class; otherwise `False`.
* **Constraints:** No modules can be imported.

---

## Code Example

```python
#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))



# 0x0A. Python - Inheritance - Task 3

This directory contains the implementation for Task 3 of the Python Inheritance project. It focuses on checking if an object is an instance of a class, or an instance of a subclass that inherited from the specified class.

## Requirements

* **Operating System:** Ubuntu 20.04 LTS
* **Language:** Python 3.8.5
* **Style Guide:** `pycodestyle` version 2.7.*
* **Executables:** All scripts must be executable and end with a new line.

---

## Tasks

### 3. Same class or inherit from (Mandatory)
A Python function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

* **File:** `3-is_kind_of_class.py`
* **Prototype:** `def is_kind_of_class(obj, a_class):`
* **Constraints:** No modules can be imported.

---

## Code Example

```python
#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))



# 0x0A. Python - Inheritance - Task 4

This directory contains the implementation for Task 4 of the Python Inheritance project. It focuses on verifying if an object is an instance of a class that inherited (directly or indirectly) from a specified class, excluding direct instantiation.

## Requirements

* **Operating System:** Ubuntu 20.04 LTS
* **Language:** Python 3.8.5
* **Style Guide:** `pycodestyle` version 2.7.*
* **Executables:** All scripts must be executable and end with a new line.

---

## Tasks

### 4. Only sub class of (Mandatory)
A Python function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.

* **File:** `4-inherits_from.py`
* **Prototype:** `def inherits_from(obj, a_class):`
* **Constraints:** No modules can be imported.

---

## Code Example

```python
#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
