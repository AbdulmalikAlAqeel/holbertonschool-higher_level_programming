# Project: Python - Abstract Base Classes (ABC)

## Task 0: Abstract Animal Class and its Subclasses

### Description
This task introduces the concept of **Abstract Base Classes (ABCs)** in Python using the native `abc` module. Abstract classes act as blueprints for other classes, allowing you to define a common interface and enforce strict implementation rules upon any derived subclasses. 

In this exercise, an abstract class `Animal` is created with a mandatory abstract method `sound()`. Two subclasses, `Dog` and `Cat`, inherit from `Animal` and provide their specific concrete implementations of the `sound()` method.

---

### Key Concepts Implemented
* **Abstract Class Construction:** Inheriting from `abc.ABC` to mark the class as abstract and prevent direct instantiation.
* **Abstract Methods:** Utilizing the `@abstractmethod` decorator to force derived subclasses to implement specific behaviors.
* **Interface Enforcements:** Demonstrating how Python raises a `TypeError` when trying to instantiate an incomplete or abstract class directly.

---

### File Structure
* `python-abc/` (Directory)
  * `task_00_abc.py`: Contains the definition of the abstract class `Animal` and its subclasses `Dog` and `Cat`.
  * `main_00_abc.py`: Test script provided to verify instantiation blocks and method responses.

---

### Requirements
* Code must strictly comply with `pycodestyle` formatting guidelines.
* Every module, class, and method must have comprehensive documentation (Docstrings).
* The abstract base class cannot be instantiated directly.

---

### Usage & Expected Output

To execute the verification script and see how the enforcement rules apply, run:

```bash
chmod +x main_00_abc.py
./main_00_abc.py
