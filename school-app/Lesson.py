class Lesson:
    def __init__(self,id,name):
        if id is None:
            self.id = 0 #yeni kayıt
        else:
            self.id = id
        self.name = name
   
