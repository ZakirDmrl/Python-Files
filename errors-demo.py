liste = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal degerleri bulunuz.
for i in liste:
    try:
        result = int(i)
        print(result)
    except ValueError:
        continue

# 2: Kullanucı 'q' degerini girmedikçe aldığınız her inputun sayı
# olduğundan emin olunuz aksi halde hata mesajı yazın

while True:    
    result = input('sayi: ')
    if result== 'q':
        break
    try:
        result = float(result)
        print(result)
    except ValueError as a:
        print('Bu bir sayı değil',a)
        continue

# 3: Girilen parola içinde türkçe karakter hatası veriniz.
def cheakPassword(psw):
    import re
    if re.search("[ıüğöçş]",psw):
        raise Exception("Türkçe karakter girmeyiniz.")

    else:
        print(psw)
parola = "Parolan123"
try:
    cheakPassword(parola)
finally:
    print('Validation tamamlandı')

# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen
#   değer için hata mesajları verin. 
def faktoriyel(sayi):
    if sayi > 0:
        return sayi*faktoriyel(sayi)
    elif sayi == 0:
        return 0
    else:
        raise Exception("Faktöriyeli alınacak sayı 0 veya bir pozitif tam sayı olmalıdır.")

sayi = int(input('sayı: '))
try:
    result = faktoriyel(sayi)
    print(result)
except Exception as ex:
    print("Hatalı sayı",ex)
else:
    print("Fonksiyon başarılı bir şekilde çalıştı")
finally:
    print("İYİ UYKULAR..") 