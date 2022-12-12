import sqlite3
import pandas as pd

conn = sqlite3.connect("HSE.db")
cur = conn.cursor()

df = pd.read_csv("ireland_health_centres.csv")
df.to_sql('HSEtable', conn, if_exists='replace', index=False)

conn.commit()
conn.close()