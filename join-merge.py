import pandas as pd 

customers = {
    'CustomerId' : [1,2,3,4],
    'FirstName' : ["Ahmet","Ali","Hasan","Canan"],
    'LastName' : ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

orders = {
    'OrderId' : [10,11,12,13],
    'CustomerId' : [1,2,5,7],
    'OrderDate' : ["2022-12-04","2023-01-30","2023-03-14","2023-02-04"]
}

df_customers = pd.DataFrame(customers,columns= ["CustomerId","FirstName","LastName"])
df_orders = pd.DataFrame(orders,columns= ["OrderId","CustomerId","OrderDate"])

print(df_customers)
print(df_orders)

result = pd.merge(df_customers,df_orders,how="inner")

print(result)

result = pd.merge(df_customers,df_orders,how="left")

print(result)

result = pd.merge(df_customers,df_orders,how="right")

print(result)

result = pd.merge(df_customers,df_orders,how="right")

print(result)

result = pd.merge(df_customers,df_orders,how="outer")

print(result)
customersA = {
    'CustomerId' : [1,2,3,4],
    'FirstName' : ["Ahmet","Ali","Hasan","Canan"],
    'LastName' : ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    'CustomerId' : [4,5,6,7],
    'FirstName' : ["Yağmur","Çınar","Cengiz","Can"],
    'LastName' : ["Yılan","Kor","Lofar","Top"]
}
df_customersA = pd.DataFrame(customersA,columns= ["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB,columns= ["CustomerId","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB])

print(result)

result = pd.concat([df_customersA,df_customersB],axis=1)

print(result)