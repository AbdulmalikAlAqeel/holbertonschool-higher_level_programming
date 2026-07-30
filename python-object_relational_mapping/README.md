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
