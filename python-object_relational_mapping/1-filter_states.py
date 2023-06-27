#!/usr/bin/python3
"""
Module: list_states_starting_with_N

This module connects to a MySQL database and lists all states with names starting with 'N' from a specific table.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Read MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to fetch states
    # starting with 'N' (case-insensitive)
    cursor.execute("SELECT * FROM states "
                   "WHERE BINARY name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
