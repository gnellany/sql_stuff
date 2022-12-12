import sqlite3

conn = sqlite3.connect("HSE.db")
cursor=conn.cursor()
cursor.execute('SELECT *FROM HSEtable')

for row in cursor:
    print(row)
