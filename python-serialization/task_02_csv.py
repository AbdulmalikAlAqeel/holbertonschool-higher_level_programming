#!/usr/bin/env python3
"""
This module provides functionality to read data from a CSV file
and convert it to a structured JSON file format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file, parses rows into dictionaries, and dumps
    the entire dataset collection into 'data.json'.
    Returns True if successful, and False if an exception occurs.
    """
    try:
        # Open and read the CSV file
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # Parse CSV rows into dictionaries using the header row
            csv_reader = csv.DictReader(csv_file)
            data_list = [row for row in csv_reader]

        # Write the serialized JSON list to data.json
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, OSError, csv.Error):
        return False
