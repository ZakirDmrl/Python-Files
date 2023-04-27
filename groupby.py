import pandas as pd
import numpy as np
perseneller = {
    'Çalışanlar': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Demirel','Begüm Durusu','Hamit Poros'],
    'Departman' : ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş' : [30,25,45,50,23,34,42],
    'Semt' : ['Kadıköy','Tuzla','Maltepe','Tuzla','Kağıthane','Ümraniye','Fatih'],
    'Maaş' : [5000,3000,4000,3500,2750,6500,4500]
}
df = pd.DataFrame(perseneller)
result = df["Maaş"].sum()
print(result)
result = df.groupby("Semt").get_group('Kadıköy')
print(result)
result = df.groupby("Departman").get_group("Muhasebe")
print(result)
result = df.groupby("Departman").mean()
print(result)
result = df.groupby("Departman")["Maaş"].agg[np.sum,np.mean,np.max,np.min]