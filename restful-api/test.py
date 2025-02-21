import unittest
import json
from task_04_flask import app, users  # Import the Flask app and the users dictionary

class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        """Set up a test client and clear the users dictionary."""
        self.client = app.test_client()
        users.clear()  # Reset users before each test

    def test_home_route(self):
        """Test the home route."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Welcome to the Flask API!")

    def test_status_route(self):
        """Test the status route."""
        response = self.client.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "OK")

    def test_data_route_empty(self):
        """Test the data route when no users are added."""
        response = self.client.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])  # Expect empty list

    def test_add_user(self):
        """Test adding a new user."""
        data = {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        response = self.client.post('/add_user', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("message", response.json)
        self.assertEqual(response.json["user"]["username"], "john")

    def test_data_route_after_adding_user(self):
        """Test the data route after adding a user."""
        data = {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        self.client.post('/add_user', json=data)  # Add user first
        response = self.client.get('/data')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, ["john"])

    def test_get_user(self):
        """Test retrieving a user."""
        data = {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        self.client.post('/add_user', json=data)  # Add user first
        response = self.client.get('/users/john')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["username"], "john")

    def test_get_nonexistent_user(self):
        """Test retrieving a user that does not exist."""
        response = self.client.get('/users/unknown')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {"error": "User not found"})

    def test_add_user_without_username(self):
        """Test adding a user without a username."""
        data = {
            "name": "Alice",
            "age": 25,
            "city": "San Francisco"
        }
        response = self.client.post('/add_user', json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Username is required"})

    def test_add_duplicate_user(self):
        """Test adding a user with a duplicate username."""
        data = {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        self.client.post('/add_user', json=data)  # Add user once
        response = self.client.post('/add_user', json=data)  # Try to add again
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "User already exists"})

if __name__ == '__main__':
    unittest.main()