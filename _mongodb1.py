# passsword: k9mkhvE5PcN4tfGS
# LOCAL SUNUCUYA BAĞLANMA
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["node-app"]
mycollection = mydb["products"]
# print(myclient.list_database_names())
print(mydb.list_collection_names()) # database içindeki tablolar
# product = {"name":"Samsung S6","price": 2000}
# result =  mycollection.insert_one(product)
# print(result)
# print(result.inserted_id) #id şekilde bir obje kaydı gösterir.

productList =[{"name":"A-Pro","price": 32000,"decription":"iyi iyi"},{"name":"B-Pro","price": 22000,"catagories":["telefon","elektornik"]}]
result = mycollection.insert_many(productList)
print(result)