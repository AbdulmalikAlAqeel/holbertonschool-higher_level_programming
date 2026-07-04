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



### 1. Write to a file (Mandatory)
* **File:** `1-write_file.py`
* **Prototype:** `def write_file(filename="", text=""):`
* **Description:** A Python function that writes a string to a text file using `UTF-8` encoding. It automatically handles file creation if it does not exist, or overwrites its content if it already exists. The function utilizes the `with` statement for clean-up and returns the total number of characters successfully written.

## Usage & Testing
To test the file-writing function, you can create a test runner script (`1-main.py`):

```python
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)



### 2. Append to a file (Mandatory)
* **File:** `2-append_write.py`
* **Prototype:** `def append_write(filename="", text=""):`
* **Description:** A Python function that appends a string to the end of a text file using `UTF-8` encoding. If the target file does not exist, it automatically creates it. It relies on the `with` statement for efficient stream handling and returns the exact number of characters appended.

## Usage & Testing
To test the appending capability, use the provided main execution script (`2-main.py`):

```python
#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)



### 3. To JSON string (Mandatory)
* **File:** `3-to_json_string.py`
* **Prototype:** `def to_json_string(my_obj):`
* **Description:** A Python function that returns the JSON string representation of an object (Serialization). It utilizes the standard `json.dumps()` method. Exception handling for non-serializable objects is not managed within the function, allowing standard Python exceptions to propagate naturally.

## Usage & Testing
To verify the JSON serialization, you can execute the provided script (`3-main.py`):

```python
#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))



### 4. From JSON string to Object (Mandatory)
* **File:** `4-from_json_string.py`
* **Prototype:** `def from_json_string(my_str):`
* **Description:** A Python function that deserializes a JSON string back into its corresponding Python data structure (e.g., `list`, `dict`). It utilizes the standard `json.loads()` method. It assumes the input string is valid JSON, so internal exception management is omitted.

## Usage & Testing
To verify the JSON deserialization process, you can execute the provided script (`4-main.py`):

```python
#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))



### 5. Save Object to a file (Mandatory)
* **File:** `5-save_to_json_file.py`
* **Prototype:** `def save_to_json_file(my_obj, filename):`
* **Description:** A Python function that serializes a Python object into JSON format and writes it directly into a text file. It utilizes the standard `json.dump()` method inside a safe `with` statement block. It does not manage exceptions for non-serializable objects internally.

## Usage & Testing
To verify saving an object directly to a JSON file, you can execute the provided script (`5-main.py`):

```python
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)



### 6. Create object from a JSON file (Mandatory)
* **File:** `6-load_from_json_file.py`
* **Prototype:** `def load_from_json_file(filename):`
* **Description:** A Python function that deserializes JSON data from an external text file back into its native Python object form. It relies on the standard `json.load()` function enclosed within a safe `with` block to ensure stream resources are cleared properly upon reading.

## Usage & Testing
To verify loading and reconstructing objects from a JSON file, you can run the provided script (`6-main.py`):

```python
#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))



### 7. Load, add, save (Mandatory)
* **File:** `7-add_item.py`
* **Dependencies:** `5-save_to_json_file.py`, `6-load_from_json_file.py`
* **Description:** A Python script that captures all command-line arguments passed via the terminal, appends them to a continuous Python list, and dynamically serializes the list into a JSON file named `add_item.json`. It intelligently leverages previously created local modules to check for an existing file, load its current state, expand the collection, and safely write back the updated data.

## Usage & Testing
To verify loading, appending, and saving arguments using the script, you can run it directly from your terminal as follows:

```bash
# Verify the file does not exist initially
guillaume@ubuntu:~/$ cat add_item.json
cat: add_item.json: No such file or directory

# Run with no arguments (initializes an empty list in the JSON file)
guillaume@ubuntu:~/$ ./7-add_item.py
guillaume@ubuntu:~/$ cat add_item.json ; echo ""
[]

# Run with new arguments
guillaume@ubuntu:~/$ ./7-add_item.py Best School
guillaume@ubuntu:~/$ cat add_item.json ; echo ""
["Best", "School"]

# Run again to append additional arguments to the existing list
guillaume@ubuntu:~/$ ./7-add_item.py 89 Python C
guillaume@ubuntu:~/$ cat add_item.json ; echo ""
["Best", "School", "89", "Python", "C"]



### 8. Class to JSON (Mandatory)
* **File:** `8-class_to_json.py`
* **Prototype:** `def class_to_json(obj):`
* **Description:** A Python function that extracts the dictionary description of an object's attributes for JSON serialization. It returns a dictionary representation containing simple serializable data structures (lists, dictionaries, strings, integers, and booleans) by retrieving the object's internal `__dict__` attribute without importing any external modules.

## Usage & Testing
To verify the extraction of the dictionary description from a class instance, you can use the provided main execution files:

### Testing with Public Attributes (`8-main.py`)
```python
#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)



### 8. Class to JSON (Mandatory)
* **File:** `8-class_to_json.py`
* **Prototype:** `def class_to_json(obj):`
* **Description:** A Python function that returns the dictionary description with a simple data structure (list, dictionary, string, integer, and boolean) for JSON serialization of an object. It extracts the structural data of an object instance directly by interfacing with its underlying `__dict__` attribute, mapping attribute keys to values without relying on external module imports.

## Usage & Testing
To verify the extraction of the dictionary description from a class instance, you can run the provided main execution scripts:

### Standard Instance Attributes (`8-main.py`)
```python
#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)
