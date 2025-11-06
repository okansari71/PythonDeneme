import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host = "192.168.1.15",user = "okans",password = "Po19482025",database = "node-app")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM product WHERE id=2')
    result = cursor.fetchall()

   # print(f'product: {result[0]} name:{result[1]} price: {result[2]}')

    for product in result:
        print(f'name:{product[0]} name: {product[1]} price: {product[2]}')
        

getProducts()

    