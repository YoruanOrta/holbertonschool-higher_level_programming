#!/usr/bin/python3
""" Task 03: HTTP Server """


from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from json import dumps


class RequestHandler(BaseHTTPRequestHandler):
    """ Request Handler """

    def do_GET(self):
        """ Handle GET request """
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")
        parsed_path = urlparse(self.path)
        if parsed_path.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(dumps(data).encode())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not Found")
            parsed_path = urlparse(self.path)
            if parsed_path.path == "/data":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                data = {"name": "John", "age": 30, "city": "New York"}
                self.wfile.write(dumps(data).encode())
            elif parsed_path.path == "/status":
                self.send_response(200)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"OK")
            else:
                self.send_response(404)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Not Found")
            parsed_path = urlparse(self.path)
            if parsed_path.path == "/data":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                data = {"name": "John", "age": 30, "city": "New York"}
                self.wfile.write(dumps(data).encode())
            elif parsed_path.path == "/status":
                self.send_response(200)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"OK")
            else:
                self.send_response(404)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Not Found")


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    """ Run the server """
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


run()