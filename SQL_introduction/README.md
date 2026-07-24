# Project: SQL - Introduction

## Task 0: List databases

### Description
This task focuses on writing an SQL script that retrieves and displays all the existing databases available on the MySQL server. It serves as an introduction to basic SQL syntax, database server interaction, and standard project formatting requirements (such as keywords in uppercase and proper comment structures).

### Learning Objectives
- Understand what a Relational Database Management System (RDBMS) is.
- Learn how to interact with MySQL via the command line interface (CLI).
- Execute SQL scripts using pipe operations.
- Master the fundamental Data Definition / Data Manipulation Language principles.

### Requirements & Standards
- **Environment:** Ubuntu 22.04 LTS running **MySQL 8.0**.
- **Allowed Editors:** `vi`, `vim`, `emacs`.
- **SQL Keywords:** MUST be in **UPPERCASE** (e.g., `SHOW DATABASES;`).
- **Comments:** The file starts with a comment describing the task, and a comment is placed before the SQL query.
- **File Termination:** All files must end with a new line.

---

### File Structure

| File | Description | SQL Command |
| :--- | :--- | :--- |
| `0-list_databases.sql` | SQL script to list all databases on the MySQL server. | `SHOW DATABASES;` |
---

### Code Implementation (`0-list_databases.sql`)

```sql
-- Lists all databases of the MySQL server
SHOW DATABASES;



## Task 1: Create a database

### Description
This task requires writing an SQL script that creates a new database named `hbtn_0c_0` in the MySQL server. The script must be idempotent, meaning if the database already exists, the script should execute without throwing an error or failing.

### Learning Objectives
- Learn how to create databases using Data Definition Language (DDL).
- Use conditional SQL clauses (`IF NOT EXISTS`) to ensure script execution safety.
- Understand script execution without relying on `SELECT` or `SHOW` statements.

### Requirements & Constraints
- **File Name:** `1-create_database_if_missing.sql`
- **Target Database:** `hbtn_0c_0`
- **Forbidden Keywords:** `SELECT`, `SHOW`
- **SQL Keywords:** Must be written in **UPPERCASE** (e.g., `CREATE DATABASE IF NOT EXISTS`).
- **Formatting:** File must start with a descriptive comment and end with a new line.

---

### File Details

| File | Description | Main SQL Command |
| :--- | :--- | :--- |
| `1-create_database_if_missing.sql` | Creates database `hbtn_0c_0` safely if it doesn't already exist. | `CREATE DATABASE IF NOT EXISTS hbtn_0c_0;` |

---

### Script Content (`1-create_database_if_missing.sql`)

```sql
-- Creates the database hbtn_0c_0 in MySQL server if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;



## Task 2: Delete a database

### Description
This task involves writing an SQL script that safely removes/deletes the database named `hbtn_0c_0` from the MySQL server. The script is designed to be idempotent; if the specified database does not exist, the script will complete gracefully without throwing an error.

### Learning Objectives
- Learn how to drop/delete databases using Data Definition Language (DDL).
- Use conditional SQL clauses (`IF EXISTS`) to ensure execution safety and prevent script failures.
- Practice running database management scripts without relying on `SELECT` or `SHOW` statements.

### Requirements & Constraints
- **File Name:** `2-remove_database.sql`
- **Target Database:** `hbtn_0c_0`
- **Forbidden Keywords:** `SELECT`, `SHOW`
- **SQL Keywords:** Must be written in **UPPERCASE** (e.g., `DROP DATABASE IF EXISTS`).
- **Formatting:** File must start with a descriptive comment and end with a new line.

---

### File Details

| File | Description | Main SQL Command |
| :--- | :--- | :--- |
| `2-remove_database.sql` | Safely drops database `hbtn_0c_0` if it exists. | `DROP DATABASE IF EXISTS hbtn_0c_0;` |

---

### Script Content (`2-remove_database.sql`)

```sql
-- Deletes the database hbtn_0c_0 in MySQL server if it exists
DROP DATABASE IF EXISTS hbtn_0c_0;



## Task 3: List tables

### Description
This task involves writing an SQL script to list all the tables contained within a specific database on the MySQL server. The database name is passed dynamically as a command-line argument when executing the `mysql` command.

### Learning Objectives
- Learn how to inspect and discover existing tables in a relational database.
- Practice executing SQL scripts against a specific target database using the MySQL CLI.
- Reinforce strict formatting and syntax compliance for SQL scripts.

### Requirements & Constraints
- **File Name:** `3-list_tables.sql`
- **Database Scope:** Passed as an argument during script execution.
- **SQL Keywords:** Must be in **UPPERCASE** (e.g., `SHOW TABLES;`).
- **Formatting:** File must start with a descriptive comment and end with a new line.

---

### File Details

| File | Description | Main SQL Command |
| :--- | :--- | :--- |
| `3-list_tables.sql` | Lists all tables in the database provided via CLI argument. | `SHOW TABLES;` |

---

### Script Content (`3-list_tables.sql`)

```sql
-- Lists all tables of a database in MySQL server
SHOW TABLES;



