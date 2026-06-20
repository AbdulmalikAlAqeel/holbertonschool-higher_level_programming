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
| `4-rectangle.py` | [4. Eval is magic](./4-rectangle.py) | A class `Rectangle` that implements a custom internal string representation (`__repr__`) to allow reconstruction via `eval()`. |
| `5-rectangle.py` | [5. Detect instance deletion](./5-rectangle.py) | A class `Rectangle` that implements a destructor method (`__del__`) to print a message when an instance is deleted. |
| `6-rectangle.py` | [6. How many instances](./6-rectangle.py) | A class `Rectangle` that introduces a public class attribute to dynamically track the number of active instances. |
| `7-rectangle.py` | [7. Change representation](./7-rectangle.py) | A class `Rectangle` that introduces a customizable class/instance attribute `print_symbol` for visual drawing. |
| `8-rectangle.py` | [8. Compare rectangles](./8-rectangle.py) | A class `Rectangle` that implements a static method `bigger_or_equal` to compare two rectangle areas. |
| `9-rectangle.py` | [9. A square is a rectangle](./9-rectangle.py) | A class `Rectangle` that implements a class method `square` to instantiate a square safely. |

## Tasks Overview

### 0. Simple rectangle
**File:** `0-rectangle.py`

Write an empty class `Rectangle` that defines a rectangle:
* You are not allowed to import any module.

#### Concepts Covered
* **Class Definition:** Introduction to Object-Oriented Programming (OOP) syntax in Python using the `class` keyword.
* **The pass Statement:** Using `pass` as a syntactic placeholder to define a structurally valid empty class layout.

#### Compilation and Testing
You can test the implementation using the following main file (`0-main.py`):

```python
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)


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
* You are not allowed to import any module.

#### Concepts Covered
* **Encapsulation:** Protecting data attributes by making them private (using double underscores `__`) to prevent direct external modification.
* **Getters and Setters:** Utilizing `@property` and `@attribute.setter` decorators for controlled data retrieval and safe modification.
* **Data Validation:** Introducing type checks (`isinstance()`) and value constraints inside setters to throw `TypeError` and `ValueError` exceptions before assigning invalid states.

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


### 2. Area and Perimeter
**File:** `2-rectangle.py`

Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)
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
* **Public instance method:** `def area(self):` that returns the rectangle area.
* **Public instance method:** `def perimeter(self):` that returns the rectangle perimeter:
  * If `width` or `height` is equal to `0`, perimeter is equal to `0`.
* You are not allowed to import any module.

#### Concepts Covered
* **Public Instance Methods:** Defining class functions that operate on the instance's internal private state (`self.__width` and `self.__height`).
* **Mathematical Operations in OOP:** Implementing geometric logic within an object to dynamically compute properties like Area and Perimeter.
* **Edge Case Handling:** Implementing conditional constraints to return specific default values (e.g., perimeter = 0) when an object state represents a flat or empty shape.

#### Compilation and Testing
You can test the implementation using the following main file (`2-main.py`):

```python
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))


### 3. String representation
**File:** `3-rectangle.py`

Write a class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)
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
* **Public instance method:** `def area(self):` that returns the rectangle area.
* **Public instance method:** `def perimeter(self):` that returns the rectangle perimeter:
  * If `width` or `height` is equal to `0`, perimeter is equal to `0`.
* `print()` and `str()` should print the rectangle with the character `#`:
  * If `width` or `height` is equal to `0`, return an empty string.
* You are not allowed to import any module.

#### Concepts Covered
* **Magic Methods:** Overriding the special method `__str__` to define a customized, user-friendly string representation of an object.
* **String Manipulation & Generation:** Constructing multi-line visual text layouts dynamically using list comprehensions and string joining (`'\n'.join()`).
* **Implicit Invocations:** Understanding how functions like `print()` and `str()` automatically look for and execute the internal `__str__` definition of an instance.

#### Compilation and Testing
You can test the implementation using the following main file (`3-main.py`):

