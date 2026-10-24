#!/usr/bin/python3
"""
A simple RESTful API built with Flask.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route('/')
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """Status endpoint."""
    return "OK"


@app.route('/data')
def get_data():
    """Returns a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route('/users/<username>')
def get_user(username):
    """Returns full user object or 404 if not found."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the in-memory storage."""
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data.get('username')
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == '__main__':
    app.run()
