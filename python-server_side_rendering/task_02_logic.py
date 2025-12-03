#!/usr/bin/python3
"""
Flask application to demonstrate dynamic templates with loops and conditions.
"""
from flask import Flask, render_template
import json
import os

app = Flask(__name__)


@app.route('/items')
def items():
    """
    Reads items from a JSON file and renders them using a Jinja template.
    """
    filename = 'items.json'
    items_list = []

    # Check if file exists and read content
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                items_list = data.get('items', [])
        except ValueError:
            # Handle empty or invalid JSON file
            items_list = []
    
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True)