## Task 4: First table

### Description
This task involves writing an SQL script that creates a table named `first_table` within a specified database on the MySQL server. The script is designed to be idempotent; if `first_table` already exists, the script executes without raising an error. The target database is passed dynamically as a command-line argument.

### Learning Objectives
- Learn how to define table schemas using Data Definition Language (DDL).
- Understand basic MySQL data types such as `INT` and `VARCHAR`.
- Practice conditional table creation using `IF NOT EXISTS`.

### Requirements & Constraints
- **File Name:** `4-first_table.sql`
- **Table Name:** `first_table`
- **Columns:**
  - `id`: `INT`
  - `name`: `VARCHAR(256)`
- **Forbidden Keywords:** `SELECT`, `SHOW`
- **SQL Keywords:** Must be in **UPPERCASE** (e.g., `CREATE TABLE IF NOT EXISTS`).
- **Formatting:** File must start with a descriptive comment and end with a new line.

---

### File Details

| File | Description | Main SQL Command |
| :--- | :--- | :--- |
| `4-first_table.sql` | Creates `first_table` with `id` and `name` columns if it doesn't already exist. | `CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));` |

---

### Script Content (`4-first_table.sql`)

```sql
-- Creates a table called first_table in the current database in MySQL server
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);



## Task 5: Full description

### Description
This task requires writing an SQL script that prints the full creation schema and description of the table `first_table` from the target database. The output displays the exact `CREATE TABLE` statement generated by MySQL, including data types, default values, storage engine, and character encoding. The database name is passed dynamically as a command-line argument.

### Learning Objectives
- Learn how to inspect full table definitions and schema structures in MySQL.
- Practice using alternative inspection commands when standard options are constrained.
- Understand storage engine and charset specifications assigned during table creation.

### Requirements & Constraints
- **File Name:** `5-full_table.sql`
- **Target Table:** `first_table`
- **Forbidden Keywords:** `DESCRIBE`, `EXPLAIN`
- **SQL Keywords:** Must be in **UPPERCASE** (e.g., `SHOW CREATE TABLE`).
- **Formatting:** File must start with a descriptive comment and end with a new line.

---

### File Details

| File | Description | Main SQL Command |
| :--- | :--- | :--- |
| `5-full_table.sql` | Prints the complete `CREATE TABLE` definition for `first_table`. | `SHOW CREATE TABLE first_table;` |

---

### Script Content (`5-full_table.sql`)

```sql
-- Prints the full description of the table first_table from database hbtn_0c_0
SHOW CREATE TABLE first_table;



## Task 6: List all in table

### Description
This task involves writing an SQL script that retrieves and lists all rows and fields from the `first_table` within the specified database. The script queries all existing data entries stored in the table. The target database name is provided dynamically as a command-line argument.

### Learning Objectives
- Learn how to use Data Manipulation Language (DML) to query data.
- Master the basic syntax of the `SELECT` statement.
- Practice selecting all columns using the wildcard (`*`) character.

### Requirements & Constraints
- **File Name:** `6-list_values.sql`
- **Target Table:** `first_table`
- **Fields:** All fields/columns must be printed.
- **SQL Keywords:** Must be in **UPPERCASE** (e.g., `SELECT * FROM`).
- **Formatting:** File must start with a descriptive comment and end with a new line.

---

### File Details

| File | Description | Main SQL Command |
| :--- | :--- | :--- |
| `6-list_values.sql` | Displays all records from `first_table`. | `SELECT * FROM first_table;` |

---

### Script Content (`6-list_values.sql`)

