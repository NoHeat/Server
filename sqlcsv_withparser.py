import sys
import csv
import re
import codecs
import optparse as op
import sqlite3 as db
from itertools import islice

parser = op.OptionParser()
parser.usage = "%prog CSVFILE"
parser.add_option('-o', action="store", dest="dbname",default="data.db", help="output sqlite3 database file")
parser.add_option('-t', action="store", dest="table", default="Records", help="default table name for data import")

def main(fpath, table, dbname):

    with codecs.open(fpath, encoding='utf-8', errors='ignore') as fh:
        rows    = csv.reader(fh)
        fields  = next(rows)
        slugify = lambda s: re.sub(r'\W+',"_", s).upper()
        schema  = "\n\t\t" + ",\n\t\t".join("%s text" % k for k in map(slugify,fields))

        print("Creating table: %s\n" % dbname)
        conn   = db.connect(dbname)
        c      = conn.cursor()

        # create table with schema
        stmt   = "CREATE TABLE %s (%s);" % (table, schema)     
        c.execute(stmt)

        print("Schema")
        print("======")
        print("\n%s\n" % stmt)

        # insert
        print("Adding records to database")
        stmt   = "INSERT INTO %s (%s) VALUES (%s);" 
        stmt   = stmt % (table, ", ".join(fields), ", ".join(['?'] * len(fields)))
        to_add = list(islice(rows, 2000))
        while to_add:
            sys.stdout.write('.')
            c.executemany(stmt, to_add)
            to_add = list(islice(rows, 2000))
            conn.commit()

if __name__ == '__main__':
    opts, args = parser.parse_args()
    main(fpath=args[0], table=opts.table, dbname=opts.dbname)