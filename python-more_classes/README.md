# 0x08. Python - More Classes and Objects

## Description
This repository contains the first task of the **0x08. Python - More Classes and Objects** project at Holberton School. The goal of this project is to dive deeper into Object-Oriented Programming (OOP) in Python 3, moving beyond basic class definitions to understand data encapsulation, attributes, and methods.

---

## Requirements

### General
* **Allowed editors:** `vi`, `vim`, `emacs`
* **Environment:** All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.8.5).
* **File Standards:** * All files must end with a new line.
  * The first line of all files must be exactly `#!/usr/bin/python3`.
  * All files must be executable (`chmod +x`).
* **Coding Style:** Your code must adhere to the `pycodestyle` (version 2.7.*) style guide.
* **Documentation:** All modules and classes must have a proper, clear documentation string (docstring).

---

## Tasks

### 0. Simple rectangle
**File:** `0-rectangle.py`

Write an empty class `Rectangle` that defines a rectangle:
* You are not allowed to import any module.

#### Concept Covered
* Creating a minimal class definition in Python.
* Understanding how Python instantiates empty objects and initializes their `__dict__` attribute.

#### Compilation and Testing
You can test the implementation using the following main file (`0-main.py`):

```python
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
