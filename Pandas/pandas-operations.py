import pandas as pd
import numpy as np

data = {
    "Column1" : [1,2,3,4,5],
    "Column2" : [10,20,30,20,50],
    "Column3" : ["abc","bca","ade","cba","dce"]
}
df = pd.DataFrame(data)
def karaAl(x):
    return x*x
karaAl2 = lambda x: x * x 
result = df["Column2"].unique()  # Farklı olanlar yazdırılır
result = df["Column2"].nunique() #Farklı olanlar sayısı
result = df["Column2"].value_counts() # her elemenadan kaç tane var 
result = df["Column1"].apply(karaAl)
print(result)
result = df["Column1"].apply(karaAl2)
result = df["Column1"].apply(lambda x: x * x )
df["Column4"] = df["Column3"].apply(len)

result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info

result = df.sort_values("Column2")
result = df.sort_values("Column3",ascending=False)

print(result)

data = {
    "Ay" : ["Mayıs","Haziran","Nisan","Mayıs","Nisan","Haziran","Mayıs"],
    "Kategori" : ["Elektronik","Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap"],
    "Gelir" : [20,30,15,14,32,42,16]
}
df = pd.DataFrame(data)

print(df)

print(df.pivot_table(index="Ay",columns="Kategori",values="Gelir"))

