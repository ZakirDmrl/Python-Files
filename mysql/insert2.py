import mysql.connector

connection = mysql.connector.connect(host = "localhost", user = "root", password = "qwer1234",database = "node_app")
mycursor = connection.cursor()
sql = "INSERT Products(id,name,price,imageUrl,deccription) VALUES (%s,%s,%s,%s,%s)"
values = (2,"Samsung S5",21340,"1.jpg","iyi telefon")
mycursor.execute(sql,values)
try:
    connection.commit()
except mysql.connector.Error as err:
    print('hata',err)
finally:
    connection.close()
    print("database bağlantısı kapandı.")