```sql
-- Lists all rows of the table first_table from database hbtn_0c_0
SELECT * FROM first_table;



## Task 7: First add

### Description
This task involves writing an SQL script that inserts a new record (row) into the `first_table` table within the target database. The target database name is supplied dynamically as a command-line argument.

### Learning Objectives
- Learn how to use Data Manipulation Language (DML) to insert new records into existing tables.
- Master the syntax of the `INSERT INTO` statement.
- Understand how values are mapped to specific column names.

### Requirements & Constraints
- **File Name:** `7-insert_value.sql`
- **Target Table:** `first_table`
- **Inserted Values:**
  - `id`: `89`
  - `name`: `'Best School'`
- **SQL Keywords:** Must be in **UPPERCASE** (e.g., `INSERT INTO`, `VALUES`).
- **Formatting:** File must start with a descriptive comment and end with a new line.

---

### File Details

| File | Description | Main SQL Command |
| :--- | :--- | :--- |
| `7-insert_value.sql` | Inserts a single record with `id = 89` and `name = 'Best School'`. | `INSERT INTO first_table (id, name) VALUES (89, 'Best School');` |

---

### Script Content (`7-insert_value.sql`)

```sql
-- Inserts a new row in the table first_table in MySQL server
INSERT INTO first_table (id, name) VALUES (89, 'Best School');



## Task 8: Count 89

### Description
This task involves writing an SQL script that counts and displays the total number of records in `first_table` where the column `id` equals `89`. The target database name is supplied dynamically as a command-line argument.

### Learning Objectives
- Learn how to use SQL Aggregate Functions (`COUNT`).
- Practice filtering datasets using conditional clauses (`WHERE`).
- Understand how to query specific metric counts from database tables.

### Requirements & Constraints
- **File Name:** `8-count_89.sql`
- **Target Table:** `first_table`
- **Filter Condition:** `id = 89`
- **SQL Keywords:** Must be in **UPPERCASE** (e.g., `SELECT`, `COUNT`, `FROM`, `WHERE`).
- **Formatting:** File must start with a descriptive comment and end with a new line.

---

### File Details

| File | Description | Main SQL Command |
| :--- | :--- | :--- |
| `8-count_89.sql` | Displays the number of rows where `id = 89`. | `SELECT COUNT(*) FROM first_table WHERE id = 89;` |

---

### Script Content (`8-count_89.sql`)

```sql
-- Displays the number of records with id = 89 in the table first_table
SELECT COUNT(*) FROM first_table WHERE id = 89;



## Task 9: Full creation

### Description
This task involves writing an SQL script that creates a table named `second_table` within the specified database and populates it with multiple initial records. The script ensures safe execution by checking if the table already exists before creating it, avoiding runtime errors. The target database name is passed dynamically as a command-line argument.

### Learning Objectives
- Practice table schema definition using Data Definition Language (DDL).
- Learn how to insert multiple records into a table within a single DML statement.
- Understand table creation with multi-column structures (`INT`, `VARCHAR`).

### Requirements & Constraints
- **File Name:** `9-full_creation.sql`
- **Table Name:** `second_table`
- **Columns:**
  - `id`: `INT`
  - `name`: `VARCHAR(256)`
  - `score`: `INT`
- **Initial Data:**
  - `(1, 'John', 10)`
  - `(2, 'Alex', 3)`
  - `(3, 'Bob', 14)`
  - `(4, 'George', 8)`
- **Forbidden Keywords:** `SELECT`, `SHOW`
- **SQL Keywords:** Must be in **UPPERCASE** (e.g., `CREATE TABLE IF NOT EXISTS`, `INSERT INTO`, `VALUES`).
- **Formatting:** File must start with a descriptive comment and end with a new line.

---

### File Details

| File | Description | Main SQL Commands |
| :--- | :--- | :--- |
| `9-full_creation.sql` | Creates `second_table` and inserts 4 pre-defined records. | `CREATE TABLE IF NOT EXISTS second_table ...;`<br>`INSERT INTO second_table ... VALUES ...;` |

---

### Script Content (`9-full_creation.sql`)

```sql
-- Creates second_table in the database hbtn_0c_0 and inserts multiple rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);



## Task 10: List by best

### Description
This task involves writing an SQL script that lists all records from the `second_table` table in the target database. The output displays the columns `score` and `name` (in that specific order) and sorts the results in descending order based on `score` so that the top scores appear first. The target database name is passed dynamically as a command-line argument.

### Learning Objectives
- Learn how to select specific columns in a designated order using `SELECT`.
- Master sorting query results using the `ORDER BY` clause.
- Understand descending ordering using the `DESC` keyword.

### Requirements & Constraints
- **File Name:** `10-top_score.sql`
- **Target Table:** `second_table`
- **Output Columns:** `score`, `name` (strictly in this order).
- **Ordering:** Ordered by `score` descending (top first).
- **SQL Keywords:** Must be in **UPPERCASE** (e.g., `SELECT`, `FROM`, `ORDER BY`, `DESC`).
- **Formatting:** File must start with a descriptive comment and end with a new line.

