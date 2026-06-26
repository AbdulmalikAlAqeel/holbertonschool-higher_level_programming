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



# Project: Python - Abstract Base Classes (ABC)

## Task 1: Shapes, Interfaces, and Duck Typing

### Description
This task demonstrates the power of **Duck Typing** and **Polymorphism** in Python, combined with the structural enforcement of Abstract Base Classes (ABCs). 

An abstract class `Shape` is defined with two abstract methods: `area()` and `perimeter()`. Two concrete subclasses, `Circle` and `Rectangle`, inherit from `Shape` and provide their specific mathematical implementations. Finally, a standalone function `shape_info()` utilizes duck typing to interact with these shapes uniformly without explicitly verifying their class types.

---

### Key Concepts Implemented
* **Duck Typing:** The `shape_info()` function calls `.area()` and `.perimeter()` by relying entirely on the object's behavior rather than its explicit class inheritance or type checks (avoiding `isinstance`).
* **Dynamic Polymorphism:** Handling different geometric shapes through a unified interface cleanly and dynamically.
* **Precise Math Integration:** Utilizing Python's built-in `math` module for accurate circle area and perimeter calculations using $\pi$.

---

### File Structure
* `python-abc/` (Directory)
  * `task_01_duck_typing.py`: Contains the `Shape` ABC, `Circle` and `Rectangle` subclasses, and the standalone `shape_info()` function.
  * `main_01_duck_typing.py`: Test script provided to verify the output and duck typing compliance.

---

### Requirements
* Strictly zero `pycodestyle` style warnings or violations (e.g., adhering to the maximum 79-character line limit).
* Full documentation (Docstrings) for the module, every class, and every method.
* Avoid using type checks like `isinstance` within the `shape_info` helper function.

---

### Usage & Expected Output

To execute the verification script and see duck typing in action, run:

```bash
chmod +x main_01_duck_typing.py
./main_01_duck_typing.py



# Project: Python - Abstract Base Classes (ABC)

## Task 2: Extending the Python List with Notifications

### Description
This task demonstrates how to extend Python's built-in classes to modify or augment their native behavior. By inheriting from the standard `list` class, we create a custom class named `VerboseList`. 

This class retains all standard list functionalities but introduces real-time terminal notifications whenever items are added (via `append` or `extend`) or removed (via `remove` or `pop`), showcasing method overriding and the proper application of the `super()` function.

---

### Key Concepts Implemented
* **Extending Built-in Classes:** Inheriting directly from `list` to subclass core Python data structures.
* **Method Overriding:** Redefining core methods (`append`, `extend`, `remove`, `pop`) to execute custom notification logic alongside original operations.
* **The `super()` Function:** Delegating execution back to the parent class (`list`) to ensure underlying memory management and list operations remain intact.
* **State Management:** Measuring state deltas (e.g., list length before and after an operation) to report precise structural changes.

---

### File Structure
* `python-abc/` (Directory)
  * `task_02_verboselist.py`: Contains the definition of the `VerboseList` class with overridden notification methods.
  * `main_02_verboselist.py`: Test script provided to verify list interactions and console outputs.

---

### Requirements
* Zero `pycodestyle` formatting errors or line-length warnings (lines kept under 79 characters).
* Robust and meaningful documentation (Docstrings) for the module, class, and all overridden methods.
* Preserving standard return values (such as `pop()` returning the removed element).

---

### Usage & Expected Output

To execute the verification script and observe the verbose logging, run:

```bash
chmod +x main_02_verboselist.py
./main_02_verboselist.py



# Project: Python - Abstract Base Classes (ABC)

## Task 3: CountedIterator - Keeping Track of Iteration

### Description
This task explores Python's internal iteration protocols by creating a custom iterator wrapper class named `CountedIterator`. 

Instead of inheriting directly from a standard collection, this class encapsulates an iterator object generated by the built-in `iter()` function. By overriding the `__next__` method, `CountedIterator` dynamically monitors execution state, incrementing a counter upon each successful data fetch while preserving the standard `StopIteration` behavior when the sequence is exhausted.

---

### Key Concepts Implemented
* **The Iteration Protocol:** Working directly with Python's core `__next__` method and `iter()` function mechanisms.
* **Stateful Wrappers / Composition:** Keeping track of internal states (like an iteration counter) on top of an underlying stream of data.
* **Exception Control Flow:** Gracefully allowing the underlying `StopIteration` exception to propagate naturally to terminate loops without corrupting the counter state.

