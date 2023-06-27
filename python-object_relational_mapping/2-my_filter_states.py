#!/usr/bin/python3
"""Script that lists all states"""

import MySQLdb
import sys

def search_states(username, password, database, state_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Create the SQL query using the provided state name
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    try:
        # Execute the query
        cursor.execute(query)

        # Fetch all the rows returned by the query
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error executing the query:", e)
        sys.exit(1)

    finally:
        # Close the database connection and cursor
        cursor.close()
        db.close()

# Get the command line arguments
if len(sys.argv) != 5:
    print("Usage: python script.py <username> <password> <database> <state_name>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]

# Call the search_states function with the provided arguments
search_states(username, password, database, state_name)
