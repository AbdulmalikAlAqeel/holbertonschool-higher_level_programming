#!/usr/bin/python3
"""
Task 04: Displaying Data from JSON, CSV, or SQLite Database in Flask
"""
import json
import csv
import sqlite3
from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)


def read_json_data():
    """Reads product data from products.json file."""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []


def read_csv_data():
    """Reads product data from products.csv file and parses fields to correct types."""
    products = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return products


def read_sql_data(product_id=None):
    """Fetches product data from SQLite database products.db."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Allow accessing columns by name like a dictionary (e.g., row['name'])
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Query all records or filter by a specific product ID
        if product_id is not None:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')

        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
        conn.close()
    except sqlite3.Error as e:
        print(f"Database query error: {e}")
    return products


@app.route('/products')
def products():
    """
    Route handler to fetch and render product data based on
    URL query parameters 'source' (json|csv|sql) and optional 'id'.
    """
    # Extract query parameters from URL (e.g., /products?source=sql&id=1)
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 1. Validate 'source' parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Parse and validate 'id' parameter if provided
    target_id = None
    if product_id:
        try:
            target_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    # 3. Retrieve and filter data based on the specified source
    if source == 'json':
        products_list = read_json_data()
        if target_id is not None:
            products_list = [p for p in products_list if p.get('id') == target_id]
    elif source == 'csv':
        products_list = read_csv_data()
        if target_id is not None:
            products_list = [p for p in products_list if p.get('id') == target_id]
    elif source == 'sql':
        products_list = read_sql_data(target_id)

    # 4. Handle edge case when specified product ID does not exist
    if target_id is not None and not products_list:
        return render_template('product_display.html', error="Product not found")

    # 5. Render the HTML template with the list of products
    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    # Start the Flask development server on port 5000
    app.run(debug=True, port=5000)
