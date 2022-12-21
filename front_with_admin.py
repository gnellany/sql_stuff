# Import necessary modules
import sqlite3
import time
import os
import sys

# Set admin login credentials
admin_username = "admin"
admin_password = "password"

# Admin role functions

def get_column_names():
    """
    Returns a list of column names for the HSEtable table in the HSE.db database.
    """
    conn = sqlite3.connect("HSE.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(HSEtable)")
    columns = [column[1] for column in cursor.fetchall()]
    return columns

def add_row(values):
    """
    Adds a row to the HSEtable table in the HSE.db database with the specified values.
    """
    columns = get_column_names()
    column_string = ", ".join(columns)
    placeholders = ", ".join(["?" for _ in range(len(columns))])
    statement = f"INSERT INTO HSEtable ({column_string}) VALUES ({placeholders})"
    conn = sqlite3.connect("HSE.db")
    cursor = conn.cursor()
    cursor.execute(statement, values)
    conn.commit()
    print("Row added successfully!")

def remove_row(id):
    """
    Removes the row with the specified id from the HSEtable table in the HSE.db database.
    """
    conn = sqlite3.connect("HSE.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM HSEtable WHERE id=?", (id,))
    conn.commit()
    print("Row removed successfully!")

def admin_login():
    """
    Prompts the user for a username and password, and returns True if the username and
    password match the predefined admin login credentials, False otherwise.
    """
    # Prompt the user for a username and password
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match the predefined admin login credentials
    if username == admin_username and password == admin_password:
        return True
    else:
        return False

# Basic user functions

def user_input():
    """
    Prints a menu of available services and prompts the user to select one.
    Returns the users selection as a string.
    """
    print("Welcome To HSE information Kiosk\n"
          "Choose From the selection presented\n"
          "\n"
          "General site Search\n"
          "1. By Town\n"
          "2. By Site\n"
          "\n"
          "Specific searches\n"
          "3. Phone Number Search\n"
          "4. Location Search\n"
          "5. Role Search\n")
    service = input("Selection: ")
    return service

def selection(service):
    """
    Determines the service selected by the user and prompts for any additional information needed
    to perform the search. Returns a tuple containing the search term and the column number to search.
    """
    # Try to convert the service string to an integer
    try:
        service = int(service)
    except ValueError:
        print("Invalid service")
        return None, None

    # Determine the service selected and prompt for additional information if necessary
    if service == 1:
        # Prompt the user for the town to search
        target = input("Which town?")
        # Set the column number to search based on the service selected
        selection = 5
    elif service == 2:
        # Prompt the user for the site to search
        target = input("Site")
        # Set the column number to search based on the service selected
        selection = 1
    elif service == 3:
        # Prompt the user for the phone number to search
        target = input("Phone Number")
        # Set the column number to search based on the service selected
        selection = 8
    elif service == 4:
        # Prompt the user for the location to search
        target = input("Location?")
        # Set the column number to search based on the service selected
        selection = 4
    elif service == 5:
        # Prompt the user for the role to search
        target = input("Role Search?")
        # Set the column number to search based on the service selected
        selection = 7
    elif service == 8:
        # Prompt the user to log in if they selected the admin service
        if admin_login():
            # Prompt the user to choose between adding or removing a row
            print("1. Add row\n2. Remove row")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                # Prompt the user for the values to add to a new row
                values = input("Enter values for the row (comma-separated): ").split(",")
                # Add the new row to the HSEtable table
                add_row(values)
                # Return None, None to prevent the search_sql function from being called
                return None, None
            elif choice == 2:
                # Prompt the user for the id of the row to remove
                id = input("Enter the id of the row to be removed: ")
                # Try to convert the id to an integer
                try:
                    id = int(id)
                    # Remove the specified row from the HSEtable table
                    remove_row(id)
                    # Return None, None to prevent the search_sql function from being called
                    return None, None
                except ValueError:
                    print("Invalid id")
            else:
                print("Invalid choice")
        else:
            # Print an error message if the login credentials are invalid
            print("Invalid login credentials")
        # Return None, None if the service selected is not valid
        return None, None


def search_sql(name, number):
    """
    Searches the HSEtable table for rows where the specified column contains the specified search term.
    Prints the matching rows.
    """
    # Set the search term to the name variable passed to the function
    search_term = name
    # Set the column number to search based on the number variable passed to the function
    service: int = number

    # Connect to the HSE.db database and create a cursor
    conn = sqlite3.connect("HSE.db")
    cursor = conn.cursor()

    # Execute a SELECT statement to retrieve all rows from the HSEtable table
    cursor.execute('SELECT * FROM HSEtable')

    # Iterate over the rows returned by the SELECT statement
    for row in cursor:
        # If the specified column in the current row matches the search term, print the row
        if search_term == row[service]:
            print(row)

while True:
    # Record the current time
    start_time = time.time()
    # Prompt the user for a service selection
    service = user_input()
    # If a service was selected, perform the search and reset the start time
    if service:
        # Determine the search term and column number based on the service selected
        service_pick = selection(service)
        # Search the HSEtable table for rows matching the search term and column number
        search_sql(service_pick[0], service_pick[1])
        # Reset the start time
        start_time = time.time()
    else:
        # Calculate the elapsed time since the last service was selected
        elapsed_time = time.time() - start_time
        # If the elapsed time exceeds 5 seconds, restart the script
        if elapsed_time > 5:
            os.execl(sys.executable, sys.executable, *sys.argv)
