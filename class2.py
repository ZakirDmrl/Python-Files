class Calisan:
    name = ""
    surname = ""
    date_Of_Start = 2020
    def __init__(self,name,surname,date_Of_Start):
        self.name = name
        self.surname = surname
        self.date_Of_Start = date_Of_Start

class MaasliCalisan(Calisan):
    
    def __init__(self,name,surname,date_Of_Start,maas):
        super().__init__(name,surname,date_Of_Start)
        self.maas = maas if maas >= 10000 else 10000
    def Yillik_Maas_Hesapla(self):
        result = self.maas*12
        print(f"Adi: {self.name} Soyadi: {self.surname} İşe Başlama Tarihi: {self.date_Of_Start} Yillik Maasi: {result}")


Mc = MaasliCalisan("Zakir","Demirel",2023,20000)
Mc.Yillik_Maas_Hesapla()
