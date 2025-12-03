#!/usr/bin/python3
"""
Flask application to display data from JSON, CSV, or SQLite database.
"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json(filename):
    """Reads data from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def read_csv(filename):
    """Reads data from a CSV file."""
    data = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        return []


def read_sql():
    """Reads data from the SQLite database."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Use Row factory to access columns by name
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            # Convert sqlite3.Row to dict
            products.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None


@app.route('/products')
def products():
    """
    Route to display products based on source (json/csv/sql) and optional id.
    """
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    products_data = []
    error_message = None

    # 1. Determine Source and Fetch Data
    if source == 'json':
        products_data = read_json('products.json')
    elif source == 'csv':
        products_data = read_csv('products.csv')
    elif source == 'sql':
        products_data = read_sql()
        if products_data is None:
            error_message = "Database error"
    else:
        error_message = "Wrong source"

    # If there was a source error (or wrong source), render immediately
    if error_message:
        return render_template('product_display.html', 
                               error_message=error_message)

    # 2. Filter by ID if provided
    if product_id:
        # Filter list where id matches. Convert to strings for comparison
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