---

### File Structure
* `python-abc/` (Directory)
  * `task_03_countediterator.py`: Contains the `CountedIterator` class definition with state tracking.
  * `main_03_countediterator.py`: Test script provided to verify manual and loop-based iteration.

---

### Requirements
* Zero `pycodestyle` style warnings or line-length errors (all lines structured under 79 characters).
* Clear, concise, and professional documentation (Docstrings) for the module, class, and individual methods.
* Precise tracking ensuring the counter only increments for items successfully fetched.

---

### Usage & Expected Output

To execute the verification script and see the iterator counter in action, run:

```bash
chmod +x main_03_countediterator.py
./main_03_countediterator.py



# Project: Python - Abstract Base Classes (ABC)

## Task 4: The Enigmatic FlyingFish - Exploring Multiple Inheritance

### Description
This task explores the concept of **Multiple Inheritance** in Python, a powerful feature where a subclass can inherit attributes and behaviors from more than one parent class. 

By constructing a `FlyingFish` class that inherits from both a `Fish` class and a `Bird` class, this exercise demonstrates how Python resolves method name conflicts using **Method Resolution Order (MRO)**. It showcases how the order of parent classes specified during definition directly impacts the look-up hierarchy.

---

### Key Concepts Implemented
* **Multiple Inheritance:** Designing a class structure where a child class (`FlyingFish`) simultaneously derives capabilities from multiple independent base classes (`Fish` and `Bird`).
* **Method Overriding:** Customizing inherited behaviors (`swim`, `fly`, `habitat`) specifically for the subclass.
* **Method Resolution Order (MRO):** Understanding the `C3 Linearization` algorithm that Python uses to determine the search order for methods.
* **MRO Introspection:** Utilizing the `.mro()` method and `__mro__` attribute to audit the inheritance chain programmatically.

---

### File Structure
* `python-abc/` (Directory)
  * `task_04_flyingfish.py`: Contains the definitions for `Fish`, `Bird`, and the multi-inherited `FlyingFish` classes.
  * `main_04_flyingfish.py`: Test script provided to instantiate the class and execute the overridden methods.

---

### Requirements
* Full compliance with `pycodestyle` formatting rules (lines strict under 79 characters).
* Complete and descriptive documentation (Docstrings) for all classes and methods.
* Proper ordering of base classes to align with the expected execution behavior.

---

### Usage & Expected Output

To run the verification script and see multiple inheritance in action, execute:

```bash
chmod +x main_04_flyingfish.py
./main_04_flyingfish.py



# Project: Python - Abstract Base Classes (ABC)

## Task 5: The Mystical Dragon - Mastering Mixins

### Description
This task introduces and demonstrates the **Mixin design pattern** in Python. Mixins are small, highly focused classes designed to provide specific, reusable behaviors to other classes through multiple inheritance. 

Unlike traditional parent classes, mixins are not meant to stand alone or be instantiated on their own. By constructing `SwimMixin` and `FlyMixin` and combining them into a `Dragon` class, this exercise showcases how to achieve horizontal code reusability and implement **Composition over Inheritance** without creating deep, rigid, or fragile inheritance hierarchies.

---

### Key Concepts Implemented
* **Mixin Design Pattern:** Building discrete, single-purpose classes that inject distinct capabilities into target classes.
* **Behavior Composition:** Combining multiple independent behavioral components (`SwimMixin` + `FlyMixin`) to dynamically construct a complex class (`Dragon`).
* **Modular Code Reuse:** Designing decoupled capabilities that can be easily plugged into any other unrelated class architectures (e.g., Duck, Airplane) in the future.

---

### File Structure
* `python-abc/` (Directory)
  * `task_05_dragon.py`: Contains the `SwimMixin`, `FlyMixin`, and the composed `Dragon` class definitions.
  * `main_05_dragon.py`: Test script provided to verify the composite capabilities of the dragon instance.

---

### Requirements
* Strict compliance with `pycodestyle` formatting standards (all lines under 79 characters).
* Complete, comprehensive Python Docstrings for all mixin classes, target classes, and individual methods.
* Correct encapsulation ensuring behaviors remain independent and reusable.

---

### Usage & Expected Output

To run the verification script and observe the modular mixin behaviors, execute:

```bash
chmod +x main_05_dragon.py
./main_05_dragon.py
