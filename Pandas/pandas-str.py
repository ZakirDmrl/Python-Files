import pandas as pd

data = pd.read_csv("datasets/layer_data.csv")
data.dropna(inplace=True) 

data["name"] = data["name"].str.upper()
print(data)
data["name"] = data["name"].str.lower()
print(data)
data["index"] = data["name"].str.find('a')
print(data)
data = data[data.name.str.contains("Stephen")]
print(data)
data = data.name.str.replace(' ','-') # boşluk gördüğü yere - yazar
print(data)
data[['FirstName','LastName']] = data["name"].loc[data['name'].str.split().str.len()==2].str.split(expent=True)

print(data)