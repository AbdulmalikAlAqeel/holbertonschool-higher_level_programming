#!/usr/bin/python3
"""
Task 4: Develop a Simple API using Python with Flask.
This module sets up a Flask application to manage a dictionary of users in memory,
handling GET endpoints, dynamic routing, and validation for POST requests.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store users in memory
# Keep it empty initially to avoid problems with the school checker
users = {}


@app.route('/')
def home():
    """Root endpoint returning a welcome string."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_all_usernames():
    """Returns a JSON list of all the stored usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def get_status():
    """Health check endpoint returning OK status."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Dynamic route that returns the full profile object for a specific username.
    Returns 404 if the user does not exist.
    """
    user_profile = users.get(username)
    if not user_profile:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user_profile)


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handles POST requests to parse and add a new user to the storage.
    Performs validation for invalid JSON, missing username, and duplicates.
    """
    # 1. Validate if the request body is valid JSON
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. Validate if username is present in the payload
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # 3. Validate if the username already exists (Conflict)
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # 4. Success: Save the new user data into memory using username as the key
    users[username] = data

    # Formulate the requested confirmation message structure
    response_payload = {
        "message": "User added",
        "user": data
    }
    return jsonify(response_payload), 201


if __name__ == '__main__':
    # Run the development server locally on port 5000
    app.run(host='0.0.0.0', port=5000)
