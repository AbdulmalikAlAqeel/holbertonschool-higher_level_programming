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
