#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor to execute queries
    cur = db.cursor()

    # Execute the query to fetch all states sorted by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all results
    for row in cur.fetchall():
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()