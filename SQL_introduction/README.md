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
