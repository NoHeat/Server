import sqlite3
import time
import datetime
import random
import csv

#connect to database file
conn = sqlite3.connect('database.db') #provide dir for file w/name
c = conn.cursor()   #create cursor object to perform cmds

#save/close connections
    conn.commit()   #save/commit changes
    c.close()       #close cursor object
    conn.close()    #close connection to db

#open from file
def open_from_file():
    with open("file.csv") as infile:
        for line in infile:
            line = line.replace('"','') #loop over each line in file
            data = line.split(",")  #split each line for individual fields
        
#create a table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS rtable(UPC TEXT, Description TEXT)')

#insert data into table
def data_entry():
    c.execute("INSERT INTO rtable VALUES(?,?)") #use "?" for a placeholder to prevent SQLinjection

#dynamically enter data, also func for time and datestamp
def dynamic_data_entry():
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %h:%M:%S))
    keyword = 'TTest'
    value = random.randrange(0,10)

    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
          (unix, date, keyword, value))

#use function params
for i in range(10):
    dynamic_data_entry()   #for loop to run prog(x10)
    time.sleep(1)

c.close
conn.close()

#read data from database
def read_from_db():
    c.execute('SELECT * FROM rtable')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT * FROM rtable WHERE value = 3')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT * FROM rtable WHERE unix > 1452554972')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT value, datestamp FROM rtable WHERE unix > 1452554972')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row[0])

#delete data and update table 
def del_and_update():
    c.execute('SELECT * FROM rtable')
    data = c.fetchall()
    [print(row) for row in data]

    c.execute('UPDATE rtable SET value = 99 WHERE value = 3')
    conn.commit()

    c.execute('SELECT * FROM rtable')
    data = c.fetchall()
    [print(row) for row in data]

    c.execute('DELETE FROM rtable WHERE value = 99')
    conn.commit()

    c.execute('SELECT * FROM rtable')
    data = c.fetchall()
    [print(row) for row in data]

#create picture from database
def create_or_open_db(db_file):
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    if db_is_new:
        print 'Creating schema'
        sql = '''create table if not exists PICTURES(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        PICTURE BLOB,
        TYPE TEXT,
        FILE_NAME TEXT);'''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    else:
        print 'Schema exists\n'
    return conn

def insert_picture(conn, picture_file):
    with open(picture_file, 'rb') as input_file:
        ablob = input_file.read()
        base=os.path.basename(picture_file)
        afile, ext = os.path.splitext(base)
        sql = '''INSERT INTO PICTURES
        (PICTURE, TYPE, FILE_NAME)
        VALUES(?, ?, ?);'''
        conn.execute(sql,[sqlite3.Binary(ablob), ext, afile]) 
        conn.commit()

#use function params
conn = create_or_open_db('picture_db.sqlite')

#create schema for picture database
picture_file = "./pictures/pic.jpg"
insert_picture(conn, picture_file)
conn.close()

def extract_picture(cursor, picture_id):
    sql = "SELECT PICTURE, TYPE, FILE_NAME FROM PICTURES WHERE id = :id"
    param = {'id': picture_id}
    cursor.execute(sql, param)
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename

#use function params
conn = create_or_open_db('picture_db.sqlite')
cur = conn.cursor()
filename = extract_picture(cur, 1)
cur.close()
conn.close()
Image(filename='./'+filename)

#bulk insert pictures into database
conn = create_or_open_db('picture_db.sqlite')
conn.execute("DELETE FROM PICTURES")
for fn in picture_list:
    picture_file = "./pictures/"+fn
    insert_picture(conn, picture_file)
     
for r in conn.execute("SELECT FILE_NAME FROM PICTURES"):
    print r[0]
 
conn.close()


#insert data from csv file, method 2
con = sqlite3.connect(":memory:") #creates db in RAM
cur = con.cursor()
cur.execute("CREATE TABLE t (col1, col2);") #col1, col2 should be from csv file

with open('data.csv','rb') as fin: 
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['col1'], i['col2']) for i in dr]

cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
con.commit()
con.close()

################################################################################
#main function
def main():
try:
    # Creates or opens a file called mydb with a SQLite3 DB
    db = sqlite3.connect('data/mydb')
    # Get a cursor object
    cursor = db.cursor()
    # Check if table users does not exist and create it
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                      users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)''')
    # Commit the change
    db.commit()
# Catch the exception
except Exception as e:
    # Roll back any change if something goes wrong
    db.rollback()
    raise e
finally:
    # Close the db connection
    db.close()

#checks to see if the function is being run directly or from an import call
if __name__ == "__main__":
    main()
else:
    print "Run from Import"