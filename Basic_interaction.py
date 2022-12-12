import sqlite3

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
    cursor.execute('SELECT *FROM HSEtable')

    for row in cursor:
        # if current rows 2nd value is equal to input, print that row
        if search_term == row[service]:  # change number to n
            print(row)
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    service = user_input()
    service_pick = selection(service)
    search_sql(service_pick[0],service_pick[1])