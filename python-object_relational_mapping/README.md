### 0. Get all states
* **File:** `0-select_states.py`
* **Directory:** `python-object_relational_mapping`
* **Description:** Write a Python script that connects to a MySQL database using `MySQLdb` and lists all `states` from the database `hbtn_0e_0_usa`. Results are sorted in ascending order by `states.id` and printed as tuples.

#### Requirements:
* Takes 3 command-line arguments: `mysql username`, `mysql password`, and `database name`.
* Connects to MySQL server running on `localhost` at port `3306`.
* Code must not execute when imported (`if __name__ == "__main__":`).

#### Script Content:
```python
#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


### 1. Filter states
* **File:** `1-filter_states.py`
* **Directory:** `python-object_relational_mapping`
* **Description:** Write a Python script that lists all `states` with a name starting with an uppercase `N` from the database `hbtn_0e_0_usa`. Uses `MySQLdb` and `LIKE BINARY 'N%'` to enforce case sensitivity. Results are sorted in ascending order by `states.id`.

#### SQL Query / Logic:
```python
cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")


### 2. Filter states by user input
* **File:** `2-my_filter_states.py`
* **Directory:** `python-object_relational_mapping`
* **Description:** Write a Python script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the user input argument. Uses `format()` to build the SQL query and `LIKE BINARY` for exact case matching. Results are sorted in ascending order by `states.id`.

#### SQL Query / Logic:
```python
query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_searched)
cursor.execute(query)


### 3. SQL Injection...
* **File:** `3-my_safe_filter_states.py`
* **Directory:** `python-object_relational_mapping`
* **Description:** Write a Python script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the user input argument. Unlike task 2, this script is fully protected against MySQL Injection attacks by using parameterized queries (`%s`). Results are sorted in ascending order by `states.id`.

#### SQL Query / Logic (Safe from Injection):
```python
cursor.execute(
    "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
    (sys.argv[4],)
)
