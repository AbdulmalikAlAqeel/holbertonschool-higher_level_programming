# 0x08. Python - More Classes and Objects

## Description
This repository contains the ongoing tasks for the **0x08. Python - More Classes and Objects** project. This project deepens the understanding of Object-Oriented Programming (OOP) in Python 3, specifically focusing on data encapsulation, private attributes, properties, getters, and setters.

---

## Requirements

### General
* **Allowed editors:** `vi`, `vim`, `emacs`
* **Environment:** All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.8.5).
* **File Standards:** * All files must end with a new line.
  * The first line of all files must be exactly `#!/usr/bin/python3`.
  * All files must be executable (`chmod +x`).
* **Coding Style:** Your code must adhere to the `pycodestyle` (version 2.7.*) style guide.
* **Documentation:** All modules, classes, and methods must have a proper, clear documentation string (docstring).

---

## Project Directory Structure

| File | Task | Description |
| --- | --- | --- |
| `0-rectangle.py` | [0. Simple rectangle](./0-rectangle.py) | An empty class `Rectangle` that defines a rectangle. |
| `1-rectangle.py` | [1. Real definition of a rectangle](./1-rectangle.py) | A class `Rectangle` that defines a rectangle with private attributes, validation, and properties. |
| `2-rectangle.py` | [2. Area and Perimeter](./2-rectangle.py) | A class `Rectangle` that defines a rectangle with public methods for area and perimeter calculations. |
| `3-rectangle.py` | [3. String representation](./3-rectangle.py) | A class `Rectangle` that implements a custom string representation (`__str__`) to print the shape using `#`. |
---

## Tasks Overview

### 1. Real definition of a rectangle
**File:** `1-rectangle.py`

Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)
* **Private instance attribute:** `width`
  * Property `def width(self):` to retrieve it.
  * Property setter `def width(self, value):` to set it:
    * `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`.
    * If `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`.
* **Private instance attribute:** `height`
  * Property `def height(self):` to retrieve it.
  * Property setter `def height(self, value):` to set it:
    * `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`.
    * If `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`.
* **Instantiation with optional width and height:** `def __init__(self, width=0, height=0):`

#### Concepts Covered
* Implementing **Data Encapsulation** and **Information Hiding**.
* Using Python `@property` decorators for getters and setters.
* Raising exceptions (`TypeError`, `ValueError`) to validate input dynamically during object creation and modification.

#### Compilation and Testing
You can test the implementation using the following main file (`1-main.py`):

```python
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
