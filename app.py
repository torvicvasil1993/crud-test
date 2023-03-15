from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import os


app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get('DATABASE_SERVICE_NAME')
app.config['MYSQL_USER'] = os.environ.get('DATABASE_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('DATABASE_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('DATABASE_NAME')

mysql = MySQL(app)

@app.route('/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return jsonify(users)

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM users WHERE id = {id}")
    user = cur.fetchone()
    cur.close()
    return jsonify(user)

@app.route('/users', methods=['POST'])
def add_user():
    name = request.json['name']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute(f"INSERT INTO users (name, email) VALUES ('{name}', '{email}')")
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User added successfully"})

@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    name = request.json['name']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute(f"UPDATE users SET name = '{name}', email = '{email}' WHERE id = {id}")
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User updated successfully"})

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute(f"DELETE FROM users WHERE id = {id}")
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "User deleted successfully"})

if __name__ == '__main__':
    app.run()
