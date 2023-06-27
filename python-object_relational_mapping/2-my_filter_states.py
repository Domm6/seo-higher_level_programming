#!/usr/bin/python3
"""
Module: list_states_starting_with_N

"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Read MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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
    query.execute("SELECT * FROM states " \
                   "WHERE BINARY name LIKE '{}' ORDER BY id ASC".format(state_name)

    # Execute the query with user input
    cursor.execute(query)    
                  
    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
