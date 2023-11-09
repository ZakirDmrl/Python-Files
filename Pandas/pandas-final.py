import pandas as pd

df = pd.read_csv("datasets/test.csv")
x = list(df["x"])
y = list(df["y"])
liste = list(zip(x,y))
oranlistesi = []
for x,y in liste:
    if(x+y) == 0:
        oranlistesi.append(0)
    else:
        oranlistesi.append(x/(x+y))
    
print(oranlistesi)    