#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys
if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    mysql_state = sys.argv[4]
    con = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                          passwd=mysql_passwd, db=mysql_db)
    cur = con.cursor()
    cur.execute("""
    SELECT cities.name
    FROM cities
    JOIN states
    ON states.id = cities.state_id
    WHERE states.name = %(mysql_state)s
    ORDER BY cities.id ASC;
    """, {'mysql_state': mysql_state})
    query_rows = cur.fetchall()
    list_cities = []
    for row in query_rows:
        list_cities.append(row[0])
    print(", ".join(list_cities))
    cur.close()
    con.close()
