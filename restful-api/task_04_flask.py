#!/usr/bin/python3
""" A simple Flask API with a dictionary of users """

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    """Welcome message for the API"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    """Return a list of all usernames"""
    return jsonify(list(users.keys())), 200

@app.route('/status')
def status():
    """Return a simple status message"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Return the user data if the user exists"""
    user = users.get(username)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the dictionary"""
    try:
        data = request.get_json()
        print("Received JSON:", data)

        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        username = data.get("username", "").strip()
        name = data.get("name", "").strip()
        city = data.get("city", "").strip()
        age = data.get("age")

        if not username:
            return jsonify({"error": "Username is required"}), 400
        if username in users:
            return jsonify({"error": "User already exists"}), 400
        if not name or not city:
            return jsonify({"error": "All fields (username, name, age, city) are required"}), 400

        try:
            age = int(age)
        except (TypeError, ValueError):
            return jsonify({"error": "Age must be a number"}), 400

        users[username] = {
            "username": username,
            "name": name,
            "age": age,
            "city": city
        }

        print("Updated users:", users)

        return jsonify({"message": "User added", "user": users[username]}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)