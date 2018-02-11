import sqlite3
import pandas

# data = pandas.read_csv("ten-more-countries.txt")
# print(data)

# conn = sqlite3.Connection("database.db")
# cur = conn.cursor()
# for index, row in data.iterrows():
#     print(row["Country"], row["Area"])
#     cur.execute("INSERT INTO countries VALUES (NULL, ?, ?, NULL)",(row["Country"], row["Area"]))
# conn.commit()
# conn.close()

conn = sqlite3.Connection("database.db")
cur = conn.cursor()
cur.execute("SELECT * FROM countries WHERE area >= 2000000")
rows = cur.fetchall()

cur.execute("SELECT * FROM countries WHERE area >= 2000000")
rows2 = cur.fetchall()

conn.close()
df1 = pandas.DataFrame.from_records(rows)
df2 = pandas.DataFrame.from_records(rows2)
print(df1)
print(df2)