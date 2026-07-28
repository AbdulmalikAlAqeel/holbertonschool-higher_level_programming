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
