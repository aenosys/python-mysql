from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Create a connection to the database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='db-container-518ef1a5-cbeb-4557-acba-2c5003290534',
            user='root',
            password='thy0aa8bq2fuitju5li53j',
            database='db_rwcsuu3v'
        )
        if connection.is_connected():
            print('Connected to MySQL database')
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Default / route
@app.route('/')
def index():
    return 'API is working! Welcome to the MySQL Flask API.'

# API to fetch all categories
@app.route('/categories', methods=['GET'])
def get_categories():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute('SELECT * FROM categories')
        rows = cursor.fetchall()
        return jsonify(rows)
    except Error as e:
        print(f"Error fetching categories: {e}")
        return jsonify({'message': 'Failed to fetch categories'}), 500
    finally:
        cursor.close()
        connection.close()

# API to fetch all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute('SELECT * FROM posts')
        rows = cursor.fetchall()
        return jsonify(rows)
    except Error as e:
        print(f"Error fetching posts: {e}")
        return jsonify({'message': 'Failed to fetch posts'}), 500
    finally:
        cursor.close()
        connection.close()

# API to fetch posts by category
@app.route('/posts/category/<int:category_id>', methods=['GET'])
def get_posts_by_category(category_id):
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute('SELECT * FROM posts WHERE category_id = %s', (category_id,))
        rows = cursor.fetchall()
        return jsonify(rows)
    except Error as e:
        print(f"Error fetching posts for category: {e}")
        return jsonify({'message': 'Failed to fetch posts for category'}), 500
    finally:
        cursor.close()
        connection.close()

# Start the server (this is optional since we'll use Gunicorn in production)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
