import pandas as pd
import numpy as np

data =np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data,index = ['a','c','e','f','h'],columns=["column1","column2","column3"])

df = df.reindex(['a','b','c','d','e','f','g','h'])
newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = newColumn 
result = df
result = df.drop("column1",axis = 1) # axis 1 columna tekabul ediyor column1 i kaldırdı
result = df.drop("a",axis = 0) # axis 0 row a tababül ediyor a kaldırıldı
result = df.isnull() #Null olanlar True olur
result = df.notnull()# NUll olayanlar True olur
result = df["column1"].notnull().sum()
result =df.dropna() #nan olan satırları kaldırır (default axis = 0 how = "any")
result = df.dropna(how = "all") # sadece tamamı nan olan satırı siler
result = df.fillna(1) #nan olan yerleri 1 yapapr
result = df.sum().sum()
result = df.size
result = df.isnull().sum().sum()
def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size -df.isnull().sum().sum()
    return toplam /adet

result = df.fillna(value=ortalama(df))

    

print(result)


