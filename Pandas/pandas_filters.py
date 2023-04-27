import pandas as py
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = py.DataFrame(data,columns = ["Column1","Column2","Column3","Column4","Column5"])
result = df
result = df.columns
result = df.head() #ilk 5 kayıtı alır
result = df.head(10) #ilk 10 kayıtı alır
result = df.tail() # son 5 kayıtı alır
result = df.tail(10) #son 10 kayıtı alır

result = df["Column1"].head() # column1 in 5 elemanı
result = df.Column1.head() # alternatif
result = df[["Column1","Column2"]].head() #c1 ve c2 nin ilk beş elemanı

result = df[5:15][["Column1","Column2"]].head() #c1 ve c2 nin 5 den itirabern 5 elemanı
#FİLTRELEME
df_filter = df > 50 
result = df[df_filter] 
result = df[df%2==0]
df_filter2 = df["Column1"] > 50
result = df["Column1"][df_filter2]
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)]
result = df[(df["Column1"] > 50) | (df["Column2"] <= 70)]
result = df.query("Column1 >= 50 & Column1 % 2 ==0")[["Column1","Column2"]]

print(result)