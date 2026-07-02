# Python - Input/Output

This project is part of the Higher-Level Programming curriculum. It covers how to handle files in Python, including reading, writing, moving the cursor, and working with serialization/deserialization using the JSON format.

## Learning Objectives
By the end of this project, you should be able to explain:
* Why Python programming is awesome.
* How to open, read, and write files safely.
* How to read a file line by line or in full.
* The purpose of the `with` statement and automatic resource management.
* What JSON, serialization, and deserialization are.

## Requirements
* **Allowed editors:** `vi`, `vim`, `emacs`
* **OS/Python Version:** Ubuntu 20.04 LTS using `python3` (version 3.8.5)
* **Style Guide:** `pycodestyle` (version 2.7.*)
* All files must end with a new line and be executable.
* All modules, classes, and functions must have proper documentation sentences.

---

## Tasks Summary

### 0. Read file (Mandatory)
* **File:** `0-read_file.py`
* **Prototype:** `def read_file(filename=""):`
* **Description:** A Python function that reads a text file (`UTF-8`) and prints its entire content to standard output (`stdout`). It utilizes the secure `with` statement to guarantee proper file closure without explicit exception handling.

## Usage & Testing
To test the function, you can use a main execution file like this:

```python
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")
