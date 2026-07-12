# Project: RESTful API - Task 2

## Consuming and Processing Data from an API using Python

### Description
This part of the project focuses on programmatic data consumption using Python. Instead of using command-line utilities like `curl`, we leverage Python's powerful and human-readable `requests` library to communicate with web services, parse JSON payloads, manipulate data structures, and export the processed data into an external structured format (`.csv`).

### Learning Objectives
- Send HTTP `GET` requests and process responses using the Python `requests` library.
- Parse, navigate, and handle JSON data formats in Python.
- Convert unstructured or semi-structured API data into static tabular formats using Python's built-in `csv` module.

### Prerequisites & Dependencies
Your scripts will be tested using **Python 3.9**. 
Before running the tasks, ensure you have the `requests` library installed:

```bash
pip install requests



# Project: RESTful API - Task 3

## Develop a Simple API using Python with the `http.server` Module

### Description
This task demonstrates how to build a lightweight web server from scratch using only Python's standard library. By subclassing `http.server.BaseHTTPRequestHandler`, we implement low-level request handling, custom routing mechanisms, header manipulation, and manual JSON serialization without relying on any third-party frameworks like Flask or Django.

### Learning Objectives
- Set up and orchestrate a baseline HTTP web server using `http.server`.
- Handle incoming HTTP `GET` requests using the `do_GET` routine.
- Implement manual server-side routing based on URI paths (`self.path`).
- Deliver various content types (`text/plain` and `application/json`) with correct response headers.
- Handle error states by serving proper HTTP `404 Not Found` status codes and messages.

### Prerequisites
- Tested and verified under **Python 3.9**.
- Uses internal modules only (`http.server` and `json`); no external installations are required.

### Files Structure
- **`task_03_http_server.py`**: The primary operational server file containing the request handler and server execution setup.

---

### Endpoints Defined

| Endpoint | Content-Type | Expected Response |
| :--- | :--- | :--- |
| `/` | `text/plain` | `Hello, this is a simple API!` |
| `/status` | `text/plain` | `OK` |
| `/data` | `application/json` | `{"name": "John", "age": 30, "city": "New York"}` |
| `/info` | `application/json` | `{"version": "1.0", "description": "A simple API built with http.server"}` |
| *Any undefined path* | `text/plain` | `404 Not Found` |

---

### How to Run and Test

1. Fire up your terminal (or WSL instance) and run the server file:
```bash
python3 task_03_http_server.py



# Project: RESTful API - Task 4

## Develop a Simple API using Python with Flask

### Description
This task transitions the project from a low-level native HTTP server into using **Flask**, a lightweight and modular web framework for Python. The application implements an in-memory data store using Python dictionaries to manage simulated user database profiles, handles complex HTTP routing, parses JSON payloads dynamically, and applies strict API validation rules for input parameters and errors.

### Learning Objectives
- Set up a Flask microservice environment and run a local development server.
- Define explicit and dynamic URI routes using Flask decorators.
- Process incoming HTTP payload states (`GET` and `POST` requests).
- Formulate standardized JSON API outputs utilizing `jsonify()`.
- Implement rigorous request payload validation with explicit HTTP status codes (`201`, `400`, `404`, `409`).

### Prerequisites & Dependencies
- Verified and fully compatible with **Python 3.9**.
- Requires the installation of the Flask framework. If not present, run:

```bash
pip install Flask



# Project: RESTful API - Task 5

## API Security and Authentication Techniques

### Description
This task focuses on securing RESTful APIs by implementing robust authentication and authorization mechanisms. It integrates two primary security strategies within a Flask application: **Basic HTTP Authentication** (using credentials validated through secure cryptographic password hashing via `werkzeug.security`) and **Token-based Authentication via JSON Web Tokens (JWT)** (using `Flask-JWT-Extended`). Furthermore, it introduces **Role-Based Access Control (RBAC)** to differentiate route privileges between standard users and administrators while enforcing unified error delivery boundaries.

### Learning Objectives
- Articulate the operational differences between Authentication and Authorization.
- Implement stateless Basic HTTP Authentication overlays to secure endpoints.
- Apply secure password hashing techniques (`generate_password_hash` and `check_password_hash`).
- Build temporary stateless token handshakes using JSON Web Tokens (JWT).
- Enforce Role-Based Access Control (RBAC) schemas to restrict unauthorized pathing.
- Implement strict custom JWT error managers to guarantee standardized API error responses.

### Prerequisites & Core Dependencies
- Fully verified and built using **Python 3.9**.
- Requires external security packages. Install them into your development environment via:

```bash
pip install Flask Flask-HTTPAuth Flask-JWT-Extended --break-system-packages
