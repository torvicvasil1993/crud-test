from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.environ.get('DATABASE_SERVICE_NAME'),
        user=os.environ.get('DATABASE_USER'),
        password=os.environ.get('DATABASE_PASSWORD'),
        database=os.environ.get('DATABASE_NAME')
    )

@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    email = data['email']

    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name, email))
    db.commit()
    cursor.close()
    db.close()

    return jsonify({'message': 'User added successfully'})

if __name__ == '__main__':
    app.run()






""" from flask import Flask
import datetime
import os

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.datetime.now()
    current_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    return 'Current timestamp: ' + current_timestamp + '<br/>'

if __name__ == '__main__':
    app.run() """
