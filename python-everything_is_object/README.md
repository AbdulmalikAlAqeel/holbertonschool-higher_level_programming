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



### 7. Is the same
* **File:** `7-answer.txt`
* **Question:** What do `s1 = "Best"`, `s2 = s1`, and `print(s1 is s2)` print?
* **Answer:** `True`

#### Explanation
The `is` operator checks if two variables refer to the exact same memory location (`id(s1) == id(s2)`). Since `s2` is assigned directly from `s1`, both variables share the same memory reference.



### 8. Is really equal
* **File:** `8-answer.txt`
* **Question:** What do `s1 = "Best School"`, `s2 = "Best School"`, and `print(s1 == s2)` print?
* **Answer:** `True`

#### Explanation
The `==` operator compares the content/values of the two strings. Since both `s1` and `s2` contain `"Best School"`, the expression evaluates to `True`.



### 9. Is really the same
* **File:** `9-answer.txt`
* **Question:** What do `s1 = "Best School"`, `s2 = "Best School"`, and `print(s1 is s2)` print?
* **Answer:** `False`

#### Explanation
In interactive CPython, automatic string interning only applies to ASCII strings that mimic valid Python identifiers (letters, numbers, underscores). Because `"Best School"` contains a space, Python allocates two distinct string objects in memory, making `s1 is s2` evaluate to `False`.



### 10. And with a list, is it equal
* **File:** `10-answer.txt`
* **Question:** What do `l1 = [1, 2, 3]`, `l2 = [1, 2, 3]`, and `print(l1 == l2)` print?
* **Answer:** `True`

#### Explanation
The `==` operator checks for value equality between objects. Although `l1` and `l2` are two separate list objects in memory, their contents are identical, so `l1 == l2` evaluates to `True`.



### 11. And with a list, is it the same
* **File:** `11-answer.txt`
* **Question:** What do `l1 = [1, 2, 3]`, `l2 = [1, 2, 3]`, and `print(l1 is l2)` print?
* **Answer:** `False`

#### Explanation
Lists are mutable objects in Python. Defining two separate list literals creates two distinct objects in memory with different addresses (`id(l1) != id(l2)`), so `l1 is l2` evaluates to `False`.



### 12. And with a list, is it really equal
* **File:** `12-answer.txt`
* **Question:** What do `l1 = [1, 2, 3]`, `l2 = l1`, and `print(l1 == l2)` print?
* **Answer:** `True`

#### Explanation
`l2 = l1` creates an alias, making `l2` reference the exact same object as `l1`. Since both reference identical contents (`[1, 2, 3]`), `l1 == l2` evaluates to `True`.



### 13. And with a list, is it really the same
* **File:** `13-answer.txt`
* **Question:** What do `l1 = [1, 2, 3]`, `l2 = l1`, and `print(l1 is l2)` print?
* **Answer:** `True`

#### Explanation
Assigning `l2 = l1` passes the reference of the existing list to `l2` (aliasing). Since both variables reference the exact same memory address, `l1 is l2` evaluates to `True`.



### 14. List append
* **File:** `14-answer.txt`
* **Question:** What does `l1 = [1, 2, 3]; l2 = l1; l1.append(4); print(l2)` print?
* **Answer:** `[1, 2, 3, 4]`

#### Explanation
Since lists are mutable and `l2` is an alias of `l1`, using `l1.append(4)` modifies the list in-place. Printing `l2` reflects this change because both variables reference the same list object in memory.



### 15. List add
* **File:** `15-answer.txt`
* **Question:** What does `l1 = [1, 2, 3]; l2 = l1; l1 = l1 + [4]; print(l2)` print?
* **Answer:** `[1, 2, 3]`

#### Explanation
The `+` operator creates a **new list object** `[1, 2, 3, 4]` rather than modifying the existing list in-place. Reassigning `l1` points it to the new object, leaving `l2` still pointing to the original unchanged list `[1, 2, 3]`.



### 16. Integer incrementation
* **File:** `16-answer.txt`
* **Question:** What does the script print when `increment(a)` is called on `a = 1`?
* **Answer:** `1`

#### Explanation
Integers are immutable. When `n += 1` executes inside `increment()`, a new integer object `2` is created and bound to local variable `n`. The original variable `a` in the outer scope remains unchanged (`1`).



### 17. List incrementation
* **File:** `17-answer.txt`
* **Question:** What does the script print when calling `increment(l)` with `l = [1, 2, 3]` and `n.append(4)` inside?
* **Answer:** `[1, 2, 3, 4]`

#### Explanation
Lists are mutable objects in Python. When passed to a function, the local parameter `n` points to the same list object as `l`. Calling `n.append(4)` mutates the original list in-place, modifying `l`.



### 18. List assignation
* **File:** `18-answer.txt`
* **Question:** What does the script print when `assign_value(l1, l2)` executes `n = v`?
* **Answer:** `[1, 2, 3]`

#### Explanation
Inside `assign_value`, `n = v` rebinds the local name `n` to point to `v`'s object. Reassigning a local variable does not mutate the original object nor does it affect the global variable `l1`, so `l1` remains `[1, 2, 3]`.



### 19. Copy a list object
* **File:** `19-copy_list.py`
* **Task:** Write a function `def copy_list(a_list):` that returns a copy of a list without importing modules, using a maximum of 3 lines.

```python
#!/usr/bin/python3
def copy_list(a_list):
    return a_list.copy()
```



### 20. Tuple or not?
* **File:** `20-answer.txt`
* **Question:** Is `a = ()` a tuple?
* **Answer:** `Yes`

#### Explanation
Empty parentheses `()` define an empty tuple object in Python (`type(a)` returns `<class 'tuple'>`).
