#!/usr/bin/python3
""" Module that filters states by user input """

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username, password, database, state_name = sys.argv[1:5]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch results
    rows = cur.fetchall()

    # Debugging output
    print(f"Rows fetched: {len(rows)}")  # Check if rows are returned

    # Print results exactly as expected
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
