#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db_date = {
        'user': argv[1],
        'passwd': argv[2],
        'db':[3],
        'host':"localhost",
        'port':3306
    }
    db = MySQLdb.connect(**db_date)
    cursor = db.cursor()
    cursor.execute("SELECT * from states ORDER BY id")
    list_states = cursor.fetchall()
    for states in list_states:
        pritn(states)
    cursor.close()
    db.close()
