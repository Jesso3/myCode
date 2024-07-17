from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to create a table if it doesn't exist
def create_table():
    conn = sqlite3.connect('textbox_contents.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS textbox_contents (content TEXT)''')
    conn.commit()
    conn.close()

create_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['textbox_content']
        save_to_database(content)
    contents = fetch_contents()
    return render_template('index.html', contents=contents)

def save_to_database(content):
    conn = sqlite3.connect('textbox_contents.db')
    c = conn.cursor()
    c.execute("INSERT INTO textbox_contents (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()

def fetch_contents():
    conn = sqlite3.connect('textbox_contents.db')
    c = conn.cursor()
    c.execute("SELECT * FROM textbox_contents")
    contents = c.fetchall()
    conn.close()
    return contents

if __name__ == '__main__':
    app.run(debug=True)
