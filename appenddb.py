import sqlite3

# Get connections to the databases
db_a = sqlite3.connect('databaseC.db')	#change to db name of old db on pi w/lcd
db_b = sqlite3.connect('databaseD.db')	#change to db name of db coming in from client

# Get the contents of a table
b_cursor = db_b.cursor()
b_cursor.execute('SELECT * FROM codes')	#codes is the table name
output = b_cursor.fetchall()   # Returns the results as a list.

# Insert those contents into another table.
a_cursor = db_a.cursor()
for row in output:
    a_cursor.execute('INSERT INTO codes VALUES (?, ?)', row)	#codes is the table name

# Cleanup
db_a.commit()
a_cursor.close()
b_cursor.close()
