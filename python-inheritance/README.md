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



# 0x0A. Python - Inheritance - Task 5

This directory contains the implementation for Task 5 of the Python Inheritance project. It establishes the foundational empty class `BaseGeometry` which will be expanded in subsequent tasks.

## Requirements

* **Operating System:** Ubuntu 20.04 LTS
* **Language:** Python 3.8.5
* **Style Guide:** `pycodestyle` version 2.7.*
* **Executables:** All scripts must be executable and end with a new line.

---

## Tasks

### 5. Geometry module (Mandatory)
An empty Python class `BaseGeometry` that serves as the base for future geometry structures.

* **File:** `5-base_geometry.py`
* **Prototype:** `class BaseGeometry:`
* **Constraints:** No modules can be imported.

---

## Code Example

```python
#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))



# 0x0A. Python - Inheritance - Task 6

This directory contains the implementation for Task 6 of the Python Inheritance project. It improves the `BaseGeometry` class by adding a placeholder method for area calculations that enforces overriding in subclasses.

## Requirements

* **Operating System:** Ubuntu 20.04 LTS
* **Language:** Python 3.8.5
* **Style Guide:** `pycodestyle` version 2.7.*
* **Executables:** All scripts must be executable and end with a new line.

---

## Tasks

### 6. Improve Geometry (Mandatory)
A Python class `BaseGeometry` with a public instance method `def area(self):` that raises an `Exception` with the message `area() is not implemented`.

* **File:** `6-base_geometry.py`
* **Prototype:** `def area(self):`
* **Constraints:** No modules can be imported.

---

## Code Example

```python
#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()
try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))



Markdown
# 0x0A. Python - Inheritance - Task 7

This directory contains the implementation for Task 7 of the Python Inheritance project. It enhances the `BaseGeometry` class by introducing a robust integer validation method.

## Requirements

* **Operating System:** Ubuntu 20.04 LTS
* **Language:** Python 3.8.5
* **Style Guide:** `pycodestyle` version 2.7.*
* **Executables:** All scripts must be executable and end with a new line.

---

## Tasks

### 7. Integer validator (Mandatory)
An improved Python class `BaseGeometry` featuring:
* `def area(self):` raises an `Exception`.
* `def integer_validator(self, name, value):` validates the input value.
  * Raises `TypeError` if `value` is not an integer.
  * Raises `ValueError` if `value` is less than or equal to 0.

* **File:** `7-base_geometry.py`
* **Constraints:** No modules can be imported.

---

## Code Example

```python
#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))



# Project: Python - Inheritance

## Task 8: Rectangle

### Description
In this task, a class `Rectangle` is implemented that inherits from the previously created `BaseGeometry` class (`7-base_geometry.py`). This project focuses on implementing object-oriented programming (OOP) principles in Python, specifically inheritance, private instance attributes, and method reuse for input validation.

---

### Requirements
* **Inheritance:** Must inherit from `BaseGeometry`.
* **Instantiation:** `def __init__(self, width, height):`
* **Attributes:** `width` and `height` must be private instance attributes (`__width` and `__height`).
* **Encapsulation:** No getter or setter methods are allowed.
* **Validation:** Both `width` and `height` must be validated as positive integers using the inherited `integer_validator` method.
* **Style:** Code complies with `pycodestyle` guidelines.

---

### File Structure
* `7-base_geometry.py`: Contains the parent class `BaseGeometry` with the validation logic.
* `8-rectangle.py`: Contains the `Rectangle` class definition.
* `8-main.py`: Test file provided by the school to verify compliance.

---

### Class Diagram Overview

```text
  BaseGeometry
       ▲
       │  (Inheritance)
   Rectangle
     ├── __width  (Private, Validated Integer)
     └── __height (Private, Validated Integer)



# Project: Python - Inheritance

## Task 9: Full Rectangle

### Description
This task extends the implementation of the `Rectangle` class from the previous task. It incorporates the complete geometric functionality by defining the actual area calculation and customizing the string representation of the object when printed or cast to a string.

---

### New Features implemented
* **Area Calculation:** Overrides and fully implements the `area()` method from the parent class to compute and return the rectangle's area ($width \times height$).
* **Custom String Representation:** Implements the `__str__` magic method to return a formatted description of the rectangle: `[Rectangle] <width>/<height>`.

---

### Requirements
* Must inherit from `BaseGeometry`.
* Instantiation with private attributes: `__width` and `__height`.
* Proper input validation using `integer_validator`.
* Code strictly complies with `pycodestyle` formatting rules.

---

### File Structure
* `7-base_geometry.py`: Parent class with data validation logic.
* `9-rectangle.py`: Full `Rectangle` class implementation with `area()` and `__str__`.
* `9-main.py`: Test script provided to verify the output.

---

### Usage & Example

To verify the implementation, execute the test file:

```bash
./9-main.py



# Project: Python - Inheritance

## Task 10: Square #1

### Description
This task introduces the concept of multi-level inheritance and polymorphism by implementing a `Square` class that inherits directly from the `Rectangle` class (`9-rectangle.py`), which in turn inherits from `BaseGeometry`. Since a square is a specific case of a rectangle where the width equals the height, this implementation leverages code reuse via the `super()` function.

---

### Key Implementations
* **Multi-level Inheritance:** `Square` $\rightarrow$ `Rectangle` $\rightarrow$ `BaseGeometry`.
* **Code Reuse:** Instead of rewriting validation or area computation, the `Square` class calls `super().__init__(size, size)`. This automatically handles both the `integer_validator` and sets up the dimensions for the inherited `area()` and `__str__` methods.
* **Attributes:** `size` is kept as a private instance attribute (`__size`).

---

### Requirements
* Must inherit from `Rectangle`.
* Instantiation: `def __init__(self, size):`
* `size` must be a private positive integer validated by `integer_validator`.
* No explicit getter or setter methods.

---

### File Structure
* `7-base_geometry.py`: Base class containing validation logic.
* `9-rectangle.py`: Intermediate class implementing `area()` and `__str__`.
* `10-square.py`: `Square` class definition inheriting from `Rectangle`.
* `10-main.py`: Test script provided to verify the implementation.

---

### Class Diagram Hierarchy

```text
  BaseGeometry
       ▲
       │
   Rectangle
       ▲
       │  (Inheritance)
     Square
       └── __size  (Private, Validated Integer)
