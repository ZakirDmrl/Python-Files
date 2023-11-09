import mysql.connector
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

def updateProduct(id,name,price):
    connection = mysql.connector.connect( 
        host = "localhost",
    user = "root",
    password = "qwer1234",
    database = "node_app"
)
    cursor = connection.cursor()
    if name!='':
        sql = "Update Products Set name= %s,price = %s where id=%s"

        # sql = "Update Products Set name ='Samsung S10',price = 23142 where id=5"
        # sql = "Update Products Set name ='Samsung S10' where id=5"
    
    values = (name,price,id)
    cursor.execute(sql,values)
    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayıt güncellendi.')
        print(f'son eklenen kaydın id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print(f"Hata: {err}")
    finally:
        connection.close()
        print("Database bağlantısı kapandı.")

updateProduct(4,'SAGA',432131)
getProducts()