import mysql.connector

def insertProduct(name,price,imageUrl,decription):
    None

def insertProducts(list):
    connection = mysql.connector(host="localhost",user = "root",password ="qwer1234",database = "node_app")
    cursor = connection.cursor()
    sql = ('INSERT INTO Products(id,name,price,imageUrl,deccription) VALUES (%s,%s,%s,%s,%s)')
    values = list
    cursor.executemany(sql,values)


def getProducts():
    connection = mysql.connector.connect(host="localhost",user = "root",password = "qwer1234",database = "node_app")
    cursor = connection.cursor()
    # cursor.execute("Select * From Products") # Bu 1
    cursor.execute("Select name,price From Products") # Bu 2

    # result = cursor.fetchall() # Bulduğu tüm kayıtları getirir
    result = cursor.fetchone() # Bulduğu ilk kayıtı getirir
    
    print(f"name: {result[0]} price: {result[1]}")

   
    print(result)
    # for product in result:
    #     # print(f"name: {product[1]} price: {product[2]}") # Bu 1
    #     print(f"name: {product[0]} price: {product[1]}") # Bu 2

        

getProducts()