#!/usr/bin/python3
"""
Flask application to display data from JSON or CSV files based on query parameters.
"""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json(filename):
    """Reads data from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def read_csv(filename):
    """Reads data from a CSV file and returns a list of dictionaries."""
    data = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # CSV reads as strings, converting id to match JSON behavior loosely
                # though usually we compare as strings in the route
                data.append(row)
        return data
    except FileNotFoundError:
        return []


@app.route('/products')
def products():
    """
    Route to display products based on source (json/csv) and optional id.
    """
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    products_data = []
    error_message = None

    # 1. Determine Source
    if source == 'json':
        products_data = read_json('products.json')
    elif source == 'csv':
        products_data = read_csv('products.csv')
    else:
        # Handle wrong source
        error_message = "Wrong source"
        return render_template('product_display.html', error_message=error_message)

    # 2. Filter by ID if provided
    if product_id:
        # Filter the list where the id matches. 
        # Converting both to strings ensures compatibility between 
        # JSON (int) and CSV/QueryParam (string)
        filtered_products = [
            p for p in products_data 
            if str(p.get('id')) == str(product_id)
        ]
        
        if not filtered_products:
            error_message = "Product not found"
            products_data = []
        else:
            products_data = filtered_products

    return render_template('product_display.html', 
                           products=products_data, 
                           error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
