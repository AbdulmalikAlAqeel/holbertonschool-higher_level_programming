#!/usr/bin/python3
"""
Script to create and populate the SQLite products database.
"""
import sqlite3


def create_database():
    """Creates products.db and populates it with sample data."""
    # Establish a connection to the SQLite database
    # Creates 'products.db' if it does not exist
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Create the Products table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Clear existing entries to prevent duplicate insertion errors on re-runs
    cursor.execute('DELETE FROM Products')

    # Insert sample records into the Products table
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    # Save (commit) the changes and close the database connection
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # Execute database creation when the script is run directly
    create_database()
