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
```



### 1. Where are you?
* **File:** `1-answer.txt`
* **Question:** How do you get the variable identifier (which is the memory address in the CPython implementation)?
* **Answer:** `id`

#### Explanation
In CPython, the built-in `id()` function returns a unique integer that represents the memory address where the object is stored. This identifier is guaranteed to be unique and constant for the object during its lifetime.

```python
>>> a = [1, 2, 3]
>>> id(a)
140512836294208  # Memory address in RAM
```



### 2. Right count
* **File:** `2-answer.txt`
* **Question:** In `a = 89` and `b = 100`, do `a` and `b` point to the same object?
* **Answer:** `No`

#### Explanation
Since `89` and `100` are distinct integer values, Python allocates two separate objects in memory. Therefore, `a` and `b` hold references to different memory addresses (`id(a) != id(b)`).



