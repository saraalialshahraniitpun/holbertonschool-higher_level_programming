import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception:
        return []


def read_csv_file(file_path):
    products = []
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception:
        return []


def read_sql_database():
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
        return products
    except Exception:
        return []


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    products = []
    error_message = None

    if source == 'json':
        products = read_json_file('products.json')
    elif source == 'csv':
        products = read_csv_file('products.csv')
    elif source == 'sql':
        products = read_sql_database()
    else:
        error_message = 'Wrong source'

    if not error_message and product_id is not None:
        try:
            product_id = int(product_id)
            products = [p for p in products if p['id'] == product_id]
            if not products:
                error_message = 'Product not found'
        except ValueError:
            error_message = 'Product not found'

    return render_template(
        'product_display.html',
        products=products,
        error=error_message
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
