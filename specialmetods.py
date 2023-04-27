class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('movie objesi oluşturuldu.')

    def __str__(self): # Special Metod
        return f"{self.title} by {self.director}"
    def __len__(self): # Special Metod
        return self.duration
    def __del__(self): # special Metod
        print('Movie object is deleted')
m1 = Movie('film adı','yönetmen adı',120)
print(m1)
string = 'Bu bir stringdir.'
print(str(string))
print(str(m1))
mylist = [1,2,3]
print(len(mylist))
print(len(m1))
del(m1) #object delete 