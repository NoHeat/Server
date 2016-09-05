import sqlite3
import time
import datetime
import random
import csv

#connect to database file
conn = sqlite3.connect('database2.db') #provide dir for file w/name
c = conn.cursor()   #create cursor object to perform cmds

with open('C:/Users/r0ug3_h@cK3r/Desktop/codes.csv','rb') as fin: # `with` statement available in 2.5+
    reader = csv.reader(fin, delimiter=',') # no header information with delimiter
    for row in reader:
        to_db = [(i['upc'], i['name']) for i in dr] #[unicode(row[0], "utf8"), unicode(row[1], "utf8")] # Appends data from CSV file representing and handling of text
        c.execute("INSERT INTO t (upc, name) VALUES(?, ?);", to_db)
        conn.commit()

    # csv.DictReader uses first line in file for column headings by default
#    dr = csv.DictReader(fin) # comma is default delimiter
#    to_db = [(i['upc'], i['name']) for i in dr]

#c.executemany("INSERT INTO test (upc, name) VALUES (?, ?);", to_db)  

#with open('C:/Users/r0ug3_h@cK3r/Desktop/codes.csv', 'rt') as csv_file:
#    csv_reader = csv.DictReader(csv_file, delimiter=',')
    
#    with sqlite3.connect('C:/Users/r0ug3_h@cK3r/Desktop/code4sr/0dbfiles/database2.db') as conn:
#        c = conn.cursor()
#        c.executemany("INSERT INTO t (upc, name) VALUES(?,?);", csv_reader)

#open from file
#def open_from_file():
#    with open("C:/Users/r0ug3_h@cK3r/Desktop/codes.csv") as infile:
#        for line in infile:
#            line = line.replace('"','') #loop over each line in file
#            data = line.split(",")  #split each line for individual fields

#open_from_file()

#open from file.csv version 2
#c.executemany("INSERT INTO test (upc, name) VALUES (?, ?);", data) # use your column names here

#save/close connections
conn.commit()   #save/commit changes
c.close()       #close cursor object
conn.close()    #close connection to dbB