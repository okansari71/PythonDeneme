import mysql.connector

def getProducts():
    connection = mysql.connector.connect(host = "192.168.1.15",user = "okans",password = "Po19482025",database = "node-app")
    cursor = connection.cursor()

    cursor.execute('SELECT name, price FROM product')
    result = cursor.fetchone()

    print(f'name:{result[0]} price: {result[1]}')
    
    # for product in result:
    #     print(f'name:{product[0]} price: {product[1]}')
        

getProducts()

    