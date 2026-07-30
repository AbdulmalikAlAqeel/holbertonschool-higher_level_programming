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


### 4. Cities by states
* **File:** `4-cities_by_state.py`
* **Directory:** `python-object_relational_mapping`
* **Description:** Write a Python script that lists all `cities` from the database `hbtn_0e_4_usa` along with their corresponding `state` name using a single SQL `JOIN` query. Results are sorted in ascending order by `cities.id`.

#### SQL Query / Logic:
```python
cursor.execute(
    "SELECT cities.id, cities.name, states.name "
    "FROM cities "
    "JOIN states ON cities.state_id = states.id "
    "ORDER BY cities.id ASC"
)


### 5. All cities by state
* **File:** `5-filter_cities.py`
* **Directory:** `python-object_relational_mapping`
* **Description:** Write a Python script that takes in the name of a state as an argument and lists all cities of that state from the database `hbtn_0e_4_usa`. Safe from SQL injection using parameterized queries (`%s`). Displays results formatted as comma-separated values on a single line (`City1, City2, ...`).

#### SQL Query / Logic:
```python
cursor.execute(
    "SELECT cities.name "
    "FROM cities "
    "JOIN states ON cities.state_id = states.id "
    "WHERE states.name = %s "
    "ORDER BY cities.id ASC",
    (sys.argv[4],)
)
print(", ".join([row[0] for row in rows]))


### 6. First state model
* **File:** `model_state.py`
* **Directory:** `python-object_relational_mapping`
* **Description:** Write a Python file that contains the class definition of a `State` and an instance `Base = declarative_base()`. Maps to the MySQL table `states` using SQLAlchemy ORM with attributes `id` (Auto-increment, Primary Key) and `name` (String max 128 chars, Not Null).

#### Class Definition / ORM Structure:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class inherits from Base and maps to MySQL table 'states'.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


### 7. All states via SQLAlchemy
* **File:** `7-model_state_fetch_all.py`
* **Directory:** `python-object_relational_mapping`
* **Description:** Write a Python script that lists all `State` objects from the database `hbtn_0e_6_usa` using SQLAlchemy ORM Sessions. Results are sorted in ascending order by `states.id` and formatted as `id: name`.

#### SQLAlchemy Query / Logic:
```python
Session = sessionmaker(bind=engine)
session = Session()

states = session.query(State).order_by(State.id).all()
for state in states:
    print("{}: {}".format(state.id, state.name))

session.close()


### 8. First state
* **File:** `8-model_state_fetch_first.py`
* **Directory:** `python-object_relational_mapping`
* **Description:** Write a Python script that prints the first `State` object from the database `hbtn_0e_6_usa` ordered by `states.id` using SQLAlchemy ORM. Uses `.first()` to query only the first record directly. Displays `Nothing` if the table is empty.

#### SQLAlchemy Query / Logic:
```python
first_state = session.query(State).order_by(State.id).first()

if first_state is None:
    print("Nothing")
else:
    print("{}: {}".format(first_state.id, first_state.name))


### 9. Contains `a`
* **File:** `9-model_state_filter_a.py`
* **Directory:** `python-object_relational_mapping`
* **Description:** Write a Python script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa` using SQLAlchemy ORM. Results are sorted in ascending order by `states.id`.

#### SQLAlchemy Query / Logic:
```python
states = session.query(State).filter(
    State.name.like('%a%')
).order_by(State.id).all()

for state in states:
    print("{}: {}".format(state.id, state.name))
