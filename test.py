import pandas as pd
import sqlite3

conn = sqlite3.connect("banco.db")

print(conn)

df = pd.read_sql_query("SELECT * FROM banco",conn)

conn.close()

print(df)