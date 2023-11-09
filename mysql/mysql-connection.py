import  mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", #192.23.45.56 gibi genel serverlar için
    user = "root",
    password = "qwer1234",
    database = "mydatabase")
print(mydb)
mycursor = mydb.cursor()
# mycurcor.execute("CREATE DATABASE mydatabase") # create database 
mycursor.execute("CREATE TABLE customers (name VARCHAR(255),address VARCHAR(255))")  # create table