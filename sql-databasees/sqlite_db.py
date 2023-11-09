import sqlite3

connection = sqlite3.connect("chinook.db") # node_app.db yi aynı klasör içinde arar yoksa oluşturur.
cursor = connection.cursor()
sql = "select * from customers"
cursor.execute(sql,)
result = cursor.fetchall()
for i in result:
    print(f"{i}\n")
connection.close()