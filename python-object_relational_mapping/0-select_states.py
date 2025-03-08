#!/usr/bin/python3
"""
This module lists all states of the state table
"""
import MySQLdb
import sys


def main():
    """
    main function that runs the module
    """
    if len(sys.argv) < 4:
        return

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database,
        charset="utf8"
        )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()