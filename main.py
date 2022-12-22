import sqlite3
import time
import os
import sys

admin_username = "admin"
admin_password = "password"



####admin role
def get_column_names():
    conn = sqlite3.connect("HSE.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(HSEtable)")
    columns = [column[1] for column in cursor.fetchall()]
    return columns


def add_row(values):
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
    conn = sqlite3.connect("HSE.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM HSEtable WHERE id=?", (id,))
    conn.commit()
    print("Row removed successfully!")


def admin_login():
    global admin_username, admin_password# in the field this would be linked to a database
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == admin_username and password == admin_password:
        return True
    else:
        return False



#####basic user####
def user_input():
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
    service: int = input("Selection: ")
    print("You picked "+ service)
    return service


def selection(service):
        if service == "1":
            target = input("Which town?")
            selection = 5
        elif service == "2":
            target = input("Site")
            selection = 1
        elif service == "3":
            target = input("Phone Number")
            selection = 8
        elif service == "4":
            target = input("Location?")
            selection = 4
        elif service == "5":
            target = input("Role Search?")
            selection = 7
        elif service == "8":#
            if admin_login():
                print("1. Add row\n2. Remove row")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    values = input("Enter values for the row (comma-separated): ").split(",")
                    add_row(values)
                    os.execl(sys.executable, sys.executable, *sys.argv)
                elif choice == 2:
                    id = input("Enter the id of the row to be removed: ")
                    remove_row(id)
                    os.execl(sys.executable, sys.executable, *sys.argv)
                else:
                    print("Invalid choice")
            else:
                print("Invalid login credentials")
        else:
            print('Invalid Service')
        return target,selection

def search_sql(name,number):
    # input varible you want to search
    search_term = name#input('Enter search term to find\n')
    service: int = number
    # read csv, and split on "," the line
    conn = sqlite3.connect("HSE.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM HSEtable')

    for row in cursor:
        # if current rows 2nd value is equal to input, print that row
        if search_term == row[service]:  # change number to n
            print(row)

def main():
    ###run
    while True:
        start_time = time.time()
        service = user_input()#goes to users input
        if service:
            service_pick = selection(service)
            search_sql(service_pick[0], service_pick[1])
            start_time = time.time()
        else:
            elapsed_time = time.time() - start_time
            if elapsed_time > 12:
                os.execl(sys.executable, sys.executable, *sys.argv)

if __name__ == '__main__':
    main()