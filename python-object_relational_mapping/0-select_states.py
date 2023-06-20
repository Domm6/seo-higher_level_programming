#!/usr/bin/python3
"""
Module: list_states_from_database

This module connects to a MySQL database\
and lists all states from a specific table.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Read MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all rows from the result set
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
