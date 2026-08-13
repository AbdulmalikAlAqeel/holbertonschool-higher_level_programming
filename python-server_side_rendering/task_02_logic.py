#!/usr/bin/python3
"""
Task 02: Dynamic Template with Loops and Conditions in Flask
"""
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Renders the Home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Renders the About Us page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Renders the Contact Us page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Reads items from JSON file and renders items.html with dynamic content."""
    items_list = []
    try:
        with open('items.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading items.json: {e}")

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
