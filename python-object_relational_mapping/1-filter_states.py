#!/usr/bin/python3
"""
script that lists all states with a name starting with N from a database
"""

import MySQLdb
import sys
if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    con = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                          passwd=mysql_passwd, db=mysql_db)
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    con.close()
