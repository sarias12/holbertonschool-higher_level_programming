#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
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
        ORDER BY id ASC"""
        )

    rows = cur.fetchall()
    for row in rows:
        print("{:s}".format(str(row)))
    cur.close()
    db.close()
