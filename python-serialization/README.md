### 0. Basic Serialization (Mandatory)
* **File:** `task_00_basic_serialization.py`
* **Prototypes:** * `def serialize_and_save_to_file(data, filename):`
  * `def load_and_deserialize(filename):`
* **Description:** A Python module that introduces core serialization concepts by converting a Python dictionary into a JSON file format and vice versa. It utilizes the standard `json.dump()` function within a secure writing block to guarantee persistence, and `json.load()` to reconstruct the native dictionary framework upon file retrieval.

## Usage & Testing
To evaluate the basic serialization and deserialization flow, you can execute the following main wrapper script:

```python
#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Sample data to be serialized
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Data serialized and saved to 'data.json'.")

# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize('data.json')
print("Deserialized Data:")
print(deserialized_data)



### 1. Pickling Custom Classes (Mandatory)
* **File:** `task_01_pickle.py`
* **Prototypes:** * `def serialize(self, filename):`
  * `@classmethod def deserialize(cls, filename):`
* **Description:** A Python class named `CustomObject` that demonstrates full object state persistence using Python's binary `pickle` protocol. Unlike text-based serializers (like JSON), `pickle` maps live instance variables and structural identities directly onto a binary data stream. The script safely wraps stream modifications within rigorous `try-except` blocks to prevent crash cycles during data ingestion from corrupted, broken, or non-existent files.

## Usage & Testing
To verify the lifecycle of binary object state storage and restoration, you can execute the following main test script:

```python
#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object
obj.serialize("object.pkl")

# Deserialize the object into a new instance
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
if new_obj:
    new_obj.display()



### 2. Converting CSV Data to JSON Format (Mandatory)
* **File:** `task_02_csv.py`
* **Prototype:** `def convert_csv_to_json(csv_filename):`
* **Description:** A Python function designed to transform tabular data from a CSV file into structured, serialized JSON data written to `data.json`. It coordinates file access streams securely using a `csv.DictReader` wrapper to systematically map raw record fields directly into dynamic key-value dictionaries before final serialization. It handles errors (such as non-existent files) gracefully by returning `False`.

## Usage & Testing
To verify tabular serialization, populate a mock `data.csv` dataset and execute the following automation test script:

```python
#!/usr/bin/env python3
from task_02_csv import convert_csv_to_json

csv_file = "data.csv"
if convert_csv_to_json(csv_file):
    print(f"Data from {csv_file} has been converted to data.json")
else:
    print(f"Failed to convert data from {csv_file}")



### 3. Serializing and Deserializing with XML (Mandatory)
* **File:** `task_03_xml.py`
* **Prototypes:** * `def serialize_to_xml(dictionary, filename):`
  * `def deserialize_from_xml(filename):`
* **Description:** A Python module implementing data conversion mechanics to parse flat dictionaries into hierarchical XML document formats and vice-versa. It creates a structural root using `xml.etree.ElementTree.Element`, appends individual child leaves corresponding to the fields, and uses an iterable tree extraction parser to loop back over nodes during dictionary reconstructions.

## Usage & Testing
To confirm serialization and parsing consistency under XML rules, execute the main validation test script below:

```python
#!/usr/bin/env python3
from task_03_xml import serialize_to_xml, deserialize_from_xml

def main():
    sample_dict = {
        'name': 'John',
        'age': '28',
        'city': 'New York'
    }

    xml_file = "data.xml"
    serialize_to_xml(sample_dict, xml_file)
    print(f"Dictionary serialized to {xml_file}")

    deserialized_data = deserialize_from_xml(xml_file)
    print("\nDeserialized Data:")
    print(deserialized_data)

if __name__ == "__main__":
    main()
