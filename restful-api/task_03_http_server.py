#!/usr/bin/python3
"""
Task 3: Develop a simple API using Python with the `http.server` module.
This module sets up a basic HTTP server that handles different GET endpoints
and serves both plain text and JSON data, with error handling for 404.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Custom request handler that defines how the server responds
    to various GET request endpoints.
    """

    def do_GET(self):
        """
        Handles GET requests by routing the user based on the requested path.
        """
        # Endpoint 1: Root path '/'
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Endpoint 2: '/data' serving a JSON dataset
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        # Endpoint 3: '/status' to check API health
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        # Endpoint 4: '/info' serving metadata
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))

        # Error Handling: Undefined endpoints (Returns the precise required text)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """
    Initializes and starts the HTTP server on the specified port.
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
        httpd.server_close()


if __name__ == '__main__':
    run()
