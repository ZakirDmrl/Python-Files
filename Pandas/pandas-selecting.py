import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Column1","Column2","Column3"])

result = df
result = df["Column1"]
result = type(df["Column1"])
result = df[["Column1","Column2"]]

# loc["row","column"] => loc["row"] => loc[:,"column"]
result = df.loc["A"]
result = type(df.loc["A"])
result = df.loc[["A","B"]]
result = df.loc[:,"Column1"]
result = df.loc[:,"Column1":"Column3"]

result = df.iloc[2] #3.row
result = df.loc["A","Column1"]
result = df.loc[["A","B"],["Column1","Column2"]]

df["Column4"] = pd.Series(randn(3),["A","B","C"]) # add Column4
df["Column5"] = df["Column1"] + df["Column3"] # add Column5

print(df.drop("Column5",axis=1))  # geçici delete Column5 gerçekte silinmez
df.drop("Column5",axis=1,inplace=True) # delete Column5 gerçekten silinir
print(df)
print(result)