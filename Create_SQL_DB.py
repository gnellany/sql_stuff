import sqlite3
conn = sqlite3.connect("HSE.db")
cur = conn.cursor()
#below doesn't work

sql = """
    CREATE TABLE HSEtable (
        ID TEXT,
        Hospital TEXT,
        Latitude INTERGER,
        Longitude INTERGER,
        Address TEXT,
        Town TEXT,
        Eircode TEXT,
        Role TEXT,
        Phone TEXT,
        primary key(ID)
    )"""

cur.execute(sql)
print("Table Created")
conn.commit()
conn.close()