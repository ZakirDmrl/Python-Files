import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Class import Class

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "SELECT * from student where id =%s"
        values = (id,) # burası önemli (id,) şeklinde atama yapmalı
        self.cursor.execute(sql,values)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connection.Error as err:
            print("Error",err)
        
    def getStudentsByClassId(self,classid):
        sql = "select * from student where classid = %s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connection.Error as err:
            print("Error",err)

    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql,)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connection.Error as err:
            print("Error",err)
    
    def deleteStudent(self,studentid):
        sql = "delete from student where id = %s"
        value = (studentid,)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt silindi.")
        except mysql.connector.Error as err:
            print("Hata: ",err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(id,StudentNumber,StudentName,StudentSurname,StudentBirthdate,StudentGender,ClassId) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        value = (student.id,student.number,student.name,student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit() 
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("hata:",err)

    def editStudent(self, student: Student):
        sql = "update student set StudentNumber=%s,StudentName=%s,StudentSurname=%s,StudentBirthdate=%s,StudentGender=%s,Classid=%s where id = %s"
        values = (student.number,student.name,student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print("hata:",err)

    def __del__(self):
        self.connection.close()
        print("db kapandı.")


db = DbManager()
student = db.getStudentById(3)

# std = Student("8","107","Abdullah","Koc","1995-12-23","E","1")
# db.addStudent(std)

std = Student("8","107","Ahmet","Koc","1995-12-23","E","1")
db.editStudent(std)
# print(student[0].name)
# print(student[0].surname)

# students = db.getStudentsByClassId(1)
# print(students[0].name)
# print(students[1].name)
