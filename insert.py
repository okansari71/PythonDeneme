import mysql.connector

def insertProducts(list):
    connection = mysql.connector.connect(
        host = "192.168.1.15",
        user = "okans",
        password = "Po19482025",
        database = "node-app")
    cursor = connection.cursor()

    sql = "INSERT INTO product(name, price, imageUrl, description) VALUES (%s,%s,%s,%s)"
    values = list
    cursor.executemany(sql,values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayit eklendi')
        print(f'son eklenen kaydin id: {cursor.lastrowid}')
    except mysql.connector.Error as err:
        print('hata: ', err)
    finally:
        connection.close()
        print('database bağlantisi kapandi')
list = []
while True:
    name = input('urun adi: ')
    price = float(input('urun fiyati: '))
    imageUrl = input('urun resim adi: ')
    description = input('urun aciklamasi: ')

    list.append((name, price, imageUrl, description))

    result = input('devam etmek istiyormusunuz (e/h)')
    if result == 'h':
        print('kayitlariniz veri tabanina aktariliyor...')
        print(list)
        insertProducts(list)
        break

#insertProduct(name,price,imageUrl,description)