```python
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)


### 4. Eval-able string representation
**File:** `4-rectangle.py`

Write a class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)
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
* **Public instance method:** `def area(self):` that returns the rectangle area.
* **Public instance method:** `def perimeter(self):` that returns the rectangle perimeter:
  * If `width` or `height` is equal to `0`, perimeter is equal to `0`.
* `print()` and `str()` should print the rectangle with the character `#`:
  * If `width` or `height` is equal to `0`, return an empty string.
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
* You are not allowed to import any module.

#### Concepts Covered
* **The __repr__ Method:** Overriding the special method `__repr__` to return an unambiguous, formal string representation of an object primarily targeted at developers and debugging.
* **Object Recreation with eval():** Designing `__repr__` output so that passing its string value into Python's built-in `eval()` function successfully instantiates a fresh, identical copy of the target object.
* **Difference Between str() and repr():** Distinguishing between `str()` (informal, pretty visual representation for end-users) and `repr()` (formal, technical code representation).

#### Compilation and Testing
You can test the implementation using the following main file (`4-main.py`):

```python
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(type(repr(my_rectangle)))
print("--")
print(hex(id(my_rectangle)))
print("--")

# Create a new instance from the repr representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(type(repr(new_rectangle)))
print("--")
print(hex(id(new_rectangle)))
print("--")
print(new_rectangle is my_rectangle)
print(type(new_rectangle) == type(my_rectangle))


### 5. Detect instance deletion
**File:** `5-rectangle.py`

Write a class `Rectangle` that defines a rectangle by: (based on `4-rectangle.py`)
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
* **Public instance method:** `def area(self):` that returns the rectangle area.
* **Public instance method:** `def perimeter(self):` that returns the rectangle perimeter:
  * If `width` or `height` is equal to `0`, perimeter is equal to `0`.
* `print()` and `str()` should print the rectangle with the character `#`:
  * If `width` or `height` is equal to `0`, return an empty string.
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
* Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is deleted.
* You are not allowed to import any module.

#### Concepts Covered
* **Overriding Magic Methods:** Implementing the special method `__del__` (Destructor) to execute custom cleanup hooks during the lifecycle of an object.
* **Garbage Collection Lifecycle:** Understanding how Python's memory management automatically invokes an object's destructor when its reference count drops to zero or when it is explicitly removed using `del`.

#### Compilation and Testing
You can test the implementation using the following main file (`5-main.py`):

```python
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))


### 6. How many instances
**File:** `6-rectangle.py`

Write a class `Rectangle` that defines a rectangle by: (based on `5-rectangle.py`)
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
* **Public class attribute:** `number_of_instances`
  * Initialized to `0`.
  * Incremented during each new instance instantiation.
  * Decremented during each instance deletion.
* **Instantiation with optional width and height:** `def __init__(self, width=0, height=0):`
* **Public instance method:** `def area(self):` that returns the rectangle area.
* **Public instance method:** `def perimeter(self):` that returns the rectangle perimeter:
  * If `width` or `height` is equal to `0`, perimeter is equal to `0`.
* `print()` and `str()` should print the rectangle with the character `#`:
  * If `width` or `height` is equal to `0`, return an empty string.
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
* Print the message `Bye rectangle...` when an instance of `Rectangle` is deleted.
* You are not allowed to import any module.

#### Concepts Covered
* **Class Attributes vs. Instance Attributes:** Understanding state that is shared across all instances of a class rather than being unique to a single object.
* **Global Instance Tracking:** Controlling class-level variables globally from within individual object lifecycle methods (`__init__` and `__del__`).

#### Compilation and Testing
You can test the implementation using the following main file (`6-main.py`):

```python
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))


### 7. Change representation
**File:** `7-rectangle.py`

Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)
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
* **Public class attribute:** `number_of_instances` (Dynamically tracks alive objects).
* **Public class attribute:** `print_symbol`
  * Initialized to `#`.
  * Used as a symbol for string representation.
  * Can be of any data type.
