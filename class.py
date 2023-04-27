class Person:
    #attributes
    # class attributes
    address = 'No information'
    #constructor ( yapıcı metod) 
    def __init__(self,name,year): #self is refferans of object(p1)
        # object(instance) attributes
        self.name = name
        self.year = year
        
    #instance methods
    def greeting(self):
        print(f'Hello There,I am {self.name}')
    def calculateAge(self):
        return 2023 - self.year
    
p1 = Person('Ali',1990)
p2 = Person('Beyza',1998)
p1.greeting()
p2.greeting()
age = p1.calculateAge()
print(f"{p1.name} yasi {age}'dir")

class Circle:
    #Class object attribute
    pi = 3.14
    #Conctuctor
    def __init__(self, r=0):
        #Object attribute
        self.yaricap = r
    #inctance Methods
    def perimeter_Calculate(self):
        return 2* self.pi * self.yaricap
    def area_Calculate(self):
        return self.pi*self.yaricap**2
    
c1 = Circle(5)
print(f"Circle permeter : {c1.perimeter_Calculate()} Cİrcle area : {c1.area_Calculate()}")
