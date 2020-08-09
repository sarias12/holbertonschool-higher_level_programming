#!/usr/bin/python3
"""
This script ists all states from the database hbtn_0e_0_usa
starting with N (upper N).
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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print("{:s}".format(str(row)))
    cur.close()
    db.close()
