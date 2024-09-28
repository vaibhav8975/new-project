from flask import Flask, request, redirect, render_template
import mysql.connector

app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="users_db"
)
cursor = db.cursor()

# Create table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

@app.route('/')
def signup():
    return render_template('signup.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']

    # Insert into the database
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
