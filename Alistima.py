def Enbuyuk(a,b,c):
    enbuyuk = a
    if a<b :
        enbuyuk = b
        if b<c:
            enbuyuk = c

    else :
        if a<c : 
            enbuyuk = c
    print(enbuyuk)

Enbuyuk(4,3,5)
def mutlak():
    a = float(input("Bir sayi girin: "))
    if a < 0:
        a = -a
        print(a)
    else:
        print(a)

mutlak()

class Circle:
    def __init__(self,r):
        print("Circle oluştu.")
        self.yaricap = r

    def Cevre(self):
        print(f"Çevre = {self.yaricap*2*3.4}'tür")
    def Alan(self):
        print(f"Alan = {self.yaricap*self.yaricap*3.4}'tır")

c = Circle(5)

c.Cevre()
c.Alan()

class Password:
    def __init__(self,mail,psw):
        self.mail = mail
        self.password = psw
        print("Password class active.")
    def Check(self):
        if self.mail != "mail.@python.com":
            print("mail hata")
        else:
            if self.password != "123abc":
                print("password hata")
            else:
                print("Hoşgeldiniz.")

p =Password("zakirr2004@gmail.com","123abc")
p2 =Password("mail.@python.com","231")
p3 =Password("mail.@python.com","123abc")
p.Check()
p2.Check()
p3.Check()

class Change:
    global pi
    pi = 3.4
    def __init__(self,derece):
        self.derece = derece

    def ChangeRadyan(self):
        radyan = (self.derece*pi)/180
        return radyan
    
    def ChangeGrad(self):
        
        grad = (self.derece*pi)/200
        return grad
    
c = Change(360)
print(f"{c.derece}'nin radyan cinsinden değeri: {c.ChangeRadyan()}")
print(f"{c.derece}'nin grad cinsinden değeri: {c.ChangeGrad()}")
