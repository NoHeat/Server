import sqlite3

# Get connections to the databases
db_a = sqlite3.connect('database1.db')	#change to db name of old db on pi w/lcd
db_b = sqlite3.connect('databaseD.db')	#change to db name of db coming in from client

# Get the contents of a table
b_cursor = db_b.cursor()
b_cursor.execute('SELECT * FROM codes')	#codes is the table name
output = b_cursor.fetchall()   # Returns the results as a list.

# Insert those contents into another table.
a_cursor = db_a.cursor()
for row in output:

	a_cursor.execute('INSERT INTO codes VALUES (?, ?)', row)	#codes is the table name 

#remove duplicate values if name and upc are equal
a_cursor.execute('''DELETE FROM codes 
						WHERE rowid NOT IN (SELECT min(rowid) FROM codes 
						GROUP BY "upc text", "name text")''')

# Cleanup
db_a.commit()
a_cursor.close()
b_cursor.close()




















########################joining functions to combine like rows and output a diff
#A INNER JOIN creates a new result table by combining column values of two tables
#column values for each matched pair of rows of A and B are combined into a result row
#SELECT upc, name, price FROM table1 INNER JOIN table2 ON table1.upc = table2.price;
#upc	      name        price
#----------  ----------  ----------
#1           Paul     	    50
#2           Allen   	    25
#7           James   	    45
#OUTER join will take any unjoined rows from one or both tables, pad them out with NULLs, and append them to the resulting table
#SELECT upc, name, price FROM table1 LEFT OUTER JOIN table2 ON table1.upc = table2.price;
#upc	      name        price
#----------  ----------  ----------
#1           Paul     	    50
#2           Allen   	    25
#            Teddy
#            Mark
#            David
#            Kim
#7           James    	    45
###############################
#think about UPDATE and DELETE SQL statements





