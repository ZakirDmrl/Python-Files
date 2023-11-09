import mysql.connector
import datetime

class Student:
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "qwer1234",
        database = "schooldb"
    )
    mycursor = connection.cursor()
    def __init__(self,id,number,name,surname,birdate,gender):
        if id is None:
            self.id = 0 #yeni kayıt
        else:
            self.id = id
        self.number= number
        self.name = name
        self.surname = surname
        self.birdate = birdate
        self.gender = gender

    @staticmethod
    def StudentInfo():
        sql = "SELECT StudentName,StudentSurname from student where StudentGender = 'K' order by StudentName,StudentSurname "
        Student.mycursor.execute(sql)
        try:
            results = Student.mycursor.fetchall()
            for result in results:
                print(result)
        except mysql.connector.Error as err:
            print("hata",err)
        finally:
            Student.connection.close()

    @staticmethod
    def getStudentById(id):
        sql = "SELECT * from student where id =%s"
        values = (id,) # burası önemli (id,) şeklinde atama yapmalı
        Student.mycursor.execute(sql,values)
        try:
            return Student.mycursor.fetchone()
        except mysql.connection.Error as err:
            print("Error",err)
     
        
    def updateStudent(self):
        sql = "update student set StudentNumber=%s,StudentName=%s,StudentSurname=%s,StudentBirthdate=%s,StudentGender=%s where id=%s"
        values = (self.number,self.name,self.surname,self.birdate,self.gender,self.id,)
        Student.mycursor.execute(sql,values)
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} tane kayıt güncellendi")
        except mysql.connector.Error as err:
            print("hata:",err)
       

obj = Student.getStudentById(4)
student = Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
student.name = 'Cinar'
student.surname = 'Turan'
student.updateStudent()


# Tüm öğrenci kayıtlarını alınız. sql = "SELECT * From Student "
# Tüm öğrencilerin sadece öğrenci no,ad ve soyad bilgilerini aliniz. "SELECT StudentNumber,StudentName,StudentSurname From Student "
# Sadece kız öğrencilerin ad ve soyadlarını alınız SELECT StudentName,StudentSurname From Student Where StudentGender = K
# 2003 doğumlu öğrencileri alınız SELECT * From Student Where StudentBirthdate LIKE '%2003%'
# İsmi Ahmet ve doğum tarihi 2005 olan "SELECT * From Student Where StudentName = 'Ahmet' And StudentBirthdate LIKE '%2005%' "
# ad ve ya soyadında '' ifadesi olan "SELECT * From Student Where StudentName LIKE '%rum%' or StudentSurname LIKE '%demi%' "
# Erkek sayısı "SELECT COUNT(*) from student where StudentGender = 'E'"
# Kızları sırala
# Student.StudentInfo()
