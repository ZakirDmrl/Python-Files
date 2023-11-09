import mysql.connector
def insertProduct(name,price,imageUrl,decription):
    None

def insertProducts(list):
    connection = mysql.connector(host="localhost",user = "root",password ="qwer1234",database = "node_app")
    cursor = connection.cursor()
    sql = ('INSERT INTO Products(id,name,price,imageUrl,deccription) VALUES (%s,%s,%s,%s,%s)')
    values = list

    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"son eklenen kayıtın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.")

def getProducts():
    connection = mysql.connector.connect(host="localhost",user = "root",password = "qwer1234",database = "node_app")
    cursor = connection.cursor()
    # cursor.execute("Select * From Products Order By name") # name e göre bir sıralama yapar
    # cursor.execute("Select * From Products Order By price") # price ye göre bir sıralama yapar
    cursor.execute("Select * From Products Order By name,price") # hem price ye göre hem de name e göre bir sıralama yapar
    try:
        result = cursor.fetchall()
        for product in result:
            print(f"id: {product[0]} name: {product[1]} price: {product[2]}")
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database bağlantısı kapandı.")

def getProductById(id):
    connection = mysql.connector.connect(host="localhost",user = "root",password="qwer1234",database="node_app")
    cursor = connection.cursor()
    sql = "Select * From Products Where id=%s"
    params = (id,)
    cursor.execute(sql,params)
    result = cursor.fetchone()
    print(f"id:{result[0]} name: {result[1]} price: {result[2]}")

def getProductInfo():
    connection = mysql.connector.connect(host="localhost",user = "root",password="qwer1234",database="node_app")
    cursor = connection.cursor()
    # cursor.execute("Select COUNT(*) from Products") # kaç tane data var
    # cursor.execute("Select AVG(Price) from Products") # fiyat ort
    # cursor.execute("Select SUM(Price) from Products") # toplam fiyat
    # cursor.execute("Select MIN(Price) from Products") # min fiyat
    cursor.execute("Select Name,Price From Products Where Price = (Select MAX(Price) From Products)")


    result = cursor.fetchone()
    # print(f"result: {result[0]}")
    print(f"result: {result[0]} {result[1]}")


getProductInfo()
# id = input("id değerini gir: ")
# getProductById(id)