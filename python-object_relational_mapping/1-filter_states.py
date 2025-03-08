#!/usr/bin/python3
import MySQLdb
import sys
""" Module that filters states that start with 'N' """

def main():
    """ Main function """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
