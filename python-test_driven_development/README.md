# Python - Test-driven development

This project focuses on the **Test-Driven Development (TDD)** methodology. The primary goal is to write tests (using `doctest`) before writing the actual code to ensure the implementation meets all requirements and handles edge cases effectively.

## Technologies
* Python 3.8.5
* Ubuntu 20.04 LTS
* `pycodestyle` (version 2.7.*)

## Learning Objectives
* Writing `doctests` for interactive testing.
* Documenting modules, classes, and functions with `Docstrings`.
* Identifying and handling edge cases before implementation.
* Following strict coding style guidelines.

## Files & Tasks

| File | Description |
| --- | --- |
| `0-add_integer.py` | Adds two integers, handling `float` casting and `TypeError` validation. |
| `tests/0-add_integer.txt` | `doctest` file for testing `0-add_integer.py`. |

## Setup & Testing
* **Run tests:**
  ```bash
  python3 -m doctest ./tests/*.txt


| File | Description |
| --- | --- |
| `2-matrix_divided.py` | Divides all elements of a matrix by a number, with proper error handling and rounding. |
| `tests/2-matrix_divided.txt` | `doctest` file for testing `2-matrix_divided.py`. |

## Setup & Testing
* **Run tests:**
  ```bash
  python3 -m doctest ./tests/2-matrix_divided.txt



| File | Description |
| --- | --- |
| `3-say_my_name.py` | Prints a formatted name, handling `string` type validation for both inputs. |
| `tests/3-say_my_name.txt` | `doctest` file for testing `3-say_my_name.py`. |

## Setup & Testing
* **Run tests:**
  ```bash
  python3 -m doctest ./tests/3-say_my_name.txt
