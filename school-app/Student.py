class Student:
    def __init__(self,id,number,name,surname,birthdate,gender,classid):
        if id is None:
            self.id = 0 #yeni kayıt
        else:
            self.id = id
        self.number= number
        if len(name) > 45:
            raise Exception("name için maksimum 45 karekter girmelisiniz.")
        else:
            self.name = name
        if len(surname) > 45:
            raise Exception("surname için maksimum 45 karekter girmelisiniz.")
        else:
            self.surname = surname
                               
        self.birthdate = birthdate
        self.gender = gender
        self.classid = classid

    @staticmethod
    def CreateStudent(obj):
        list = []
        
        if isinstance(obj,tuple):
            list.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5],obj[6]))
        else:
            for i in obj:
                list.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6])) 
        return list