#!/usr/bin/python3
"""
Task 2: Consuming and processing data from an API using Python.
This module provides functions to fetch data from JSONPlaceholder API,
print specific fields, and save the data into a structured CSV file.
"""
import csv
import requests


def fetch_and_print_posts():
    """
    Fetches all posts from the JSONPlaceholder API.
    Prints the HTTP status code and the titles of all fetched posts.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Send a GET request to the API
    response = requests.get(url)

    # Print the HTTP status code as required by the expected output
    print(f"Status Code: {response.status_code}")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response body into a Python list of dictionaries
        posts = response.json()

        # Iterate through the list and print the title of each post
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetches all posts from the JSONPlaceholder API.
    Filters specific fields (id, title, body) and saves them into a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Send a GET request to the API
    response = requests.get(url)

    # Process data only if the response status is 200 OK
    if response.status_code == 200:
        posts = response.json()

        # Restructure data to contain only required keys using list comprehension
        filtered_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in posts
        ]

        # Define the header/column names for the CSV file
        fieldnames = ["id", "title", "body"]

        # Safely open a new file named 'posts.csv' for writing
        with open("posts.csv", mode="w", encoding="utf-8", newline="") as file:
            # Initialize the CSV DictWriter with the specified column headers
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the column headers row
            writer.writeheader()

            # Write all filtered dictionary rows at once
            writer.writerows(filtered_posts)
