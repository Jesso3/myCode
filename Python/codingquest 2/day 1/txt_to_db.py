import sqlite3

# Open the TXT file
with open('inventory_input.txt', 'r') as file:
    # Read the lines from the TXT file
    lines = file.readlines()

# Create a new SQLite database
conn = sqlite3.connect('output.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS my_table (
        column1 TEXT,
        column2 INTEGER,
        column3 REAL
    )
''')

# Insert data into the table
for line in lines:
    # Split the line by spaces
    data = line.split()

    # Check if the line has the required number of values
    if len(data) >= 3:
        # Insert the data into the table
        cursor.execute('''
            INSERT INTO my_table (column1, column2, column3)
            VALUES (?, ?, ?)
        ''', (data[0], data[1], data[2]))

# Commit the changes and close the database connection
conn.commit()
conn.close()
