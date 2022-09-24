import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

with open("create_tables.sql", encoding="utf-8") as file:
    cur.executescript(file.read())
query = "SELECT * FROM tbl1 LIMIT 5 ORDER BY c14 ASC"

data = conn.execute(query)
for i in data:
    print(i)
pd.read_sql(query, conn).to_dict()