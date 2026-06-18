# Python - Classes and Objects

## Description
This project marks the beginning of Object-Oriented Programming (OOP) in Python. The goal is to understand the concept of encapsulating data and functionality into classes and objects, learning about attributes, methods, and data abstraction without using external modules.

## Resource Requirements
* **Operating System:** Ubuntu 20.04 LTS
* **Language:** Python 3.8.5
* **Style Guide:** `pycodestyle` (version 2.7.*)
* **Allowed Editors:** vi, vim, emacs

## General Rules
* All files are executable and must end with a new line.
* The first line of all files must be exactly `#!/usr/bin/python3`.
* All modules, classes, and methods must have a meaningful documentation string (Docstring) explaining their purpose.

## Tasks Overview

| Task File | Description |
| :--- | :--- |
| [0-square.py](./0-square.py) | An empty class `Square` that defines a square. Created to understand the baseline structure of a Python class and its `__dict__` attribute. |
| [1-square.py](./1-square.py) | A class `Square` that defines a square by a private instance attribute `size`. Instantiation with size without type/value verification to understand Data Encapsulation and Name Mangling. |
| [2-square.py](./2-square.py) | A class `Square` that defines a square by a private instance attribute `size` with strict data validation. Handles default size values, type checking (`int`), and value constraints (`>= 0`). |
| [3-square.py](./3-square.py) | A class `Square` that defines a square by a private instance attribute `size` with validation, and includes a public instance method `area()` to compute and return the current square's area. |
## Environment & Testing Verification
To check the code formatting and style compliance, run:
```bash
pycodestyle 0-square.py 1-square.py 2-square.py 3-square.py



