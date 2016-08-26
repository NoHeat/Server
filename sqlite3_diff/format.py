from sqlite3_diff import *
from sqlite3_diff.utils import *

def format_table_header_diff(db1, db2):
    result = ""
    tnd = table_name_diff(db1.cursor(), db2.cursor())
    if tnd: # First print tables which exist in one but not the other
        for d in tnd[1]:
            kind, nm, tbl_nm, ind, sql = sqlite_master_table_def(db2.cursor(), d)
            result += "Table("+ tbl_nm + ")," + str(ind) + "\n"
            result += "> " + sql + "\n"
            result += "> " + str(row_count(db2.cursor(), d)) + " rows\n"
        for d in tnd[0]:
            kind, nm, tbl_nm, ind, sql = sqlite_master_table_def(db1.cursor(), d)
            result += "Table("+ tbl_nm + ")," + str(ind) + "\n"
            result += "< " + sql + "\n"
            result += "< " + str(row_count(db1.cursor(), d)) + " rows\n"
    #Now print tables which differ
    shared = shared_tables(db1.cursor(), db2.cursor())
    for n in shared:
        result += format_one_table_header_diff(table_header_diff(db1, db2, n), db1, db2)
    return result

def format_one_table_header_diff(diff, db1, db2):
    """Assumes we are given output of table_header_diff function."""
    if not diff:
        return ""
    result = ""
    #First display if one table has differing headers
    if diff[0]:
        oldkind, oldnm, old_tbl_nm, oldind, oldsql = diff[0][0]
        newkind, newnm, new_tbl_nm, newind, newsql = diff[0][1]
        result += "Table(" + new_tbl_nm + ")," + str(newind) + "\n"
        result += "> " + newsql + "\n"
        result += "> " + str(row_count(db2.cursor(), new_tbl_nm)) + " rows\n"
        result += "---\n"
        #result += "Table(" + old_tbl_nm + ")," + str(oldind) + "\n"
        result += "< " + oldsql + "\n"
        result += "< " + str(row_count(db1.cursor(), new_tbl_nm)) + " rows\n"
    #Then display differing indexes
    if diff[1]:
        for old, new in diff[1]: # One of these variables stores the table_name
            table_name = None
            rootpage = None
            if old:
                table_name = old[2]
                rootpage = old[3]
            if new:
                table_name = new[2]
                rootpage = new[3]
            result += "Table("+table_name+"),"+str(rootpage) + "\n"
            if new:
                result += "> " + str(new[4]) + "\n"
            if old and new:
                result += "---\n"
            if old:
                result += "< " + str(old[4]) + "\n"
    return result

def format_table_diff(tbl_name, diff):
    result = ''
    for (old, new) in diff:
        if ((old is None) and not (new is None)):
            result += "> INSERT INTO " + tbl_name + " VALUES " + render_tuple_for_sql(new) + ";"
        if (not (old is None) and (new is None)):
            result += "< INSERT INTO " + tbl_name + " VALUES " + render_tuple_for_sql(old) + ";"
        if (not (old is None) and not (new is None)):
            result += "< INSERT INTO " + tbl_name + " VALUES " + render_tuple_for_sql(old) + ";\n---\n"
            result += "> INSERT INTO " + tbl_name + " VALUES " + render_tuple_for_sql(new) + ";"
        result += "\n"

    return result