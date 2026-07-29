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


### 5. Unique ID
* **File:** `5-unique_id.sql`
* **Description:** Write a SQL script that creates the table `unique_id` on your MySQL server with columns `id` (INT DEFAULT 1 UNIQUE) and `name` (VARCHAR(256)). The database name will be passed as an argument. Safe against existing tables.

#### SQL Script Content:
```sql
-- Creates the table unique_id on MySQL server
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);


### 6. States table
* **File:** `6-states.sql`
* **Description:** Write a SQL script that creates the database `hbtn_0d_usa` and the table `states` with columns `id` (INT AUTO_INCREMENT PRIMARY KEY) and `name` (VARCHAR(256) NOT NULL). Safe against existing items.

#### SQL Script Content:
```sql
-- Creates the database hbtn_0d_usa and the table states on MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);


### 7. Cities table
* **File:** `7-cities.sql`
* **Description:** Write a SQL script that creates the database `hbtn_0d_usa` and the table `cities` with columns `id` (INT AUTO_INCREMENT PRIMARY KEY), `state_id` (INT NOT NULL, FOREIGN KEY referencing `states(id)`), and `name` (VARCHAR(256) NOT NULL). Safe against existing items.

#### SQL Script Content:
```sql
-- Creates the database hbtn_0d_usa and the table cities on MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);


### 8. Cities of California
* **File:** `8-cities_of_california_subquery.sql`
* **Description:** Write a SQL script that lists all the cities of California found in `hbtn_0d_usa` without using the `JOIN` keyword (using subqueries instead). Results are sorted in ascending order by `cities.id`.

#### SQL Script Content:
```sql
-- Lists all the cities of California found in the database hbtn_0d_usa using a subquery
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;


### 9. Cities by States
* **File:** `9-cities_by_state_join.sql`
* **Description:** Write a SQL script that lists all cities contained in `hbtn_0d_usa` with their corresponding state names using a single `SELECT` statement with `JOIN`. Each record displays `cities.id`, `cities.name`, and `states.name`, sorted in ascending order by `cities.id`.

#### SQL Script Content:
```sql
-- Lists all cities in hbtn_0d_usa with their state names using JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;


### 10. Genre ID by show
* **File:** `10-genre_id_by_show.sql`
* **Description:** Write a SQL script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked. Displaying `tv_shows.title` and `tv_show_genres.genre_id`, sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id` using a single `SELECT` statement.

#### SQL Script Content:
```sql
-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
