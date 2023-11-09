import mysql.connector
import datetime

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "qwer1234",
    database = "schooldb"
)

mycursor = connection.cursor()
sql = "INSERT INTO Student(id,StudentNumber,StudentName,StudentSurname,StudentBirthdate,StudentGender) VALUES (%s,%s,%s,%s,%s,%s)"
ogrenciler = [(2,"101","Ahmet","Demirel",datetime.datetime(2005,5,17),"E"),
              (3,"101","Ahmet","Demirel",datetime.datetime(2005,5,17),"E"),
              (4,"101","Ahmet","Demirel",datetime.datetime(2005,5,17),"E"),
              (5,"101","Ahmet","Demirel",datetime.datetime(2005,5,17),"E"),
              (6,"101","Ahmet","Demirel",datetime.datetime(2005,5,17),"E")              
            ]
mycursor.executemany(sql,ogrenciler)

try:
    connection.commit()
    print(f'{mycursor.rowcount} tane kayıt eklendi.')
except mysql.connector.Error as err:
    print('hata:',err)
finally:
    connection.close()
    