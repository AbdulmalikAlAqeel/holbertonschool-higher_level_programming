## Tasks

### 0. My privileges!
* **File:** `0-privileges.sql`
* **Description:** Write a SQL script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the server (`localhost`).

#### SQL Script Content:
```sql
-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on the server
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
