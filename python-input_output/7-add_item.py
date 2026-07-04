#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and saves them to a JSON file named 'add_item.json'.
"""
import sys
import os

# Import the required functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Check if the file already exists to load its content,
# otherwise initialize an empty list
if os.path.exists(filename):
    items_list = load_from_json_file(filename)
else:
    items_list = []

# Append all command-line arguments (excluding the script name) to the list
items_list.extend(sys.argv[1:])

# Save the updated list back into the JSON file
save_to_json_file(items_list, filename)
