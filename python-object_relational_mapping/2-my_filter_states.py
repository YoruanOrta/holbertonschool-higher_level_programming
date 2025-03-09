#!/usr/bin/python3
""" Module that lists all states from the database hbtn_0e_0_usa
    using the module MySQLdb and the command execute """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connecting to a MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()

    # Executing the Query
    cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4]))

    # Obtaining the Query results
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    # Closing cursor and database
    cursor.close()
    db.close()
