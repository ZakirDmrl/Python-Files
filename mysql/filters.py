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
    # cursor.execute("Select * From Products Where name ='HuwaiP9'") 
    # cursor.execute("Select * From Products Where price ='12312'")
    # cursor.execute("Select * From Products Where price >='12312'")
    # cursor.execute("Select * From Products Where price >'12312' and price<'21400'")
    # cursor.execute("Select * From Products Where price ='12312' or name ='Samsung S5'")
    cursor.execute("Select * From Products Where name LIKE '%Samsung%'") # içinde samsung geçen tüm kayıtlar büyük harf küçük harf fark etmeksizin
    result = cursor.fetchall()
    for product in result:
        print(f"id: {product[0]} name: {product[1]} price: {product[2]}")

def getProductById(id):
    connection = mysql.connector.connect(host="localhost",user = "root",password="qwer1234",database="node_app")
    cursor = connection.cursor()
    sql = "Select * From Products Where id=%s"
    params = (id,)
    cursor.execute(sql,params)
    result = cursor.fetchone()
    print(f"id:{result[0]} name: {result[1]} price: {result[2]}")

# getProducts()
id = input("id değerini gir: ")
getProductById(id)