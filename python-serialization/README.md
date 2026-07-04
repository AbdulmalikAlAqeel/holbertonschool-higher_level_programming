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
