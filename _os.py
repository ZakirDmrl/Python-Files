import os
result = dir(os)
result = os.name # Bilgisayarın İşletim Sistemini gösterir.
result = os.getcwd # Dosyanın bulunduğu dizini gösterir.
os.chdir('C:\\') # Varsayılan dizin adresi bu şekilde değiştirilebilir.
os.mkdir("newdirector")
print(result)

os.chdir('C:\\')
os.makedirs("newdirectory/yeniklasör") #İçiçe Klasör Oluşturma

#Listeleme
result = os.listdir() # ls komutu
print(result)
#Filtreleme

for dosya in os.listdir():
    if dosya.endswith('.py'):
        print(dosya)

#path
result = os.path.dirname(os.path.abspath("_os.py")) # Yolunu bilmediğin bir dosyanın tam konumunu bulmak için kullanılır.
result = os.path.exists("c:/Users/USER/workspace/Python/_os.py") # İlgili konumda dosyanın var olup olmadığını kontrol eder.
result = os.path.isdir("c:/Users/USER/workspace/Python/_os.py") # İlgili konum bir klasör mü?
result = os.path.isfile("c:/Users/USER/workspace/Python/_os.py") # İlgili konum bir dosya mı?
result = os.path.join("c://","Users","USER") # dizin oluşturna için
result = os.path.split("c:/Users/USER/workspace") # dizin parçalama
result = os.path.splitext("_os.py") # dosya ile uzantıyı ayırmak için




print(result)