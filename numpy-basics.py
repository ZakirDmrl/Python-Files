# *******************************************
# CHAPTER 1
import numpy as np


# python list
py_list = [1,2,3,4,5,6,7,8,9]

# numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])
print(type(py_list))
print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)
print(py_multi)
print(np_multi)

print(np_array.ndim) #.ndim kaç boyutlu?
print(np_multi.ndim)

print(np_array.shape) #kaça kaçlık?
print(np_multi.shape)

# *******************************************
# CHAPTER 2

result = np.arange(1,10) #1-9 aralığındaki sayılarla dizi oluşturma
result = np.arange(10,100,3) # 10-99 aralığında 3 er 3 er artarark dizi oluşturma
result = np.zeros(10) # 10 sıfırdan oluşan dizi oluşturma her elememan float türünde
result = np.linspace(0,100,5) # 0-100 aralığını 5 eşit parçaya böler.
result = np.random.randint(0,10) #0-9 aralığında rastgele sayı oluşturur.
result = np.random.randint(1,10,3) # rastgele 3 sayı 0-9 aralığında
result = np.random.randn(5) # negatif sayılar dahil rastgele 5 sayı
np_array = np.arange(50)
np_multi = np_array.reshape(5,10) # 5 e 10 luk bir matris oluşturma
print(np_multi.sum(axis=1)) # satırların değerlerini verir
print(np_multi.sum(axis=0)) # sütünların değerlerini verir

rnd_numbers =np.random.randint(1,100,10)
print(rnd_numbers)
result = rnd_numbers.max() # üretilen sayılarda en büyük olanı
result = rnd_numbers.mean() # üretilen sayiların ort.
result = rnd_numbers.argmax() # en yüksek sayının indexi
print(result)

# ********************************************
# CHAPTER 3

numbers = np.array([0,5,15,20,25,50,75])

result = numbers[5]
result = numbers[0:3] # ilk 3 index i alır3
result = numbers[3:] # 3. den sona
result = numbers[::] # tamamı
result = numbers[::-1] # liste sondan başa yazdırılır

numbers2 = np.array([[0,5,15],[20,25,50],[75,80,85]])
print(numbers2)
result = numbers2[0][2] # or [0,2]
result = numbers2[1][::] # 2.satır tüm elemanlar
result = numbers2[:,2] # tüm satırladaki 3.indexler
result = numbers2[:,0:2] #tüm satırlar 0 ve 1 . indexler

#print(result)
arr1 = np.arange(0,10)
# arr2 = arr1  # aynı adres
arr2 = arr1.copy() #farklı adresler
print(arr1)
print(arr2)
arr2[0] = 20
print(arr1)
print(arr2)

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)
print(numbers1)
print(numbers2)
result = numbers1+numbers2
print(result)
result =np.sin(numbers1)
print(result)

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)
print(mnumbers1)
print(mnumbers2)
result = np.vstack((mnumbers1,mnumbers2)) # dikey birleştirme
result = np.hstack((mnumbers1,mnumbers2)) #yatay birleştirme
print(result)

result = numbers1 >= 50 #tüm elemanlar için koşulu kontrol eder
print(numbers1[result]) #koşulu sağlayanları ayrı listtede gönderir

print(result)


# ***************** UYGULAMA *****************

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisini oluşturunuz.
numbers1 = np.array([10,15,30,45,60])
print(numbers1)

# 2- (5,15) arasında sayılarla numpy dizisi oluşturunuz
numbers = np.arange(5,16)
print(numbers)

# 3- (50,100) aralığında 5'er 5'er artarak numpy dizisini oluşturunuz.
numbers= np.arange(50,101,5)
print(numbers)

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz
numbers = np.zeros(10)
print(numbers)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturunuz
numbers = np.ones(10)
print(numbers)

# 6- (0,100) aralığında eşit aralıklı 5 sayı üretin
numbers = np.linspace(0,100,5)
print(numbers)

# 7- (10,30) aralığında rastgele 5 tane tamsayı üretin
numbers = np.random.randint(10,30,5)
print(numbers)

# 8 [-1 ile 1] arasında 10 adet sayı üretin
numbers = np.random.randn(10)
print(numbers)

# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz
nparray = np.random.rand(15) 
array = nparray.reshape(3,5)
print(array)

# 10- Üretilen matrsin satır ve sütün sayıları toplamlarını hesaplayınız
nparray = np.random.randint(10,50,15).reshape(3,5)
rowTotal = nparray.sum(axis=1)
colTotal = nparray.sum(axis=0)
print(rowTotal)
print(colTotal)
result = nparray.max()
print(result)
result = nparray.min()
print(result)
result = nparray.mean()
print(result)
result = nparray.argmax()
print(result)

# 11- (10,20) arasındaki sayıları içeren dizinin ilk 3 elemeanını seçiniz
array = np.arange(10,20)
result = array[:3]
print(result)
result = array[::-1]
print(result)
matris = array.reshape(2,5)
result = matris[0][:]
print(result)
numbers2 = np.array([[0,5,15],[20,25,50],[75,80,85]])
result = numbers2[1,2]
print(result)
result = matris[:,0]
print(result)
result = numbers2[:,0]
print(result)
result = numbers2 ** 2
print(result)
# 12- Üretilen matrisin her bir elemanının hangisi pozitif çift sayıdır ?
array = np.arange(-50,50)
result = array % 2 == 0
print(array[result])
