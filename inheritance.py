# class Person():
#     def __init__(self,fname,lname):
#         self.firstname = fname
#         self.lastname = lname
#         print('Person Created')
#     def Greeting(self):
#         print("I am Person")
# class Student(Person):
#     def __init__(self,fname,lname,num):
#         Person.__init__(self,fname,lname)
#         self.number = num
#         print('Student Created')
#     def Greeting(self): # override
#         print("I am Student")
#     def sayHello(self):
#         print("Hello")

# p1 = Person('Çınar','Turan')
# s1 = Student('ALi','Yilmaz',1304)
# print(p1.firstname + ' ' + p1.lastname)
# print(s1.firstname + ' ' + s1.lastname + ' ' + str(s1.number))
# print(f"{s1.firstname} {s1.lastname} {int(s1.number)} ")  # Alternatif

# p1.Greeting()
# s1.Greeting()
# s1.sayHello()