---

### File Details

| File | Description | Main SQL Command |
| :--- | :--- | :--- |
| `10-top_score.sql` | Selects `score` and `name` from `second_table`, ordered by `score` from highest to lowest. | `SELECT score, name FROM second_table ORDER BY score DESC;` |

---

### Script Content (`10-top_score.sql`)

```sql
-- Lists all records of second_table ordered by score (top first)
SELECT score, name FROM second_table ORDER BY score DESC;



## Task 11: Select the best

### Description
This task involves writing an SQL script that filters and lists records from the `second_table` table where the `score` is greater than or equal to `10`. The output displays the columns `score` and `name` (in that specific order) and sorts the matching results in descending order by `score` (top scores first). The target database name is passed dynamically as a command-line argument.

### Learning Objectives
- Master combining conditional filtering (`WHERE`) with result sorting (`ORDER BY`).
- Practice relational comparison operators (`>=`).
- Learn to filter and structure output queries effectively.

### Requirements & Constraints
- **File Name:** `11-best_score.sql`
- **Target Table:** `second_table`
- **Filter Condition:** `score >= 10`
- **Output Columns:** `score`, `name` (strictly in this order).
- **Ordering:** Ordered by `score` descending (top first).
- **SQL Keywords:** Must be in **UPPERCASE** (e.g., `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `DESC`).
- **Formatting:** File must start with a descriptive comment and end with a new line.

---

### File Details

| File | Description | Main SQL Command |
| :--- | :--- | :--- |
| `11-best_score.sql` | Selects `score` and `name` for records with `score >= 10`, ordered from highest to lowest score. | `SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;` |

---

### Script Content (`11-best_score.sql`)

```sql
-- Lists all records with a score >= 10 in second_table ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;



## Task 12: Cheating is bad

### Description
This task involves writing an SQL script that updates the `score` column value for the record corresponding to `Bob` in the `second_table` table, setting it to `10`. To adhere to project constraints, the record must be targeted strictly using the `name` column without referencing Bob's `id`. The target database name is passed dynamically as a command-line argument.

### Learning Objectives
- Learn how to update existing records in a database using Data Manipulation Language (DML).
- Master the syntax and usage of the `UPDATE` statement along with the `SET` clause.
- Practice applying non-primary key filtering conditions in `WHERE` clauses.

### Requirements & Constraints
- **File Name:** `12-no_cheating.sql`
- **Target Table:** `second_table`
- **Target Record:** `name = 'Bob'`
- **Updated Value:** `score = 10`
- **Constraint:** Do NOT use `id` (must use `name = 'Bob'`).
- **SQL Keywords:** Must be in **UPPERCASE** (e.g., `UPDATE`, `SET`, `WHERE`).
- **Formatting:** File must start with a descriptive comment and end with a new line.

---

### File Details

| File | Description | Main SQL Command |
| :--- | :--- | :--- |
| `12-no_cheating.sql` | Updates Bob's score to `10` in `second_table`. | `UPDATE second_table SET score = 10 WHERE name = 'Bob';` |

---

### Script Content (`12-no_cheating.sql`)

```sql
-- Updates the score of Bob to 10 in second_table using name field
UPDATE second_table SET score = 10 WHERE name = 'Bob';



## Task 13: Score too low

### Description
This task involves writing an SQL script that removes all records from the `second_table` table where the `score` is less than or equal to `5`. The target database name is passed dynamically as a command-line argument.

### Learning Objectives
- Learn how to delete specific rows from a table using Data Manipulation Language (DML).
- Master the syntax and safe usage of the `DELETE FROM` statement.
- Practice using relational operators (`<=`) with conditional `WHERE` filtering.

### Requirements & Constraints
- **File Name:** `13-change_class.sql`
- **Target Table:** `second_table`
- **Deletion Condition:** `score <= 5`
- **SQL Keywords:** Must be in **UPPERCASE** (e.g., `DELETE`, `FROM`, `WHERE`).
- **Formatting:** File must start with a descriptive comment and end with a new line.

---

### File Details

| File | Description | Main SQL Command |
| :--- | :--- | :--- |
| `13-change_class.sql` | Deletes all records from `second_table` where `score <= 5`. | `DELETE FROM second_table WHERE score <= 5;` |

---

### Script Content (`13-change_class.sql`)

```sql
-- Removes all records with a score <= 5 in the table second_table
DELETE FROM second_table WHERE score <= 5;