* **Instantiation with optional width and height:** `def __init__(self, width=0, height=0):`
* **Public instance method:** `def area(self):` that returns the rectangle area.
* **Public instance method:** `def perimeter(self):` that returns the rectangle perimeter:
  * If `width` or `height` is equal to `0`, perimeter is equal to `0`.
* `print()` and `str()` should print the rectangle with the character(s) stored in `print_symbol`:
  * If `width` or `height` is equal to `0`, return an empty string.
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
* Print the message `Bye rectangle...` when an instance of `Rectangle` is deleted.
* You are not allowed to import any module.

#### Concepts Covered
* **Class Namespaces vs Instance Namespaces:** Understanding attribute resolution order and how changing a class attribute impacts all instances unless overridden at the individual instance level.
* **Dynamic Type Handling in Special Methods:** Safely casting dynamically typed attributes (`print_symbol`) during string multiplication within `__str__` to support rendering diverse types like lists or strings.

#### Compilation and Testing
You can test the implementation using the following main file (`7-main.py`):

```python
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")

my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")

Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)
print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)
print("--")


### 8. Compare rectangles
**File:** `8-rectangle.py`

Write a class `Rectangle` that defines a rectangle by: (based on `7-rectangle.py`)
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
* **Public class attribute:** `number_of_instances` (Dynamically tracks alive objects).
* **Public class attribute:** `print_symbol` (Used as a symbol for string representation).
* **Instantiation with optional width and height:** `def __init__(self, width=0, height=0):`
* **Public instance method:** `def area(self):` that returns the rectangle area.
* **Public instance method:** `def perimeter(self):` that returns the rectangle perimeter:
  * If `width` or `height` is equal to `0`, perimeter is equal to `0`.
* `print()` and `str()` should print the rectangle with the character(s) stored in `print_symbol`:
  * If `width` or `height` is equal to `0`, return an empty string.
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
* Print the message `Bye rectangle...` when an instance of `Rectangle` is deleted.
* **Static method:** `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area.
  * `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`.
  * `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`.
  * Returns `rect_1` if both have the same area value.
* You are not allowed to import any module.

#### Concepts Covered
* **Static Methods:** Using the `@staticmethod` decorator to define logical utilities that belong to the class namespace but do not require access to instance (`self`) or class (`cls`) state.
* **Instance Type Validation:** Implementing strict object-type checks within custom methods using `isinstance()` to ensure safe interactions between multiple instances.

#### Compilation and Testing
You can test the implementation using the following main file (`8-main.py`):

```python
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

my_rectangle_2.width = 10
my_rectangle_2.height = 5

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


### 9. A square is a rectangle
**File:** `9-rectangle.py`

Write a class `Rectangle` that defines a rectangle by: (based on `8-rectangle.py`)
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
* **Public class attribute:** `number_of_instances` (Dynamically tracks alive objects).
* **Public class attribute:** `print_symbol` (Used as a symbol for string representation).
* **Instantiation with optional width and height:** `def __init__(self, width=0, height=0):`
* **Public instance method:** `def area(self):` that returns the rectangle area.
* **Public instance method:** `def perimeter(self):` that returns the rectangle perimeter:
  * If `width` or `height` is equal to `0`, perimeter is equal to `0`.
* `print()` and `str()` should print the rectangle with the character(s) stored in `print_symbol`:
  * If `width` or `height` is equal to `0`, return an empty string.
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`.
* Print the message `Bye rectangle...` when an instance of `Rectangle` is deleted.
* **Static method:** `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area.
* **Class method:** `def square(cls, size=0):` that returns a new `Rectangle` instance with `width == height == size`.
* You are not allowed to import any module.

#### Concepts Covered
* **Class Methods:** Using the `@classmethod` decorator to build custom factory methods that instantiate class instances dynamically via `cls`.
* **Object Creational Patterns:** Utilizing existing constructors inside class-level interfaces to specialize object layouts (e.g., transforming a general Rectangle blueprint into a specialized Square).

#### Compilation and Testing
You can test the implementation using the following main file (`9-main.py`):

```python
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
