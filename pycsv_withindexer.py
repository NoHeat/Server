from __future__ import print_function
import sqlite3
import csv
import os
import glob
import sys
 
db = sys.argv[1]
print ('test1') 
conn = sqlite3.connect(db)
conn.text_factory = str  # allows utf-8 data to be stored
 
c = conn.cursor()
print ('test2') 
# traverse the directory and process each .csv file
for csvfile in glob.glob(os.path.join(sys.argv[2], "*.csv")):
    print ('test3')
    # remove the path and extension and use what's left as a table name
    tablename = os.path.splitext(os.path.basename(csvfile))[0]
    print ('test4') 
    with open(csvfile, "rb") as f:
        reader = csv.reader(f)
 
        header = True
        for row in reader:
            if header:
                # gather column names from the first row of the csv
                header = False
 
                sql = "DROP TABLE IF EXISTS ?" % tablename
                c.execute(sql)
                sql = "CREATE TABLE ? (?, ?)" % (tablename,
                          ", ".join([ "? text" % column for column in row ]))
                c.execute(sql)
 
                for column in row:
                    if column.lower().endswith("_id"):
                        index = "?__?" % ( tablename, column )
                        sql = "CREATE INDEX ? on ? (?)" % ( index, tablename, column )
                        c.execute(sql)
 
                insertsql = "INSERT INTO ? VALUES (?)" % (tablename,
                            ", ".join([ "?" for column in row ]))
 
                rowlen = len(row)
            else:
                # skip lines that don't have the right number of columns
                #if len(row) == rowlen:
                #    c.execute(insertsql, row)
 
                conn.commit()
    conn.commit()

c.close()
conn.close()