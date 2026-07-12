#!/usr/bin/python3
"""
Task 5: API Security and Authentication Techniques.
This module implements Basic Auth and JWT Authentication with Role-Based
Access Control (RBAC) in a Flask application, enforcing strict 401 error codes.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Setup secure key for JWT configuration
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-in-production"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# Hardcoded user database in memory with hashed passwords as instructed
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# --- Basic Authentication Verification Callback ---
@auth.verify_password
def verify_password(username, password):
    """Verifies user credentials using safe hash comparison."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


# --- Custom JWT Error Handlers (Forcing 401 status code for tests) ---
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


# --- API Routes & Endpoints ---

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Handles login via POST JSON payload.
    Generates and returns a JWT access token embedding the user identity.
    """
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad username or password"}), 401

    # Safe casting to string identity to accommodate all framework updates
    access_token = create_access_token(identity=str(username))
    return jsonify(access_token=access_token), 200


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Route protected globally by valid JWT authentication."""
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Route protected by JWT authentication with an explicit role-check constraint.
    Returns 403 Forbidden if the user's role is not admin.
    """
    current_username = get_jwt_identity()
    user_info = users.get(current_username)

    # Authorization Check: Verify if role is explicitly set to admin
    if not user_info or user_info.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
