#!/usr/bin/python3
"""
Task 03: Displaying Data from JSON or CSV Files in Flask
"""
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_data():
    """Reads products data from products.json"""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []


def read_csv_data():
    """Reads products data from products.csv"""
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
        print(f"Error reading CSV: {e}")
    return products


@app.route('/products')
def products():
    """Route to display products based on query parameters source and id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 1. Handle invalid source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Fetch data based on source
    if source == 'json':
        products_list = read_json_data()
    else:
        products_list = read_csv_data()

    # 3. Filter by ID if provided
    if product_id:
        try:
            target_id = int(product_id)
            filtered_products = [p for p in products_list if p.get('id') == target_id]
            if not filtered_products:
                return render_template('product_display.html', error="Product not found")
            products_list = filtered_products
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
