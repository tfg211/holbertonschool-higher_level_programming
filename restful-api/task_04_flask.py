#!/usr/bin/python3
"""
A simple Flask API that handles users, status, and data retrieval.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route('/')
def home():
    """
    Root endpoint returning a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    """
    Returns a list of all usernames stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Returns the status of the API.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Returns the full object corresponding to the provided username.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user to the dictionary via POST request.
    """
    # Parse incoming JSON data. silent=True prevents automatic 400 error
    # allows handling invalid JSON manually.
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add new user
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
