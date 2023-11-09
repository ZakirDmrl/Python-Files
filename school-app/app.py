from dbmanager import DbManager
import datetime
from Student import Student
class App:
    def __init__(self):
        self.db = DbManager()
    
    def initApp(self):
        msg = "******\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Çıkış"
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == '1':
                self.displayStudents()
            elif islem == '2':
                self.addStudent() 
            elif islem == '3':
                self.editStudent()
            elif islem == '4':
                self.deleteStudent() 
            elif islem == '5':
                print("Çıkış yapıldı.")
                break
            else:
                print("Yanlış seçim")
        
    def displayStudents(self):
        self.displayClasses()

        classid = input("hangi sınıf: " )
        students = self.db.getStudentsByClassId(classid)
        print("Öğrenci Listesi")
        # for index,std in enumerate(students):
        #     print(f"{index}-{std.name} {std.surname}")
        for std in students:
            print(f"{std.id}-{std.name} {std.surname}")
    def addStudent(self):
        self.displayClasses()
        classid = int(input("hangi sınıf: " ))
        id = int(input("id: "))
        number = int(input("numara: "))
        name = input("ad: ")
        surname = input("soyad: ")
        year = int(input("yıl: "))
        month = int(input("ay: "))
        day = int(input("gün: "))
        birthdate = datetime.date(year,month,day)
        gender = input("cinsiyet (E/K): ")
        student = Student(id,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)
    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("öğrenci id: "))
        self.db.deleteStudent(studentid) # id alan silme fonk buradaki fonkdan farklı dbmanager.py dosyasında tanımlı
    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("öğrenci id:: "))
        student = self.db.getStudentById(studentid)
        student[0].name = input("name: ") or student[0].name
        student[0].surname = input("surname: ") or student[0].surname
        student[0].gender= input("gender: ") or student[0].gender
        student[0].classid = input("classid: ") or student[0].classid
        self.db.editStudent(student[0])
    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f"{c.id}: {c.name}")

            
app = App()
app.initApp()