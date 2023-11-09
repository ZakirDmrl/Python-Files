import mysql.connector

connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "akpinar40",
        database = "sakila"
        )

sql = "SELECT * FROM sakila.actor;"

cursor = connection.cursor()

cursor.execute(sql)

try:
    result = cursor.fetchall()
    for actor in result:
        print(actor)
except mysql.connector.Error as err:
    print("hata",err)
finally:
    connection.close()
    print("database bağlantısı kapandı.")