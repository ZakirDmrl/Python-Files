import pandas as pd

df = pd.DataFrame()
df = pd.DataFrame([1,2,3,4])
df = pd.DataFrame([["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]])
data = [["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
df = pd.DataFrame(data,index=[1,2,3,4],columns=['Name','Grade'],dtype=float)
print(df)

dict = {"Name": ["Ahmet","Ali","Yağmur","Çınar"], "Grade": [50,60,70,80]}
df = pd.DataFrame(dict)
df = pd.DataFrame(dict, index = ["201","321","231","542"])
print(df)

dict_list = [
                {"Name":"Ahmet","Grade":50},
                {"Name":"Ali","Grade":60},
                {"Name":"Yağmur","Grade":70},
                {"Name":"Çınar","Grade":80}

            ]

df = pd.DataFrame(dict_list)
df = pd.DataFrame(dict_list, index = ["201","321","231","542"])

print(df)

# pandas_Series1 = pd.Series([3,2,0,1])
# pandas_Series2 = pd.Series([0,3,7,2])

# data = dict(apples = pandas_Series1 , oranges = pandas_Series2)

# df = pd.DataFrame(data)

# print(df) 