## Tasks

### 0. My privileges!
* **File:** `0-privileges.sql`
* **Description:** Write a SQL script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the server (`localhost`).

#### SQL Script Content:
```sql
-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the server
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';


### 1. Root user
* **File:** `1-create_user.sql`
* **Description:** Write a SQL script that creates the MySQL server user `user_0d_1` with all privileges on the server and password `user_0d_1_pwd`. If the user already exists, the script should not fail.

#### SQL Script Content:
```sql
-- Creates the MySQL server user user_0d_1 with all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';


### 2. Read user
* **File:** `2-create_read_user.sql`
* **Description:** Write a SQL script that creates the database `hbtn_0d_2` and the user `user_0d_2` with only `SELECT` privilege on `hbtn_0d_2`. Password should be `user_0d_2_pwd`, and the script should not fail if either the database or user already exists.

#### SQL Script Content:
```sql
-- Creates the database hbtn_0d_2 and the user user_0d_2 with SELECT privilege
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';


### 3. Always a name
* **File:** `3-force_name.sql`
* **Description:** Write a SQL script that creates the table `force_name` on your MySQL server. Table description: `id` (INT), `name` (VARCHAR(256) NOT NULL). The database name will be passed as an argument. Safe against existing tables.

#### SQL Script Content:
```sql
-- Creates the table force_name on MySQL server
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);


### 4. ID can't be null
* **File:** `4-never_empty.sql`
* **Description:** Write a SQL script that creates the table `id_not_null` on your MySQL server with columns `id` (INT with default value 1) and `name` (VARCHAR(256)). The database name will be passed as an argument. Safe against existing tables.

#### SQL Script Content:
```sql
-- Creates the table id_not_null on MySQL server
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
