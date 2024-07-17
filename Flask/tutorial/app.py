from flask import Flask, render_template, request
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# Getting the directory where the script is located
basedir = os.path.abspath(os.path.dirname(__file__))
# Database path
db_path = os.path.join(basedir, 'test.db')

# Function to create a table if it doesn't exist
def create_table():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS todo (
                 id INTEGER PRIMARY KEY,
                 content TEXT NOT NULL,
                 completed INTEGER DEFAULT 0,
                 date_created TEXT DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

create_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['textbox_content']
        save_to_database(content)
    tasks = fetch_tasks()
    return render_template('index.html', tasks=tasks)

def save_to_database(content):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("INSERT INTO todo (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()

def fetch_tasks():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM todo")
    tasks = c.fetchall()
    conn.close()
    return tasks

if __name__ == '__main__':
    app.run(debug=True)
