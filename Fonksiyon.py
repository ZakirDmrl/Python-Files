# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
def kprint(word,num):
   print(word * num)
kprint('YA HAK\n',5)
# 2- Gönderilen sonsuz sayıdaki paramatreyi bir listeye çeviren fonk..
def cevir(*params):
   liste = []
   for param in params:
       liste.append(param)
   return liste

result = cevir(10,20,30,'MERRHABA')
print(result)
# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonk..
def asalsayiBul(sayi1,sayi2):
    for sayi in range(sayi1, sayi2+1):
        for a in range(2,sayi):
            if (sayi % a == 0):
                break
        else:
            print(sayi)

sayi1= int(input('sayi1: '))
sayi2= int(input('sayi2: '))
asalsayiBul(sayi1,sayi2)
input('WAİT')
# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste halinde oluşturan fonk..
def tambolenBul(sayi):
    tambolenler = []
    for a in range(2,sayi+1):
        if sayi % a == 0:
            tambolenler.append(a)
    return tambolenler

sayi=int(input('sayi: '))
result = tambolenBul(sayi)
print(result)