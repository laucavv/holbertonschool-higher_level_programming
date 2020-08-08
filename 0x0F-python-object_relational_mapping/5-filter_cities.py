#!/usr/bin/python3
""" Script that lists all states from a database  hbtn_0e_0_usawith a name
    starting with N
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db_date = {
        'host': "localhost",
        'port': 3306,
        'user': argv[1],
        'passwd': argv[2],
        'db': argv[3]
    }

    db = MySQLdb.connect(**db_date)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities  JOIN states\
                   ON  cities.state_id=states.id\
                   WHERE states.name=%s ORDER BY cities.id",
                   (argv[4],))

    list_states = cursor.fetchall()
    print(", ".join(states[1] for states in list_states))
    cursor.close()
    db.close()
