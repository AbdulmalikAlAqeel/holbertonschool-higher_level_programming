# Python - Server-Side Rendering

## 📋 Description
This project covers the fundamentals of Server-Side Rendering (SSR) in Python. It includes building custom templating functions, handling files, working with JSON/CSV data sources, and building web applications using Flask and SQL databases.

---

## 📂 Project Tasks

| Task | File | Description |
| :--- | :--- | :--- |
| **0. Creating a Simple Templating Program** | `task_00_intro.py` | Python function that generates personalized invitation files from a template and handles edge cases/errors gracefully. |
| **1. Creating a Basic HTML Template in Flask** | `task_01_jinja.py` | A basic Flask application that serves dynamic web pages (`/`, `/about`, `/contact`) using Jinja2 templates with reusable `header.html` and `footer.html` components. |
| **2. Creating a Dynamic Template with Loops and Conditions in Flask** | `task_02_logic.py` | Enhances the Flask application with a dynamic route (`/items`) that parses JSON data (`items.json`) and renders it using Jinja2 `for` loops and `if/else` conditional logic in `items.html`. |
| **3. Displaying Data from JSON or CSV Files in Flask** | `task_03_files.py` | Builds a `/products` route that dynamically fetches and filters product data from either `products.json` or `products.csv` using query parameters (`source` and optional `id`). Handles edge cases like invalid sources or missing IDs. |
| **4. Displaying Data from SQLite Database in Flask** | `task_04_db.py`, `create_database.py` | Extends the `/products` route to support reading from an **SQLite database** (`products.db`) alongside JSON and CSV formats. Uses parameterized SQL queries to filter items by `id` safely and handle invalid parameters. |

---

## 🛠️ Requirements & Environment
- **OS:** Ubuntu 20.04 LTS
- **Python Version:** Python 3.8+
- **Style Guide:** `pycodestyle` (PEP 8)

---

## 📁 Directory Structure (Task 1)

```text
python-server_side_rendering/
│
├── task_00_intro.py
├── task_01_jinja.py
├── README.md
└── templates/
    ├── header.html
    ├── footer.html
    ├── index.html
    ├── about.html
    └── contact.html
```

## 📁 Directory Structure (Task 2)

```text
python-server_side_rendering/
│
├── task_00_intro.py
├── task_01_jinja.py
├── task_02_logic.py
├── items.json
├── README.md
└── templates/
    ├── header.html
    ├── footer.html
    ├── index.html
    ├── about.html
    ├── contact.html
    └── items.html
```

## 📁 Directory Structure (Task 3)

```text
python-server_side_rendering/
│
├── task_00_intro.py
├── task_01_jinja.py
├── task_02_logic.py
├── task_03_files.py
├── items.json
├── products.json
├── products.csv
├── README.md
└── templates/
    ├── header.html
    ├── footer.html
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── items.html
    └── product_display.html
```

## 📁 Directory Structure (Task 4)

```text
python-server_side_rendering/
│
├── task_00_intro.py
├── task_01_jinja.py
├── task_02_logic.py
├── task_03_files.py
├── task_04_db.py
├── create_database.py
├── items.json
├── products.json
├── products.csv
├── products.db
├── README.md
└── templates/
    ├── header.html
    ├── footer.html
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── items.html
    └── product_display.html
