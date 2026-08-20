# Python - Everything is Object

## Description
This project covers the core fundamentals of Python's memory model and object-oriented structure. It explores how Python handles variables, memory references, mutability vs. immutability, and object identity.

## Requirements
* All code interpreted on **Ubuntu 20.04 LTS** using `python3` (version 3.8.5).
* Code formatted according to `pycodestyle` (version 2.7.*).
* `.txt` answer files contain exactly one line with no extra spaces or shebangs, ending with a new line.

---

## Tasks

### 0. Who am I?
* **File:** `0-answer.txt`
* **Question:** What function would you use to print the type of an object?
* **Answer:** `type`

#### Explanation
In Python, every data piece (numbers, strings, lists, functions) is an object. The built-in `type()` function inspects an object and returns its class/type definition.

```python
>>> type(42)
<class 'int'>
>>> type("Holberton")
<class 'str'>
