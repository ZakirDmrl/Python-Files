def ortalamalari_oku():
    with open("sinav_notlari.txt","r", encoding="utf-8") as file: #file read
        for satir in file:
            print(not_hesapla(satir))
def not_gir():
    ad = input('Öğrenci adı: ')
    soyad = input('Öğrenci soyad: ')
    not1 = int(input('Öğrenci not1: '))
    not2 = int(input('Öğrenci not2: '))
    not3 = int(input('Öğrenci not3: '))
    with open("sinav_notlari.txt","a", encoding="utf-8") as file:# file append 
        file.write(f"{ad} {soyad}:{not1},{not2},{not3}\n")

    
def not_hesapla(satir):
    satir =satir[:-1]
    liste =satir.split(":")
    ogrenciAdi = liste[0]
    notlar =  liste[1].split(',')
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ortalama = (not1+ not2+ not3)/3
    if ortalama<=100 and ortalama >= 85: 
            harf = 'AA'
    elif ortalama<85 and ortalama >= 70:
            harf = 'AB'
    elif ortalama< 70 and ortalama >= 60:
            harf = 'BB'
    elif ortalama<60 and ortalama >= 50:
            harf = 'BC'
    elif ortalama<50 and ortalama >= 40:
            harf = 'CC'
    elif ortalama<40 and ortalama >= 30:
            harf = 'CD'
    elif ortalama<30 and ortalama >= 25:
            harf = 'DD'
    else:
            harf = 'FF'
    print(f"{ogrenciAdi} adlı kişinin not ortalamasının harf notu: {harf}")

def not_kayıtet():
    with open('sinav_notlari.txt','r',encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(not_hesapla(i))
    
    with open('sonuclar.txt','w',encoding='utf-8') as file2:
        for i in liste :
            file2.write(i)

while True:
    islem = input ('1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n')

    if islem == '1':
        ortalamalari_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        not_kayıtet()
    else:
        break
