class Teacher:
    def __init__(self,id,branch,name,surname,birdate,gender):
        if id is None:
            self.id = 0 #yeni kayıt
        else:
            self.id = id
        self.branch= branch
        self.name = name
        self.surname = surname
        self.birdate = birdate
        self.gender = gender
   
