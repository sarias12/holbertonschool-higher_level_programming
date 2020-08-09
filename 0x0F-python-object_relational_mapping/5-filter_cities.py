#!/usr/bin/python3
"""
This script takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
        )

    cur = db.cursor()
    cur.execute(
        """SELECT cities.id, cities.name, states.name
        FROM states JOIN cities ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY id ASC""", (argv[4],)
        )

    rows = cur.fetchall()
    tmp = 0
    for row in rows:
        tmp += 1
        print("{:s}".format(str(row[1])), end='')
        if tmp < len(rows):
            print(', ', end='')
    print()
    cur.close()
    db.close()
