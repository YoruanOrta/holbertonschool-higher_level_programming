#!/usr/bin/python3
""" Task 04 - Flask """

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    """Return a list of all usernames."""
    return jsonify(list(users.keys())), 200

@app.route('/status')
def status():
    """Return a simple status message."""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Return the user data if the user exists."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the dictionary."""
    data = request.get_json()

    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        print(f"DEBUG: Duplicate username detected: {username}")
        return jsonify({"error": "User already exists"}), 400
    users[username] = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)
