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



### 3. Right count =
* **File:** `3-answer.txt`
* **Question:** In `a = 89` and `b = 89`, do `a` and `b` point to the same object?
* **Answer:** `Yes`

#### Explanation
CPython pre-allocates and caches small integers in the range `-5` to `256`. Since `89` falls within this range, both `a` and `b` reference the exact same memory object (`a is b` returns `True`).



### 4. Right count =
* **File:** `4-answer.txt`
* **Question:** In `a = 89` and `b = a`, do `a` and `b` point to the same object?
* **Answer:** `Yes`

#### Explanation
Assigning one variable to another (`b = a`) copies the object reference, not the object itself (aliasing). Therefore, both variables point to the exact same memory address (`a is b` returns `True`).



### 5. Right count =+
* **File:** `5-answer.txt`
* **Question:** In `a = 89` and `b = a + 1`, do `a` and `b` point to the same object?
* **Answer:** `No`

#### Explanation
Integers are immutable. Evaluating `a + 1` produces a new integer object (`90`). Since `a` references `89` and `b` references `90`, they point to two distinct memory objects (`a is b` returns `False`).



### 6. Is equal
* **File:** `6-answer.txt`
* **Question:** What do `s1 = "Best School"`, `s2 = s1`, and `print(s1 == s2)` print?
* **Answer:** `True`

#### Explanation
The `==` operator compares values rather than memory identities. Since both `s1` and `s2` contain the exact same string (`"Best School"`), `s1 == s2` evaluates to `True`.



