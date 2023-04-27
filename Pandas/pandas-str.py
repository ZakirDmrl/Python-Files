import pandas as pd

data = pd.read_csv("player_data.csv")
data.dropna(inplace=True) 

data["name"] = data["name"].str.upper()
data["name"] = data["name"].str.lower()
data["index"] = data["name"].str.find('a')
data = data[data.name.str.contains("Stephen")]
data = data.name.str.replace(' ','-') # boşluk gördüğü yere - yazar
data[['FirstName','LastName']] = data["name"].loc[data['name'].str.split().str.len()==2].str.split(expent=True)

print(data)