import sqlite3
import pandas as pd

def createSQL():
    conn = sqlite3.connect("HSE.db")
    df = pd.read_csv("ireland_health_centres.csv")
    df.to_sql('HSEtable', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    createSQL()
    print("Table Created")